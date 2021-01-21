#!/usr/bin/env python3
# thoth-adviser
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

"""Representation of runtime environment entry collapsing hardware, runtime and other information."""

import os
import logging
from typing import Optional
from typing import Any
from typing import Dict
from typing import Tuple

import attr
import yaml

from .hardware_information import HardwareInformation
from .operating_system import OperatingSystem

from ..exceptions import ConfigurationError

_LOGGER = logging.getLogger(__name__)


@attr.s(slots=True)
class RuntimeEnvironment:
    """An entry collapsing configuration options in the user configuration file."""

    hardware = attr.ib(type=HardwareInformation)
    operating_system = attr.ib(type=OperatingSystem)
    python_version = attr.ib(type=str, default=None)
    cuda_version = attr.ib(type=str, default=None)
    openblas_version = attr.ib(type=str, default=None)
    openmpi_version = attr.ib(type=str, default=None)
    cudnn_version = attr.ib(type=str, default=None)
    mkl_version = attr.ib(type=str, default=None)
    base_image = attr.ib(type=str, default=None)
    name = attr.ib(type=str, default=None)
    platform = attr.ib(type=str, default=None)
    _python_version_tuple = attr.ib(
        type=Optional[Tuple[int, int]], default=None, init=False
    )

    @classmethod
    def load(cls, content: Optional[str] = None) -> "RuntimeEnvironment":
        """Load runtime environment information from file or from a JSON representation, transparently."""
        if content is None:
            return cls.from_dict({})

        if os.path.isfile(content):
            with open(content, "r") as input_file:
                content = input_file.read()

        file_content = yaml.safe_load(content)
        return cls.from_dict(file_content)

    @classmethod
    def from_dict(cls, dict_: Optional[Dict[Any, Any]] = None) -> "RuntimeEnvironment":
        """Parse one configuration entry from a dictionary."""
        dict_ = dict(dict_ or {})

        hardware = dict_.pop("hardware", {})
        operating_system = dict_.pop("operating_system", {})
        python_version = dict_.pop("python_version", None)
        cuda_version = dict_.pop("cuda_version", None)
        name = dict_.pop("name", None)
        platform = dict_.pop("platform", None)

        for key, value in dict_.items():
            _LOGGER.warning(
                "Unknown configuration entry in the configuration file %r with value %r",
                key,
                value,
            )

        instance = cls(
            hardware=HardwareInformation.from_dict(hardware),  # type: ignore
            operating_system=OperatingSystem.from_dict(  # type: ignore
                operating_system
            ),
            python_version=python_version,
            cuda_version=cuda_version,
            name=name,
            platform=platform,
        )

        if instance.operating_system.version and not instance.operating_system.name:
            raise ConfigurationError(
                "Runtime environment stated operating system version but no operating system name provided"
            )

        return instance

    def get_python_version_tuple(self) -> Tuple[int, int]:
        """Get tuple with Python version (major, minor) information."""
        if self.python_version is None:
            raise ValueError("No Python version provided")

        if self._python_version_tuple is None:
            self._python_version_tuple = tuple(map(int, self.python_version.split(".", maxsplit=2)))  # type: ignore

        return self._python_version_tuple  # type: ignore

    def to_dict(self, without_none: bool = False) -> Dict[str, Any]:
        """Convert runtime environment configuration to a dict representation."""
        dict_ = attr.asdict(self)
        dict_.pop("_python_version_tuple", None)

        if not without_none:
            return dict_

        result: Dict[str, Any] = {}
        for key, value in dict_.items():
            # We support one nested configuration entries.
            if isinstance(value, dict):
                for k, v in dict_[key].items():
                    if v is not None:
                        if key not in result:
                            result[key] = {}
                        if k not in result[key]:
                            result[key][k] = {}
                        result[key][k] = v
                continue

            if value is not None:
                result[key] = value

        return result

    def to_string(self) -> str:
        """Convert runtime environment configuration to a string representation."""
        dict_representation = self.to_dict(without_none=True)
        return str(dict_representation)

    def is_fully_specified(self) -> bool:
        """Check if the given runtime environment is fully specified."""
        runtime_environment = (
            self.operating_system.name,
            self.operating_system.version,
            self.python_version,
            self.platform,
        )
        return all(i is not None for i in runtime_environment)
