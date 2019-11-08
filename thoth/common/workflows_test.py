"""Workflows test suite."""

import pytest
import tempfile
import yaml

from flexmock import flexmock
from pathlib import Path

from thoth.common.workflows import Workflow


_HERE = Path(__file__).parent
_WORKFLOW_FILE_PATH = Path(_HERE, "../../fixtures/workflows/hello-world.yaml")


@pytest.fixture
def url() -> str:
    """Fake URL fixture."""


def test_from_file() -> None:
    """Test `Workflow.from_file` methods."""
    wf = Workflow.from_file(_WORKFLOW_FILE_PATH)

    assert isinstance(wf, Workflow)
    assert wf.name == "test"
    assert wf.kind == "Workflow"
    assert len(wf.spec.templates) == 1


def test_from_url(url: str) -> None:
    """Test `Workflow.from_url` methods."""
    from thoth.common import workflows

    fake_response = type("Response", (), {})
    fake_response.text = _WORKFLOW_FILE_PATH.read_text()
    fake_response.raise_for_status = lambda: None
    flexmock(workflows).should_receive("requests.get").and_return(fake_response)

    wf = Workflow.from_url(url)

    assert isinstance(wf, Workflow)
    assert wf.name == "test"
    assert wf.kind == "Workflow"
    assert len(wf.spec.templates) == 1
