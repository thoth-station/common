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

"""Exceptions used within thoth-common package."""


class ThothCommonException(Exception):
    """A base class for Thoth-common exception hierarchy."""


class NotFoundException(ThothCommonException):
    """Raised if the given resource cannot be found."""


class ConfigurationError(ThothCommonException):
    """Raised on miss-configuration issues."""


class WorkflowError(ThothCommonException):
    """Raised on workflow related issues."""


class NotKnownThothIntegration(ThothCommonException):
    """An exception raised if the given integration is not known to Thoth."""


class QebHwtInputsMissing(ThothCommonException):
    """An exception raised if there are inputs missing for QebHwt Github App."""


class KebechetInputsMissing(ThothCommonException):
    """An exception raised if there are inputs missing for Kebechet."""


class SolverNameParseError(ThothCommonException):
    """Raised if unable to determine solver information out of solver name run."""
