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

"""Shared code across Thoth analyzers."""

from .config import HardwareInformation
from .config import OperatingSystem
from .config import RuntimeEnvironment
from .enums import ThothAdviserIntegrationEnum
from .helpers import cwd
from .helpers import datetime2datetime_str
from .helpers import datetime_str2timestamp
from .helpers import datetime_str_from_timestamp
from .helpers import get_service_account_token
from .helpers import parse_datetime
from .helpers import timestamp2datetime
from .json import SafeJSONEncoder
from .logging import init_logging
from .openshift import OpenShift
from .workflows import Workflow
from .workflows import WorkflowManager

__name__ = "thoth-common"
__version__ = "0.13.10"


__all__ = [
    "cwd",
    "datetime2datetime_str",
    "datetime_str2timestamp",
    "datetime_str_from_timestamp",
    "get_service_account_token",
    "HardwareInformation",
    "init_logging",
    "OpenShift",
    "OperatingSystem",
    "parse_datetime",
    "RuntimeEnvironment",
    "SafeJSONEncoder",
    "ThothAdviserIntegrationEnum",
    "Workflow",
    "WorkflowManager",
    "timestamp2datetime",
]
