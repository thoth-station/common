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

"""Shared code across Thoth analyzers."""

from .helpers import cwd
from .helpers import datetime2datetime_str
from .helpers import datetime_str2timestamp
from .helpers import datetime_str_from_timestamp
from .helpers import get_service_account_token
from .helpers import parse_datetime
from .json import SafeJSONEncoder
from .logging import init_logging
from .logging import logger_setup

__name__ = 'thoth-common'
__version__ = "0.2.2"
