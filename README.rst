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
