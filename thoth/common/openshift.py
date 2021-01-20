#!/usr/bin/env python3
# thoth-common
# Copyright(C) 2018, 2019, 2020 Fridolin Pokorny
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
import datetime
import logging
import requests
import typing
import json
import random
import urllib3

from urllib.parse import urlparse

from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from openshift.dynamic.exceptions import NotFoundError as OpenShiftNotFoundError
from .exceptions import ThothCommonException
from .exceptions import NotKnownThothIntegration
from .exceptions import QebHwtInputsMissing
from .exceptions import KebechetInputsMissing
from .exceptions import NotFoundException
from .exceptions import ConfigurationError
from .exceptions import SolverNameParseError
from .helpers import (
    _get_incluster_ca_file,
    _get_incluster_token_file,
    get_service_account_token,
    normalize_os_version,
)
from .enums import ThothAdviserIntegrationEnum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .workflows import WorkflowManager

urllib3.disable_warnings()
_LOGGER = logging.getLogger(__name__)


class OpenShift:
    """Interaction with OpenShift Master."""

    _DEFAULT_WORKLOAD_LABELS = {"app": "thoth", "operator": "workload"}

    def __init__(
        self,
        *,
        frontend_namespace: Optional[str] = None,
        middletier_namespace: Optional[str] = None,
        backend_namespace: Optional[str] = None,
        infra_namespace: Optional[str] = None,
        amun_infra_namespace: Optional[str] = None,
        amun_inspection_namespace: Optional[str] = None,
        kubernetes_api_url: Optional[str] = None,
        kubernetes_verify_tls: bool = True,
        openshift_api_url: Optional[str] = None,
        token: Optional[str] = None,
        token_file: Optional[str] = None,
        cert_file: Optional[str] = None,
        environ: Optional[Dict[str, str]] = None,
    ):
        """Initialize OpenShift class responsible for handling objects in deployment."""
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
                environ=environ or os.environ,
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

        self.configuration = self.ocp_client.configuration

        # TODO: Update openshift.
        # These parameters are missing in openshift configuration, but required for Argo API validation
        self.configuration.retries = 5
        self.configuration.client_side_validation = True

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
        self._workflow_manager: Optional["WorkflowManager"] = None

    @property
    def token(self) -> str:
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

    @property
    def workflow_manager(
        self,
    ) -> "WorkflowManager":  # by using a string here we create a forward reference
        """Return WorkflowManager instance.

        This property lazily initializes the WorkflowManager.
        """
        if self._workflow_manager is None:
            from .workflows import WorkflowManager

            self._workflow_manager = WorkflowManager(openshift=self)
        return self._workflow_manager

    @classmethod
    def parse_python_solver_name(cls, solver_name: str) -> Dict[str, Any]:
        """Parse os and Python identifiers encoded into solver name."""
        if solver_name.startswith("solver-"):
            solver_identifiers = solver_name[len("solver-") :]
        else:
            raise SolverNameParseError(
                f"Solver name has to start with 'solver-' prefix: {solver_name!r}"
            )

        parts = solver_identifiers.split("-")
        if len(parts) != 3:
            raise SolverNameParseError(
                "Solver should be in a form of 'solver-<os_name>-<os_version>-<python_version>, "
                f"solver name {solver_name!r} does not correspond to this naming schema"
            )

        python_version = parts[2]
        if python_version.startswith("py"):
            python_version = python_version[len("py") :]
        else:
            raise SolverNameParseError(
                f"Python version encoded into Python solver name does not start with 'py' prefix: {solver_name!r}"
            )

        python_version = ".".join(list(python_version))
        return {
            "os_name": parts[0],
            "os_version": normalize_os_version(parts[0], parts[1]),
            "python_version": python_version,
        }

    @classmethod
    def obtain_solver_from_runtime_environment(
        cls, runtime_environment: Dict[str, Any]
    ) -> Optional[str]:
        """Define solver from runtime_environment."""
        solver = None
        operating_system = runtime_environment.get("operating_system", {})

        if not operating_system:
            return solver

        os_name = runtime_environment["operating_system"].get("name")
        os_version = normalize_os_version(
            operating_system.get("name"), operating_system.get("version")
        )
        python_version = runtime_environment.get("python_version")

        if not os_name or not os_version:
            return solver

        if python_version is not None:
            solver = (
                f"solver-{os_name}-{os_version}-py{python_version.replace('.', '')}"
            )
        else:
            solver = f"solver-{os_name}-{os_version}"

        cls.parse_python_solver_name(solver)

        return solver

    @staticmethod
    def _set_env_var(template: Dict[str, Any], **env_var: str) -> None:
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
    def set_template_parameters(template: Dict[str, Any], **parameters: Any) -> None:
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

    def get_pod_log(
        self,
        pod_id: str,
        namespace: Optional[str] = None,
        container: Optional[str] = None,
    ) -> Optional[str]:
        """Get log of a pod based on assigned pod ID."""
        if not namespace:
            if not self.middletier_namespace:
                raise ConfigurationError(
                    "Middletier namespace is required to check log of pods run in this namespace"
                )
            namespace = self.middletier_namespace

        params = None
        if container:
            params = {"container": container}

        # TODO: rewrite to OpenShift rest client once it will support it.
        endpoint = "{}/api/v1/namespaces/{}/pods/{}/log".format(
            self.openshift_api_url,
            namespace,
            pod_id,
        )

        response = requests.get(
            endpoint,
            headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            },
            verify=self.kubernetes_verify_tls,
            params=params,
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

        if (
            response.status_code == 400
            and "a container name must be specified for pod"
            not in response.json()["message"]
        ):
            # If Pod has not been initialized yet, there is returned 400 status code. Return None in this case.
            return None
        elif response.status_code == 400:
            raise ThothCommonException(
                f"Failed to obtain logs, container name has to be specified: {response.json()['message']}"
            )

        try:
            response.raise_for_status()
        except Exception as exc:
            _LOGGER.error("Error response when obtaining pod logs: %r", response.json())
            raise ThothCommonException(
                f"Failed to obtain logs for pod: {str(exc)}"
            ) from exc

        return response.text

    def get_workflow_pod_name(
        self, node_name: str, workflow_id: str, namespace: str
    ) -> str:
        """Get pod name where task is being executed."""
        workflow = self.get_workflow(workflow_id, namespace=namespace)
        nodes = workflow.get("status", {}).get("nodes", {})

        for pod_name, node_info in nodes.items():
            if node_info["displayName"] == node_name:
                return pod_name  # type: ignore

        raise NotFoundException(
            f"No node named {node_name!r} found in workflow {workflow_id!r} in namespace {namespace!r}"
        )

    def get_workflow_node_log(
        self, node_name: str, workflow_id: str, namespace: str
    ) -> Optional[str]:
        """Get log from a task/node in a workflow."""
        pod_name = self.get_workflow_pod_name(node_name, workflow_id, namespace)
        return self.get_pod_log(pod_name, namespace=namespace, container="main")

    def get_workflow_node_status(
        self, node_name: str, workflow_id: str, namespace: str
    ) -> Dict[str, Any]:
        """Get status from a task/node in a workflow."""
        pod_id = self.get_workflow_pod_name(node_name, workflow_id, namespace)
        return self.get_pod_status(pod_id, namespace)

    def get_build(self, build_id: str, namespace: str) -> Dict[str, Any]:
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

        result: Dict[str, Any] = response.json()
        return result

    def get_buildconfig(self, buildconfig_id: str, namespace: str) -> Dict[str, Any]:
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

        result: Dict[str, Any] = response.json()
        return result

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

    def get_pod_status(self, pod_id: str, namespace: str) -> Dict[str, Any]:
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

        state: Dict[str, Any] = response["status"]["containerStatuses"][0]["state"]
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
    def _status_report(status: Dict[str, Dict[str, str]]) -> Dict[str, Optional[str]]:
        """Construct status response for API response from master API response."""
        _TRANSLATION_TABLE = {  # noqa
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
                    value[len("docker://") :]
                    if value.startswith("docker://")
                    else value
                )
                reported_status["container"] = value
            else:
                reported_status[_TRANSLATION_TABLE[key]] = value

        return reported_status

    def get_pod_status_report(
        self, pod_id: str, namespace: str
    ) -> Dict[str, Optional[str]]:
        """Get pod state and convert it to a user-friendly response."""
        state = self.get_pod_status(pod_id, namespace)
        return self._status_report(state)

    def _get_pod_id_from_job(self, job_id: str, namespace: str) -> str:
        """Get a single pod name from a job."""
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

        result: str = response["items"][0]["metadata"]["name"]

        return result

    def _get_pod_ids_from_job(self, job_id: str, namespace: str) -> List[str]:
        """Get multiple pod names from a job.

        This function is useful for a Job which schedules multiple pods, i.e.
        when run to completion.
        """
        # Kubernetes automatically adds 'job-name' label -> reuse it.
        response = self.ocp_client.resources.get(api_version="v1", kind="Pod").get(
            namespace=namespace or self.infra_namespace,
            label_selector=f"job-name={job_id}",
        )
        response = response.to_dict()
        _LOGGER.debug("OpenShift response for pod ids from job: %r", response)

        if not len(response.get("items", [])):
            raise NotFoundException(f"Job with the given id {job_id} was not found")

        result: List[str] = [pod["metadata"]["name"] for pod in response["items"]]

        return result

    def get_configmap(self, configmap_id: str, namespace: str) -> Dict[str, Any]:
        """Get the given configmap in a namespace, return object representing config map."""
        v1_configmap = self.ocp_client.resources.get(api_version="v1", kind="ConfigMap")
        try:
            result: Dict[str, Any] = v1_configmap.get(
                name=configmap_id, namespace=namespace
            )
            return result
        except OpenShiftNotFoundError as exc:
            raise NotFoundException(
                f"Configmap {configmap_id!r} not found in namespace {namespace!r}"
            ) from exc

    def get_configmaps(self, namespace: str, label_selector: str) -> Dict[str, Any]:
        """Get all configmaps in a namespace and select them by label."""
        v1_configmap = self.ocp_client.resources.get(api_version="v1", kind="ConfigMap")
        result: Dict[str, Any] = v1_configmap.get(
            label_selector=label_selector, namespace=namespace
        )
        return result

    def get_image_streams(self, namespace: str, label_selector: str) -> Dict[str, Any]:
        """Get all image streams in a namespace and select them by label."""
        v1_image_streams = self.ocp_client.resources.get(
            api_version="image.openshift.io/v1", kind="ImageStream"
        )
        result: Dict[str, Any] = v1_image_streams.get(
            label_selector=label_selector, namespace=namespace
        )
        return result

    def get_job_status(self, job_id: str, namespace: str) -> Dict[str, Any]:
        """Get status of a Job and Pods created by the Job.

        :raises: NotFoundError if no Job of such name is found in the namespace
        """
        _TRANSLATION_TABLE = {  # noqa
            "startTime": "started_at",
            "completionTime": "finished_at",
        }

        job_status: Dict[str, Any] = {}
        try:
            resources = self.ocp_client.resources.get(
                api_version="batch/v1", kind="Job"
            )

            job: Dict[str, Any] = resources.get(name=job_id, namespace=namespace)
            for k, v in job["status"].items():
                if k == "conditions":
                    # conditions are discarded
                    continue
                job_status[_TRANSLATION_TABLE.get(k, k)] = v

            # add completions information so that we can determine whether
            # the Job is already finished according to the number of `succeeded`
            # pods
            job_status["completions"] = job["spec"]["completions"]

        except OpenShiftNotFoundError as exc:
            raise NotFoundException(
                f"Job {job_id!r} not found in namespace {namespace!r}"
            ) from exc

        return job_status

    def get_job_status_report(
        self, job_id: str, namespace: str
    ) -> Dict[str, Optional[str]]:
        """Get status report of a Job and Pods created by the Job."""
        report: Dict[str, Any] = self.get_job_status(job_id, namespace)

        pod_ids: List[str] = self._get_pod_ids_from_job(job_id, namespace)
        pods: List[Dict[str, Any]] = [
            self.get_pod_status_report(p, namespace) for p in pod_ids
        ]

        report["pods"] = pods
        return report

    def get_job_log(self, job_id: str, namespace: str) -> Optional[str]:
        """Get log of a pod running inside a job."""
        pod_id = self._get_pod_id_from_job(job_id, namespace)
        return self.get_pod_log(pod_id, namespace)

    def get_job_logs(self, job_id: str, namespace: str) -> Optional[str]:
        """Get log of a pod running inside a job."""
        pod_id = self._get_pod_id_from_job(job_id, namespace)
        return self.get_pod_log(pod_id, namespace)

    def get_jobs(
        self, label_selector: str, namespace: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get all Jobs, select them by the provided label."""
        import openshift

        try:
            response: Dict[str, Any] = self.ocp_client.resources.get(
                api_version="batch/v1", kind="Job"
            ).get(namespace=namespace, label_selector=label_selector)
        except openshift.dynamic.exceptions.NotFoundError as exc:
            raise NotFoundException(
                f"No Jobs with label {label_selector} could be found"
            ) from exc

        _LOGGER.debug("OpenShift response: %r", response)
        return response

    def _get_template(
        self, _label_selector: str, namespace: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get template from infra namespace, use label_selector to identify which template to get."""
        response = self.ocp_client.resources.get(
            api_version="template.openshift.io/v1", kind="Template", name="templates"
        ).get(
            namespace=namespace or self.infra_namespace, label_selector=_label_selector
        )
        _LOGGER.debug(
            "OpenShift response for getting template by label_selector %r: %r",
            _label_selector,
            response.to_dict(),
        )
        self._raise_on_invalid_response_size(
            response, label_selector=_label_selector, namespace=namespace
        )
        template: Dict[str, Any] = response.to_dict()["items"][0]
        return template

    def _get_cronjob(self, _label_selector: str, namespace: str) -> Dict[str, Any]:
        """Get template from infra namespace, use label_selector to identify which template to get."""
        response = self.ocp_client.resources.get(
            api_version="batch/v1beta1", kind="CronJob"
        ).get(namespace=namespace, label_selector=_label_selector)
        _LOGGER.debug(
            "OpenShift response for getting CronJob by label_selector %r: %r",
            _label_selector,
            response.to_dict(),
        )
        self._raise_on_invalid_response_size(
            response, label_selector=_label_selector, namespace=namespace
        )
        template: Dict[str, Any] = response.to_dict()["items"][0]
        return template

    @staticmethod
    def _transform_cronjob_to_job(item: Dict[str, Any]) -> Dict[str, Any]:
        """Turn a CronJob into a job so that it can be directly run."""
        job_spec: Dict[str, Any] = item["spec"]["jobTemplate"]
        job_spec["apiVersion"] = "batch/v1"
        job_spec["kind"] = "Job"
        job_spec["metadata"]["generateName"] = item["metadata"]["name"] + "-"
        return job_spec

    def schedule_graph_schema_update(
        self, job_id: Optional[str] = None, namespace: Optional[str] = None
    ) -> str:
        """Schedule graph schema update job in infra namespace by default."""
        if namespace is None:
            if not self.infra_namespace:
                raise ConfigurationError(
                    "No infra namespace configured to run graph-schema-update job"
                )

            namespace = self.infra_namespace

        template = self._get_template(
            "template=graph-schema-update-job", namespace=namespace
        )

        job_id = job_id or self.generate_id("graph-update-schema")
        self.set_template_parameters(
            template,
            THOTH_SCHEMA_UPDATE_JOB_ID=job_id,
        )

        template = self.oc_process(namespace, template)

        graph_update_schema_template = template["objects"][0]

        response = self.ocp_client.resources.get(
            api_version=graph_update_schema_template["apiVersion"],
            kind=graph_update_schema_template["kind"],
        ).create(body=graph_update_schema_template, namespace=namespace)

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())

        name: str = response["metadata"]["name"]

        return name

    def schedule_graph_refresh(self, namespace: Optional[str] = None) -> str:
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

        result: str = response["metadata"]["name"]
        return result

    def schedule_inspection(
        self,
        dockerfile: str,
        specification: Dict[str, Any],
        target: str,
        parameters: Dict[str, Any],
        *,
        raw_specification: Optional[Dict[str, Any]] = None,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule an inspection run."""
        if not self.amun_inspection_namespace:
            raise ConfigurationError(
                "Unable to schedule inspection without Amun inspection namespace being set."
            )

        inspection_id = job_id or self.generate_id(
            prefix="inspection", identifier=specification.get("identifier")
        )

        template_parameters = dict(parameters)
        template_parameters["THOTH_INFRA_NAMESPACE"] = self.infra_namespace
        template_parameters["AMUN_INSPECTION_ID"] = inspection_id
        template_parameters["AMUN_BUILD_CPU"] = specification["build"]["requests"][
            "cpu"
        ]
        template_parameters["AMUN_BUILD_MEMORY"] = specification["build"]["requests"][
            "memory"
        ]
        template_parameters["AMUN_RUN_CPU"] = specification["run"]["requests"]["cpu"]
        template_parameters["AMUN_RUN_MEMORY"] = specification["run"]["requests"][
            "memory"
        ]

        workflow_parameters = self._assign_workflow_parameters_for_ceph()
        workflow_parameters["dockerfile"] = dockerfile
        # Propagate raw specification to be placed on Ceph, not to submit escaped specification.
        workflow_parameters["specification"] = (
            json.dumps(raw_specification, sort_keys=True, indent=2)
            if raw_specification is not None
            else json.dumps(specification, sort_keys=True, indent=2)
        )
        workflow_parameters["target"] = target

        if "batch_size" in specification:
            workflow_parameters["batch-size"] = specification["batch_size"]

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_inspection,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def get_solver_names(self) -> List[str]:
        """Retrieve name of solvers available in installation."""
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required in order to list solvers"
            )

        cm = self.get_configmap("solvers", namespace=self.infra_namespace)
        solvers = [s.strip() for s in cm["data"].get("solvers", "").splitlines()]
        if not solvers:
            _LOGGER.warning("No solvers found in solvers ConfigMap")

        return solvers

    def schedule_all_solvers(
        self,
        packages: str,
        *,
        indexes: Optional[List[str]] = None,
        debug: bool = False,
        transitive: bool = False,
    ) -> typing.List[str]:
        """Schedule all solvers for the given packages."""
        solver_ids = []
        for solver_name in self.get_solver_names():
            solver_id = self.schedule_solver(
                packages=packages,
                solver=solver_name,
                indexes=indexes,
                debug=debug,
                transitive=transitive,
            )
            if solver_id is not None:
                solver_ids.append(solver_id)

        return solver_ids

    def schedule_solver(
        self,
        packages: str,
        solver: str,
        *,
        indexes: Optional[List[str]] = None,
        debug: bool = False,
        transitive: bool = True,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule the given solver."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule solver job without middletier namespace being set"
            )

        workflow_id = job_id or self.generate_id(solver)
        template_parameters = {
            "THOTH_SOLVER_WORKFLOW_ID": workflow_id,
            "THOTH_SOLVER_NAME": solver,
            "THOTH_SOLVER_PACKAGES": packages.replace("\n", "\\n"),
            "THOTH_SOLVER_NO_TRANSITIVE": int(not transitive),
            "THOTH_SOLVER_INDEXES": ",".join(indexes) if indexes else "",
            "THOTH_LOG_SOLVER": "DEBUG" if debug else "INFO",
        }

        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_solver,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def schedule_revsolver(
        self,
        package_name: str,
        package_version: str,
        *,
        debug: bool = False,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule reverse solver."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule reverse solver without middletier namespace being set"
            )

        workflow_id = job_id or self.generate_id("revsolver")
        template_parameters = {
            "THOTH_REVSOLVER_WORKFLOW_ID": workflow_id,
            "THOTH_REVSOLVER_PACKAGE_NAME": package_name,
            "THOTH_REVSOLVER_PACKAGE_VERSION": package_version,
            "THOTH_LOG_REVSOLVER": "DEBUG" if debug else "INFO",
        }
        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_revsolver,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def schedule_package_extract(
        self,
        image: str,
        *,
        environment_type: str,
        is_external: bool = True,
        origin: Optional[str] = None,
        registry_user: Optional[str] = None,
        registry_password: Optional[str] = None,
        verify_tls: bool = True,
        debug: bool = False,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule package extract workflow."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule package extract job without middletier namespace being set"
            )

        if environment_type not in ("runtime", "buildtime"):
            raise ValueError(
                "Unknown environment type %r, has to be runtime or buildtime"
            )

        template_parameters = {
            "THOTH_LOG_PACKAGE_EXTRACT": "DEBUG" if debug else "INFO",
            "THOTH_ANALYZED_IMAGE": image,
            "THOTH_ANALYZER_NO_TLS_VERIFY": int(not verify_tls),
            "THOTH_PACKAGE_EXTRACT_JOB_ID": job_id
            or self.generate_id("package-extract"),
            "THOTH_DOCUMENT_ID": job_id,
            "THOTH_PACKAGE_EXTRACT_METADATA": json.dumps(
                {
                    "origin": origin,
                    "environment_type": environment_type,
                    "is_external": is_external,
                }
            ),
        }

        if registry_user and registry_password:
            template_parameters[
                "THOTH_REGISTRY_CREDENTIALS"
            ] = f"{registry_user}:{registry_password}"

        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_package_extract,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def create_config_map(
        self,
        configmap_name: str,
        namespace: str,
        labels: Dict[str, str],
        data: Dict[str, str],
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

    @staticmethod
    def _schedule_workflow(
        workflow: typing.Callable[..., Optional[str]], parameters: Dict[str, Any]
    ) -> Optional[str]:
        """Schedule an Argo Workflow."""
        return workflow(**parameters)

    @staticmethod
    def generate_id(
        prefix: Optional[str] = None, identifier: Optional[str] = None
    ) -> str:
        """Generate an identifier."""
        suffix = f"-{datetime.datetime.now():%y%m%d%H%M%S}-{random.getrandbits(64):08x}"
        if prefix and identifier:
            return f"{prefix}-{identifier}{suffix}"

        if prefix:
            return f"{prefix}{suffix}"

        return suffix

    def schedule_dependency_monkey(
        self,
        requirements: Dict[str, Any],
        context: Dict[str, Any],
        *,
        pipeline: Optional[Dict[str, Any]] = None,
        predictor: Optional[str] = None,
        predictor_config: Optional[Dict[str, Any]] = None,
        stack_output: Optional[str] = None,
        runtime_environment: Optional[Dict[Any, Any]] = None,
        seed: Optional[int] = None,
        dry_run: bool = False,
        decision: Optional[str] = None,
        count: Optional[int] = None,
        debug: bool = False,
        job_id: Optional[str] = None,
        limit_latest_versions: Optional[int] = None,
    ) -> Optional[str]:
        """Schedule a dependency monkey run."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule dependency monkey without middletier namespace being set"
            )

        job_id = job_id or self.generate_id("dependency-monkey")
        template_parameters = {
            "THOTH_ADVISER_REQUIREMENTS": json.dumps(requirements).replace("\n", "\\n"),
            "THOTH_ADVISER_RUNTIME_ENVIRONMENT": None
            if runtime_environment is None
            else json.dumps(runtime_environment),
            "THOTH_AMUN_CONTEXT": json.dumps(context).replace("\n", "\\n"),
            "THOTH_DEPENDENCY_MONKEY_STACK_OUTPUT": stack_output or "-",
            "THOTH_DEPENDENCY_MONKEY_DRY_RUN": int(bool(dry_run)),
            "THOTH_LOG_ADVISER": "DEBUG" if debug else "INFO",
            "THOTH_DEPENDENCY_MONKEY_JOB_ID": job_id,
            "THOTH_DOCUMENT_ID": job_id,
            "THOTH_ADVISER_PIPELINE": json.dumps(pipeline) if pipeline else "{}",
            "THOTH_ADVISER_PREDICTOR": predictor or "AUTO",
            "THOTH_ADVISER_PREDICTOR_CONFIG": json.dumps(predictor_config)
            if predictor_config
            else "{}",
        }

        if decision is not None:
            template_parameters[
                "THOTH_DEPENDENCY_MONKEY_DECISION_TYPE"
            ] = decision.lower()

        if seed is not None:
            template_parameters["THOTH_DEPENDENCY_MONKEY_SEED"] = seed

        if count is not None:
            template_parameters["THOTH_DEPENDENCY_MONKEY_COUNT"] = count

        if limit_latest_versions is not None:
            template_parameters[
                "THOTH_ADVISER_LIMIT_LATEST_VERSIONS"
            ] = limit_latest_versions

        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_dependency_monkey,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def schedule_build_analysis(
        self,
        *,
        base_image: Optional[str] = None,
        base_image_analysis_id: Optional[str] = None,
        base_registry_password: Optional[str] = None,
        base_registry_user: Optional[str] = None,
        base_registry_verify_tls: bool = True,
        output_image: Optional[str] = None,
        output_image_analysis_id: Optional[str] = None,
        output_registry_password: Optional[str] = None,
        output_registry_user: Optional[str] = None,
        output_registry_verify_tls: bool = True,
        buildlog_document_id: Optional[str] = None,
        buildlog_parser_id: Optional[str] = None,
        environment_type: Optional[str] = None,
        origin: Optional[str] = None,
        debug: bool = False,
        is_external: bool = True,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule a build analysis workflow."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule build analysis without middletier namespace being set"
            )

        if not base_image and not output_image and not buildlog_document_id:
            raise ValueError(
                "Nothing to do, expected any combination of base image, output image and buildlog document id"
            )

        base_registry_credentials = None
        if base_registry_user:
            if not base_registry_password:
                raise ValueError(
                    "Base registry user provided but no base registry password supplied"
                )

            base_registry_credentials = f"{base_registry_user}:{base_registry_password}"

        output_registry_credentials = None
        if output_registry_user:
            if not output_registry_password:
                raise ValueError(
                    "Output registry user provided but no base registry password supplied"
                )

            output_registry_credentials = (
                f"{output_registry_user}:{output_registry_password}"
            )

        if base_image and not base_image_analysis_id:
            base_image_analysis_id = self.generate_id("package-extract")

        if output_image and not output_image_analysis_id:
            output_image_analysis_id = self.generate_id("package-extract")

        if buildlog_document_id and not buildlog_parser_id:
            buildlog_parser_id = self.generate_id("buildlog-parser")

        if not job_id:
            job_id = self.generate_id("build-analysis")

        template_parameters = {
            "THOTH_BUILD_ANALYSIS_BASE_IMAGE": base_image,
            "THOTH_BUILD_ANALYSIS_BASE_IMAGE_ANALYSIS_ID": base_image_analysis_id,
            "THOTH_BUILD_ANALYSIS_BASE_IMAGE_DOCUMENT_ID": base_image_analysis_id,
            "THOTH_BUILD_ANALYSIS_BASE_REGISTRY_CREDENTIALS": base_registry_credentials,
            "THOTH_BUILD_ANALYSIS_BASE_REGISTRY_NO_TLS_VERIFY": str(
                int(not base_registry_verify_tls)
            ),
            "THOTH_BUILD_ANALYSIS_OUTPUT_IMAGE": output_image,
            "THOTH_BUILD_ANALYSIS_OUTPUT_IMAGE_ANALYSIS_ID": output_image_analysis_id,
            "THOTH_BUILD_ANALYSIS_OUTPUT_IMAGE_DOCUMENT_ID": output_image_analysis_id,
            "THOTH_BUILD_ANALYSIS_OUTPUT_REGISTRY_CREDENTIALS": output_registry_credentials,
            "THOTH_BUILD_ANALYSIS_OUTPUT_REGISTRY_NO_TLS_VERIFY": str(
                int(not output_registry_verify_tls)
            ),
            "THOTH_BUILD_ANALYSIS_BUILDLOG_DOCUMENT_ID": buildlog_document_id,
            "THOTH_BUILD_ANALYSIS_BUILDLOG_PARSER_ID": buildlog_parser_id,
            "THOTH_BUILD_ANALYSIS_ENVIRONMENT_TYPE": environment_type,
            "THOTH_BUILD_ANALYSIS_ORIGIN": origin,
            "THOTH_BUILD_ANALYSIS_LOG": "DEBUG" if debug else "INFO",
            "THOTH_BUILD_ANALYSIS_JOB_ID": job_id,
            "THOTH_BUILD_ANALYSIS_METADATA": json.dumps(
                {
                    "origin": origin,
                    "environment_type": environment_type,
                    "base_image_analysis_id": base_image_analysis_id,
                    "output_image_analysis_id": output_image_analysis_id,
                    "buildlog_document_id": buildlog_document_id,
                    "build_analysis_job_id": job_id,
                    "is_external": is_external,
                }
            ),
        }

        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_build_analysis,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    @staticmethod
    def _verify_thoth_integration(source_type: Optional[str]) -> None:
        """Verify if Thoth integration exists."""
        if (
            source_type not in ThothAdviserIntegrationEnum.__members__
            and source_type is not None
        ):
            raise NotKnownThothIntegration(
                f"This integration {source_type} is not provided \
                    in Thoth: {ThothAdviserIntegrationEnum.__members__.keys()}"
            )

    @staticmethod
    def verify_github_app_inputs(
        github_event_type: Optional[str],
        github_check_run_id: Optional[int],
        github_installation_id: Optional[int],
        github_base_repo_url: Optional[str],
        origin: Optional[str],
    ) -> None:
        """Verify if Thoth GitHub App integration inputs are correct."""
        parameters = locals()
        if not all(parameters.values()):
            raise QebHwtInputsMissing(
                f"Not all inputs to schedule Qeb-Hwt GitHub App are provided: {parameters}"
            )

    @staticmethod
    def verify_kebechet_inputs(
        origin: Optional[str],
    ) -> None:
        """Verify if Thoth Kebechet integration inputs are correct."""
        parameters = locals()
        if not all(parameters.values()):
            raise KebechetInputsMissing(
                f"Not all inputs to schedule Kebechet are provided: {parameters}"
            )

    def verify_integration_inputs(
        self,
        source_type: Optional[ThothAdviserIntegrationEnum],
        github_event_type: Optional[str] = None,
        github_check_run_id: Optional[int] = None,
        github_installation_id: Optional[int] = None,
        github_base_repo_url: Optional[str] = None,
        origin: Optional[str] = None,
    ) -> None:
        """Verify if inputs for registered Thoth integrations are correct."""
        if source_type is ThothAdviserIntegrationEnum.GITHUB_APP:
            self.verify_github_app_inputs(
                github_event_type=github_event_type,
                github_check_run_id=github_check_run_id,
                github_installation_id=github_installation_id,
                github_base_repo_url=github_base_repo_url,
                origin=origin,
            )

        if source_type is ThothAdviserIntegrationEnum.KEBECHET:
            self.verify_kebechet_inputs(origin=origin)

    def schedule_adviser(
        self,
        application_stack: Dict[Any, Any],
        recommendation_type: str,
        *,
        count: Optional[int] = None,
        limit: Optional[int] = None,
        predictor_config: Optional[Dict[str, Any]] = None,
        runtime_environment: Optional[Dict[Any, Any]] = None,
        library_usage: Optional[Dict[Any, Any]] = None,
        origin: Optional[str] = None,
        dev: bool = False,
        debug: bool = False,
        job_id: Optional[str] = None,
        github_event_type: Optional[str] = None,
        github_check_run_id: Optional[int] = None,
        github_installation_id: Optional[int] = None,
        github_base_repo_url: Optional[str] = None,
        re_run_adviser_id: Optional[str] = None,
        source_type: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule an adviser run."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Unable to schedule adviser without backend namespace being set"
            )

        if source_type is not None:
            self._verify_thoth_integration(source_type=source_type)
        source_type_enum = (
            getattr(ThothAdviserIntegrationEnum, source_type) if source_type else None
        )

        self.verify_integration_inputs(
            source_type=source_type_enum,
            github_event_type=github_event_type,
            github_check_run_id=github_check_run_id,
            github_installation_id=github_installation_id,
            github_base_repo_url=github_base_repo_url,
            origin=origin,
        )

        adviser_id = job_id or self.generate_id("adviser")
        template_parameters = {}

        if application_stack.get("requirements_lock"):
            template_parameters[
                "THOTH_ADVISER_REQUIREMENTS_LOCKED"
            ] = application_stack["requirements_lock"]
        template_parameters["THOTH_ADVISER_JOB_ID"] = adviser_id
        template_parameters["THOTH_ADVISER_DEV"] = "1" if dev else "0"
        template_parameters["THOTH_ADVISER_REQUIREMENTS"] = application_stack[
            "requirements"
        ]
        template_parameters["THOTH_ADVISER_LIBRARY_USAGE"] = json.dumps(library_usage)
        template_parameters["THOTH_LOG_ADVISER"] = "DEBUG" if debug else "INFO"
        template_parameters[
            "THOTH_ADVISER_REQUIREMENTS_FORMAT"
        ] = application_stack.get("requirements_format", "pipenv")
        template_parameters["THOTH_ADVISER_RECOMMENDATION_TYPE"] = recommendation_type
        template_parameters["THOTH_ADVISER_RUNTIME_ENVIRONMENT"] = json.dumps(
            runtime_environment
        )
        template_parameters["THOTH_ADVISER_PREDICTOR_CONFIG"] = (
            json.dumps(predictor_config) if predictor_config else "{}"
        )

        template_parameters["THOTH_ADVISER_METADATA"] = json.dumps(
            {
                "github_event_type": github_event_type,
                "github_check_run_id": github_check_run_id,
                "github_installation_id": github_installation_id,
                "github_base_repo_url": github_base_repo_url,
                "origin": origin,
                "re_run_adviser_id": re_run_adviser_id,
                "source_type": source_type if source_type is not None else None,
            }
        )

        if limit is not None:
            template_parameters["THOTH_ADVISER_LIMIT"] = limit

        if count is not None:
            template_parameters["THOTH_ADVISER_COUNT"] = count

        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_adviser,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    @staticmethod
    def _assign_workflow_parameters_for_ceph() -> Dict[str, Any]:
        """Check and assign workflow parameters for different services to interact with Ceph."""
        workflow_parameters = {
            "ceph_bucket_prefix": os.environ["THOTH_CEPH_BUCKET_PREFIX"],
            "ceph_bucket_name": os.environ["THOTH_CEPH_BUCKET"],
            "ceph_host": urlparse(os.environ["THOTH_S3_ENDPOINT_URL"]).netloc,
            "deployment_name": os.environ["THOTH_DEPLOYMENT_NAME"],
        }

        return workflow_parameters

    def schedule_provenance_checker(
        self,
        application_stack: Dict[Any, Any],
        *,
        origin: Optional[str] = None,
        whitelisted_sources: Optional[List[str]] = None,
        debug: bool = False,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Run provenance checks on the provided user input."""
        if not self.backend_namespace:
            raise ConfigurationError(
                "Running provenance checks requires backend namespace configuration"
            )

        job_id = job_id or self.generate_id("provenance-checker")

        requirements = application_stack.pop("requirements").replace("\n", "\\n")
        requirements_locked = application_stack.pop("requirements_lock").replace(
            "\n", "\\n"
        )
        template_parameters = {
            "THOTH_ADVISER_REQUIREMENTS": requirements,
            "THOTH_ADVISER_REQUIREMENTS_LOCKED": requirements_locked,
            "THOTH_ADVISER_METADATA": json.dumps({"origin": origin}),
            "THOTH_WHITELISTED_SOURCES": ",".join(whitelisted_sources or []),
            "THOTH_LOG_ADVISER": "DEBUG" if debug else "INFO",
            "THOTH_PROVENANCE_CHECKER_JOB_ID": job_id,
            "THOTH_DOCUMENT_ID": job_id,
        }

        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_provenance_checker,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def schedule_qebhwt_workflow(
        self,
        github_event_type: str,
        github_check_run_id: int,
        github_installation_id: int,
        github_base_repo_url: str,
        github_head_repo_url: str,
        origin: str,
        revision: str,
        host: str,
        *,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule Workflow for Qeb-Hwt GitHub App.."""
        workflow_id = job_id or self.generate_id("qeb-hwt")
        template_parameters = {
            "WORKFLOW_ID": workflow_id,
            "GITHUB_EVENT_TYPE": github_event_type,
            "GITHUB_CHECK_RUN_ID": str(github_check_run_id),
            "GITHUB_INSTALLATION_ID": str(github_installation_id),
            "GITHUB_BASE_REPO_URL": github_base_repo_url,
            "GITHUB_HEAD_REPO_URL": github_head_repo_url,
            "ORIGIN": origin,
            "REVISION": revision,
            "THOTH_HOST": host,
        }

        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_qebhwt,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def schedule_mi_workflow(
        self,
        repository: str,
        entities: Optional[str] = None,
        *,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule Meta-information Indicators Workflow.

        :param repository:str: GitHub repository in full name format: <repo_owner>/<repo_name>
        :param entities:Optional[str]: Meta-information Indicator Entities that will be inspected
                                       multiple entities are in form of Foo,Bar,...
        """
        workflow_id = job_id or self.generate_id("mi")
        template_parameters = {
            "WORKFLOW_ID": workflow_id,
            "REPOSITORY": repository,
            "ENTITIES": entities,
        }

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_mi,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": {},
            },
        )

    def schedule_kebechet_workflow(
        self,
        webhook_payload: Dict[str, Any],
        *,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule Kebechet Workflow for a Webhook from GitHub App.."""
        workflow_id = job_id or self.generate_id("kebechet-job")
        template_parameters = {
            "WORKFLOW_ID": workflow_id,
            "WEBHOOK_PAYLOAD": json.dumps(webhook_payload),
        }

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_kebechet,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": {},
            },
        )

    def schedule_kebechet_administrator(
        self,
        message_info: Dict[str, str],
        message_type: str,
        *,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule Kebechet Administrator Workflow for an internal trigger message."""
        workflow_id = job_id or self.generate_id("kebechet-administrator")
        template_parameters = {
            "WORKFLOW_ID": workflow_id,
            "THOTH_PACKAGE_NAME": message_info.get("PACKAGE_NAME"),
            "THOTH_PACKAGE_VERSION": message_info.get(
                "PACKAGE_VERSION"
            ),  # Optional value
            "THOTH_PACKAGE_INDEX": message_info.get("PACKAGE_INDEX"),
            "THOTH_SOLVER_NAME": message_info.get("SOLVER_NAME"),  # Optional value
            "THOTH_MESSAGE_TYPE": message_type,
        }

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_kebechet_administrator,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": {},
            },
        )

    def schedule_kebechet_run_url_workflow(
        self,
        repo_url: str,
        service_name: str = "github",
        *,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule Kebechet Workflow for a particular valid slug and service name."""
        workflow_id = job_id or self.generate_id("kebechet-run-url")
        template_parameters = {
            "WORKFLOW_ID": workflow_id,
            "KEBECHET_REPO_URL": repo_url,
            "KEBECHET_SERVICE_NAME": service_name,
        }

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_kebechet_run_url,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": {},
            },
        )

    def schedule_security_indicator(
        self,
        python_package_name: str,
        python_package_version: str,
        python_package_index: str,
        aggregation_function: str,
        *,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule a security indicator run."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule security-indicator without middletier namespace being set"
            )

        security_indicator_id = job_id or self.generate_id("security-indicator")
        template_parameters = {
            "THOTH_SECURITY_INDICATORS_JOB_ID": security_indicator_id,
            "THOTH_SECURITY_INDICATORS_PACKAGE_NAME": python_package_name,
            "THOTH_SECURITY_INDICATORS_PACKAGE_VERSION": python_package_version,
            "THOTH_SECURITY_INDICATORS_PACKAGE_INDEX": python_package_index,
            "THOTH_SECURITY_INDICATORS_AGGREGATION_FUNCTION": aggregation_function,
        }
        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_security_indicator,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def schedule_graph_sync(
        self,
        document_id: str,
        force_sync: bool = False,
        *,
        job_id: Optional[str] = None,
    ) -> Optional[str]:
        """Schedule graph sync for specific document id."""
        if not self.middletier_namespace:
            raise ConfigurationError(
                "Unable to schedule graph-sync without middletier namespace being set"
            )

        graph_sync_id = job_id or self.generate_id("graph-sync")
        template_parameters = {
            "THOTH_SYNC_JOB_ID": graph_sync_id,
            "THOTH_SYNC_DOCUMENT_ID": document_id,
            "THOTH_FORCE_SYNC": force_sync,
        }
        workflow_parameters = self._assign_workflow_parameters_for_ceph()

        return self._schedule_workflow(
            workflow=self.workflow_manager.submit_graph_sync,
            parameters={
                "template_parameters": template_parameters,
                "workflow_parameters": workflow_parameters,
            },
        )

    def _raise_on_invalid_response_size(
        self,
        response: Any,
        *,
        label_selector: Optional[str] = None,
        name: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> None:
        """Expect that there is only one object type for the given item."""
        if len(response.items) != 1:
            raise RuntimeError(
                f"Application misconfiguration - number of templates available in namespace {namespace!r} "
                f"is {len(response.items)}, should be 1: "
                f"label selector: {label_selector!r}, name: {name!r}"
            )

            # TODO add name of template we were looking for...

    def oc_process(self, namespace: str, template: Dict[str, Any]) -> Dict[str, Any]:
        """Process the given template in OpenShift."""
        # TODO: This does not work - see issue reported upstream:
        #   https://github.com/openshift/openshift-restclient-python/issues/190
        # return TemplateOpenshiftIoApi().create_namespaced_processed_template_v1(namespace, template)
        endpoint = (
            "{}/apis/template.openshift.io/v1/namespaces/{}/processedtemplates".format(
                self.openshift_api_url, namespace
            )
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

        result: Dict[str, Any] = response.json()
        return result

    def get_mi_repositories_and_organizations(
        self,
    ) -> Tuple[List[str], List[str]]:
        """Get all of the repositories and organizations for mi-analysis.

        :rtype: Tuple of (repositories, organizations)
        """
        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required in order to get repositories"
            )

        cm = self.get_configmap(
            configmap_id="mi-scheduler", namespace=self.infra_namespace
        )

        organizations = cm["data"].get("organizations", "")
        _LOGGER.info(
            "Detected %s organizations from configMap for inspection", organizations
        )
        repositories = cm["data"].get("repositories", "")
        _LOGGER.info(
            "Detected %s repositories from configMap for inspection", repositories
        )

        orgs = (
            organizations.split(",")
            if organizations is not None and organizations != ""
            else []
        )
        repos = (
            repositories.split(",")
            if repositories is not None and repositories != ""
            else []
        )
        return (repos, orgs)

    @staticmethod
    def parse_cpu_spec(cpu_spec: typing.Optional[str]) -> typing.Optional[float]:
        """Parse the given CPU requirement as used by OpenShift/Kubernetes."""
        if isinstance(cpu_spec, str) and cpu_spec.endswith("m"):
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
            parsed = float(memory_spec[:-1])
            return parsed * 1000 ** 6
        elif memory_spec.endswith("P"):
            parsed = float(memory_spec[:-1])
            return parsed * 1000 ** 5
        elif memory_spec.endswith("T"):
            parsed = float(memory_spec[:-1])
            return parsed * 1000 ** 4
        elif memory_spec.endswith("G"):
            parsed = float(memory_spec[:-1])
            return parsed * 1000 ** 3
        elif memory_spec.endswith("M"):
            parsed = float(memory_spec[:-1])
            return parsed * 1000 ** 2
        elif memory_spec.endswith("K"):
            parsed = float(memory_spec[:-1])
            return parsed * 1000
        elif memory_spec.endswith("Ei"):
            parsed = float(memory_spec[:-2])
            return parsed * 1024 ** 6
        elif memory_spec.endswith("Pi"):
            parsed = float(memory_spec[:-2])
            return parsed * 1024 ** 5
        elif memory_spec.endswith("Ti"):
            parsed = float(memory_spec[:-2])
            return parsed * 1024 ** 4
        elif memory_spec.endswith("Gi"):
            parsed = float(memory_spec[:-2])
            return parsed * 1024 ** 3
        elif memory_spec.endswith("Mi"):
            parsed = float(memory_spec[:-2])
            return parsed * 1024 ** 2
        elif memory_spec.endswith("Ki"):
            parsed = float(memory_spec[:-2])
            return parsed * 1024

        raise ValueError(f"Cannot parse memory specification from {memory_spec!r}")

    def get_job_status_count(
        self, label_selector: str, namespace: str
    ) -> Dict[str, int]:
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
            elif (
                "startTime" in item["status"].keys() and len(item["status"].keys()) == 1
            ):
                jobs_status_count["started"] += 1
            else:
                try:
                    if (
                        "BackoffLimitExceeded"
                        in item["status"]["conditions"][0]["reason"]
                    ):
                        jobs_status_count["retry"] += 1
                except Exception as excptn:
                    _LOGGER.error("Unknown job status %r", item)
                    _LOGGER.exception(excptn)

        return jobs_status_count

    def get_workflow(
        self,
        name: Optional[str] = None,
        label_selector: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get Workflow from a namespace, use one of name or label_selector to identify which one to get."""
        wf: Dict[str, Any]
        if name:
            if label_selector is not None:
                _LOGGER.warning(
                    "Only one of `name` or `label_selector` can be provided."
                    f"Ignoring `label_selector={label_selector}`."
                )

            try:
                response = self.ocp_client.resources.get(
                    api_version="argoproj.io/v1alpha1",
                    kind="Workflow",
                    name="workflows",
                ).get(namespace=namespace or self.infra_namespace, name=name)
                _LOGGER.debug(
                    "OpenShift response for getting template by name %r: %r",
                    name,
                    response.to_dict(),
                )
            except OpenShiftNotFoundError as exc:
                raise NotFoundException(
                    f"The given Workflow {name} could not be found"
                ) from exc

            wf = response.to_dict()

        elif label_selector:
            try:
                response = self.ocp_client.resources.get(
                    api_version="argoproj.io/v1alpha1",
                    kind="Workflow",
                    name="workflows",
                ).get(
                    namespace=namespace or self.infra_namespace,
                    label_selector=label_selector,
                )
                _LOGGER.debug(
                    "OpenShift response for getting template by label_selector %r: %r",
                    label_selector,
                    response.to_dict(),
                )
            except OpenShiftNotFoundError as exc:
                raise NotFoundException(
                    f"The given Workflow containing label {label_selector} could not be found"
                ) from exc

            self._raise_on_invalid_response_size(
                response, label_selector=label_selector, namespace=namespace
            )

            wf = response.to_dict()["items"][0]

        else:
            raise ValueError("Either `name` or `label_selector` has to be provided.")

        return wf

    def get_workflow_status_report(
        self,
        workflow_id: str,
        label_selector: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Dict[str, Optional[str]]:
        """Get workflow status report, derived from workflow status."""
        try:
            wf_status = self.get_workflow_status(
                name=workflow_id, label_selector=label_selector, namespace=namespace
            )
            status = {
                "finished_at": wf_status.get("finishedAt"),
                "reason": None,
                "started_at": wf_status.get("startedAt"),
                "state": wf_status.get("phase", "pending").lower(),
            }
        except NotFoundException as exc:
            raise NotFoundException(
                f"Requested status for analysis {workflow_id!r} was not found"
            ) from exc
        return status

    def get_workflow_status(
        self,
        name: Optional[str] = None,
        label_selector: Optional[str] = None,
        namespace: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get a Workflow status, use one of name or label_selector to identify which one to get."""
        wf: Dict[str, Any] = self.get_workflow(
            name=name, label_selector=label_selector, namespace=namespace
        )
        to_ret: Dict[str, Any] = wf["status"]
        return to_ret
