import random

from typing import Optional

from argo.workflows import client
from argo.workflows import models

from .exceptions import ConfigurationError
from .exceptions import WorkflowError

from .openshift import OpenShift


class Workflow(models.V1alpha1Workflow):
    def __init__(
        self, api_version=None, kind=None, metadata=None, spec=None, status=None
    ):
        super().__init__(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
        )

        self.__dict__.update(self.metadata)

    @classmethod
    def from_dict(cls, wf: dict) -> Workflow:
        """Create a Workflow from a dict."""

    @classmethod
    def from_file(cls, fp: str) -> Workflow:
        """Create a Workflow from a file."""

    @classmethod
    def from_url(cls, url: str) -> Workflow:
        """Create a Workflow from a remote file."""


class WorkflowManager:
    """Argo Workflow manager."""

    def __init__(self, ocp_client: Optional[OpenShift] = None):
        self.openshift = ocp_client or OpenShift()
        self.api = client.V1alpha1Api(client.ApiClient(self.openshift.configuration))

    def _submit_workflow(
        self,
        namespace: Optional[str],
        wf: Union[models.V1alpha1Workflow, dict],
        *,
        parameters: Optional[Dict[str, str]] = None,
    ) -> string:
        """Submit an Argo Workflow to a given namespace."""
        parameters = parameters or {}

        if not isinstance(wf, Workflow):
            wf = Workflow.from_dict(wf)

        new_parameters: List[models.V1alpha1Parameter] = []
        for name, value in parameters.items():
            param = models.V1alpha1Parameter(name=name, value=value)
            new_parameters.append(param)

        for p in wf.spec.arguments.parameters:
            if p.name in parameters:
                continue  # overridden
            elif not p.value and not p.default:
                raise WorkflowError(f"Missing required workflow parameter {p.name}")

            new_parameters.append(p)

        wf.spec.arguments.parameters = new_parameters

        # submit the workflow
        created = self.api.create_namespaced_workflow(namespace, wf)

        return created.name
