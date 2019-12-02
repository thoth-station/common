# thoth-common
# Copyright(C) 2019 Marek Cermak
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

from attrdict import AttrDict

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
    managemend easier.
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
        return f"workflow-{digest}"

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
        else:
            _LOGGER.warning(
                "Validation is turned off. This may result in missing or invalid attributes."
            )
            obj = json.loads(body["data"])
            aux = to_snake_case(obj)

            wf = AttrDict(**aux)

        instance = cls(
            api_version=wf.api_version,
            kind=wf.kind,
            metadata=wf.metadata,
            spec=wf.spec,
            status=wf.status,  # a small hack to overcome validation
        )

        instance.__validated = validate

        return instance


class WorkflowManager:
    """Argo Workflow manager."""

    def __init__(
        self,
        ocp_client: Optional[OpenShift] = None,
        ocp_config: Optional[Mapping[str, str]] = None,
    ):
        """Initialize WorkflowManager instance."""
        ocp_config = ocp_config or {}

        self.openshift = ocp_client or OpenShift(**ocp_config)
        self.api = client.V1alpha1Api(client.ApiClient(self.openshift.configuration))

    def get_workflow_template(
        self, namespace: str, label_selector: str, *, parameters: Dict[str, str]
    ):
        """Get Workflow template."""
        template = self.openshift._get_template(label_selector, namespace=namespace)

        self.openshift.set_template_parameters(template, **parameters)

        template = self.openshift.oc_process(namespace, template)
        return template

    def submit_workflow(
        self,
        namespace: str,
        wf: Union[models.V1alpha1Workflow, Dict[str, Any]],
        *,
        parameters: Optional[Dict[str, str]] = None,
        validate: bool = True,
    ) -> str:
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
                elif not getattr(p, "value") and not getattr(p, "default"):
                    raise WorkflowError(f"Missing required workflow parameter {p.name}")

                new_parameters.append(p)

            wf.spec.arguments.parameters = new_parameters

        # Set the ID to the name that we can track it easily later on
        wf.metadata.name = wf.id

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
        created: models.V1alpha1Workflow = self.api.create_namespaced_workflow(
            namespace, body
        )

        # return the computed Workflow ID
        return wf.name

    def submit_workflow_from_template(
        self,
        namespace: str,
        label_selector: str,
        *,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
        workflow_namespace: Optional[str] = None,
    ) -> str:
        """Retrieve and Submit Workflow from an OpenShift template.

        :param namespace: namespace to lookup the template in

            If `workflow_namespace` is not provided, this namespace
            is also implicitly the namespace where the workflow is submitted

        :param label_selector: selector for the template, i.e. 'template=workflow-template'
        :param template_parameters: parameters for the template
        :param workflow_parameters: parameters for the workflow
        :param workflow_namespace: namespace to submit the workflow to
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

    def submit_inspection_workflow(
        self,
        inspection_id: str,
        template_parameters: Optional[Dict[str, str]] = None,
        workflow_parameters: Optional[Dict[str, Any]] = None,
        use_hw_template: bool = False,
    ) -> str:
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

        template_parameters["AMUN_INSPECTION_ID"] = inspection_id
        template_parameters["THOTH_INFRA_NAMESPACE"] = template_parameters.get(
            "THOTH_INFRA_NAMESPACE", self.openshift.amun_infra_namespace
        )

        workflow_id: str = self.submit_workflow_from_template(
            template_parameters["THOTH_INFRA_NAMESPACE"],
            label_selector,
            template_parameters=template_parameters,
            workflow_parameters=workflow_parameters,
            workflow_namespace=self.openshift.amun_inspection_namespace
        )

        return workflow_id
