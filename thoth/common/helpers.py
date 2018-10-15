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

"""Various utilities to make your life easier."""

import datetime
import os

from contextlib import contextmanager


@contextmanager
def cwd(target):
    """Manage cwd in a pushd/popd fashion."""
    curdir = os.getcwd()
    os.chdir(target)
    try:
        yield curdir
    finally:
        os.chdir(curdir)


def parse_datetime(datetime_string: str) -> datetime.datetime:
    """Parse datetime string represented in ISO format."""
    return datetime.datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S.%f")


def datetime_str2timestamp(datetime_string: str) -> int:
    """Parse datetime string represented in ISO format and return timestamp."""
    return int(parse_datetime(datetime_string).timestamp())


def datetime2datetime_str(dt: datetime.datetime = None) -> str:
    """Create a string representation of a datetime."""
    if not dt:
        return datetime.datetime.utcnow().isoformat()

    return dt.isoformat()


def datetime_str_from_timestamp(timestamp: int) -> str:
    """Convert a timestamp to datetime string representation."""
    return datetime2datetime_str(datetime.datetime.fromtimestamp(timestamp))


def get_service_account_token():
    """Get token from service account token file."""
    try:
        with open('/var/run/secrets/kubernetes.io/serviceaccount/token', 'r') as token_file:
            return token_file.read()
    except FileNotFoundError as exc:
        raise FileNotFoundError("Unable to get service account token, please check "
                                "that service has service account assigned with exposed token") from exc
