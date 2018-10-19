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

from .exceptions import NotFoundException
from .exceptions import ConfigurationError
from .helpers import get_service_account_token

_LOGGER = logging.getLogger(__name__)


class OpenShift(object):
    """Interaction with OpenShift Master."""

    def __init__(self, *,
                 frontend_namespace: str = None, middletier_namespace: str = None, backend_namespace: str = None,
                 infra_namespace: str = None, kubernetes_api_url: str = None, kubernetes_verify_tls: bool = True,
                 openshift_api_url: str = None, token: str = None):
        """Initialize OpenShift class responsible for handling objects in deployment."""
        try:
            from kubernetes import client, config
            from openshift.dynamic import DynamicClient
        except ImportError as exc:
            raise ImportError(
                "Unable to import OpenShift and Kubernetes packages. Was thoth-common library "
                "installed with openshift extras?"
            ) from exc

        self.kubernetes_verify_tls = bool(int(os.getenv('KUBERNETES_VERIFY_TLS', 1)) and kubernetes_verify_tls)

        # Load in-cluster configuration that is exposed by OpenShift/k8s configuration.
        config.load_incluster_config()

        # We need to explicitly set whether we want to verify SSL/TLS connection to the master.
        configuration = client.Configuration()
        configuration.verify_ssl = self.kubernetes_verify_tls

        self.ocp_client = DynamicClient(client.ApiClient(configuration=configuration))
        self.frontend_namespace = frontend_namespace or os.getenv('THOTH_FRONTEND_NAMESPACE')
        self.middletier_namespace = middletier_namespace or os.getenv('THOTH_MIDDLETIER_NAMESPACE')
        self.backend_namespace = backend_namespace or os.getenv('THOTH_BACKEND_NAMESPACE')
        self.infra_namespace = infra_namespace or os.getenv('THOTH_INFRA_NAMESPACE')
        self.kubernetes_api_url = kubernetes_api_url or \
            os.getenv('KUBERNETES_API_URL', 'https://kubernetes.default.svc.cluster.local')
        self.openshift_api_url = openshift_api_url or \
            os.getenv('OPENSHIFT_API_URL', 'https://openshift.default.svc.cluster.local')
        self._token = token

    @property
    def token(self):
        """Access service account token mounted to the pod."""
        if self._token is None:
            self._token = get_service_account_token()

        return self._token

    @staticmethod
    def _set_env_var(template: dict, **env_var):
        """Set environment in the given template."""
        for env_var_name, env_var_value in env_var.items():
            for entry in template['spec']['containers'][0]['env']:
                if entry['name'] == env_var_name:
                    entry['value'] = env_var_value
                    break
            else:
                template['spec']['containers'][0]['env'].append(
                    {'name': env_var_name, 'value': str(env_var_value)}
                )

    @staticmethod
    def set_template_parameters(template: dict, **parameters: object) -> None:
        """Set parameters in the template - replace existing ones or append to parameter list if not exist.

        >>> set_template_parameters(template, THOTH_LOG_ADVISER='DEBUG')
        """
        if 'parameters' not in template:
            template['parameters'] = []

        for parameter_name, parameter_value in parameters.items():
            for entry in template['parameters']:
                if entry['name'] == parameter_name:
                    entry['value'] = str(
                        parameter_value) if parameter_value is not None else ''
                    break
            else:
                _LOGGER.warning(
                    "Requested to assign parameter %r (value %r) to template but template "
                    "does not provide the given parameter, forcing...",
                    parameter_name, parameter_value
                )
                template['parameters'].append({
                    'name': parameter_name,
                    'value': str(parameter_value) if parameter_value is not None else ''
                })

    def run_sync(self, force_analysis_results_sync: bool = False, force_solver_results_sync: bool = False) -> str:
        """Run graph sync, base pod definition based on job definition."""
        # Let's reuse pod definition from the cronjob definition so any changes in
        # deployed application work out of the box.
        if not self.frontend_namespace:
            raise ConfigurationError("Graph sync requires frontend namespace configuration")

        _LOGGER.debug("Retrieving graph-sync CronJob definition")
        response = self.ocp_client.resources.get(api_version='v2alpha1', kind='CronJob').get(
            namespace=self.frontend_namespace,
            name='graph-sync'
        )
        template = response.to_dict()
        labels = template['metadata']['labels']
        labels.pop('template', None)  # remove template label
        job_template = template['spec']['jobTemplate']['spec']['template']
        self._set_env_var(
            job_template,
            THOTH_GRAPH_SYNC_FORCE_ANALYSIS_RESULTS_SYNC=int(
                force_analysis_results_sync),
            THOTH_GRAPH_SYNC_FORCE_SOLVER_RESULTS_SYNC=int(
                force_solver_results_sync)
        )

        # Construct a Pod spec.
        pod_template = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "generateName": 'graph-sync-',
                "labels": labels
            },
            "spec": job_template['spec']
        }

        response = self.ocp_client.resources.get(api_version='v1', kind='Pod').create(
            body=pod_template,
            namespace=self.frontend_namespace
        )

        _LOGGER.debug(f"Started graph-sync pod with name {response.metadata.name}")
        return response.metadata.name

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
            self.kubernetes_api_url,
            namespace,
            pod_id
        )

        response = requests.get(
            endpoint,
            headers={
                'Authorization': 'Bearer {}'.format(self.token),
                'Content-Type': 'application/json'
            },
            verify=self.kubernetes_verify_tls
        )
        _LOGGER.debug("Kubernetes master response for pod log (%d): %r", response.status_code, response.text)

        if response.status_code == 404:
            raise NotFoundException(f"Pod with id {pod_id} was not found in namespace {namespace}")

        if response.status_code == 400:
            # If Pod has not been initialized yet, there is returned 400 status code. Return None in this case.
            return None

        response.raise_for_status()
        return response.text

    def get_build_log(self, build_id: str, namespace: str) -> str:
        """Get log of a build in the given namespace."""
        # TODO: rewrite to OpenShift rest client once it will support it.
        endpoint = "{}/apis/build.openshift.io/v1/namespaces/{}/builds/{}/log".format(
            self.openshift_api_url,
            namespace,
            build_id
        )

        response = requests.get(
            endpoint,
            headers={
                'Authorization': 'Bearer {}'.format(self.token),
                'Content-Type': 'application/json'
            },
            verify=self.kubernetes_verify_tls
        )

        if response.status_code == 404:
            raise NotFoundException(f"Build with id {build_id} was not found in namespace {namespace}")

        _LOGGER.debug("OpenShift master response for build log (%d): %r", response.status_code, response.text)
        response.raise_for_status()

        return response.text

    def get_pod_status(self, pod_id: str, namespace: str) -> dict:
        """Get status entry for a pod - low level routine."""
        import openshift

        try:
            response = self.ocp_client.resources.get(api_version='v1', kind='Pod').get(
                namespace=namespace,
                name=pod_id
            )
        except openshift.dynamic.exceptions.NotFoundError as exc:
            raise NotFoundException(
                f"The given pod with id {pod_id} could not be found") from exc

        response = response.to_dict()
        _LOGGER.debug("OpenShift master response for pod status: %r", response)

        if 'containerStatuses' not in response['status']:
            # No status - pod is being scheduled.
            return {}

        state = response['status']['containerStatuses'][0]['state']
        # Translate kills of liveness probes to our messages reported to user.
        if state.get('terminated', {}).get('exitCode') == 137 and state['terminated']['reason'] == 'Error':
            # Reason can be set by OpenShift to be OOMKilled for example - we expect only "Error" to be set to
            # treat this as timeout.
            state['terminated']['reason'] = "TimeoutKilled"

        return state

    @staticmethod
    def _status_report(status):
        """Construct status response for API response from master API response."""
        _TRANSLATION_TABLE = {
            'exitCode': 'exit_code',
            'finishedAt': 'finished_at',
            'reason': 'reason',
            'startedAt': 'started_at',
            'containerID': 'container',
            'message': 'reason'
        }

        if len(status.keys()) != 1:
            # If pod was not initialized yet and user asks for status, return default values with state scheduling.
            reported_status = dict.fromkeys(tuple(_TRANSLATION_TABLE.values()))
            reported_status['state'] = 'scheduling'
            return reported_status

        state = list(status.keys())[0]

        reported_status = dict.fromkeys(tuple(_TRANSLATION_TABLE.values()))
        reported_status['state'] = state
        for key, value in status[state].items():
            if key == 'containerID':
                value = value[len('docker://'):] if value.startswith('docker://') else value
                reported_status['container'] = value
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
        response = self.ocp_client.resources.get(api_version='v1', kind='Pod').get(
            namespace=namespace or self.infra_namespace,
            label_selector=f'job-name={job_id}'
        )
        response = response.to_dict()
        _LOGGER.debug("OpenShift response for pod id from job: %r", response)

        if len(response['items']) != 1:
            if len(response['items']) > 1:
                # Log this error and report back to user not found.
                _LOGGER.error(f"Multiple pods for the same job name selector {job_id} found")

            raise NotFoundException(f"Job with the given id {job_id} was not found")

        return response['items'][0]['metadata']['name']

    def get_job_status_report(self, job_id: str, namespace: str) -> dict:
        """Get status of a pod running inside a job."""
        pod_id = self._get_pod_id_from_job(job_id, namespace)
        return self.get_pod_status_report(pod_id, namespace)

    def get_job_log(self, job_id: str, namespace: str = None) -> str:
        """Get log of a pod running inside a job."""
        pod_id = self._get_pod_id_from_job(job_id, namespace)
        return self.get_pod_log(pod_id, namespace)

    def get_jobs(self, label_selector: str, namespace: str = None) -> dict:
        """Get all Jobs, select them by the provided label."""
        import openshift

        response = None

        try:
            response = self.ocp_client.resources.get(api_version='v1', kind='JobList').get(
                namespace=namespace,
                label_selector=label_selector
            )
        except openshift.dynamic.exceptions.NotFoundError as exc:
            raise NotFoundException(
                f"No Jobs with label {label_selector} could be found") from exc

        _LOGGER.debug("OpenShift response: %r", response)

        return response

    def get_solver_names(self) -> list:
        """Retrieve name of solvers available in installation."""
        if not self.infra_namespace:
            raise ConfigurationError("Infra namespace is required in order to list solvers")

        response = self.ocp_client.resources.get(api_version='v1', kind='Template').get(
            namespace=self.infra_namespace,
            label_selector='template=solver'
        )
        _LOGGER.debug("OpenShift response for getting solver template: %r", response.to_dict())
        self._raise_on_invalid_response_size(response)
        return [obj['metadata']['labels']['component'] for obj in response.to_dict()['items'][0]['objects']]

    def run_solver(self, packages: str, output: str, debug: bool = False,
                   transitive: bool = True, solver: str = None) -> dict:
        """Run solver or all solver to solve the given requirements."""
        if not self.middletier_namespace:
            ConfigurationError("Solver requires middletier namespace to be specified")

        if not self.infra_namespace:
            raise ConfigurationError("Infra namespace is required to gather solver template when running solver")

        response = self.ocp_client.resources.get(api_version='v1', kind='Template').get(
            namespace=self.infra_namespace,
            label_selector='template=solver'
        )
        _LOGGER.debug("OpenShift response for getting solver template: %r", response.to_dict())

        self._raise_on_invalid_response_size(response)
        template = response.to_dict()['items'][0]

        self.set_template_parameters(
            template,
            THOTH_SOLVER_NO_TRANSITIVE=int(not transitive),
            THOTH_SOLVER_PACKAGES=packages.replace('\n', '\\n'),
            THOTH_LOG_SOLVER='DEBUG' if debug else 'INFO',
            THOTH_SOLVER_OUTPUT=output
        )

        template = self.oc_process(self.middletier_namespace, template)

        solvers = {}
        for obj in template['objects']:
            solver_name = obj['metadata']['labels']['component']
            if solver and solver != solver_name:
                _LOGGER.debug(f"Skipping solver %r as the requested solver is %r", solver_name, solver)
                continue

            response = self.ocp_client.resources.get(api_version='v1', kind=obj['kind']).create(
                body=obj,
                namespace=self.middletier_namespace
            )

            _LOGGER.debug("Starting solver %r", solver_name)
            _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
            solvers[solver_name] = response.metadata.name

        return solvers

    def run_package_extract(self, image: str, output: str, debug: bool = False,
                            registry_user: str = None, registry_password: str = None, verify_tls: bool = True) -> str:
        """Run package-extract analyzer to extract information from the provided image."""
        if not self.middletier_namespace:
            raise ConfigurationError("Running package-extract requires middletier namespace to be specified")

        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather package-extract template when running it"
            )

        response = self.ocp_client.resources.get(api_version='v1', kind='Template').get(
            namespace=self.infra_namespace,
            label_selector='template=package-extract'
        )
        _LOGGER.debug("OpenShift response for getting package-extract template: %r", response.to_dict())
        self._raise_on_invalid_response_size(response)
        template = response.to_dict()['items'][0]

        self.set_template_parameters(
            template,
            THOTH_LOG_PACKAGE_EXTRACT='DEBUG' if debug else 'INFO',
            THOTH_ANALYZED_IMAGE=image,
            THOTH_ANALYZER_NO_TLS_VERIFY=int(not verify_tls),
            THOTH_ANALYZER_OUTPUT=output
        )

        if registry_user and registry_password:
            self.set_template_parameters(
                template,
                THOTH_REGISTRY_CREDENTIALS=f"{registry_user}:{registry_password}"
            )

        template = self.oc_process(self.middletier_namespace, template)
        analyzer = template['objects'][0]

        response = self.ocp_client.resources.get(api_version='v1', kind=analyzer['kind']).create(
            body=analyzer,
            namespace=self.middletier_namespace
        )

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def run_dependency_monkey(self, application_stack: dict, output: str, runtime_environment: str,
                              debug: bool = False) -> str:
        """Run Dependency Monkey on the provided user input."""
        if not self.middletier_namespace:
            raise ConfigurationError("Running Dependency Monkey requires middletier namespace configuration")

        if not self.infra_namespace:
            raise ConfigurationError(
                "Infra namespace is required to gather Dependency Monkey template when running it"
            )

        response = self.ocp_client.resources.get(api_version='v1', kind='Template').get(
            namespace=self.infra_namespace,
            label_selector='template=dependency-monkey'
        )
        _LOGGER.debug("OpenShift response for getting dependency-monkey template: %r", response.to_dict())
        self._raise_on_invalid_response_size(response)

        template = response.to_dict()['items'][0]

        self.set_template_parameters(
            template,
            THOTH_ADVISER_REQUIREMENTS=application_stack.pop('requirements').replace('\n', '\\n'),
            THOTH_ADVISER_RUNTIME_ENVIRONMENT=runtime_environment,
            THOTH_ADVISER_OUTPUT=output,
            THOTH_LOG_ADVISER='DEBUG' if debug else 'INFO'
        )

        template = self.oc_process(self.middletier_namespace, template)
        dependency_monkey = template['objects'][0]

        response = self.ocp_client.resources.get(api_version='v1', kind=dependency_monkey['kind']).create(
            body=dependency_monkey,
            namespace=self.middletier_namespace
        )

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def run_adviser(self, application_stack: dict, output: str, recommendation_type: str,
                    runtime_environment: str = None, debug: bool = False) -> str:
        """Run adviser on the provided user input."""
        if not self.backend_namespace:
            raise ConfigurationError("Running adviser requires backend namespace configuration")

        if not self.infra_namespace:
            raise ConfigurationError("Infra namespace is required to gather adviser template when running it")

        response = self.ocp_client.resources.get(api_version='v1', kind='Template').get(
            namespace=self.infra_namespace,
            label_selector='template=adviser'
        )
        _LOGGER.debug("OpenShift response for getting adviser template: %r", response.to_dict())
        self._raise_on_invalid_response_size(response)

        template = response.to_dict()['items'][0]
        self.set_template_parameters(
            template,
            THOTH_ADVISER_REQUIREMENTS=application_stack.pop('requirements').replace('\n', '\\n'),
            THOTH_ADVISER_REQUIREMENTS_LOCKED=application_stack.get('requirements_lock', '').replace('\n', '\\n'),
            THOTH_ADVISER_REQUIREMENTS_FORMAT=application_stack.get('requirements_formant', 'pipenv'),
            THOTH_ADVISER_RECOMMENDATION_TYPE=recommendation_type,
            THOTH_ADVISER_RUNTIME_ENVIRONMENT=runtime_environment,
            THOTH_ADVISER_OUTPUT=output,
            THOTH_LOG_ADVISER='DEBUG' if debug else 'INFO'
        )

        template = self.oc_process(self.backend_namespace, template)
        adviser = template['objects'][0]

        response = self.ocp_client.resources.get(api_version='v1', kind=adviser['kind']).create(
            body=adviser,
            namespace=self.backend_namespace
        )

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def run_provenance_checker(self, application_stack: dict, output: str, debug: bool = False) -> str:
        """Run provenance checks on the provided user input."""
        if not self.backend_namespace:
            raise ConfigurationError("Running provenance checks requires backend namespace configuration")

        if not self.infra_namespace:
            raise ConfigurationError("Infra namespace is required to gather provenance template when running it")

        response = self.ocp_client.resources.get(api_version='v1', kind='Template').get(
            namespace=self.infra_namespace,
            label_selector='template=provenance-checker'
        )
        _LOGGER.debug("OpenShift response for getting provenance-checker template: %r", response.to_dict())
        self._raise_on_invalid_response_size(response)

        requirements = application_stack.pop('requirements').replace('\n', '\\n')
        requirements_locked = application_stack.pop('requirements_lock').replace('\n', '\\n')
        template = response.to_dict()['items'][0]
        self.set_template_parameters(
            template,
            THOTH_ADVISER_REQUIREMENTS=requirements,
            THOTH_ADVISER_REQUIREMENTS_LOCKED=requirements_locked,
            THOTH_ADVISER_OUTPUT=output,
            THOTH_LOG_ADVISER='DEBUG' if debug else 'INFO'
        )

        template = self.oc_process(self.backend_namespace, template)
        provenance_checker = template['objects'][0]

        response = self.ocp_client.resources.get(api_version='v1', kind=provenance_checker['kind']).create(
            body=provenance_checker,
            namespace=self.backend_namespace
        )

        _LOGGER.debug("OpenShift response for creating a pod: %r", response.to_dict())
        return response.metadata.name

    def _raise_on_invalid_response_size(self, response):
        """It is expected that there is only one object type for the given item."""
        if len(response.items) != 1:
            raise RuntimeError(
                f"Application misconfiguration - number of templates available in the infra namespace "
                f"{self.infra_namespace!r} is {len(response.items)}, should be 1."
            )

    def oc_process(self, namespace: str, template: dict) -> dict:
        """Process the given template in OpenShift."""
        # TODO: This does not work - see issue reported upstream:
        #   https://github.com/openshift/openshift-restclient-python/issues/190
        # return TemplateOpenshiftIoApi().create_namespaced_processed_template_v1(namespace, template)
        endpoint = "{}/apis/template.openshift.io/v1/namespaces/{}/processedtemplates".format(
            self.openshift_api_url,
            namespace
        )
        response = requests.post(
            endpoint,
            json=template,
            headers={
                'Authorization': 'Bearer {}'.format(self.token),
                'Content-Type': 'application/json'
            },
            verify=self.kubernetes_verify_tls
        )
        _LOGGER.debug("OpenShift master response template (%d): %r", response.status_code, response.text)

        try:
            response.raise_for_status()
        except Exception:
            _LOGGER.error("Failed to process template: %s", response.text)
            raise

        return response.json()
