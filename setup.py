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

"""Setup for thoth-common."""

import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand  # noqa
from pathlib import Path


def _get_install_requires():
    with open("requirements.txt", "r") as requirements_file:
        return [req for req in requirements_file.readlines() if req]


def _get_version():
    with open(os.path.join("thoth", "common", "__init__.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            # dirty, remove trailing and leading chars
            return line.split(" = ")[1][1:-2]
    raise ValueError("No version identifier found")


class Test(TestCommand):
    """Introduce test command to run testsuite using pytest."""

    _IMPLICIT_PYTEST_ARGS = [
        "--timeout=20",
        "--cov=thoth",
        "--cov-report=xml",
        "--mypy",
        "--capture=no",
        "--verbose",
        "-l",
        "-s",
        "-vv",
        "tests/",
    ]

    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        """Initialize command options."""
        super().initialize_options()
        self.pytest_args = None

    def finalize_options(self):
        """Finalize command options."""
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Run pytests."""
        import pytest

        passed_args = list(self._IMPLICIT_PYTEST_ARGS)

        if self.pytest_args:
            self.pytest_args = [arg for arg in self.pytest_args.split() if arg]
            passed_args.extend(self.pytest_args)

        sys.exit(pytest.main(passed_args))


VERSION = _get_version()
setup(
    name="thoth-common",
    version=VERSION,
    description="Shared code logic in the project Thoth.",
    long_description=Path("README.rst").read_text(),
    author="Fridolin Pokorny",
    author_email="fridolin@redhat.com",
    license="GPLv3+",
    packages=["thoth.common", "thoth.common.config"],
    package_data={"thoth.common": ["py.typed"]},
    zip_safe=False,
    cmdclass={"test": Test},
    install_requires=_get_install_requires(),
    command_options={
        "build_sphinx": {
            "version": ("setup.py", VERSION),
            "release": ("setup.py", VERSION),
        }
    },
)
