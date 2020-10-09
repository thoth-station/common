#!/usr/bin/env python3
# thoth-common
# Copyright(C) 2019, 2020 Thoth team
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

"""Workflows test suite."""

import pytest

import requests
from flexmock import flexmock

from thoth.common import Workflow  # type: ignore

from .base_test import CommonTestCase


@pytest.fixture
def url() -> str:
    """Fake URL fixture."""


class TestWorkflows(CommonTestCase):
    """Test implementation of workflows."""

    _WORKFLOW_FILE = CommonTestCase.DATA / "workflows" / "hello-world.yaml"

    def test_from_file(self) -> None:
        """Test `Workflow.from_file` methods."""
        wf = Workflow.from_file(self._WORKFLOW_FILE)

        assert isinstance(wf, Workflow)
        assert wf.name == "test"
        assert wf.kind == "Workflow"
        assert len(wf.spec.templates) == 1

    def test_from_url(self, url: str) -> None:
        """Test `Workflow.from_url` methods."""
        fake_response = type(
            "Response",
            (),
            {"text": self._WORKFLOW_FILE.read_text(), "raise_for_status": lambda: None},
        )
        flexmock(requests).should_receive("get").and_return(fake_response)

        wf = Workflow.from_url(url)

        assert isinstance(wf, Workflow)
        assert wf.name == "test"
        assert wf.kind == "Workflow"
        assert len(wf.spec.templates) == 1
