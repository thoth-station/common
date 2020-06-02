Thoth Common
------------

A library used in project `Thoth <https://thoth-station.ninja>`_. It's aim is to
provide core utilities for logger setup, manipulation with datetimes and
similar handy helpers.

Installation
============

This project is released on
`PyPI <https://pypi.org/project/thoth-common>`_, so the latest release can be
installed via pip or `Pipenv <https://pipenv.readthedocs.io>`_ as shown below:

.. code-block:: console

  pipenv install thoth-common

This library will automatically discover installed packages and enable `Sentry
integrations <https://docs.sentry.io/platforms/python/>`_ if you use Flask,
SQLAlchemy or AIOHTTP. An exception is for Flask applications, that need to
explicitly install ``sentry-sdk[flask]`` due to integrations dependencies.

Logging setup
=============

To setup a logger in any of Thoth's component (component that are namespaced
with ``thoth``), you can simply set an environment variable. The name of
environment variable is constructed from module name. Let's say you want to
debug ``thoth.adviser.pipeline`` module, in that case you can set environment
variable:

``THOTH_LOG_ADVISER_PIPELINE=DEBUG`` which will cause loggers
``thoth.adviser.pipeline`` to be set to ``DEBUG`` mode. See `log-levels
documentation <https://docs.python.org/3/library/logging.html#logging-levels>`_
for more info. If a module has underscore in its name, replace it with double
underscore in the environment variable name.

To setup a logger that is not introduced by a Thoth's component, you can set
``THOTH_ADJUST_LOGGING`` environment variable. The format of this environment
variable THOTH_ADJUST_LOGGING is a comma separated list where each entry is
made out of a logger name and a corresponding log-level ("DEBUG", "INFO",
"WARNING", "ERROR" as for standard Python's logging). These two are delimited
by a colon, an example:

.. code-block:: console

        THOTH_ADJUST_LOGGING="flask:WARNING,alembic.migrations:ERROR"

Structured logging
==================

The library will automatically detect when it is running inside an OpenShift
cluster (based on ``OPENSHIFT_BUILD_NAME`` environment variable that is
inserted into the container if build the container was built in an OpenShift
cluster), In such case, the library will setup structured logging suitable for
automated logs aggregation (e.g. automated logs aggregation using the ELK
stack). This behavior can be suppressed by setting environment variable
``THOTH_LOGGING_NO_JSON=1``.

Ignoring reports from a logger
==============================

In some cases it's expected to turn off reporting of some logger to Sentry. You
can provide ``THOTH_SENTRY_IGNORE_LOGGER`` environment variable which holds a
comma separated list of loggers that should be ignored when reporting errors
to Sentry:

.. code-block:: console

  THOTH_SENTRY_IGNORE_LOGGER="thoth.adviser.resolver,thoth.adviser.run"


This is helpful if you want to report errors to users but not to Thoth
application itself.


If you want some certain classes of error not to be reported to Sentry, you can
can provide ``THOTH_SENTRY_IGNORE_EXCEPTION`` environment variable which holds
the comma-separated list of exception classes to be ignored when reporting to Sentry:

.. code-block:: console

  THOTH_SENTRY_IGNORE_EXCEPTION="connexion.decorators.validation,builtins.ValueError"

Remember all builtin exception classes need to be specified as in the same manner as
ValueError is specified above.
