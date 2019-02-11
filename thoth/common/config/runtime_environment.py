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

        content = yaml.load(content)
        return cls.from_dict(content)

    @classmethod
    def from_dict(cls, dict_: dict):
        """Parse one configuration entry from a dictionary."""
        dict_ = dict(dict_)

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
        return instance

    def to_dict(self):
        """Convert configuration to a dict representation."""
        return attr.asdict(self)
