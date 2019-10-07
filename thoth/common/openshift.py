#!/usr/bin/env python3
# thoth-common
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Handling OpenShift and Kubernetes objects across project."""

import os
import logging
import requests
import typing
import json
import random
import urllib3

from .exceptions import NotFoundException
from .exceptions import ConfigurationError
from .helpers import (
    get_service_account_token,
    _get_incluster_token_file,
    _get_incluster_ca_file,
)

urllib3.disable_warnings()
_LOGGER = logging.getLogger(__name__)


class OpenShift:
    """Interaction with OpenShift Master."""

    _DEFAULT_WORKLOAD_LABELS = {"app": "thoth", "operator": "workload"}

    def __init__(
        self,
        *,
        frontend_namespace: str = None,
        middletier_namespace: str = None,
        backend_namespace: str = None,
        infra_namespace: str = None,
        amun_infra_namespace: str = None,
        amun_inspection_namespace: str = None,
        kubernetes_api_url: str = None,
        kubernetes_verify_tls: bool = True,
        openshift_api_url: str = None,
        token: str = None,
        token_file: str = None,
        cert_file: str = None,
        environ: dict = None,
    ):
        """Initialize OpenShift class responsible for handling objects in deployment."""
        environ = environ or os.environ
        try:
            from kubernetes import client, config
            from openshift.dynamic import DynamicClient
            from kubernetes.config.incluster_config import InClusterConfigLoader
            from kubernetes.client.rest import RESTClientObject
        except ImportError as exc:
            raise ImportError(
                "Unable to import OpenShift and Kubernetes packages. Was thoth-common library "
                "installed with openshift extras?"
            ) from exc

        self.kubernetes_verify_tls = bool(
            int(os.getenv("KUBERNETES_VERIFY_TLS", 1)) and kubernetes_verify_tls
        )

        self.in_cluster = True
        # Try to load configuration as used in cluster. If not possible, try to load it from local configuration.
        try:
            # Load in-cluster configuration that is exposed by OpenShift/k8s configuration.
            InClusterConfigLoader(
                token_filename=_get_incluster_token_file(token_file),
                cert_filename=_get_incluster_ca_file(cert_file),
                environ=environ,
            ).load_and_set()

            # We need to explicitly set whether we want to verify SSL/TLS connection to the master.
            configuration = client.Configuration()
            configuration.verify_ssl = self.kubernetes_verify_tls
            self.ocp_client = DynamicClient(
                client.ApiClient(configuration=configuration)
            )
        except Exception as exc:
            _LOGGER.warning(
                "Failed to load in cluster configuration, fallback to a local development setup: %s",
                str(exc),
            )
            k8s_client = config.new_client_from_config()
            k8s_client.configuration.verify_ssl = self.kubernetes_verify_tls
            k8s_client.rest_client = RESTClientObject(k8s_client.configuration)
            self.ocp_client = DynamicClient(k8s_client)
            self.in_cluster = False

        self.amun_inspection_namespace = amun_inspection_namespace or os.getenv(
            "THOTH_AMUN_INSPECTION_NAMESPACE"
        )
        self.amun_infra_namespace = amun_infra_namespace or os.getenv(
            "THOTH_AMUN_INFRA_NAMESPACE"
        )
        self.frontend_namespace = frontend_namespace or os.getenv(
            "THOTH_FRONTEND_NAMESPACE"
        )
        self.middletier_namespace = middletier_namespace or os.getenv(
            "THOTH_MIDDLETIER_NAMESPACE"
        )
        self.backend_namespace = backend_namespace or os.getenv(
            "THOTH_BACKEND_NAMESPACE"
        )
        self.infra_namespace = infra_namespace or os.getenv("THOTH_INFRA_NAMESPACE")
        self.kubernetes_api_url = kubernetes_api_url or os.getenv(
            "KUBERNETES_API_URL", "https://kubernetes.default.svc.cluster.local"
        )
        self.openshift_api_url = openshift_api_url or os.getenv(
            "OPENSHIFT_API_URL", self.ocp_client.configuration.host
        )
        self._token = token

        if not self.kubernetes_verify_tls:
            _LOGGER.warning(
                "TLS verification when communicating with k8s/okd master is disabled"
            )

    @property
    def token(self):
        """Access service account token mounted to the pod."""
        if self._token is None:
            if self.in_cluster:
                self._token = get_service_account_token()
            else:
                # Ugly, but k8s client does not expose a nice API for this.
                self._token = self.ocp_client.configuration.auth_settings()[
                    "BearerToken"
                ]["value"].split(" ")[1]

        return self._token

    @staticmethod
    def _set_env_var(template: dict, **env_var):
        """Set environment in the given template."""
        for env_var_name, env_var_value in env_var.items():
            for entry in template["spec"]["containers"][0]["env"]:
                if entry["name"] == env_var_name:
                    entry["value"] = env_var_value
                    break
            else:
                template["spec"]["containers"][0]["env"].append(
                    {"name": env_var_name, "value": str(env_var_value)}
                )

    @staticmethod
    def set_template_parameters(template: dict, **parameters: object) -> None:
        """Set parameters in the template - replace existing ones or append to parameter list if not exist.

        >>> set_template_parameters(template, THOTH_LOG_ADVISER='DEBUG')
        """
        _LOGGER.debug(
            "Setting parameters for template %r: %s",
            template["metadata"]["name"],
            parameters,
        )

        if "parameters" not in template:
            template["parameters"] = []

        for parameter_name, parameter_value in parameters.items():
            for entry in template["parameters"]:
                if entry["name"] == parameter_name:
                    entry["value"] = (
                        str(parameter_value) if parameter_value is not None else ""
                    )
                    break
            else:
                _LOGGER.warning(
                    "Requested to assign parameter %r (value %r) to template but template "
                    "does not provide the given parameter, forcing...",
                    parameter_name,
                    parameter_value,
                )
                template["parameters"].append(
                    {
                        "name": parameter_name,
                        "value": str(parameter_value)
                        if parameter_value is not None
                        else "",
                    }
                )

    def get_pod_log(self, pod_id: str, namespace: str = None) -> typing.Optional[str]:
        """Get log of a pod based on assigned pod ID."""
        if not namespace:
            if not self.middletier_namespace:
                raise ConfigurationError(
                    "Middletier namespace is required to check log of pods run in this namespace"
                )
            namespace = self.middletier_namespace

        # TODO: rewrite to OpenShift rest client once it will support it.
        endpoint = "{}/api/v1/namespaces/{}/pods/{}/log".format(
            self.openshift_api_url, namespace, pod_id
        )

        response = requests.get(
            endpoint,
            headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            },
            verify=self.kubernetes_verify_tls,
        )
        _LOGGER.debug(
            "Kubernetes master response for pod log (%d): %r",
            response.status_code,
            response.text,
        )

        if response.status_code == 404:
            raise NotFoundException(
                f"Pod with id {pod_id} was not found in namespace {namespace}"
            )

        if response.status_code == 400:
            # If Pod has not been initialized yet, there is returned 400 status code. Return None in this case.
            return None

        response.raise_for_status()
        return response.text

    def get_build(self, build_id: str, namespace: str) -> dict:
        """Get a build in the given namespace."""
        # TODO: rewrite to OpenShift rest client once it will support it.
        endpoint = "{}/apis/build.openshift.io/v1/namespaces/{}/builds/{}".format(
            self.openshift_api_url, namespace, build_id
        )

        response = requests.get(
            endpoint,
            headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            },
            verify=self.kubernetes_verify_tls,
        )

        if response.status_code == 404:
            raise NotFoundException(
                f"Build with id {build_id} was not found in namespace {namespace}"
            )

        _LOGGER.debug(
            "OpenShift master response for build (%d): %r",
            response.status_code,
            response.text,
        )
        response.raise_for_status()

        return response.json()

    def get_buildconfig(self, buildconfig_id: str, namespace: str) -> dict:
        """Get a buildconfig in the given namespace."""
        # TODO: rewrite to OpenShift rest client once it will support it.
        endpoint = "{}/apis/build.openshift.io/v1/namespaces/{}/buildconfigs/{}".format(
            self.openshift_api_url, namespace, buildconfig_id
        )

        response = requests.get(
            endpoint,
            headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            },
            verify=self.kubernetes_verify_tls,
        )

        if response.status_code == 404:
            raise NotFoundException(
                f"BuildConfig with id {buildconfig_id} was not found in namespace {namespace}"
            )

        _LOGGER.debug(
            "OpenShift master response for build (%d): %r",
            response.status_code,
            response.text,
        )
        response.raise_for_status()

        return response.json()

    def get_build_log(self, build_id: str, namespace: str) -> str:
        """Get log of a build in the given namespace."""
        # TODO: rewrite to OpenShift rest client once it will support it.
        endpoint = "{}/apis/build.openshift.io/v1/namespaces/{}/builds/{}/log".format(
            self.openshift_api_url, namespace, build_id
        )

        response = requests.get(
            endpoint,
            headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            },
            verify=self.kubernetes_verify_tls,
        )

        if response.status_code == 404:
            raise NotFoundException(
                f"Build with id {build_id} was not found in namespace {namespace}"
            )

        _LOGGER.debug(
            "OpenShift master response for build log (%d): %r",
            response.status_code,
            response.text,
        )
        response.raise_for_status()

        return response.text

    def get_pod_status(self, pod_id: str, namespace: str) -> dict:
        """Get status entry for a pod - low level routine."""
        import openshift

        try:
            response = self.ocp_client.resources.get(api_version="v1", kind="Pod").get(
                namespace=namespace, name=pod_id
            )
        except openshift.dynamic.exceptions.NotFoundError as exc:
            raise NotFoundException(
                f"The given pod with id {pod_id} could not be found"
            ) from exc

        response = response.to_dict()
        _LOGGER.debug("OpenShift master response for pod status: %r", response)

        if "containerStatuses" not in response["status"]:
            # No status - pod is being scheduled.
            return {}

        state = response["status"]["containerStatuses"][0]["state"]
        # Translate kills of liveness probes to our messages reported to user.
        if (
            state.get("terminated", {}).get("exitCode") == 137
            and state["terminated"]["reason"] == "Error"
        ):
            # Reason can be set by OpenShift to be OOMKilled for example - we expect only "Error" to be set to
            # treat this as timeout.
            state["terminated"]["reason"] = "TimeoutKilled"

        return state

    @staticmethod
    def _status_report(status):
        """Construct status response for API response from master API response."""
        _TRANSLATION_TABLE = {
            "exitCode": "exit_code",
            "finishedAt": "finished_at",
            "reason": "reason",
            "startedAt": "started_at",
            "containerID": "container",
            "message": "reason",
        }

        if len(status.keys()) != 1:
            # If pod was not initialized yet and user asks for status, return default values with state scheduling.
            reported_status = dict.fromkeys(tuple(_TRANSLATION_TABLE.values()))
            reported_status["state"] = "scheduling"
            return reported_status

        state = list(status.keys())[0]

        reported_status = dict.fromkeys(tuple(_TRANSLATION_TABLE.values()))
        reported_status["state"] = state
        for key, value in status[state].items():
            if key == "containerID":
                value = (
                    value[len("docker://"):]
                    if value.startswith("docker://")
                    else value
                )
                reported_status["container"] = value
            else:
                reported_status[_TRANSLATION_TABLE[key]] = value

        return reported_status

    def get_pod_status_report(self, pod_id: str, namespace: str) -> dict:
        """Get pod state and convert it to a user-friendly response."""
        state = self.get_pod_status(pod_id, namespace)
        return self._status_report(state)

    def _get_pod_id_from_job(self, job_id: str, namespace: str) -> str:
        """Get pod name from a job."""
        # Kubernetes automatically adds 'job-name' label -> reuse it.
        response = self.ocp_client.resources.get(api_version="v1", kind="Pod").get(
            namespace=namespace or self.infra_namespace,
            label_selector=f"job-name={job_id}",
        )
        response = response.to_dict()
        _LOGGER.debug("OpenShift response for pod id from job: %r", response)

        if len(response["items"]) != 1:
            if len(response["items"]) > 1:
                # Log this error and report back to user not found.
                _LOGGER.error(
                    f"Multiple pods for the same job name selector {job_id} found"
                )

            raise NotFoundException(f"Job with the given id {job_id} was not found")

        return response["items"][0]["metadata"]["name"]

    def get_configmap(self, configmap_id: str, namespace: str):
        """Get the given configmap in a namespace, return object representing config map."""
        v1_configmap = self.ocp_client.resources.get(api_version="v1", kind="ConfigMap")
        return v1_configmap.get(name=configmap_id, namespace=namespace)

    def get_configmaps(self, namespace: str, label_selector: str) -> dict:
        """Get all configmaps in a namespace and select them by label."""
        v1_configmap = self.ocp_client.resources.get(api_version="v1", kind="ConfigMap")
        return v1_configmap.get(label_selector=label_selector, namespace=namespace)

    def get_job_status_report(self, job_id: str, namespace: str) -> dict:
        """Get status of a pod running inside a job."""
        try:
            job_id = self._get_pod_id_from_job(job_id, namespace)
        except Exception:
            try:
                # Try to retrieve configmap - if we are successful it means we have registered the given
                # job (workload), but it was queued due to resources not being available. This code will go away
                # once we introduce a proper workflow management.
                self.get_configmap(job_id, namespace)
                return {
                    "container": None,
                    "exit_code": None,
                    "finished_at": None,
                    "reason": "WorkloadRegistered",
                    "started_at": None,
                    "state": "registered",
                }
            except Exception:
                pass

            # Raise the original exception as the given pod was not found based on job id.
            raise

        return self.get_pod_status_report(job_id, namespace)

    def get_job_log(self, job_id: str, namespace: str = None) -> str:
        """Get log of a pod running inside a job."""
        pod_id = self._get_pod_id_from_job(job_id, namespace)
        return self.get_pod_log(pod_id, namespace)

    def get_jobs(self, label_selector: str, namespace: str = None) -> dict:
        """Get all Jobs, select them by the provided label."""
        import openshift

        response = None
        try:
            response = self.ocp_client.resources.get(
                api_version="batch/v1", kind="JobList"
            ).get(namespace=namespace, label_selector=label_selector)
        except openshift.dynamic.exceptions.NotFoundError as exc:
            raise NotFoundException(
                f"No Jobs with label {label_selector} could be found"
            ) from exc

        _LOGGER.debug("OpenShift response: %r", response)

        return response

    def _get_template(self, _label_selector: str, namespace: str = None) -> dict:
        """Get template from infra namespace, use label_selector to identify which template to get."""
        response = self.ocp_client.resources.get(
            api_version="template.openshift.io/v1", kind="Template"
        ).get(
            namespace=namespace or self.infra_namespace, label_selector=_label_selector
        )
        _LOGGER.debug(
            "OpenShift response for getting template by label_selector %r: %r",
            _label_selector,
            response.to_dict(),
        )
        self._raise_on_invalid_response_size(response)
        template = response.to_dict()["items"][0]
        return template

    def _get_cronjob(self, _label_selector: str, namespace: str) -> dict:
        """Get template from infra namespace, use label_selector to identify which template to get."""
        response = self.ocp_client.resources.get(
            api_version="batch/v1beta1", kind="CronJob"
        ).get(namespace=namespace, label_selector=_label_selector)
        _LOGGER.debug(
            "OpenShift response for getting CronJob by label_selector %r: %r",
            _label_selector,
            response.to_dict(),
        )
        self._raise_on_invalid_response_size(response)
        template = response.to_dict()["items"][0]
        return template

    @staticmethod
    def _transform_cronjob_to_job(item: dict) -> dict:
        """Turn a CronJob into a job so that it can be directly run."""
        job_spec = item["spec"]["jobTemplate"]
        job_spec["apiVersion"] = "batch/v1"
        job_spec["kind"] = "Job"
        job_spec["metadata"]["generateName"] = item["metadata"]["name"] + "-"
        return job_spec

    def schedule_graph_refresh(self, namespace: str = None):
        """Schedule graph refresh job in frontend namespace by default."""
        if namespace is None:
            if not self.frontend_namespace:
                raise ConfigurationError(
                    "No frontend namespace configured to run graph-refresh job"
                )

            namespace = self.frontend_namespace

        template = self._get_cronjob("component=graph-refresh", namespace=namespace)
        template = self._transform_cronjob_to_job(template)

        # There are no template parameters as we are directly using a cronjob as a template, directly run the job.
        response = self.ocp_client.resources.get(
            api_version=template["apiVersion"], kind=template["kind"]
        ).create(body=template, namespace=namespace)

        response = response.to_dict()
        _LOGGER.debug("OpenShift response for creating job: %r", response)

        return response["metadata"]["name"]

    def create_inspection_imagestream(self, inspection_id: str) -> str:
        """Create imagestream for Amun."""
        if not self.amun_infra_namespace:
            raise ConfigurationError(
                "Amun infra namespace is required in order to create Amun inspection imagestreams"
            )

        if not self.amun_inspection_namespace:
            raise ConfigurationError(
                "Unable to create inspection image stream without Amun inspection namespace being set"
            )

        template = self._get_template(
            "template=amun-inspection-imagestream", self.amun_infra_namespace
        )

        self.set_template_parameters(template, AMUN_INSPECTION_ID=inspection_id)
        template = self.oc_process(self.amun_infra_namespace, template)
        imagestream = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=imagestream["apiVersion"], kind=imagestream["kind"]
        ).create(body=imagestream, namespace=self.amun_inspection_namespace)

        response = response.to_dict()
        _LOGGER.debug("OpenShift response for creating Amun ImageStream: %r", response)

        return response["metadata"]["name"]

    def schedule_inspection_build(
        self, parameters: dict, inspection_id: str, use_hw_template: bool
    ) -> str:
        """Schedule inspection build."""
        if not self.amun_inspection_namespace:
            raise ConfigurationError(
                "Unable to schedule inspection build without Amun inspection namespace being set"
            )

        return self._schedule_workload(
            run_method_name=self.run_inspection_build.__name__,
            template_method_name=self.get_inspection_build_template.__name__,
            template_method_parameters={
                "parameters": parameters,
                "use_hw_template": use_hw_template,
            },
            namespace=self.amun_inspection_namespace,
            labels={"component": "amun-inspection-build", "inspection": inspection_id},
            job_id=inspection_id + "-build",
        )

    def get_inspection_build_template(
        self, use_hw_template: bool, parameters: dict
    ) -> dict:
        """Get inspection buildconfig that should be run."""
        if not self.amun_infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required in order to create inspection imagestreams"
            )

        if not self.amun_inspection_namespace:
            raise ConfigurationError(
                "Unable to create inspection buildconfig without Amun inspection namespace being set"
            )

        if use_hw_template:
            label_selector = "template=amun-inspection-buildconfig-with-cpu"
        else:
            label_selector = "template=amun-inspection-buildconfig"

        template = self._get_template(label_selector, self.amun_infra_namespace)

        self.set_template_parameters(template, **parameters)

        template = self.oc_process(self.amun_inspection_namespace, template)
        return template

    def run_inspection_build(self, template: dict):
        """Run the inspection build."""
        buildconfig = template["objects"][0]
        response = self.ocp_client.resources.get(
            api_version=buildconfig["apiVersion"], kind=buildconfig["kind"]
        ).create(body=buildconfig, namespace=self.amun_inspection_namespace)

        _LOGGER.debug(
            "OpenShift response for creating Amun BuildConfig: %r", response.to_dict()
        )
        return response.metadata.name

    def schedule_inspection_job(
        self,
        inspection_id,
        parameters: dict,
        use_hw_template: bool,
        cpu_requests: str,
        memory_requests: str,
        infra_namespace: str = None,
        registry: str = None,
    ) -> str:
        """Schedule the given job run, the scheduled job is handled by workload operator based resources available."""
        if not self.amun_inspection_namespace:
            raise ConfigurationError(
                "Unable to schedule inspection job without Amun inspection namespace being set"
            )

        parameters = locals()
        parameters.pop("self", None)
        parameters.pop("inspection_id", None)

        return self._schedule_workload(
            run_method_name=self.run_inspection_job.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_inspection_job_template.__name__,
            template_method_parameters={
                "use_hw_template": use_hw_template,
                "cpu_requests": cpu_requests,
                "memory_requests": memory_requests,
            },
            job_id=inspection_id,
            namespace=self.amun_inspection_namespace,
            labels={"component": "amun-inspection"},
        )

    def run_inspection_job(
        self,
        parameters: dict,
        template: dict = None,
        *,
        use_hw_template: bool = False,
        cpu_requests: str = None,
        memory_requests: str = None,
        infra_namespace: str = None,
        registry: str = None,
    ) -> str:
        """Create the actual inspection job."""
        if not self.amun_infra_namespace:
            raise ConfigurationError(
                "Amun infra namespace is required in order to create inspection job"
            )

        # Fill in required fields for image pulling.
        parameters["THOTH_INFRA_NAMESPACE"] = infra_namespace or self.infra_namespace
        if registry:
            parameters["THOTH_REGISTRY"] = registry

        template = template or self.get_inspection_job_template(
            use_hw_template=use_hw_template,
            cpu_requests=cpu_requests,
            memory_requests=memory_requests,
        )
        self.set_template_parameters(template, **parameters)

        template = self.oc_process(self.amun_inspection_namespace, template)
        job = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=job["apiVersion"], kind=job["kind"]
        ).create(body=job, namespace=self.amun_inspection_namespace)

        _LOGGER.debug(
            "OpenShift response for creating Amun Job: %r", response.to_dict()
        )
        return response.metadata.name

    def get_inspection_job_template(
        self,
        *,
        use_hw_template: bool,
        cpu_requests: str = None,
        memory_requests: str = None,
    ) -> dict:
        """Get template for an inspection job."""
        if not self.amun_inspection_namespace:
            raise ConfigurationError(
                "Unable to create inspection job without Amun inspection namespace being set"
            )

        if use_hw_template:
            label_selector = "template=amun-inspection-job-with-cpu"
        else:
            label_selector = "template=amun-inspection-job"

        template = self._get_template(label_selector, self.amun_infra_namespace)

        # We explicitly set template CPU and memory here so that we can schedule based
        # on resources needed in the workload-operator. We cannot do this as a partial oc process,
        # so we explicitly modify template here (other parameters are about to be expanded later).
        container_spec = template["objects"][0]["spec"]["template"]["spec"][
            "containers"
        ][0]

        if cpu_requests:
            container_spec["resources"]["limits"]["cpu"] = cpu_requests
            container_spec["resources"]["requests"]["cpu"] = cpu_requests

        if memory_requests:
            container_spec["resources"]["limits"]["memory"] = memory_requests
            container_spec["resources"]["requests"]["memory"] = memory_requests

        return template

    def get_solver_names(self) -> list:
        """Retrieve name of solvers available in installation."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required in order to list solvers"
            )

        response = self.ocp_client.resources.get(
            api_version="template.openshift.io/v1", kind="Template"
        ).get(namespace=self.infra_namespace, label_selector="template=solver")
        _LOGGER.debug(
            "OpenShift response for getting solver template: %r", response.to_dict()
        )
        self._raise_on_invalid_response_size(response)
        return [
            obj["metadata"]["labels"]["solver-type"]
            for obj in response.to_dict()["items"][0]["objects"]
        ]

    def schedule_all_solvers(
        self,
        packages: str,
        output: str,
        *,
        indexes: list = None,
        debug: bool = False,
        transitive: bool = False,
    ) -> typing.List[str]:
        """Schedule all solvers for the given packages."""
        solver_ids = []
        for solver_name in self.get_solver_names():
            solver_id = self.schedule_solver(
                packages=packages,
                output=output,
                solver=solver_name,
                indexes=indexes,
                debug=debug,
                transitive=transitive,
            )

            solver_ids.append(solver_id)

        return solver_ids

    def run_solver(
        self,
        packages: str,
        output: str,
        solver: str,
        *,
        indexes: list = None,
        debug: bool = False,
        transitive: bool = True,
        job_id: str = None,
        template: dict = None,
    ) -> dict:
        """Run solver or all solver to solve the given requirements."""
        if not self.middletier_namespace:
            ConfigurationError("Solver requires middletier namespace to be specified")

        template = template or self.get_solver_template(solver)

        self.set_template_parameters(
            template,
            THOTH_SOLVER_NO_TRANSITIVE=int(not transitive),
            THOTH_SOLVER_PACKAGES=packages.replace("\n", "\\n"),
            THOTH_SOLVER_INDEXES=",".join(indexes) if indexes else "",
            THOTH_LOG_SOLVER="DEBUG" if debug else "INFO",
            THOTH_SOLVER_OUTPUT=output,
            THOTH_SOLVER_JOB_ID=job_id or self._generate_id(solver),
        )

        template = self.oc_process(self.middletier_namespace, template)
        solver_template = template["objects"][0]
        response = self.ocp_client.resources.get(
            api_version=solver_template["apiVersion"], kind=solver_template["kind"]
        ).create(body=solver_template, namespace=self.middletier_namespace)

        _LOGGER.debug("Starting solver %r", solver)
        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def schedule_solver(
        self,
        packages: str,
        output: str,
        solver: str,
        *,
        indexes: list = None,
        debug: bool = False,
        transitive: bool = True,
        job_id: str = None,
    ) -> str:
        """Schedule the given solver."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule solver job without middletier namespace being set"
            )

        job_id = job_id or self._generate_id(solver)
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_solver.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_solver_template.__name__,
            template_method_parameters={"solver": solver},
            job_id=job_id,
            namespace=self.middletier_namespace,
            labels={"component": "solver"},
        )

    def get_solver_template(self, solver: str) -> dict:
        """Retrieve a solver template."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather solver template when running solver"
            )

        template = self._get_template("template=solver")

        # Get only one solver - the solver that was requested.
        solver_entry = None
        for idx, obj in enumerate(template["objects"]):
            if obj["metadata"]["labels"]["solver-type"] == solver:
                solver_entry = obj
                break

        if solver_entry is None:
            raise ConfigurationError(
                f"No template for solver {solver!r} registered in {self.infra_namespace!r}"
            )

        template["objects"] = [solver_entry]
        return template

    def schedule_package_extract(
        self,
        image: str,
        output: str,
        *,
        environment_type: str,
        origin: str = None,
        registry_user: str = None,
        registry_password: str = None,
        verify_tls: bool = True,
        debug: bool = False,
        job_id: str = None,
    ) -> str:
        """Schedule the given job run, the scheduled job is handled by workload operator based resources available."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule package extract job without middletier namespace being set"
            )

        if environment_type not in ("runtime", "buildtime"):
            raise ValueError(
                "Unknown environment type %r, has to be runtime or buildtime"
            )

        job_id = job_id or self._generate_id("package-extract")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_package_extract.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_package_extract_template.__name__,
            job_id=job_id,
            namespace=self.middletier_namespace,
            labels={"component": "package-extract"},
        )

    def run_package_extract(
        self,
        image: str,
        output: str,
        *,
        environment_type: str,
        origin: str = None,
        registry_user: str = None,
        registry_password: str = None,
        verify_tls: bool = True,
        debug: bool = False,
        job_id: str = None,
        template: dict = None,
    ) -> str:
        """Run package-extract analyzer to extract information from the provided image."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Running package-extract requires middletier namespace to be specified"
            )

        if environment_type not in ("runtime", "buildtime"):
            raise ValueError(
                "Unknown environment type %r, has to be runtime or buildtime"
            )

        template = template or self.get_package_extract_template()

        self.set_template_parameters(
            template,
            THOTH_LOG_PACKAGE_EXTRACT="DEBUG" if debug else "INFO",
            THOTH_ANALYZED_IMAGE=image,
            THOTH_ANALYZER_NO_TLS_VERIFY=int(not verify_tls),
            THOTH_ANALYZER_OUTPUT=output,
            THOTH_PACKAGE_EXTRACT_JOB_ID=job_id or self._generate_id("package-extract"),
            THOTH_PACKAGE_EXTRACT_METADATA=json.dumps(
                {"origin": origin, "environment_type": environment_type}
            ),
        )

        if registry_user and registry_password:
            self.set_template_parameters(
                template,
                THOTH_REGISTRY_CREDENTIALS=f"{registry_user}:{registry_password}",
            )

        template = self.oc_process(self.middletier_namespace, template)
        analyzer = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=analyzer["apiVersion"], kind=analyzer["kind"]
        ).create(body=analyzer, namespace=self.middletier_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_package_extract_template(self):
        """Get template for package-extract."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather package-extract template when running it"
            )

        return self._get_template("template=package-extract")

    def schedule_package_analyzer(
        self,
        package_name: str,
        package_version: str,
        index_url: str,
        *,
        output: str,
        debug: bool = False,
        dry_run: bool = False,
        job_id: str = None,
    ) -> str:
        """Schedule the given job run, the scheduled job is handled by workload operator based resources available."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule package analyzer job without middletier namespace being set"
            )

        job_id = job_id or self._generate_id("package-analyzer")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_package_analyzer.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_package_analyzer_template.__name__,
            job_id=job_id,
            namespace=self.middletier_namespace,
            labels={"component": "package-analyzer"},
        )

    def run_package_analyzer(
        self,
        package_name: str,
        package_version: str,
        index_url: str,
        *,
        output: str,
        debug: bool = False,
        dry_run: bool = False,
        job_id: str = None,
        template: dict = None,
    ) -> str:
        """Run package-analyzer to gather digests of packages and files present inside packages."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Running package-analyzer requires middletier namespace to be specified"
            )

        template = template or self.get_package_analyzer_template()

        self.set_template_parameters(
            template,
            THOTH_PACKAGE_ANALYZER_PACKAGE_NAME=package_name,
            THOTH_PACKAGE_ANALYZER_PACKAGE_VERSION=package_version,
            THOTH_PACKAGE_ANALYZER_INDEX_URL=index_url,
            THOTH_PACKAGE_ANALYZER_DEBUG=debug,
            THOTH_PACKAGE_ANALYZER_OUTPUT=output,
            THOTH_PACKAGE_ANALYZER_DRY_RUN=dry_run,
            THOTH_PACKAGE_ANALYZER_JOB_ID=job_id
            or self._generate_id("package-analyzer"),
        )

        template = self.oc_process(self.middletier_namespace, template)
        analyzer = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=analyzer["apiVersion"], kind=analyzer["kind"]
        ).create(body=analyzer, namespace=self.middletier_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_package_analyzer_template(self):
        """Get template for package-analyzer."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather package-analyzer template when running it"
            )

        return self._get_template("template=package-analyzer")

    def create_config_map(
        self, configmap_name: str, namespace: str, labels: dict, data: dict
    ) -> str:
        """Create a ConfigMap in the given namespace."""
        v1_configmaps = self.ocp_client.resources.get(
            api_version="v1", kind="ConfigMap"
        )
        v1_configmaps.create(
            body={
                "apiVersion": "v1",
                "kind": "ConfigMap",
                "data": data,
                "metadata": {
                    "labels": labels,
                    "name": configmap_name,
                    "namespace": namespace,
                },
            }
        )
        return configmap_name

    def _schedule_workload(
        self,
        *,
        run_method_name: str,
        job_id: str,
        namespace: str,
        template_method_name: str,
        run_method_parameters: dict = None,
        template_method_parameters: dict = None,
        labels: dict = None,
    ) -> str:
        """Schedule the given job run, the scheduled job is handled by workload operator based resources available."""
        if labels:
            # Inject labels needed by default.
            labels.update(self._DEFAULT_WORKLOAD_LABELS)

        self.create_config_map(
            job_id,
            namespace,
            labels=labels or self._DEFAULT_WORKLOAD_LABELS,
            data={
                "run_method_name": run_method_name,
                "run_method_parameters": json.dumps(run_method_parameters or {}),
                "template_method_name": template_method_name,
                "template_method_parameters": json.dumps(
                    template_method_parameters or {}
                ),
            },
        )
        return job_id

    @staticmethod
    def _generate_id(prefix: str):
        """Generate an identifier."""
        return prefix + "-%016x" % random.getrandbits(64)

    def schedule_dependency_monkey(
        self,
        requirements: typing.Union[str, dict],
        context: dict,
        *,
        stack_output: str = None,
        report_output: str = None,
        seed: int = None,
        dry_run: bool = False,
        decision: str = None,
        count: int = None,
        debug: bool = False,
        job_id: str = None,
        limit_latest_versions: int = None,
    ) -> str:
        """Schedule a dependency monkey run."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule dependency monkey without middletier namespace being set"
            )

        job_id = job_id or self._generate_id("dependency-monkey")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_dependency_monkey.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_dependency_monkey_template.__name__,
            job_id=job_id,
            namespace=self.middletier_namespace,
            labels={"component": "dependency-monkey"},
        )

    def run_dependency_monkey(
        self,
        requirements: typing.Union[str, dict],
        context: dict,
        *,
        stack_output: str = None,
        report_output: str = None,
        seed: int = None,
        dry_run: bool = False,
        decision: str = None,
        count: int = None,
        debug: bool = False,
        job_id: str = None,
        limit_latest_versions: int = None,
        template: dict = None,
    ) -> str:
        """Run Dependency Monkey on the provided user input."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Running Dependency Monkey requires middletier namespace configuration"
            )

        template = template or self.get_dependency_monkey_template()

        if isinstance(requirements, dict):
            # There was passed a serialized Pipfile into dict, serialize it into JSON.
            requirements = json.dumps(requirements)

        parameters = {
            "THOTH_ADVISER_REQUIREMENTS": requirements.replace("\n", "\\n"),
            "THOTH_AMUN_CONTEXT": json.dumps(context).replace("\n", "\\n"),
            "THOTH_DEPENDENCY_MONKEY_STACK_OUTPUT": stack_output or "-",
            "THOTH_DEPENDENCY_MONKEY_REPORT_OUTPUT": report_output or "-",
            "THOTH_DEPENDENCY_MONKEY_DRY_RUN": int(bool(dry_run)),
            "THOTH_LOG_ADVISER": "DEBUG" if debug else "INFO",
            "THOTH_DEPENDENCY_MONKEY_JOB_ID": job_id
            or self._generate_id("dependency-monkey"),
        }

        if decision is not None:
            parameters["THOTH_DEPENDENCY_MONKEY_DECISION"] = decision

        if seed is not None:
            parameters["THOTH_DEPENDENCY_MONKEY_SEED"] = seed

        if count is not None:
            parameters["THOTH_DEPENDENCY_MONKEY_COUNT"] = count

        if limit_latest_versions is not None:
            parameters["THOTH_ADVISER_LIMIT_LATEST_VERSIONS"] = limit_latest_versions
        else:
            parameters["THOTH_ADVISER_LIMIT_LATEST_VERSIONS"] = -1

        self.set_template_parameters(template, **parameters)

        template = self.oc_process(self.middletier_namespace, template)
        dependency_monkey = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=dependency_monkey["apiVersion"], kind=dependency_monkey["kind"]
        ).create(body=dependency_monkey, namespace=self.middletier_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_dependency_monkey_template(self):
        """Get template for a dependency monkey."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather Dependency Monkey template when running it"
            )

        return self._get_template("template=dependency-monkey")

    def schedule_build_analyze(
        self, document_id: str, output: str, job_id: str = None
    ) -> str:
        """Schedule an build analyze run."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule build analyze without middletier namespace being set"
            )

        job_id = job_id or self._generate_id("build-analyze")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_build_analyze.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_build_analyze_template.__name__,
            job_id=job_id,
            namespace=self.middletier_namespace,
            labels={"component": "build-analyze"},
        )

    def run_build_analyze(
        self, document_id: str, output: str, job_id: str = None, template: dict = None
    ) -> str:
        """Run build analyze on the provided user input."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Running build-analyze requires middletier namespace configuration"
            )

        template = template or self.get_build_analyze_template()

        parameters = {
            "THOTH_BUILD_LOG_DOC_ID": document_id,
            "THOTH_REPORT_OUTPUT": output,
            "THOTH_BUILD_ANALYZER_JOB_ID": job_id or self._generate_id("build-analyze"),
        }

        self.set_template_parameters(template, **parameters)

        template = self.oc_process(self.middletier_namespace, template)
        build_analyze = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=build_analyze["apiVersion"], kind=build_analyze["kind"]
        ).create(body=build_analyze, namespace=self.middletier_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_build_analyze_template(self):
        """Get template for build analyze run."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather build analyzer template when running it"
            )

        return self._get_template("template=build-analyze")

    def schedule_build_report(
        self, document_id: str, output: str, job_id: str = None
    ) -> str:
        """Schedule an build report run."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule build report without middletier namespace being set"
            )

        job_id = job_id or self._generate_id("build-report")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_build_report.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_build_report_template.__name__,
            job_id=job_id,
            namespace=self.middletier_namespace,
            labels={"component": "build-report"},
        )

    def run_build_report(
        self, document_id: str, output: str, job_id: str = None, template: dict = None
    ) -> str:
        """Run build report on the provided user input."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Running build-report requires middletier namespace configuration"
            )

        template = template or self.get_build_report_template()

        parameters = {
            "THOTH_BUILD_LOG_DOC_ID": document_id,
            "THOTH_REPORT_OUTPUT": output,
            "THOTH_BUILD_ANALYSER_JOB_ID": job_id or self._generate_id("build-report"),
        }

        self.set_template_parameters(template, **parameters)

        template = self.oc_process(self.middletier_namespace, template)
        build_report = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=build_report["apiVersion"], kind=build_report["kind"]
        ).create(body=build_report, namespace=self.middletier_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_build_report_template(self):
        """Get template for build report run."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather build analyzer template when running it"
            )

        return self._get_template("template=build-report")

    def schedule_build_dependencies(
        self, document_id: str, output: str, job_id: str = None
    ) -> str:
        """Schedule an build analyze run."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule build dependencies without middletier namespace being set"
            )

        job_id = job_id or self._generate_id("build-dependencies")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_build_dependencies.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_build_dependencies_template.__name__,
            job_id=job_id,
            namespace=self.middletier_namespace,
            labels={"component": "build-dependencies"},
        )

    def run_build_dependencies(
        self, document_id: str, output: str, job_id: str = None, template: dict = None
    ) -> str:
        """Run build dependencies on the provided user input."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Running build-dependencies requires middletier namespace configuration"
            )

        template = template or self.get_build_dependencies_template()

        parameters = {
            "THOTH_BUILD_LOG_DOC_ID": document_id,
            "THOTH_REPORT_OUTPUT": output,
            "THOTH_BUILD_ANALYZER_JOB_ID": job_id
            or self._generate_id("build-dependencies"),
        }

        self.set_template_parameters(template, **parameters)

        template = self.oc_process(self.middletier_namespace, template)
        build_dependencies = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=build_dependencies["apiVersion"],
            kind=build_dependencies["kind"],
        ).create(body=build_dependencies, namespace=self.middletier_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_build_dependencies_template(self):
        """Get template for build dependencies run."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather build analyzer template when running it"
            )

        return self._get_template("template=build-dependencies")

    def schedule_adviser(
        self,
        application_stack: dict,
        output: str,
        recommendation_type: str,
        *,
        count: int = None,
        limit: int = None,
        runtime_environment: dict = None,
        library_usage: dict = None,
        origin: str = None,
        debug: bool = False,
        job_id: str = None,
        limit_latest_versions: int = None,
    ) -> str:
        """Schedule an adviser run."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Unable to schedule adviser without backend namespace being set"
            )

        job_id = job_id or self._generate_id("adviser")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_adviser.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_adviser_template.__name__,
            job_id=job_id,
            namespace=self.backend_namespace,
            labels={"component": "adviser"},
        )

    def run_adviser(
        self,
        application_stack: dict,
        output: str,
        recommendation_type: str,
        *,
        count: int = None,
        limit: int = None,
        runtime_environment: dict = None,
        library_usage: dict = None,
        origin: str = None,
        debug: bool = False,
        job_id: str = None,
        limit_latest_versions: int = None,
        template: dict = None,
    ) -> str:
        """Run adviser on the provided user input."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Running adviser requires backend namespace configuration"
            )

        template = template or self.get_adviser_template()

        if runtime_environment:
            runtime_environment = json.dumps(runtime_environment)

        parameters = {
            "THOTH_ADVISER_REQUIREMENTS": application_stack.pop("requirements").replace(
                "\n", "\\n"
            ),
            "THOTH_ADVISER_REQUIREMENTS_LOCKED": application_stack.get(
                "requirements_lock", ""
            ).replace("\n", "\\n"),
            "THOTH_ADVISER_REQUIREMENTS_FORMAT": application_stack.get(
                "requirements_formant", "pipenv"
            ),
            "THOTH_ADVISER_RECOMMENDATION_TYPE": recommendation_type.upper(),
            "THOTH_ADVISER_RUNTIME_ENVIRONMENT": runtime_environment,
            "THOTH_ADVISER_LIBRARY_USAGE": json.dumps(library_usage),
            "THOTH_ADVISER_METADATA": json.dumps({"origin": origin}),
            "THOTH_ADVISER_OUTPUT": output,
            "THOTH_LOG_ADVISER": "DEBUG" if debug else "INFO",
            "THOTH_ADVISER_JOB_ID": job_id or self._generate_id("adviser"),
        }

        if count:
            parameters["THOTH_ADVISER_COUNT"] = count

        if limit:
            parameters["THOTH_ADVISER_LIMIT"] = limit

        if limit_latest_versions is not None:
            parameters["THOTH_ADVISER_LIMIT_LATEST_VERSIONS"] = limit_latest_versions
        else:
            parameters["THOTH_ADVISER_LIMIT_LATEST_VERSIONS"] = -1

        self.set_template_parameters(template, **parameters)

        template = self.oc_process(self.backend_namespace, template)
        adviser = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=adviser["apiVersion"], kind=adviser["kind"]
        ).create(body=adviser, namespace=self.backend_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_adviser_template(self):
        """Get template for an adviser run."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather adviser template when running it"
            )

        return self._get_template("template=adviser")

    def schedule_provenance_checker(
        self,
        application_stack: dict,
        output: str,
        *,
        origin: str = None,
        whitelisted_sources: list = None,
        debug: bool = False,
        job_id: str = None,
    ) -> str:
        """Schedule a provenance checker run."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Unable to schedule provenance checker without backend namespace being set"
            )

        job_id = job_id or self._generate_id("provenance-checker")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_provenance_checker.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_provenance_checker_template.__name__,
            job_id=job_id,
            namespace=self.backend_namespace,
            labels={"component": "provenance-checker"},
        )

    def run_provenance_checker(
        self,
        application_stack: dict,
        output: str,
        *,
        origin: str = None,
        whitelisted_sources: list = None,
        debug: bool = False,
        job_id: str = None,
        template: dict = None,
    ) -> str:
        """Run provenance checks on the provided user input."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Running provenance checks requires backend namespace configuration"
            )

        template = template or self.get_provenance_checker_template()

        requirements = application_stack.pop("requirements").replace("\n", "\\n")
        requirements_locked = application_stack.pop("requirements_lock").replace(
            "\n", "\\n"
        )
        whitelisted_sources = ",".join(whitelisted_sources or [])
        self.set_template_parameters(
            template,
            THOTH_ADVISER_REQUIREMENTS=requirements,
            THOTH_ADVISER_REQUIREMENTS_LOCKED=requirements_locked,
            THOTH_ADVISER_OUTPUT=output,
            THOTH_ADVISER_METADATA=json.dumps({"origin": origin}),
            THOTH_WHITELISTED_SOURCES=whitelisted_sources,
            THOTH_LOG_ADVISER="DEBUG" if debug else "INFO",
            THOTH_PROVENANCE_CHECKER_JOB_ID=job_id
            or self._generate_id("provenance-checker"),
        )

        template = self.oc_process(self.backend_namespace, template)
        provenance_checker = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=provenance_checker["apiVersion"],
            kind=provenance_checker["kind"],
        ).create(body=provenance_checker, namespace=self.backend_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_provenance_checker_template(self) -> dict:
        """Get template for a provenance checker."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather provenance template when running it"
            )

        return self._get_template("template=provenance-checker")

    def _schedule_graph_sync(
        self,
        document_id: str,
        *,
        force_sync: bool,
        namespace: str,
        graph_sync_type: str,
    ):
        """Schedule a graph sync."""
        job_id = "graph-sync-" + document_id
        parameters = locals()
        parameters.pop("self", None)

        if namespace is None:
            raise ConfigurationError(
                "No namespace provided - in the environment nor explcitly on graph sync "
                f"scheduling for {document_id} (graph sync type: {graph_sync_type!r})"
            )

        return self._schedule_workload(
            run_method_name=self.run_graph_sync.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_graph_sync_template.__name__,
            template_method_parameters={},
            job_id=job_id,
            namespace=namespace,
            labels={
                "component": "graph-sync",
                "graph-sync-type": graph_sync_type,
                "graph-sync-document-id": document_id,
            },
        )

    def schedule_graph_sync_adviser(
        self, document_id: str, *, force_sync: bool = False, namespace: str = None
    ) -> str:
        """Schedule a sync of an adviser document."""
        if not document_id.startswith("adviser"):
            raise ValueError(
                f"Cannot sync document {document_id!r} as adviser document - document is not adviser result"
            )

        return self._schedule_graph_sync(
            document_id,
            namespace=namespace or self.backend_namespace,
            graph_sync_type="adviser",
            force_sync=force_sync,
        )

    def schedule_graph_sync_package_analyzer(
        self, document_id: str, *, force_sync: bool = False, namespace: str = None
    ) -> str:
        """Schedule a sync of an package-analysis document."""
        if not document_id.startswith("package-analyzer"):
            raise ValueError(
                f"Cannot sync document {document_id!r} as package-analyzer document - document "
                "is not package-analyzer result"
            )

        return self._schedule_graph_sync(
            document_id,
            namespace=namespace or self.middletier_namespace,
            graph_sync_type="package-analyzer",
            force_sync=force_sync,
        )

    def schedule_graph_sync_inspection(
        self, document_id: str, *, force_sync: bool = False, namespace: str = None
    ) -> str:
        """Schedule a sync of inspection."""
        if not document_id.startswith("inspection"):
            raise ValueError(
                f"Cannot sync document {document_id!r} as inspection document - document is not inspection result"
            )

        return self._schedule_graph_sync(
            document_id,
            namespace=namespace or self.amun_inspection_namespace,
            graph_sync_type="inspection",
            force_sync=force_sync,
        )

    def schedule_graph_sync_provenance_checker(
        self, document_id: str, *, force_sync: bool = False, namespace: str = None
    ) -> str:
        """Schedule a sync of a provenance checker result."""
        if not document_id.startswith("provenance-checker"):
            raise ValueError(
                f"Cannot sync document {document_id!r} as provenance checker document - document is not"
                "provenance checker result"
            )

        return self._schedule_graph_sync(
            document_id,
            namespace=namespace or self.backend_namespace,
            graph_sync_type="provenance-checker",
            force_sync=force_sync,
        )

    def schedule_graph_sync_solver(
        self, document_id: str, *, force_sync: bool = False, namespace: str = None
    ) -> str:
        """Schedule a sync of solver result."""
        if not document_id.startswith("solver"):
            raise ValueError(
                f"Cannot sync document {document_id!r} as solver document - document is not solver result"
            )

        return self._schedule_graph_sync(
            document_id,
            namespace=namespace or self.middletier_namespace,
            graph_sync_type="solver",
            force_sync=force_sync,
        )

    def schedule_graph_dependency_monkey(
        self, document_id: str, *, force_sync: bool = False, namespace: str
    ) -> str:
        """Schedule a sync of a dependency monkey result."""
        if not document_id.startswith("dependency-monkey"):
            raise ValueError(
                f"Cannot sync document {document_id!r} as dependency monkey "
                "document - document is not solver result"
            )

        return self._schedule_graph_sync(
            document_id,
            namespace=namespace or self.middletier_namespace,
            graph_sync_type="dependency-monkey",
            force_sync=force_sync,
        )

    def schedule_graph_sync_package_extract(
        self, document_id: str, *, force_sync: bool = False, namespace: str = None
    ) -> str:
        """Schedule a sync of package-extract."""
        if not document_id.startswith("package-extract"):
            raise ValueError(
                f"Cannot sync document {document_id!r} as package-extract document - document "
                f"is not package-extract result"
            )

        return self._schedule_graph_sync(
            document_id,
            namespace=namespace or self.middletier_namespace,
            graph_sync_type="package-extract",
            force_sync=force_sync,
        )

    def run_graph_sync(
        self,
        document_id: str,
        namespace: str,
        graph_sync_type: str,
        force_sync: str,
        *,
        template: dict = None,
        job_id: str = None,
    ):
        """Run the given graph sync."""
        if not namespace:
            raise ValueError(
                "Unable to run graph sync without namespace being specified"
            )

        template = template or self.get_graph_sync_template()
        self.set_template_parameters(
            template,
            THOTH_SYNC_DOCUMENT_ID=document_id,
            THOTH_JOB_ID=job_id or self._generate_id(graph_sync_type),
            THOTH_FORCE_SYNC=force_sync,
            THOTH_GRAPH_SYNC_TYPE=graph_sync_type,
        )
        template = self.oc_process(namespace, template)
        graph_sync = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=graph_sync["apiVersion"], kind=graph_sync["kind"]
        ).create(body=graph_sync, namespace=namespace)

        _LOGGER.info("Scheduled new sync with id %r", response.metadata.name)
        return response.metadata.name

    def get_graph_sync_template(self) -> dict:
        """Get graph sync template."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required in order to gather graph sync template"
            )

        return self._get_template("template=graph-sync-job")

    def schedule_kebechet_run_url(
        self, url: str, service: str, *, verbose=False, job_id=None
    ) -> str:
        """Schedule a kebechet run."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Unable to schedule Kebechet without backend namespace being set"
            )

        job_id = job_id or self._generate_id("kebechet-run-url")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_kebechet_run_url.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_kebechet_template.__name__,
            job_id=job_id,
            namespace=self.backend_namespace,
            labels={"component": "kebechet"},
        )

    def schedule_kebechet_run_results(
        self, url: str, service: str, analysis_id: str, *, verbose=False, job_id=None
    ) -> str:
        """Schedule a kebechet run."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Unable to schedule Kebechet without backend namespace being set"
            )

        job_id = job_id or self._generate_id("kebechet-run-results")
        parameters = locals()
        parameters.pop("self", None)
        return self._schedule_workload(
            run_method_name=self.run_kebechet_run_results.__name__,
            run_method_parameters=parameters,
            template_method_name=self.get_kebechet_template.__name__,
            job_id=job_id,
            namespace=self.backend_namespace,
            labels={"component": "kebechet"},
        )

    def run_kebechet_run_url(
        self,
        url: str,
        service: str,
        *,
        verbose=False,
        job_id=None,
        template: dict = None,
    ) -> str:
        """Create a kebechet run-url job."""
        job_id = job_id or self._generate_id("kebechet-run-url")
        template = template or self.get_kebechet_template()
        self.set_template_parameters(
            template,
            KEBECHET_SUBCOMMAND="run-url",
            KEBECHET_VERBOSE=verbose,
            KEBECHET_REPO_URL=url,
            KEBECHET_SERVICE_NAME=service,
            KEBECHET_JOB_ID=job_id,
        )
        template = self.oc_process(self.backend_namespace, template)
        kebechet = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=kebechet["apiVersion"], kind=kebechet["kind"]
        ).create(body=kebechet, namespace=self.backend_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def run_kebechet_run_results(
        self,
        url: str,
        service: str,
        analysis_id: str,
        *,
        verbose=False,
        job_id=None,
        template: dict = None,
    ) -> str:
        """Create a kebechet run-results job."""
        job_id = job_id or self._generate_id("kebechet-run-results")
        template = template or self.get_kebechet_template()
        self.set_template_parameters(
            template,
            KEBECHET_SUBCOMMAND="run-results",
            KEBECHET_VERBOSE=verbose,
            KEBECHET_REPO_URL=url,
            KEBECHET_SERVICE_NAME=service,
            KEBECHET_JOB_ID=job_id,
            KEBECHET_ANALYSIS_ID=analysis_id,
        )
        template = self.oc_process(self.backend_namespace, template)
        kebechet = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=kebechet["apiVersion"], kind=kebechet["kind"]
        ).create(body=kebechet, namespace=self.backend_namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def get_kebechet_template(self) -> dict:
        """Get template for a Kebechet job."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather kebechet template when running it"
            )

        return self._get_template("template=kebechet")

    def _raise_on_invalid_response_size(self, response):
        """Expect that there is only one object type for the given item."""
        if len(response.items) != 1:
            raise RuntimeError(
                f"Application misconfiguration - number of templates available in the infra namespace "
                f"{self.infra_namespace!r} is {len(response.items)}, should be 1."
            )

            # TODO add name of template we were looking for...

    def oc_process(self, namespace: str, template: dict) -> dict:
        """Process the given template in OpenShift."""
        # TODO: This does not work - see issue reported upstream:
        #   https://github.com/openshift/openshift-restclient-python/issues/190
        # return TemplateOpenshiftIoApi().create_namespaced_processed_template_v1(namespace, template)
        endpoint = "{}/apis/template.openshift.io/v1/namespaces/{}/processedtemplates".format(
            self.openshift_api_url, namespace
        )
        response = requests.post(
            endpoint,
            json=template,
            headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            },
            verify=self.kubernetes_verify_tls,
        )
        _LOGGER.debug(
            "OpenShift master response template (%d): %r",
            response.status_code,
            response.text,
        )

        try:
            response.raise_for_status()
        except Exception:
            _LOGGER.error("Failed to process template: %s", response.text)
            raise

        return response.json()

    @staticmethod
    def parse_cpu_spec(cpu_spec: typing.Optional[str]) -> typing.Optional[float]:
        """Parse the given CPU requirement as used by OpenShift/Kubernetes."""
        if isinstance(cpu_spec, str):
            if cpu_spec.endswith("m"):
                cpu_spec = cpu_spec[:-1]
                return int(cpu_spec) / 1000

        if cpu_spec is None:
            return None

        return float(cpu_spec)

    @staticmethod
    def parse_memory_spec(memory_spec: typing.Optional[str]) -> typing.Optional[float]:
        """Parse the given CPU requirement as used by OpenShift/Kubernetes."""
        if isinstance(memory_spec, (float, int)):
            return float(memory_spec)

        if memory_spec is None:
            return None

        if memory_spec.endswith("E"):
            memory_spec = float(memory_spec[:-1])
            return memory_spec * 1000 ** 6
        elif memory_spec.endswith("P"):
            memory_spec = float(memory_spec[:-1])
            return memory_spec * 1000 ** 5
        elif memory_spec.endswith("T"):
            memory_spec = float(memory_spec[:-1])
            return memory_spec * 1000 ** 4
        elif memory_spec.endswith("G"):
            memory_spec = float(memory_spec[:-1])
            return memory_spec * 1000 ** 3
        elif memory_spec.endswith("M"):
            memory_spec = float(memory_spec[:-1])
            return memory_spec * 1000 ** 2
        elif memory_spec.endswith("K"):
            memory_spec = float(memory_spec[:-1])
            return memory_spec * 1000
        elif memory_spec.endswith("Ei"):
            memory_spec = float(memory_spec[:-2])
            return memory_spec * 1024 ** 6
        elif memory_spec.endswith("Pi"):
            memory_spec = float(memory_spec[:-2])
            return memory_spec * 1024 ** 5
        elif memory_spec.endswith("Ti"):
            memory_spec = float(memory_spec[:-2])
            return memory_spec * 1024 ** 4
        elif memory_spec.endswith("Gi"):
            memory_spec = float(memory_spec[:-2])
            return memory_spec * 1024 ** 3
        elif memory_spec.endswith("Mi"):
            memory_spec = float(memory_spec[:-2])
            return memory_spec * 1024 ** 2
        elif memory_spec.endswith("Ki"):
            memory_spec = float(memory_spec[:-2])
            return memory_spec * 1024

    def get_quota_status(self, namespace: str):
        """Get quota status.

        For now, there is retrieved a very first quota specification and its status from resource quota list, we
        gather information about memory, CPU usage and number of pods.
        """
        # TODO: rewrite to OpenShift REST client
        endpoint = "{}/api/v1/namespaces/{}/resourcequotas".format(
            self.openshift_api_url, namespace
        )
        response = requests.get(
            endpoint,
            headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            },
            verify=self.kubernetes_verify_tls,
        )
        _LOGGER.debug(
            "OpenShift master response for quota (%d): %r",
            response.status_code,
            response.text,
        )

        try:
            response.raise_for_status()
        except Exception:
            _LOGGER.error("Failed to obtain quota: %s", response.text)
            raise

        if len(response.json()["items"]) != 1:
            raise ValueError(f"No or multiple cluster resources configured in namespace {namespace!r}")

        # We get a very first item for now.
        status = response.json()["items"][0]["status"]
        pods_used = status["used"].get("pods")
        pods_hard = status["hard"].get("pods")

        result = {
            "used": {
                "cpu": self.parse_cpu_spec(status["used"].get("limits.cpu")) or 0,
                "memory": self.parse_memory_spec(status["used"].get("limits.memory"))
                or 0,
                "pods": int(pods_used) if pods_used is not None else None,
            },
            "hard": {
                "cpu": self.parse_cpu_spec(status["hard"].get("limits.cpu")) or 0,
                "memory": self.parse_memory_spec(status["hard"].get("limits.memory"))
                or 0,
                "pods": int(pods_hard) if pods_hard is not None else None,
            },
        }

        return result

    def can_run_workload(self, template: dict, namespace: str) -> bool:
        """Check if the given (job) can be run in the given namespace based on mem, cpu and pod restrictions."""
        quota_status = self.get_quota_status(namespace)
        if (
            quota_status["hard"]["pods"] is not None
            and quota_status["used"]["pods"] + 1 > quota_status["hard"]["pods"]
        ):
            _LOGGER.debug("Cannot run workload, no pods available")
            return False

        template_name = template["metadata"]["name"]

        if template["objects"][0]["kind"] == "Job":
            cpu_requested, mem_requested = self._get_job_requests(template)
        elif template["objects"][0]["kind"] == "BuildConfig":
            cpu_requested, mem_requested = self._get_build_requests(template)
        else:
            raise ValueError(
                f"Unable to handle template {template_name} - no requests gathering method defined for "
                f"workload of type {template['objects'][0]['kind']}"
            )

        if (
            quota_status["used"]["memory"] + mem_requested
            > quota_status["hard"]["memory"]
        ):
            _LOGGER.debug("Cannot run workload %r, no memory available", template_name)

            return False

        if quota_status["used"]["cpu"] + cpu_requested > quota_status["hard"]["cpu"]:
            _LOGGER.debug("Cannot run workload %r, no CPU available", template_name)
            return False

        return True

    def _get_job_requests(self, template) -> tuple:
        """Get resources needed for running a workload of type Job."""
        template_name = template["metadata"]["name"]

        if len(template["objects"]) > 1:
            _LOGGER.warning(
                "Template %r has multiple pods defined, only the first will be considered in workload computation",
                template_name,
            )

        pod_mem_requested = 0
        pod_cpu_requested = 0
        for container in template["objects"][0]["spec"]["template"]["spec"][
            "containers"
        ]:
            container_mem_requested = (
                container.get("resources", {}).get("requests", {}).get("memory", 0)
            )
            if not container_mem_requested:
                _LOGGER.warning(
                    "No memory requests for container %r in template %r",
                    container["name"],
                    template_name,
                )
            else:
                container_mem_requested = self.parse_memory_spec(
                    container_mem_requested
                )
                if container_mem_requested is not None:
                    pod_mem_requested += container_mem_requested

            container_cpu_requested = (
                container.get("resources", {}).get("requests", {}).get("cpu", 0)
            )
            if not container_cpu_requested:
                _LOGGER.warning(
                    "No CPU requests for container %r in template %r",
                    container["name"],
                    template_name,
                )
            else:
                container_cpu_requested = self.parse_cpu_spec(container_cpu_requested)
                if container_cpu_requested is not None:
                    pod_cpu_requested += container_cpu_requested

        return pod_cpu_requested, pod_mem_requested

    def _get_build_requests(self, template: dict) -> tuple:
        """Get resources needed for running a workload of type BuildConfig (running the build)."""
        template_name = template["metadata"]["name"]
        if len(template["objects"]) != 1:
            _LOGGER.warning(
                "Template %r has multiple objects defined, only the first will be considered in workload computation",
                template_name,
            )

        build_memory = (
            template["objects"][0]["spec"]
            .get("resources", {})
            .get("requests", {})
            .get("memory", 0)
        )
        if not build_memory:
            _LOGGER.warning(
                "No memory requests for build in template %r", template_name
            )
        else:
            build_memory = self.parse_memory_spec(build_memory)

        build_cpu = (
            template["objects"][0]["spec"]
            .get("resources", {})
            .get("requests", {})
            .get("cpu", 0)
        )
        if not build_cpu:
            _LOGGER.warning("No CPU requests for build in template %r", template_name)
        else:
            build_cpu = self.parse_cpu_spec(build_cpu)

        return build_cpu, build_memory

    def get_job_status_count(self, label_selector: str, namespace: str) -> dict:
        """Count the number of Jobs per status in a specific namespace."""
        response = self.get_jobs(label_selector=label_selector, namespace=namespace)
        status = [
            "created",
            "active",
            "failed",
            "succeeded",
            "pending",
            "retry",
            "waiting",
            "started",
        ]

        # Initialize
        jobs_status_count = dict.fromkeys(status, 0)

        # Count jobs per status
        for item in response["items"]:
            jobs_status_count["created"] += 1

            if "succeeded" in item["status"].keys():
                jobs_status_count["succeeded"] += 1
            elif "failed" in item["status"].keys():
                jobs_status_count["failed"] += 1
            elif "active" in item["status"].keys():
                jobs_status_count["active"] += 1
            elif "pending" in item["status"].keys():
                jobs_status_count["pending"] += 1
            elif not item["status"].keys():
                jobs_status_count["waiting"] += 1
            elif "startTime" in item["status"].keys() and len(item["status"].keys()) == 1:
                jobs_status_count["started"] += 1
            else:
                try:
                    if "BackoffLimitExceeded" in item["status"]["conditions"][0]["reason"]:
                        jobs_status_count["retry"] += 1
                except Exception as excptn:
                    _LOGGER.error("Unknown job status %r", item)
                    _LOGGER.exception(excptn)

        return jobs_status_count
