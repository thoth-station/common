#!/usr/bin/env python3
# thoth-adviser
# Copyright(C) 2018, 2019 Fridolin Pokorny
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
    name = attr.ib(type=str, default=None)

    @classmethod
    def load(cls, content: str = None):
        """Load runtime environment information from file or from a JSON representation, transparently."""
        if content is None:
            return cls.from_dict({})

        if os.path.isfile(content):
            with open(content, "r") as input_file:
                content = input_file.read()

        content = yaml.safe_load(content)
        return cls.from_dict(content)

    @classmethod
    def from_dict(cls, dict_: dict = None):
        """Parse one configuration entry from a dictionary."""
        dict_ = dict(dict_ or {})

        hardware = dict_.pop("hardware", {})
        operating_system = dict_.pop("operating_system", {})
        python_version = dict_.pop("python_version", None)
        cuda_version = dict_.pop("cuda_version", None)
        name = dict_.pop("name", None)

        for key, value in dict_.items():
            _LOGGER.warning(
                "Unknown configuration entry in the configuration file %s with value %s",
                key,
                value
            )

        instance = cls(
            hardware=HardwareInformation.from_dict(hardware),
            operating_system=OperatingSystem.from_dict(operating_system),
            python_version=python_version,
            cuda_version=cuda_version,
            name=name
        )

        if instance.operating_system.version and not instance.operating_system.name:
            raise ConfigurationError(
                "Runtime environment stated operating system version but no operating system name provided"
            )

        return instance

    def to_dict(self, without_none: bool = False):
        """Convert runtime environment configuration to a dict representation."""
        dict_ = attr.asdict(self)
        if not without_none:
            return dict_

        result = {}
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

    def to_string(self):
        """Convert runtime environment configuration to a string representation."""
        dict_representation = self.to_dict(without_none=True)
        return str(dict_representation)
