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
import random
import re
import requests
import yaml

from pathlib import Path

from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from attrdict import AttrDict

from argo.workflows import client
from argo.workflows import models

from .exceptions import ConfigurationError
from .exceptions import WorkflowError

from .openshift import OpenShift

_LOGGER = logging.getLogger(__name__)


class Workflow(models.V1alpha1Workflow):
    """Argo Workflow instance.

    This is a subclass of argo.workflows V1alpha1Workflow model
    which provides a convenient set of methods to make workflow
    managemend easier.
    """

    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: models.V1alpha1Metadata = None,
        spec: models.V1alpha1WorkflowSpec = None,
        status: models.V1alpha1WorkflowStatus = None,
    ):
        """Initialize Workflow instance."""
        super().__init__(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
        )

        if not status:
            # fixup the status empty dict to prevent serialization issues
            status = None

        self.__validated = False

    @property
    def name(self) -> str:
        """Get Workflow name."""
        return self.metadata.get("name")

    @property
    def id(self) -> str:
        """Get Workflow ID."""
        digest = abs(self.__hash__())
        return f"workflow{'-' + self.name if self.name else ''}-{digest}"

    @property
    def validated(self) -> str:
        """Return whether this workflow has been validated."""
        return self.__validated

    def __eq__(self, other):
        """Compare workflows for equality."""
        return self.id == other.id

    def __hash__(self):
        """Compute hash of this Workflow."""
        return self.to_str().__hash__()

    @classmethod
    def from_file(cls, fp: str, fmt: str = "yaml") -> "Workflow":
        """Create a Workflow from a file."""
        wf_path = Path(fp)

        fmt = fmt.lower()
        if fmt == "yaml":
            wf: dict = yaml.safe_load(wf_path.read_text())
        elif fmt == "json":
            wf: dict = json.loads(wf_path.read_text())
        else:
            raise ValueError(f"Argument `fmt` expected 'yaml' or 'json', got: {fmt}")

        return cls.from_dict(wf)

    @classmethod
    def from_url(cls, url: str, validate: bool = True) -> "Workflow":
        """Create a Workflow from a remote file."""
        resp = requests.get(
            "https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml"
        )
        resp.raise_for_status()

        wf = yaml.safe_load(resp.text)
        return cls.from_dict(wf, validate=validate)

    @classmethod
    def from_dict(cls, wf: dict, validate: bool = True) -> "Workflow":
        """Create a Workflow from a dict."""
        return cls.from_string(json.dumps(wf), validate=validate)

    @classmethod
    def from_string(cls, wf: str, validate: bool = True) -> "Workflow":
        """Create a Workflow from a YAML string."""
        body = {"data": wf}

        return cls.__deserialize(body, validate=validate)

    @classmethod
    def __deserialize(cls, body: dict, *, validate: bool) -> "Workflow":
        """Deserialize given object into a Workflow instance."""

        def __to_snake_case(obj: dict):
            if isinstance(obj, dict):
                aux = dict()
                for key, value in obj.items():
                    new_key = re.sub(
                        r"(?<=.{1})([A-Z])", lambda m: f"_{m.group(0)}", key
                    ).lower()
                    aux[new_key] = __to_snake_case(value)

                return aux

            return obj

        if validate:
            attr = type("AttributeDict", (), body)

            wf: models.V1alpha1Workflow = client.ApiClient().deserialize(
                attr, models.V1alpha1Workflow
            )
        else:
            _LOGGER.warning(
                "Validation is turned off. This may result in missing or invalid attributes."
            )
            obj = json.loads(body["data"])
            aux = __to_snake_case(obj)

            wf: models.V1alpha1Workflow = AttrDict(**aux)

        instance = cls(
            api_version=wf.api_version,
            kind=wf.kind,
            metadata=wf.metadata,
            spec=wf.spec,
            status=wf.get("status", {}),  # a small hack to overcome validation
        )

        instance.__validated = validate

        return instance


class WorkflowManager:
    """Argo Workflow manager."""

    def __init__(
        self,
        ocp_client: Optional[OpenShift] = None,
        ocp_config: Optional[Dict[str, str]] = None,
    ):
        """Initialize WorkflowManager instance."""
        ocp_config = ocp_config or {}

        self.openshift = ocp_client or OpenShift(**ocp_config)
        self.api = client.V1alpha1Api(client.ApiClient(self.openshift.configuration))

    def _submit_workflow(
        self,
        namespace: str,
        wf: Union[models.V1alpha1Workflow, dict],
        *,
        parameters: Optional[Dict[str, str]] = None,
        validate: bool = True,
    ) -> str:
        """Submit an Argo Workflow to a given namespace."""
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
            for p in wf.spec.arguments.get("parameters", []):
                if p.name in parameters:
                    continue  # overridden
                elif not p.value and not p.default:
                    raise WorkflowError(f"Missing required workflow parameter {p.name}")

                new_parameters.append(p)

            wf.spec.arguments.parameters = new_parameters

        body = wf.to_dict()
        if not getattr(wf, "validated", True):
            _LOGGER.debug(
                "The Workflow has not been previously validated. Sanitizing for serialization.",
                wf,
            )
            body = __to_camel_case(wf)

            def __to_camel_case(obj: dict):
                if isinstance(obj, dict):
                    aux = dict()
                    for key, value in obj.items():
                        new_key = re.sub(
                            r"(?<=.{1})_([a-z])", lambda m: f"{m.group(1).upper()}", key
                        )
                        aux[new_key] = __to_camel_case(value)

                    return aux

                return obj

        _LOGGER.debug("Submitting workflow: ", wf)

        # submit the workflow
        created: models.V1alpha1Workflow = self.api.create_namespaced_workflow(
            namespace, body
        )

        return created.metadata.name
