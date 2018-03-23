"""Logging configuration for whole Thoth."""

import os
import logging

_LOGGING_CONF_START = 'THOTH_LOG_'


def init_logging(logging_configuration: dict=None) -> None:
    """Initialize Thoth's logging - respects all namespaces.

    This function allows you to control logging facilities in Thoth. Logging can be configured via env variables
    so that deployment can respect your configuration. The structure of environment variables is THOTH_LOG_<MODULE>
    and the value of env variable states verbosity level as in the logging module (DEBUG, INFO, WARNING, ERROR).

    >>> import os
    >>> os.environ['THOTH_LOG_SOLVER']
    WARNING

    You can also specify more closely which sub-module logging you are configuring - submodules are separated with dash:
    >>> os.environ['THOTH_LOG_SOLVER_PYTHON']
    DEBUG

    You can also use arguments explicitly that override configuration in env variables (a shorthand for
    standard logging functionality):
    >>> init_logging({'thoth.solver': 'DEBUG'})
    """
    # TODO: JSON in deployments?
    #deployed_to_cluster = bool(int(os.getenv('THOTH_CLUSTER_DEPLOYMENT', '0')))

    logging.basicConfig()

    thoth_root_logger = logging.getLogger('thoth')
    thoth_root_logger.setLevel(logging.INFO)

    env_logging_conf = {
        key: val for key, val in os.environ.items() if key.startswith(_LOGGING_CONF_START)
    }

    for logger, level in env_logging_conf.items():
        logger = 'thoth.' + logger[len(_LOGGING_CONF_START):].lower().replace('_', '.')
        level = getattr(logging, level)
        logging.getLogger(logger).setLevel(level)

    if logging_configuration is not None:
        for logger, level in logging_configuration.items():
            level = getattr(logging, level)
            logging.getLogger(logger).setLevel(level)
