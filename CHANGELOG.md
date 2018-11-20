# Changelog for the Thoth common module

## [0.2.1] - 2018-Jul-10 - goern

### Fixed

- some minor syntax error ;)

## [0.2.0] - 2018-Jul-09 - goern

### Fixed

- https://github.com/thoth-station/result-api/issues/39

## [0.1.0] - 2018-Jul-06 - goern

### Changed

Nothing, just to bounce from 0.0.9 to 0.1.0

## [0.0.9] - 2018-Jun-28 - goern

### Fixed

- argument name in logger_setup() see https://github.com/thoth-station/common/pull/31

## [0.0.8] - 2018-Jun-25 - goern

### Added

Starting with this release we have a Zuul-CI pipeline that:

- lints on Pull Requrest and gate/merge
- uploads to pypi (test) on tag

## Release 0.2.6 (2018-09-03T09:48:51)


## Release 0.2.7 (2018-09-03T13:53:07)


## Release 0.3.0 (2018-09-05T12:27:24)
* Let's reuse adviser env var names
* Issue warning on suspicious parameter expansion in templates
* Fix propagating debug flag to package-extract
* Fix gathering pod logs for default middletier namespace
* Fix gathering pod status for default middletier namespace
* Automatic update of dependency pytest-cov from 2.5.1 to 2.6.0
* Introduce routine for running provenance checker

## Release 0.3.1 (2018-09-17T07:39:06)
* added github configuration
* Automatic update of dependency pytest from 3.7.4 to 3.8.0
* Fix built-in type shadowing

## Release 0.3.2 (2018-09-26T20:34:32)
* Add Sentry support
* Report scheduling status if pod was not initialized yet
* Report back empty pod status is pod is being scheduled
* Automatic update of dependency pytest from 3.8.0 to 3.8.1
* Automatic update of dependency rfc5424-logging-handler from 1.1.2 to 1.2.1
* Unify pod status reports
* Treat None parameter values as empty values

## Release 0.3.3 (2018-09-27T18:45:47)
* fixed the typo, this closes #114
* Automatic update of dependency sentry-sdk from 0.3.5 to 0.3.6
* Initial dependency lock

## Release 0.3.4 (2018-09-28T13:37:30)
* Release of version 0.3.3
* fixed the typo, this closes #114
* Automatic update of dependency sentry-sdk from 0.3.5 to 0.3.6
* Release of version 0.3.2
* Initial dependency lock
* Add Sentry support
* Report scheduling status if pod was not initialized yet
* Report back empty pod status is pod is being scheduled
* Automatic update of dependency pytest from 3.8.0 to 3.8.1
* Automatic update of dependency rfc5424-logging-handler from 1.1.2 to 1.2.1
* Unify pod status reports
* Treat None parameter values as empty values
* Release of version 0.3.1
* added github configuration
* Automatic update of dependency pytest from 3.7.4 to 3.8.0
* Fix built-in type shadowing
* Release of version 0.3.0
* Let's reuse adviser env var names
* Issue warning on suspicious parameter expansion in templates
* Fix propagating debug flag to package-extract
* Fix gathering pod logs for default middletier namespace
* Fix gathering pod status for default middletier namespace
* Automatic update of dependency pytest-cov from 2.5.1 to 2.6.0
* Release of version 0.2.7
* Fix default TLS verification behavior
* Introduce routine for running provenance checker
* Release of version 0.2.6
* Initial dependency lock
* change the queue
* change the queue
* Fix TLS/SSL certification verification configuration
* Release of version 0.2.5
* Configure SSL/TLS correctly when communicating with master
* Initial dependency lock
* Release of version 0.2.4
* Pin down Kubernetes and OpenShift clients to specific versions
* Release of version 0.2.3
* Initial dependency lock
* Fix over-intended block
* Remove Pipfile.lock for initial lock from Kebechet
* Add TODO comment based on review
* Allow passing configuration via env vars
* Place all the OpenShift related logic at one place
* Automatic update of dependency pytest-timeout from 1.3.1 to 1.3.2
* Automatic update of dependency pytest from 3.7.1 to 3.7.3
* Automatic update of dependency pylint from 2.1.0 to 2.1.1
* Automatic update of dependency pytest from 3.7.0 to 3.7.1
* Automatic update of dependency pylint from 2.0.1 to 2.1.0
* Automatic update of dependency pytest from 3.6.4 to 3.7.0
* Automatic update of dependency pytest from 3.6.3 to 3.6.4
* Update .zuul.yaml
* Release of version 0.2.2
* Automatic update of dependency pylint from 1.9.2 to 2.0.1
* Automatic update of dependency pytest-timeout from 1.3.0 to 1.3.1
* Allow completely suppressing logs
* Automatic update of dependency daiquiri from 1.3.0 to 1.5.0
* releasing 0.2.1
* Fix syntax error in logging
* Initial dependency lock
* Delete Pipfile.lock for relocking dependencies
* preparing release 0.2.0
* using logger.exception()
* catching and logging a "[Errno -2] Name or service not known"
* Remove pydocstyle from Pipfile
* releasing 0.1.0
* Introduce a function for getting service account token
* releasing 0.0.9
* Change in var name
* fixed trailing space issue
* added the gate pipeline to the core queue
* releasing 0.0.8
* uploading to production pypi now... using sesheta account
* trigger
* fixed some coala errors
* preparing release 0.0.8: Zuul
* Version 0.0.7
* Change in Indentation
* Change in Indentation and variable names
* Generic wrappers to define verbose level on every method
* Fix logging issues
* added daiquiri
* Disable annoying unverified HTTPS warnings
* Fix typo in docstring
* Setup logging for root logger
* Remove a temporary dependency for kebechet testing
* Automatic update of dependency thoth-storages from 0.0.26 to 0.0.28
* Automatic update of dependency rfc5424-logging-handler from 1.1.0 to 1.1.2
* Testing dependencies
* A temporary dependency downgrade to test kebechet
* Version 0.0.6
* Add support for rsyslog logging endpoint
* Run coala in non-interactive mode
* Run coala in CI
* Create OWNERS
* Remove dependencies.yml
* Add missing headers to files
* Use coala for code checks
* Use GPLv3 in setup.py
* Use GPLv3
* Add missing import
* Version 0.0.5
* Convert a timestamp to datetime string
* Version 0.0.4
* Argument 2 to isinstance has to be a type
* Add README file
* Version 0.0.3
* Add datetime2datetime_str conversion function
* Version 0.0.2
* Abstract manipulation with datetime
* Add space so Sphinx interpret docstrings correctly
* Respect double dash as module separator
* Version 0.0.1
* Provide version information properly
* Add init_logging function
* Fix package name
* Create initial dependencies.yml config
* Initial project import

## Release 0.3.5 (2018-09-28T14:30:12)
* Release of version 0.3.4
* Release of version 0.3.3
* fixed the typo, this closes #114
* Automatic update of dependency sentry-sdk from 0.3.5 to 0.3.6
* Release of version 0.3.2
* Initial dependency lock
* Add Sentry support
* Report scheduling status if pod was not initialized yet
* Report back empty pod status is pod is being scheduled
* Automatic update of dependency pytest from 3.8.0 to 3.8.1
* Automatic update of dependency rfc5424-logging-handler from 1.1.2 to 1.2.1
* Unify pod status reports
* Treat None parameter values as empty values
* Release of version 0.3.1
* added github configuration
* Automatic update of dependency pytest from 3.7.4 to 3.8.0
* Fix built-in type shadowing
* Release of version 0.3.0
* Let's reuse adviser env var names
* Issue warning on suspicious parameter expansion in templates
* Fix propagating debug flag to package-extract
* Fix gathering pod logs for default middletier namespace
* Fix gathering pod status for default middletier namespace
* Automatic update of dependency pytest-cov from 2.5.1 to 2.6.0
* Release of version 0.2.7
* Fix default TLS verification behavior
* Introduce routine for running provenance checker
* Release of version 0.2.6
* Initial dependency lock
* change the queue
* change the queue
* Fix TLS/SSL certification verification configuration
* Release of version 0.2.5
* Configure SSL/TLS correctly when communicating with master
* Initial dependency lock
* Release of version 0.2.4
* Pin down Kubernetes and OpenShift clients to specific versions
* Release of version 0.2.3
* Initial dependency lock
* Fix over-intended block
* Remove Pipfile.lock for initial lock from Kebechet
* Add TODO comment based on review
* Allow passing configuration via env vars
* Place all the OpenShift related logic at one place
* Automatic update of dependency pytest-timeout from 1.3.1 to 1.3.2
* Automatic update of dependency pytest from 3.7.1 to 3.7.3
* Automatic update of dependency pylint from 2.1.0 to 2.1.1
* Automatic update of dependency pytest from 3.7.0 to 3.7.1
* Automatic update of dependency pylint from 2.0.1 to 2.1.0
* Automatic update of dependency pytest from 3.6.4 to 3.7.0
* Automatic update of dependency pytest from 3.6.3 to 3.6.4
* Update .zuul.yaml
* Release of version 0.2.2
* Automatic update of dependency pylint from 1.9.2 to 2.0.1
* Automatic update of dependency pytest-timeout from 1.3.0 to 1.3.1
* Allow completely suppressing logs
* Automatic update of dependency daiquiri from 1.3.0 to 1.5.0
* releasing 0.2.1
* Fix syntax error in logging
* Initial dependency lock
* Delete Pipfile.lock for relocking dependencies
* preparing release 0.2.0
* using logger.exception()
* catching and logging a "[Errno -2] Name or service not known"
* Remove pydocstyle from Pipfile
* releasing 0.1.0
* Introduce a function for getting service account token
* releasing 0.0.9
* Change in var name
* fixed trailing space issue
* added the gate pipeline to the core queue
* releasing 0.0.8
* uploading to production pypi now... using sesheta account
* trigger
* fixed some coala errors
* preparing release 0.0.8: Zuul
* Version 0.0.7
* Change in Indentation
* Change in Indentation and variable names
* Generic wrappers to define verbose level on every method
* Fix logging issues
* added daiquiri
* Disable annoying unverified HTTPS warnings
* Fix typo in docstring
* Setup logging for root logger
* Remove a temporary dependency for kebechet testing
* Automatic update of dependency thoth-storages from 0.0.26 to 0.0.28
* Automatic update of dependency rfc5424-logging-handler from 1.1.0 to 1.1.2
* Testing dependencies
* A temporary dependency downgrade to test kebechet
* Version 0.0.6
* Add support for rsyslog logging endpoint
* Run coala in non-interactive mode
* Run coala in CI
* Create OWNERS
* Remove dependencies.yml
* Add missing headers to files
* Use coala for code checks
* Use GPLv3 in setup.py
* Use GPLv3
* Add missing import
* Version 0.0.5
* Convert a timestamp to datetime string
* Version 0.0.4
* Argument 2 to isinstance has to be a type
* Add README file
* Version 0.0.3
* Add datetime2datetime_str conversion function
* Version 0.0.2
* Abstract manipulation with datetime
* Add space so Sphinx interpret docstrings correctly
* Respect double dash as module separator
* Version 0.0.1
* Provide version information properly
* Add init_logging function
* Fix package name
* Create initial dependencies.yml config
* Initial project import

## Release 0.3.6 (2018-09-29T09:25:43)
* fixed another typo
* fixed a few typos

## Release 0.3.7 (2018-10-09T11:15:31)
* Automatic update of dependency sentry-sdk from 0.3.9 to 0.3.11
* Add routines for jobs handling
* Gather build logs from OpenShift
* Allow explicitly specifying the logging configuration prefix
* Make reusable methods public
* Introduce methods for running dependency monkey
* Automatic update of dependency sentry-sdk from 0.3.8 to 0.3.9
* Automatic update of dependency pytest from 3.8.1 to 3.8.2
* Automatic update of dependency sentry-sdk from 0.3.7 to 0.3.8
* Automatic update of dependency sentry-sdk from 0.3.6 to 0.3.7

## Release 0.3.8 (2018-10-09T20:35:55)
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error

## Release 0.3.9 (2018-10-09T22:14:22)
* Fix gathering pod id from job name

## Release 0.3.10 (2018-10-10T17:53:11)
* Return None if there are no pod logs yet
* Add message to translate table
* Raise appropriate not found exception exception

## Release 0.3.11 (2018-10-11T14:17:58)
* Fix syntax error

## Release 0.3.12 (2018-10-21T15:04:13)
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1

## Release 0.3.13 (2018-10-28T13:17:08)
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2

## Release 0.3.14 (2018-10-29T15:40:41)
* refactor methods into pythonic way

## Release 0.3.15 (2018-10-30T19:36:48)
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2

## Release 0.3.16 (2018-10-30T22:14:31)
* Fix missing import
* Make CI happy again

## Release 0.4.0 (2018-11-04T21:28:14)
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* using thoht-* jobs now

## Release 0.4.1 (2018-11-15T23:20:21)
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3

## Release 0.4.2 (2018-11-16T11:53:53)
* Add count parameter to dependency monkey
* Use api version from template

## Release 0.4.3 (2018-11-17T13:19:36)
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3

## Release 0.4.4 (2018-11-19T19:08:36)
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser

## Release 0.4.5 (2018-11-20T22:33:13)
* Introduce method for gathering buildconfigs
