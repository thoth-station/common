# thoth-common
# Copyright(C) 2019, 2020 Marek Cermak
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

"""Workflow management for Thoth."""

import logging
import json
import requests
import yaml

from pathlib import Path

from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Union

from argo.workflows import client
from argo.workflows import models

from .exceptions import ConfigurationError
from .exceptions import WorkflowError

from .helpers import to_camel_case
from .helpers import to_snake_case

from .openshift import OpenShift

_LOGGER = logging.getLogger(__name__)


class Workflow(models.V1alpha1Workflow):  # type: ignore
    """Argo Workflow instance.

    This is a subclass of argo.workflows V1alpha1Workflow model
    which provides a convenient set of methods to make workflow
    management easier.
    """

    def __init__(
        self,
        api_version: str,
        kind: str,
        metadata: models.V1alpha1Metadata,
        spec: models.V1alpha1WorkflowSpec,
        status: Optional[models.V1alpha1WorkflowStatus] = None,
    ):
        """Initialize Workflow instance."""
        super().__init__(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status or {},
        )

        self.__validated = False

    @property
    def name(self) -> Union[str, None]:
        """Get Workflow name."""
        name: Union[str, None] = getattr(self.metadata, "name", None)
        return name

    @property
    def id(self) -> str:
        """Get Workflow ID."""
        prefix: str = self.name or getattr(self.metadata, "generate_name")
        digest: str = OpenShift.generate_id(prefix)
        return digest

    @property
    def validated(self) -> bool:
        """Return whether this workflow has been validated."""
        return self.__validated

    def __eq__(self, other: Any) -> Any:
        """Compare workflows for equality."""
        return self.id == other.id

    def __hash__(self) -> Any:
        """Compute hash of this Workflow."""
        return self.to_str().__hash__()

    @classmethod
    def from_file(cls, fp: Union[str, Path], validate: bool = True) -> "Workflow":
        """Create a Workflow from a file."""
        wf_path = Path(fp)

        wf: Dict[str, Any] = yaml.safe_load(wf_path.read_text())
        return cls.from_dict(wf, validate=validate)

    @classmethod
    def from_url(cls, url: str, validate: bool = True) -> "Workflow":
        """Create a Workflow from a remote file."""
        resp = requests.get(
            "https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml"
        )
        resp.raise_for_status()

        wf: Dict[str, Any] = yaml.safe_load(resp.text)
        return cls.from_dict(wf, validate=validate)

    @classmethod
    def from_dict(cls, wf: Dict[str, Any], validate: bool = True) -> "Workflow":
        """Create a Workflow from a dict."""
        # work around validation issues and allow empty status
        wf["status"] = wf.get("status", {}) or {}

        return cls.from_string(json.dumps(wf), validate=validate)

    @classmethod
    def from_string(cls, wf: str, validate: bool = True) -> "Workflow":
        """Create a Workflow from a YAML string."""
        body = {"data": wf}

        return cls.__deserialize(body, validate=validate)

    @classmethod
    def __deserialize(cls, body: Dict[str, str], *, validate: bool) -> "Workflow":
        """Deserialize given object into a Workflow instance."""
        wf: models.V1alpha1Workflow
        if validate:
            attr = type("AttributeDict", (), body)

            wf = client.ApiClient().deserialize(attr, models.V1alpha1Workflow)

            instance = cls(
                api_version=wf.api_version,
                kind=wf.kind,
                metadata=wf.metadata,
                spec=wf.spec,
                status=wf.status,  # a small hack to overcome validation
            )
        else:
            _LOGGER.warning(
                "Validation is turned off. This may result in missing or invalid attributes."
            )
            obj = json.loads(body["data"])
            aux = to_snake_case(obj)

            instance = cls(
                api_version=aux.get("api_version"),
                kind=aux.get("kind"),
                metadata=aux.get("metadata"),
                spec=aux.get("spec"),
                status=aux.get("status"),
            )

        instance.__validated = validate
        return instance


class WorkflowManager:
    """Argo Workflow manager."""

    def __init__(
        self,
        openshift: Optional[OpenShift] = None,
        openshift_config: Optional[Mapping[str, str]] = None,
    ):
        """Initialize WorkflowManager instance."""
        ocp_config = openshift_config or {}

        self.openshift = openshift or OpenShift(**ocp_config)
        self.api = client.V1alpha1Api(client.ApiClient(self.openshift.configuration))

    def get_workflow_template(
        self,
        namespace: str,
        label_selector: str,
        *,
        parameters: Optional[Dict[str, str]],
    ) -> Dict[str, Any]:
        """Get Workflow template."""
        template = self.openshift._get_template(label_selector, namespace=namespace)

        if parameters:
            self.openshift.set_template_parameters(template, **parameters)

        template = self.openshift.oc_process(namespace, template)
        return template

    def get_workflow(self, namespace: str, name: str) -> Dict[str, Any]:
        """Get Workflow in namespace by name."""
        response: Dict[str, Any] = self.api.get_namespaced_workflow(
            namespace=namespace, name=name
        ).to_dict()
        return response

    def get_workflows(
        self, namespace: str, *, label_selector: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get Workflows in namespace."""
        parameters = locals()
        parameters.pop("self")
        if not label_selector:
            parameters.pop("label_selector")
        response: Dict[str, Any] = self.api.list_namespaced_workflows(
            **parameters
        ).to_dict()
        return response

    def get_workflow_info(self, namespace: str, name: str) -> Dict[str, Any]:
        """Get Workflow in namespace by name."""
        workflow = self.get_workflow(namespace=namespace, name=name)
        workflow_main = self._collect_workflow_info(workflow=workflow)
        return {workflow_main["name"]: workflow_main}

    def get_workflows_info(
        self, namespace: str, *, label_selector: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get workflows info from a specific namespace."""
        workflows = self.get_workflows(
            namespace=namespace, label_selector=label_selector
        )
        workflow_data = {}
        for workflow in workflows["items"]:

            workflow_main = self._collect_workflow_info(workflow=workflow)

            workflow_data[workflow["metadata"]["name"]] = workflow_main

        return workflow_data

    def _collect_workflow_info(self, workflow: Dict[str, Any]) -> Dict[str, Any]:
        """Collect Workflow info."""
        started_at = workflow["status"]["started_at"]
        finished_at = workflow["status"]["finished_at"]

        duration = None
        if started_at and finished_at:
            duration = (finished_at - started_at).total_seconds()

        tasks_names = self._collect_tasks_names(templates=workflow["spec"]["templates"])
        nodes = self._collect_workflows_tasks_info(
            nodes=workflow["status"]["nodes"], tasks_names=tasks_names
        )

        workflow_info = {
            "name": workflow["metadata"]["name"],
            "labels": workflow["metadata"]["labels"],
            "started_at": started_at,
            "finished_at": finished_at,
            "duration": duration,
            "phase": workflow["status"]["phase"],
            "nodes": nodes,
        }

        return workflow_info

    @staticmethod
    def _collect_tasks_names(templates: List[Dict[str, Any]]) -> List[str]:
        """Collect tasks names from Workflow template."""
        tasks_names = []

        for template in templates:
            # TODO: Extend to other structures beside dag and consider also steps
            if "dag" in template.keys():
                if template["dag"]:
                    for task in template["dag"]["tasks"]:
                        tasks_names.append(task["name"])
        return tasks_names

    @staticmethod
    def _collect_workflows_tasks_info(
        nodes: Dict[str, Any], tasks_names: List[str]
    ) -> Dict[str, Any]:
        """Collect info about tasks in the Workflow."""
        nodes_info: Dict[str, Any] = {}
        if not nodes:
            return nodes_info

        for pod_id, node in nodes.items():

            if node["display_name"] in tasks_names:
                duration = None
                if node["started_at"] and node["finished_at"]:
                    duration = (
                        node["finished_at"] - node["started_at"]
                    ).total_seconds()

                nodes_info[pod_id] = {
                    "pod_id": pod_id,
                    "display_name": node["display_name"],
                    "started_at": node["started_at"],
                    "finished_at": node["finished_at"],
                    "duration": duration,
                    "phase": node["phase"],
                    "message": node["message"],
                }

        return nodes_info

    def get_workflow_and_tasks_status(
        self, namespace: str, name: str
    ) -> Dict[str, Any]:
        """Get workflow and tasks status from a specific namespace."""
        workflow_info = self.get_workflow_info(namespace=namespace, name=name)
        return self._analyze_workflows_info(workflow_info)

    def get_workflows_and_tasks_status(
        self, namespace: str, label_selector: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get workflows and tasks status from a specific namespace."""
        workflows_info = self.get_workflows_info(
            namespace=namespace, label_selector=label_selector
        )
        return self._analyze_workflows_info(workflows_info)

    def _analyze_workflows_info(self, workflows_info: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze workflows info."""
        workflows_status: Dict[str, Any] = {}
        for workflow_id, workflow_data in workflows_info.items():
            workflow_phase = workflow_data["phase"]
            labels = workflow_data["labels"]
            workflow_type = self._check_component_label(
                workflow_id=workflow_id, labels=labels
            )
            nodes = workflow_data["nodes"]
            workflows_status = self._update_workflows_status(
                workflows_status=workflows_status,
                workflow_type=workflow_type,
                workflow_phase=workflow_phase,
                nodes=nodes,
            )
        return workflows_status

    @staticmethod
    def _check_component_label(workflow_id: str, labels: Dict[str, Any]) -> str:
        """Check if component label is present in order to know which component is running in the workflow."""
        workflow_type = [label for key, label in labels.items() if key == "component"]
        if workflow_type:
            to_ret: str = workflow_type[0]
        else:
            to_ret = "missing_component_label"
            _LOGGER.warning(f"Missing component label for workflow: {workflow_id}")

        return to_ret

    def _update_workflows_status(
        self,
        workflows_status: Dict[str, Any],
        workflow_type: str,
        workflow_phase: str,
        nodes: Optional[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Update workflows status collection."""
        if workflow_type not in workflows_status:
            workflows_status[workflow_type] = {
                "component": workflow_type,
                "status": {},
                "tasks": {},
            }

        if workflow_phase:
            if workflow_phase not in workflows_status[workflow_type]["status"].keys():
                workflows_status[workflow_type]["status"][workflow_phase] = 1
            else:
                workflows_status[workflow_type]["status"][workflow_phase] += 1
        else:
            if "Unknown" not in workflows_status[workflow_type]["status"].keys():
                workflows_status[workflow_type]["status"]["Unknown"] = 1
            else:
                workflows_status[workflow_type]["status"]["Unknown"] += 1

        workflows_status[workflow_type]["tasks"] = self._update_tasks_status(
            workflows_status[workflow_type]["tasks"], nodes
        )

        return workflows_status

    @staticmethod
    def _update_tasks_status(
        task_status: Dict[str, Any], nodes: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Update tasks status collection."""
        if not nodes:
            return task_status

        for pod_id, pod_data in nodes.items():
            task_name = pod_data["display_name"]
            if task_name not in task_status.keys():
                task_status[task_name] = {}
                pod_phase = pod_data["phase"]
                task_status[task_name][pod_phase] = 1
            else:
                pod_phase = pod_data["phase"]
                if pod_phase not in task_status[task_name].keys():
                    task_status[task_name][pod_phase] = 1
                else:
                    task_status[task_name][pod_phase] += 1

        return task_status

    def submit_workflow(
        self,
        namespace: str,
        wf: Union[models.V1alpha1Workflow, Dict[str, Any]],
        *,
        parameters: Optional[Dict[str, str]] = None,
        validate: bool = True,
    ) -> Union[str, None]:
        """Submit an Argo Workflow to a given namespace.

        :returns: Workflow ID
        """
        parameters = parameters or {}

        if not isinstance(wf, Workflow) and isinstance(wf, dict):
            wf = Workflow.from_dict(wf, validate=validate)
        elif not isinstance(wf, models.V1alpha1Workflow):
            raise TypeError(
                f"Expected {Union[models.V1alpha1Workflow, dict]}, got {type(wf)}"
            )

        new_parameters: List[models.V1alpha1Parameter] = []
        for name, value in parameters.items():
            param = models.V1alpha1Parameter(name=name, value=value)
            new_parameters.append(param)

        if hasattr(wf.spec, "arguments"):
            for p in getattr(wf.spec.arguments, "parameters", []):
                if p.name in parameters:
                    continue  # overridden
                elif not (getattr(p, "value") or hasattr(p, "default")):
                    raise WorkflowError(f"Missing required workflow parameter {p.name}")

                new_parameters.append(p)

            wf.spec.arguments.parameters = new_parameters

        if not getattr(wf, "validated", True):
            _LOGGER.debug(
                "The Workflow has not been previously validated."
                "Sanitizing for serialization."
            )
            body = to_camel_case(wf.to_dict())
        else:
            body = self.api.api_client.sanitize_for_serialization(wf)

        _LOGGER.debug(f"Submitting workflow: {body}")

        # submit the workflow
        created: models.V1alpha1Workflow = self.api.create_namespaced_workflow(  # noqa
            namespace, body
        )

        return wf.name

    def get_pending_workflows(self, workflow_namespace: str) -> int:
        """Get the total number of pending workflows in a given namespace."""
        count = 0
        for i in self.api.list_namespaced_workflows(workflow_namespace).items:
            count += i.status.started_at is None

        return count

    def submit_workflow_from_template(
        self,
        namespace: str,
        label_selector: str,
        *,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
        workflow_namespace: Optional[str] = None,
        workflow_limit: Optional[int] = None,
    ) -> Union[str, None]:
        """Retrieve and Submit Workflow from an OpenShift template.

        :param namespace: namespace to lookup the template in

            If `workflow_namespace` is not provided, this namespace
            is also implicitly the namespace where the workflow is submitted

        :param label_selector: selector for the template, i.e. 'template=workflow-template'
        :param template_parameters: parameters for the template
        :param workflow_parameters: parameters for the workflow
        :param workflow_namespace: namespace to submit the workflow to
        :param workflow_limit: limit number of workflows currently in memory for workflowController
        """
        template = self.get_workflow_template(
            namespace, label_selector, parameters=template_parameters
        )

        workflow_object: Dict[str, Any] = template["objects"][0]
        workflow: Workflow = Workflow.from_dict(workflow_object, validate=True)

        workflow_id = self.submit_workflow(
            workflow_namespace or namespace, workflow, parameters=workflow_parameters
        )

        return workflow_id

    def submit_inspection(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
        use_hw_template: bool = False,
    ) -> Optional[str]:
        """Submit the Inspection Workflow."""
        if not self.openshift.amun_infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.amun_inspection_namespace:
            raise ConfigurationError("Inspection namespace was not provided.")

        if use_hw_template:
            label_selector = "template=amun-inspection-workflow-with-cpu"
        else:
            label_selector = "template=amun-inspection-workflow"

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        template_parameters[
            "THOTH_INFRA_NAMESPACE"
        ] = self.openshift.amun_infra_namespace

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.amun_infra_namespace,
            label_selector,
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.amun_inspection_namespace,
        )

        return workflow_id

    def submit_adviser(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Adviser Workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.backend_namespace:
            raise ConfigurationError("Backend namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=adviser",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.backend_namespace,
        )

        return workflow_id

    def submit_package_extract(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, str]] = None,
    ) -> Optional[str]:
        """Submit package-extract workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=package-extract",
            template_parameters=template_parameters or {},
            workflow_parameters=workflow_parameters or {},
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id

    def submit_dependency_monkey(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Dependency Monkey workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=dependency-monkey",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id

    def submit_provenance_checker(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit provenance checker workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.backend_namespace:
            raise ConfigurationError("Backend namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=provenance-checker",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.backend_namespace,
        )

        return workflow_id

    def submit_kebechet(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Kebechet Workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.backend_namespace:
            raise ConfigurationError("Backend namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=kebechet",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.backend_namespace,
        )

        return workflow_id

    def submit_kebechet_administrator(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Kebechet Administrator Workflow for an internal trigger message."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.backend_namespace:
            raise ConfigurationError("Backend namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=kebechet-administrator",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.backend_namespace,
        )

        return workflow_id

    def submit_kebechet_run_url(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Kebechet Run-URL Workflow for a single slug."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.backend_namespace:
            raise ConfigurationError("Backend namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=kebechet-run-url",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.backend_namespace,
        )

        return workflow_id

    def submit_solver(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Solver Workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=solver",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id

    def submit_revsolver(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit reverse solver workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=revsolver",
            template_parameters=template_parameters or {},
            workflow_parameters=workflow_parameters or {},
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id

    def submit_qebhwt(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Workflow for Qeb-Hwt GitHub App."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.backend_namespace:
            raise ConfigurationError("Backend namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=qeb-hwt",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.backend_namespace,
        )

        return workflow_id

    def submit_security_indicator(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Security Indicator Workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=security-indicators",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id

    def submit_mi(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit Meta-information Indicators workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=mi",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id

    def submit_build_analysis(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit build analysis workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=build-analysis",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id

    def submit_graph_sync(
        self,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
    ) -> Optional[str]:
        """Submit graph-sync workflow."""
        if not self.openshift.infra_namespace:
            raise ConfigurationError("Infra namespace was not provided.")

        if not self.openshift.middletier_namespace:
            raise ConfigurationError("Middletier namespace was not provided.")

        template_parameters = template_parameters or {}
        workflow_parameters = workflow_parameters or {}

        workflow_id: Optional[str] = self.submit_workflow_from_template(
            self.openshift.infra_namespace,
            label_selector="template=graph-sync",
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.middletier_namespace,
        )

        return workflow_id
