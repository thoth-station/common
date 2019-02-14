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

"""Exceptions used within thoth-common package."""


class ThothCommonException(Exception):
    """A base class for Thoth-common exception hierarchy."""


class NotFoundException(ThothCommonException):
    """Raised if the given resource cannot be found."""


class ConfigurationError(ThothCommonException):
    """Raised on miss-configuration issues."""


class DiscardError(ThothCommonException):
    """Raised if the calle should discard the given resource.

    Currently used to signalize failure of builds of Amun inspections - workload
    operator should cancel workload scheduling.
    """
