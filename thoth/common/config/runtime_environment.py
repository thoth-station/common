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

import logging

import attr

from .hardware_information import HardwareInformation
from .operating_system import OperatingSystem

_LOGGER = logging.getLogger(__name__)


@attr.s(slots=True)
class RuntimeEnvironment:
    """An entry collapsing configuration options in the user configuration file."""

    hardware_information = attr.ib(type=HardwareInformation)
    operating_system = attr.ib(type=OperatingSystem)
    python_version = attr.ib(type=str, default=None)
    cuda_version = attr.ib(type=str, default=None)

    @classmethod
    def from_dict(cls, dict_: dict):
        """Parse one configuration entry from a dictionary."""
        dict_ = dict(dict_)

        hardware_information = dict_.pop("hardware_information", {})
        operating_system = dict_.pop("operating_system", {})
        python_version = dict_.pop("python_version", None)
        cuda_version = dict_.pop("cuda_version", None)

        for key, value in dict_.values():
            _LOGGER.warning(
                "Unknown configuration entry in the configuration file %s with value %s",
                key,
                value
            )

        instance = cls(
            hardware_information=HardwareInformation.from_dict(hardware_information),
            operating_system=OperatingSystem.from_dict(operating_system),
            python_version=python_version,
            cuda_version=cuda_version
        )
        return instance

    def to_dict(self):
        """Convert configuration to a dict representation."""
        return attr.asdict(self)
