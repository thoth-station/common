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

"""Logging configuration for whole Thoth."""

import os
import logging
import socket
import time
from typing import Optional
from typing import Dict

from sentry_sdk import init as sentry_sdk_init  # type: ignore
import daiquiri
import daiquiri.formatter
from rfc5424logging import Rfc5424SysLogHandler

_RSYSLOG_HOST = os.getenv("RSYSLOG_HOST")
_RSYSLOG_PORT = os.getenv("RSYSLOG_PORT")
_DEFAULT_LOGGING_CONF_START = "THOTH_LOG_"
_SENTRY_DSN = os.getenv("SENTRY_DSN")


def _init_log_levels(logging_env_var_start: str, logging_configuration: Optional[Dict[str, str]]) -> None:
    """Initialize log level based on configuration or env variables."""
    env_logging_conf = {
        key: val
        for key, val in os.environ.items()
        if key.startswith(logging_env_var_start)
    }

    for logger, level in env_logging_conf.items():
        logger = "thoth." + logger[len(logging_env_var_start):].lower().replace(
            "__", "."
        )
        level = getattr(logging, level)
        logging.getLogger(logger).setLevel(level)

    if logging_configuration is not None:
        for logger, level in logging_configuration.items():
            level = getattr(logging, level)
            logging.getLogger(logger).setLevel(level)


def init_logging(
    logging_configuration: Optional[Dict[str, str]] = None, logging_env_var_start: Optional[str] = None
) -> None:
    """Initialize Thoth's logging - respects all namespaces.

    This function allows you to control logging facilities in Thoth. Logging can be configured via env variables
    so that deployment can respect your configuration. The structure of environment variables is THOTH_LOG_(MODULE)
    and the value of env variable states verbosity level as in the logging module (DEBUG, INFO, WARNING, ERROR).

    >>> import os
    >>> os.environ['THOTH_LOG_SOLVER']
    WARNING

    You can also specify more closely which sub-module logging you are configuring - submodules are separated with
    double dash:

    >>> os.environ['THOTH_LOG_SOLVER__PYTHON']
    DEBUG

    You can also use arguments explicitly that override configuration in env variables (a shorthand for
    standard logging functionality):

    >>> init_logging({'thoth.solver': 'DEBUG'})

    Optionally you can specify prefix of the logging environment variable
    determining logging configuration via env vars (defaults to THOTH_LOG_).
    """
    # TODO: JSON in deployments?
    # deployed_to_cluster = bool(int(os.getenv('THOTH_CLUSTER_DEPLOYMENT', '0')))

    formatter = daiquiri.formatter.ColorFormatter(
        fmt="%(asctime)s [%(process)d] %(color)s%(levelname)-8.8s %(name)s:"
        "%(lineno)d: %(message)s%(color_stop)s"
    )

    # Always log in UTC to be consistent with team members all over the world.
    formatter.converter = time.gmtime

    daiquiri.setup(
        level=logging.INFO,
        outputs=(
            daiquiri.output.Stream(formatter=formatter),
        ),
    )
    root_logger = logging.getLogger()
    environment = os.getenv("SENTRY_ENVIRONMENT", os.getenv("THOTH_DEPLOYMENT_NAME"))

    # Disable annoying unverified HTTPS request warnings.
    try:
        import urllib3

        urllib3.disable_warnings()
    except ImportError:
        pass

    _init_log_levels(
        logging_env_var_start or _DEFAULT_LOGGING_CONF_START, logging_configuration
    )

    if _SENTRY_DSN:
        try:
            root_logger.info(
                "Setting up logging to a Sentry instance %r, environment %r",
                _SENTRY_DSN.rsplit("@", maxsplit=1)[1],
                environment
            )
            sentry_sdk_init(_SENTRY_DSN, environment=environment)
        except Exception:
            root_logger.exception(
                "Failed to initialize logging to Sentry instance, check configuration"
            )
            raise

        if environment is None:
            root_logger.warning(
                "No Sentry environment configured: it is recommended to provide Sentry environment "
                "to split reported exceptions based on different deployments when running in a cluster"
            )
    else:
        root_logger.warning("Logging to a Sentry instance is turned off")

    if _RSYSLOG_HOST and _RSYSLOG_PORT:
        root_logger.info(
            f"Setting up logging to rsyslog endpoint {_RSYSLOG_HOST}:{_RSYSLOG_PORT}"
        )

        try:
            syslog_handler = Rfc5424SysLogHandler(
                address=(_RSYSLOG_HOST, int(_RSYSLOG_PORT))
            )
            root_logger.addHandler(syslog_handler)
        except socket.gaierror as exc:
            root_logger.exception(
                f"RSYSLOG_HOST and RSYSLOG_PORT have been set but {_RSYSLOG_HOST}:{_RSYSLOG_PORT} cannot be reached"
            )
    elif int(bool(_RSYSLOG_PORT)) + int(bool(_RSYSLOG_HOST)) == 1:
        raise RuntimeError(
            f"Please provide both RSYSLOG_HOST and RSYSLOG_PORT configuration"
            f"in order to use rsyslog logging, host: {_RSYSLOG_HOST}, port: {_RSYSLOG_PORT}"
        )
    else:
        root_logger.info("Logging to rsyslog endpoint is turned off")
