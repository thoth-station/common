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


def datetime2datetime_str(dt: datetime.datetime) -> str:
    """Create a string representation of a datetime."""
    return dt.isoformat()
