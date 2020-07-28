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
* Add TO.DO comment based on review
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

## Release 0.4.6 (2018-11-22T04:57:58)
* Runtime environment is now a dict

## Release 0.4.7 (2018-12-03T10:11:46)
* Automatic update of dependency pylint from 2.2.1 to 2.2.2

## Release 0.5.0 (2018-12-11T23:34:06)
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0

## Release 0.6.0 (2019-01-22T17:45:37)
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2

## Release 0.7.0 (2019-02-13T17:10:50)
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Fix more coala issues
* Fix coala errors

## Release 0.7.1 (2019-02-14T06:43:01)
* Add missing MANIFEST.in

## Release 0.8.0 (2019-03-13T09:39:32)
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5

## Release 0.8.1 (2019-03-16T15:10:25)
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()

## Release 0.8.2 (2019-04-03T10:05:52)
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment

## Release 0.8.3 (2019-04-05T10:53:55)
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)

## Release 0.8.4 (2019-04-08T10:14:11)
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10

## Release 0.8.5 (2019-04-09T07:21:23)
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2

## Release 0.8.6 (2019-05-08T17:42:08)
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements

## Release 0.8.7 (2019-05-15T05:29:49)
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2

## Release 0.8.8 (2019-05-15T06:58:12)
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.8.9 (2019-05-15T07:54:55)
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.8.10 (2019-06-05T17:24:44)
* Supply environment variable for registry and infra namespace for inspections
* minor fix of error msg
* :bug: minor fix for correct namespace
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.8.11 (2019-06-06T13:55:16)
* Fix solver temlate handling
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* Implement Sentry environment

## Release 0.9.0 (2019-06-19T15:20:47)
* New function for all ConfigMaps
* Fix retrieving pod logs - use OpenShift API
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1

## Release 0.9.1 (2019-06-24T09:15:25)
* Provide method for scheduling graph-refresh on demand
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1

## Release 0.9.2 (2019-07-10T15:08:23)
* Fix wrong argument handling
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* :arrow_double_up: Increase the limit for file line size
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* Introduce graph sync multiple
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3

## Release 0.9.3 (2019-07-12T11:47:28)
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Broke up run and schedule for stable api
* Copy paste remnants
* Increase maximum lines
* Conditional statement
* Subcommand env
* Coala fixes
* Logic to run and schedule kebechet builds

## Release 0.9.4 (2019-07-18T21:00:09)
* openshift scheduler job for package analyzer
* Changed env variable names
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2

## Release 0.9.5 (2019-07-24T18:39:51)
* :sunrise: Modified the names to standard convention

## Release 0.9.6 (2019-08-07T20:40:29)
* Add template as optional param
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* New function to count jobs per status per label
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2

## Release 0.9.7 (2019-08-13T07:44:10)
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste

## Release 0.9.8 (2019-08-14T13:19:13)
* Do not pin to a specific Kubernetes release

## Release 0.9.9 (2019-09-18T16:05:04)
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* Be consistent with solver type labels

## Release 0.9.10 (2019-09-18T19:34:42)
* Hotfix for errors when getting solver templates

## Release 0.9.11 (2019-10-02T14:10:00)
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* Improve error message shown when getting cluster resources
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1

## Release 0.9.12 (2019-10-07T13:47:41)
* Add warnings when there is something fishy in environment configuration for logging
* Fix missing bracket
* Refactor out scheduling graph syncs
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Drop subgraph check
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3

## Release 0.9.13 (2019-10-08T09:58:53)


## Release 0.9.14 (2019-10-10T08:30:46)
* Fix method name to comply with other methods
* Propagate is_external flag to package-extract runs
* relocked dependencies, cleaned up the coala deps
* Release of version 0.9.13
* Release of version 0.9.12
* Add warnings when there is something fishy in environment configuration for logging
* Always log in UTC to be consistent with team members all over the world
* Fix missing bracket
* Refactor out scheduling graph syncs
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Drop subgraph check
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* Release of version 0.9.11
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* Improve error message shown when getting cluster resources
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* Release of version 0.9.10
* Hotfix for errors when getting solver templates
* Release of version 0.9.9
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* Be consistent with solver type labels
* Release of version 0.9.8
* Do not pin to a specific Kubernetes release
* Release of version 0.9.7
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste
* Release of version 0.9.6
* Add template as optional param
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* New function to count jobs per status per label
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* Release of version 0.9.5
* :sunrise: Modified the names to standard convention
* Release of version 0.9.4
* openshift scheduler job for package analyzer
* Changed env variable names
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* Release of version 0.9.3
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Broke up run and schedule for stable api
* Release of version 0.9.2
* Fix wrong argument handling
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* Copy paste remnants
* :arrow_double_up: Increase the limit for file line size
* Increase maximum lines
* Conditional statement
* Subcommand env
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* Introduce graph sync multiple
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* Coala fixes
* Release of version 0.9.1
* Provide method for scheduling graph-refresh on demand
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* Release of version 0.9.0
* New function for all ConfigMaps
* Logic to run and schedule kebechet builds
* Fix retrieving pod logs - use OpenShift API
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* Release of version 0.8.11
* Fix solver temlate handling
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* Release of version 0.8.10
* :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* Implement Sentry environment
* Supply environment variable for registry and infra namespace for inspections
* minor fix of error msg
* :bug: minor fix for correct namespace
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.9.15 (2019-11-13T11:05:15)
* Provide a method to check if the given environment is fully specified
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* Fix boolean types in mypy.ini
* :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* Start using mypy for type checking
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0

## Release 0.9.16 (2019-11-14T02:34:54)
* Do not propagate private property on to_dict()
* Release of version 0.9.15
* Provide a method to check if the given environment is fully specified
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* Fix boolean types in mypy.ini
* :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* Start using mypy for type checking
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0
* Release of version 0.9.14
* Fix method name to comply with other methods
* Propagate is_external flag to package-extract runs
* relocked dependencies, cleaned up the coala deps
* Release of version 0.9.13
* Release of version 0.9.12
* Add warnings when there is something fishy in environment configuration for logging
* Always log in UTC to be consistent with team members all over the world
* Fix missing bracket
* Refactor out scheduling graph syncs
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Drop subgraph check
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* Release of version 0.9.11
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* Improve error message shown when getting cluster resources
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* Release of version 0.9.10
* Hotfix for errors when getting solver templates
* Release of version 0.9.9
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* Be consistent with solver type labels
* Release of version 0.9.8
* Do not pin to a specific Kubernetes release
* Release of version 0.9.7
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste
* Release of version 0.9.6
* Add template as optional param
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* New function to count jobs per status per label
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* Release of version 0.9.5
* :sunrise: Modified the names to standard convention
* Release of version 0.9.4
* openshift scheduler job for package analyzer
* Changed env variable names
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* Release of version 0.9.3
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Broke up run and schedule for stable api
* Release of version 0.9.2
* Fix wrong argument handling
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* Copy paste remnants
* :arrow_double_up: Increase the limit for file line size
* Increase maximum lines
* Conditional statement
* Subcommand env
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* Introduce graph sync multiple
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* Coala fixes
* Release of version 0.9.1
* Provide method for scheduling graph-refresh on demand
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* Release of version 0.9.0
* New function for all ConfigMaps
* Logic to run and schedule kebechet builds
* Fix retrieving pod logs - use OpenShift API
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* Release of version 0.8.11
* Fix solver temlate handling
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* Release of version 0.8.10
* :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* Implement Sentry environment
* Supply environment variable for registry and infra namespace for inspections
* minor fix of error msg
* :bug: minor fix for correct namespace
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.9.17 (2019-11-29T07:44:51)
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.3 to 0.13.4
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency argo-workflows from 2.1.1 to 2.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.2 to 0.13.3
* Add configuration of ignored loggers
* Imlicitly assign workflow ID to the workflow name
* Sanitize workflow before submitting
* Process inspection template before retrieval
* Added methods to submit inspection workflows
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* Add few notes about logging to the README file
* Print integrations to log
* Update README file
* Enable Sentry integrations
* :pushpin: Automatic update of dependency argo-workflows from 2.1.0 to 2.1.1
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* Fix error due to ambiguous template resources
* Move data related files to tests/data dir
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Move workflows tests to the tests/ folder
* fixed W391 blank line at end of file
* Generate workflow ID by the unified `generate_id`
* Refactorings
* Fixed typing issues
* Reduce complexity of _submit_workflow method
* Return Workflow ID on submission
* Fix coala issues
* :pushpin: Lock dependencies for Argo
* Added missing flexmock dependency to the Pipfile
* Sanitize for serialization and validate by default
* Added deserialization of Workflow
* Implement Workflow.from_file method
* Syntactic sugar to load Workflow from a file
* Namespace is no longer optional
* Added configuration property to OpenShift instance
* Moved Workflow management to a separate module
* Added Argo client to the OpenShift class
* Release of version 0.9.16
* Enable running pytest for testsuite implementation

## Release 0.9.18 (2019-11-29T11:24:38)
* Release of version 0.9.17
* :pushpin: Relock
* Make workflow management publicly consumable
* Propagate document id into templates

## Release 0.9.19 (2019-11-29T13:25:32)
* Fix testsuite
* Library fixes

## Release 0.9.20 (2019-12-04T13:25:53)
* Updated randbits to fix #568
* Use 8 random digits in the ID instead of 16
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* Inspection Workflow template is stored in amun infra
* Fixed ResourceNotUniqueError in get_solver_names
* Fixed accessor to amun_infra_namespace attribute
* Allow for different workflow and template namespaces
* :pushpin: Automatic update of dependency mypy from 0.740 to 0.750

## Release 0.9.21 (2019-12-05T09:05:19)
* Sentry's aiohttp integration is supported only for Python 3.7+

## Release 0.9.22 (2019-12-11T16:04:37)
* Correct bug in one function
* Add Thamos documentation
* Add is_s2i flag to adviser scheduling
* Point documentation to other libraries
* Introduce a generic logger adjustment
* Add Google Analytics
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.4 to 0.13.5
* Change Sphinx theme

## Release 0.9.23 (2020-01-07T17:06:29)
* correct namespace use
* Schedule adviser workflow
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Be more aggressive with busy wait
* Busy wait on configmap creation to make sure cm gets propagated in the cluster
* Raise not found error if configmap was not found
* Happy new year!
* :pushpin: Automatic update of dependency mypy from 0.760 to 0.761
* :pushpin: Automatic update of dependency argo-workflows from 2.1.3 to 2.1.4
* :pushpin: Automatic update of dependency argo-workflows from 2.1.2 to 2.1.3
* :pushpin: Automatic update of dependency mypy from 0.750 to 0.760
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2

## Release 0.9.24 (2020-01-10T09:44:49)
* Fix decision type environment variable name
* Add missing argument to dependency monkey runs
* Pass OpenShift instance instead of dynamic client to workflow manager
* I had to do it... it was so annoying
* Fix relative import issue
* adjust-code
* Add env variable to select type of scheduling
* Migrate to workflow for Adviser
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.5 to 0.14.0

## Release 0.9.25 (2020-01-13T15:18:53)
* Enable providing pipeline configuration to Dependency Monkey

## Release 0.9.26 (2020-01-14T14:09:36)
* remove wrong default value to run Dependency Monkey

## Release 0.9.27 (2020-01-16T17:37:40)
* Try to avoid timing issues between job and configmap creation
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* Solver runs with Argo workflows

## Release 0.9.28 (2020-01-16T19:38:12)
* Use thoth.common as a root logger for logging information

## Release 0.9.29 (2020-01-20T15:55:34)
* Rename template used by workload opeartor
* Correct solver id input
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3

## Release 0.9.30 (2020-01-24T16:45:49)
* Thamos workflow for GitHub App Qeb-Hwt
* Fixed the spelling mistake causing issue
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.0 to 0.14.1
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4

## Release 0.9.31 (2020-01-27T14:58:02)
* :sparkles: added pre-commit and did a little bit of coala cleanup
* added xml coverage report

## Release 0.10.0 (2020-01-29T09:07:31)
* Extend parameters for Adviser
* :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* Changed string formatting
* Added log error
* Added minor changes
* Modified documentation
* Reverted back autoindent
* Removed dummy files
* Modified function for init to handle env variables
* Do not cache fully specified environment check
* Added missing return
* Fixed coala errors
* Added suggested changes
* Added suggested changes
* Added readme back
* Delete .env
* Added to read me.
* Added to read me.
* Fixed Coala errors
* Added modified filter function
* Added before send filter
* Experiment logging
* Experiment logging

## Release 0.10.1 (2020-01-30T18:25:38)
* Add host parameter for Thamos GitHub App
* function to sync build analyzers report
* :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5

## Release 0.10.2 (2020-02-03T11:15:27)
* Remove prefix to avoid error in Thoth components

## Release 0.10.3 (2020-02-06T09:43:49)
* Adjust parameter for Thamos Workflos
* Add method to retrieve image streams
* Make decision type and recommendation type lowercase

## Release 0.10.4 (2020-02-06T13:13:44)
* Change template name for Argo migration
* add missing parameter to advise method

## Release 0.10.5 (2020-02-07T15:57:38)
* Remove revision

## Release 0.10.6 (2020-02-12T16:46:56)
* Fix check for default value in workflow template
* Return directly result
* Simplfiy condition, do not use nested if
* Simplify dictionary handling with dict instantiation
* Propagate missing is_s2i flag to adviser metadata
* Simplify dictionary handling with inlined dict
* Add locked application stack optionally
* Fix confusion with lowercase decision type
* Add templates for releases
* Update .thoth.yaml
* Update .thoth.yaml

## Release 0.10.7 (2020-02-14T12:35:20)
* Always use Argo for thamos workflow

## Release 0.10.8 (2020-02-24T09:51:55)
* Correct datatype
* Added get_workflow_status method
* Handle debug parameter for adviser in argo workflows
* Changed `nodes` -> `pods` in job status report
* Changed Job status report according to Amun API
* Openshift methods for inspection workflows
* Missing metadata parameters

## Release 0.10.9 (2020-02-28T13:21:48)
* Migrate method to be used for Argo

## Release 0.10.10 (2020-03-02T17:12:37)
* Adjust inputs for solvers

## Release 0.10.11 (2020-03-10T19:09:12)


## Release 0.10.12 (2020-03-19T10:45:30)
* remove unused env variables
* Add empty env template
* :pushpin: Automatic update of dependency pytest from 5.3.5 to 5.4.1
* :pushpin: Automatic update of dependency pytest-mypy from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency pyyaml from 5.3 to 3.13
* :pushpin: Automatic update of dependency openshift from 0.10.2 to 0.10.3
* Remove again lines
* Reintroduce wf id
* Adjust solver workflows ID
* Fix issue with returning None instead of workflow id
* Add warning
* Modify logic of get_solver_names not to depend on Openshift template
* Removed unnecessary assignment
* Fix multiple spaces after operator
* Refactor get_workflow
* Allow to get_workflow by name
* Do not implicitly modify Workflow name
* Return adviser_id instead of workflow_id
* Move env variables to right place
* Remove old methods to schedule inspections
* Introduce Schedule inspection method in Openshift Class
* :pushpin: Automatic update of dependency mypy from 0.761 to 0.770

## Release 0.11.0 (2020-03-24T21:18:42)
* Implement structured logging for cluster deployments
* add re_run metadata for qeb-hwt app
* Increase mypy timeout
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.2 to 0.14.3

## Release 0.12.0 (2020-03-24T23:25:29)
* Release of version 0.11.0
* Implement structured logging for cluster deployments
* add re_run metadata for qeb-hwt app
* Increase mypy timeout
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.2 to 0.14.3
* Release of version 0.10.12
* remove unused env variables
* Add empty env template
* :pushpin: Automatic update of dependency pytest from 5.3.5 to 5.4.1
* :pushpin: Automatic update of dependency pytest-mypy from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency pyyaml from 5.3 to 3.13
* :pushpin: Automatic update of dependency openshift from 0.10.2 to 0.10.3
* Remove again lines
* Reintroduce wf id
* Adjust solver workflows ID
* Fix issue with returning None instead of workflow id
* Add warning
* Modify logic of get_solver_names not to depend on Openshift template
* Removed unnecessary assignment
* Fix multiple spaces after operator
* Refactor get_workflow
* Allow to get_workflow by name
* Do not implicitly modify Workflow name
* Return adviser_id instead of workflow_id
* Move env variables to right place
* Remove old methods to schedule inspections
* Introduce Schedule inspection method in Openshift Class
* :pushpin: Automatic update of dependency mypy from 0.761 to 0.770
* Release of version 0.10.11
* Introduce method to assign workflow parameters
* Add variables for Ceph for adviser workflows
* Generalize variables for Ceph storage for workflow
* Add method to check workflow parameters
* Generalize variables for Ceph storage for workflow
* Adjust .thoth.yaml
* Adjust Pipfile and Pipfile.lock
* Release of version 0.10.10
* Adjust inputs for solvers
* Release of version 0.10.9
* Migrate method to be used for Argo
* Release of version 0.10.8
* Correct datatype
* Added get_workflow_status method
* Handle debug parameter for adviser in argo workflows
* Changed `nodes` -> `pods` in job status report
* Changed Job status report according to Amun API
* Openshift methods for inspection workflows
* Missing metadata parameters
* Release of version 0.10.7
* Always use Argo for thamos workflow
* Release of version 0.10.6
* Fix check for default value in workflow template
* Return directly result
* Simplfiy condition, do not use nested if
* Simplify dictionary handling with dict instantiation
* Propagate missing is_s2i flag to adviser metadata
* Simplify dictionary handling with inlined dict
* Add locked application stack optionally
* Fix confusion with lowercase decision type
* Add templates for releases
* Update .thoth.yaml
* Update .thoth.yaml
* Release of version 0.10.5
* Remove revision
* Release of version 0.10.4
* Change template name for Argo migration
* add missing parameter to advise method
* Release of version 0.10.3
* Adjust parameter for Thamos Workflos
* Add method to retrieve image streams
* Make decision type and recommendation type lowercase
* Release of version 0.10.2
* Remove prefix to avoid error in Thoth components
* Release of version 0.10.1
* Add host parameter for Thamos GitHub App
* function to sync build analyzers report
* :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.10.0
* Extend parameters for Adviser
* :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* Changed string formatting
* Added log error
* Added minor changes
* Modified documentation
* Reverted back autoindent
* Removed dummy files
* Modified function for init to handle env variables
* Release of version 0.9.31
* Do not cache fully specified environment check
* Adjust exception for thamos advise workflow
* Modify method to accept None
* Release of version 0.9.30
* :sparkles: added pre-commit and did a little bit of coala cleanup
* Thamos workflow for GitHub App Qeb-Hwt
* added xml coverage report
* Added missing return
* Fixed coala errors
* Added suggested changes
* Added suggested changes
* Fixed the spelling mistake causing issue
* Added readme back
* Delete .env
* Added to read me.
* Added to read me.
* Fixed Coala errors
* Added modified filter function
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.0 to 0.14.1
* Added before send filter
* Experiment logging
* Experiment logging
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* Release of version 0.9.29
* Rename template used by workload opeartor
* Correct solver id input
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* Release of version 0.9.28
* Use thoth.common as a root logger for logging information
* Release of version 0.9.27
* Try to avoid timing issues between job and configmap creation
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* Solver runs with Argo workflows
* Release of version 0.9.26
* remove wrong default value to run Dependency Monkey
* Release of version 0.9.25
* Enable providing pipeline configuration to Dependency Monkey
* Release of version 0.9.24
* Fix decision type environment variable name
* Add missing argument to dependency monkey runs
* Pass OpenShift instance instead of dynamic client to workflow manager
* I had to do it... it was so annoying
* Fix relative import issue
* adjust-code
* Add env variable to select type of scheduling
* Migrate to workflow for Adviser
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.5 to 0.14.0
* Release of version 0.9.23
* correct namespace use
* Schedule adviser workflow
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Be more aggressive with busy wait
* Busy wait on configmap creation to make sure cm gets propagated in the cluster
* Raise not found error if configmap was not found
* Happy new year!
* :pushpin: Automatic update of dependency mypy from 0.760 to 0.761
* :pushpin: Automatic update of dependency argo-workflows from 2.1.3 to 2.1.4
* :pushpin: Automatic update of dependency argo-workflows from 2.1.2 to 2.1.3
* :pushpin: Automatic update of dependency mypy from 0.750 to 0.760
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* :pushpin: Automatic update of dependency openshift from 0.10.0 to 0.10.1
* Release of version 0.9.22
* Correct bug in one function
* Add Thamos documentation
* Add is_s2i flag to adviser scheduling
* Point documentation to other libraries
* Introduce a generic logger adjustment
* Add Google Analytics
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.4 to 0.13.5
* Change Sphinx theme
* Release of version 0.9.21
* Sentry's aiohttp integration is supported only for Python 3.7+
* Release of version 0.9.20
* Updated randbits to fix #568
* Use 8 random digits in the ID instead of 16
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* Inspection Workflow template is stored in amun infra
* Fixed ResourceNotUniqueError in get_solver_names
* Fixed accessor to amun_infra_namespace attribute
* Allow for different workflow and template namespaces
* :pushpin: Automatic update of dependency mypy from 0.740 to 0.750
* Release of version 0.9.19
* Fix testsuite
* Library fixes
* Release of version 0.9.18
* Release of version 0.9.17
* :pushpin: Relock
* Make workflow management publicly consumable
* Propagate document id into templates
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.3 to 0.13.4
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency argo-workflows from 2.1.1 to 2.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.2 to 0.13.3
* Add configuration of ignored loggers
* Imlicitly assign workflow ID to the workflow name
* Sanitize workflow before submitting
* Process inspection template before retrieval
* Added methods to submit inspection workflows
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* Add few notes about logging to the README file
* Print integrations to log
* Update README file
* Enable Sentry integrations
* :pushpin: Automatic update of dependency argo-workflows from 2.1.0 to 2.1.1
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* Fix error due to ambiguous template resources
* Move data related files to tests/data dir
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Move workflows tests to the tests/ folder
* fixed W391 blank line at end of file
* Generate workflow ID by the unified `generate_id`
* Refactorings
* Fixed typing issues
* Reduce complexity of _submit_workflow method
* Return Workflow ID on submission
* Fix coala issues
* :pushpin: Lock dependencies for Argo
* Added missing flexmock dependency to the Pipfile
* Sanitize for serialization and validate by default
* Added deserialization of Workflow
* Implement Workflow.from_file method
* Syntactic sugar to load Workflow from a file
* Namespace is no longer optional
* Added configuration property to OpenShift instance
* Moved Workflow management to a separate module
* Added Argo client to the OpenShift class
* Release of version 0.9.16
* Do not propagate private property on to_dict()
* Enable running pytest for testsuite implementation
* Release of version 0.9.15
* Provide a method to check if the given environment is fully specified
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* Fix boolean types in mypy.ini
* :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* Start using mypy for type checking
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0
* Release of version 0.9.14
* Fix method name to comply with other methods
* Propagate is_external flag to package-extract runs
* relocked dependencies, cleaned up the coala deps
* Release of version 0.9.13
* Release of version 0.9.12
* Add warnings when there is something fishy in environment configuration for logging
* Always log in UTC to be consistent with team members all over the world
* Fix missing bracket
* Refactor out scheduling graph syncs
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Drop subgraph check
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* Release of version 0.9.11
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* Improve error message shown when getting cluster resources
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* Release of version 0.9.10
* Hotfix for errors when getting solver templates
* Release of version 0.9.9
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* Be consistent with solver type labels
* Release of version 0.9.8
* Do not pin to a specific Kubernetes release
* Release of version 0.9.7
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste
* Release of version 0.9.6
* Add template as optional param
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* New function to count jobs per status per label
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* Release of version 0.9.5
* :sunrise: Modified the names to standard convention
* Release of version 0.9.4
* openshift scheduler job for package analyzer
* Changed env variable names
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* Release of version 0.9.3
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Broke up run and schedule for stable api
* Release of version 0.9.2
* Fix wrong argument handling
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* Copy paste remnants
* :arrow_double_up: Increase the limit for file line size
* Increase maximum lines
* Conditional statement
* Subcommand env
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* Introduce graph sync multiple
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* Coala fixes
* Release of version 0.9.1
* Provide method for scheduling graph-refresh on demand
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* Release of version 0.9.0
* New function for all ConfigMaps
* Logic to run and schedule kebechet builds
* Fix retrieving pod logs - use OpenShift API
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* Release of version 0.8.11
* Fix solver temlate handling
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* Release of version 0.8.10
* :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* Implement Sentry environment
* Supply environment variable for registry and infra namespace for inspections
* minor fix of error msg
* :bug: minor fix for correct namespace
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.12.1 (2020-03-25T11:45:18)
* added the missing jsonformatter

## Release 0.12.2 (2020-03-25T19:10:07)
* Fix requirements parsing
* Stopping bots
* Remove TODO for bot creating issues

## Release 0.12.3 (2020-03-25T23:07:40)
* We don't use threads, do not log info about them
* Remove warning produced by jsonformatter
* Removed coala bear

## Release 0.12.4 (2020-03-26T18:05:02)
* Adjust id for qeb-hwt workflow
* Force JSON logger for all registered loggers

## Release 0.12.5 (2020-03-31T22:43:49)
* Initial dependency lock
* Delete Pipfile.lock
* Lock down kubernetes version to 0.10.0 due to CVE-2017-18342
* Propagate THOTH_ADVISER_DEV parameter to adviser runs

## Release 0.12.6 (2020-04-01T17:23:29)
* Set default loglevel to WARNING
* Lazily initialize the WorkflowManager

## Release 0.12.7 (2020-04-07T18:04:21)
* Correct default and typo
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.0 to 0.6.1

## Release 0.12.8 (2020-04-08T15:44:57)
* :nut_and_bolt: provide imagestream name while processing template

## Release 0.12.9 (2020-04-08T21:51:02)
* Remove assignment of the Dockerfile
* Remove parallelism and allowed failures configuration
* Propagate requests and limits for inspection run and build

## Release 0.12.10 (2020-04-22T09:13:56)
* Provide platform in Thoth's runtime environment config option

## Release 0.13.0 (2020-04-25T06:23:51)
* Added workflow functions

## Release 0.13.1 (2020-04-27T17:45:04)
* Renamed to kebechet
* :pushpin: Automatic update of dependency pylint from 2.4.4 to 2.5.0
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.1 to 0.6.2

## Release 0.13.2 (2020-04-29T22:33:40)
* :pushpin: Automatic update of dependency jsonformatter from 0.1.4 to 0.2.1
* Add status analysis and make label selector optional
* Little adjustments
* Adjust name of method
* New methods to monitor Argo workflows

## Release 0.13.3 (2020-05-01T16:33:33)
* all the github standard templates
* :pushpin: Automatic dependency re-locking
* :pushpin: Automatic dependency re-locking
* Quote unknown configuration entries

## Release 0.13.4 (2020-05-21T08:05:50)
* Add missing parameters
* Correct docstring
* New check method for Qeb-HWt inputs
* remove method
* Use name
* Add check for Thoth integration
* Add exception for integrations
* import auto
* Add exception for integrations
* Use solvers ConfigMap
* remove is_s2i flag
* Adjust enums
* Add enum to init
* Add TODO
* Add source type for Thoth adviser integrations
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.3 to 0.14.4
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* :pushpin: Automatic update of dependency pylint from 2.5.0 to 2.5.2

## Release 0.13.5 (2020-05-22T10:57:15)
* Introduce logic for solver

## Release 0.13.6 (2020-05-22T13:56:08)
* rename method
* Missing self

## Release 0.13.7 (2020-05-26T08:14:33)
* Missing self in methods
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0

## Release 0.13.8 (2020-05-29T11:17:38)
* add missing import
* adjust config
* Be consistent
* only change pre-commit config

## Release 0.13.9 (2020-06-09T12:43:54)
* :pushpin: Automatic update of dependency pylint from 2.5.2 to 2.5.3
* Introudce method for verifying Kebechet inputs
* Reformat code using black
* :sparkles: standard pre-commit-config
* :pushpin: Automatic update of dependency mypy from 0.770 to 0.780
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* wrong function name and use enum.name
* remove coala from zuul
* added a 'tekton trigger tag_release pipeline issue'
* Release of version 0.13.8
* add missing import
* adjust config
* Be consistent
* use strings to indicate futures
* move import to fix circular dependency issue
* move type: ignore
* only change pre-commit config
* rename base test
* typing checks, docstrings, test renamed
* Release of version 0.13.7
* make output in solve optional
* Missing self in methods
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* Release of version 0.13.6
* rename method
* Missing self
* Release of version 0.13.5
* Introduce logic for solver
* Release of version 0.13.4
* Add missing parameters
* Correct docstring
* New check method for Qeb-HWt inputs
* remove method
* Use name
* Add check for Thoth integration
* Add exception for integrations
* import auto
* Add exception for integrations
* Use solvers ConfigMap
* remove is_s2i flag
* Adjust enums
* Add enum to init
* Add TODO
* Add source type for Thoth adviser integrations
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.3 to 0.14.4
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* :pushpin: Automatic update of dependency pylint from 2.5.0 to 2.5.2
* Release of version 0.13.3
* all the github standard templates
* :pushpin: Automatic dependency re-locking
* :pushpin: Automatic dependency re-locking
* Quote unknown configuration entries
* Release of version 0.13.2
* :pushpin: Automatic update of dependency jsonformatter from 0.1.4 to 0.2.1
* Add status analysis and make label selector optional
* Little adjustments
* Adjust name of method
* New methods to monitor Argo workflows
* Changed parameter type
* Moved json serialization
* Release of version 0.13.1
* Renamed to kebechet
* :pushpin: Automatic update of dependency pylint from 2.4.4 to 2.5.0
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.1 to 0.6.2
* Release of version 0.13.0
* Added workflow functions
* Release of version 0.12.10
* Provide platform in Thoth's runtime environment config option
* Release of version 0.12.9
* Remove assignment of the Dockerfile
* Remove parallelism and allowed failures configuration
* Propagate requests and limits for inspection run and build
* Release of version 0.12.8
* :nut_and_bolt: provide imagestream name while processing template
* Release of version 0.12.7
* Correct default and typo
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.0 to 0.6.1
* Release of version 0.12.6
* Set default loglevel to WARNING
* Lazily initialize the WorkflowManager
* Release of version 0.12.5
* Initial dependency lock
* Delete Pipfile.lock
* Lock down kubernetes version to 0.10.0 due to CVE-2017-18342
* Propagate THOTH_ADVISER_DEV parameter to adviser runs
* Release of version 0.12.4
* Adjust id for qeb-hwt workflow
* Force JSON logger for all registered loggers
* Release of version 0.12.3
* We don't use threads, do not log info about them
* Remove warning produced by jsonformatter
* Release of version 0.12.2
* Fix requirements parsing
* Stopping bots
* Remove TODO for bot creating issues
* Release of version 0.12.1
* added the missing jsonformatter
* Release of version 0.12.0
* Release of version 0.11.0
* Implement structured logging for cluster deployments
* Removed coala bear
* add re_run metadata for qeb-hwt app
* Increase mypy timeout
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.2 to 0.14.3
* Release of version 0.10.12
* remove unused env variables
* Add empty env template
* :pushpin: Automatic update of dependency pytest from 5.3.5 to 5.4.1
* :pushpin: Automatic update of dependency pytest-mypy from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency pyyaml from 5.3 to 3.13
* :pushpin: Automatic update of dependency openshift from 0.10.2 to 0.10.3
* Remove again lines
* Reintroduce wf id
* Adjust solver workflows ID
* Fix issue with returning None instead of workflow id
* Add warning
* Modify logic of get_solver_names not to depend on Openshift template
* Removed unnecessary assignment
* Fix multiple spaces after operator
* Refactor get_workflow
* Allow to get_workflow by name
* Do not implicitly modify Workflow name
* Return adviser_id instead of workflow_id
* Move env variables to right place
* Remove old methods to schedule inspections
* Introduce Schedule inspection method in Openshift Class
* :pushpin: Automatic update of dependency mypy from 0.761 to 0.770
* Release of version 0.10.11
* Introduce method to assign workflow parameters
* Add variables for Ceph for adviser workflows
* Generalize variables for Ceph storage for workflow
* Add method to check workflow parameters
* Generalize variables for Ceph storage for workflow
* Adjust .thoth.yaml
* Adjust Pipfile and Pipfile.lock
* Release of version 0.10.10
* Adjust inputs for solvers
* Release of version 0.10.9
* Migrate method to be used for Argo
* Release of version 0.10.8
* Correct datatype
* Added get_workflow_status method
* Handle debug parameter for adviser in argo workflows
* Changed `nodes` -> `pods` in job status report
* Changed Job status report according to Amun API
* Openshift methods for inspection workflows
* Missing metadata parameters
* Release of version 0.10.7
* Always use Argo for thamos workflow
* Release of version 0.10.6
* Fix check for default value in workflow template
* Return directly result
* Simplfiy condition, do not use nested if
* Simplify dictionary handling with dict instantiation
* Propagate missing is_s2i flag to adviser metadata
* Simplify dictionary handling with inlined dict
* Add locked application stack optionally
* Fix confusion with lowercase decision type
* Add templates for releases
* Update .thoth.yaml
* Update .thoth.yaml
* Release of version 0.10.5
* Remove revision
* Release of version 0.10.4
* Change template name for Argo migration
* add missing parameter to advise method
* Release of version 0.10.3
* Adjust parameter for Thamos Workflos
* Add method to retrieve image streams
* Make decision type and recommendation type lowercase
* Release of version 0.10.2
* Remove prefix to avoid error in Thoth components
* Release of version 0.10.1
* Add host parameter for Thamos GitHub App
* function to sync build analyzers report
* :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.10.0
* Extend parameters for Adviser
* :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* Changed string formatting
* Added log error
* Added minor changes
* Modified documentation
* Reverted back autoindent
* Removed dummy files
* Modified function for init to handle env variables
* Release of version 0.9.31
* Do not cache fully specified environment check
* Adjust exception for thamos advise workflow
* Modify method to accept None
* Release of version 0.9.30
* :sparkles: added pre-commit and did a little bit of coala cleanup
* Thamos workflow for GitHub App Qeb-Hwt
* added xml coverage report
* Added missing return
* Fixed coala errors
* Added suggested changes
* Added suggested changes
* Fixed the spelling mistake causing issue
* Added readme back
* Delete .env
* Added to read me.
* Added to read me.
* Fixed Coala errors
* Added modified filter function
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.0 to 0.14.1
* Added before send filter
* Experiment logging
* Experiment logging
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* Release of version 0.9.29
* Rename template used by workload opeartor
* Correct solver id input
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* Release of version 0.9.28
* Use thoth.common as a root logger for logging information
* Release of version 0.9.27
* Try to avoid timing issues between job and configmap creation
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* Solver runs with Argo workflows
* Release of version 0.9.26
* remove wrong default value to run Dependency Monkey
* Release of version 0.9.25
* Enable providing pipeline configuration to Dependency Monkey
* Release of version 0.9.24
* Fix decision type environment variable name
* Add missing argument to dependency monkey runs
* Pass OpenShift instance instead of dynamic client to workflow manager
* I had to do it... it was so annoying
* Fix relative import issue
* adjust-code
* Add env variable to select type of scheduling
* Migrate to workflow for Adviser
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.5 to 0.14.0
* Release of version 0.9.23
* correct namespace use
* Schedule adviser workflow
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Be more aggressive with busy wait
* Busy wait on configmap creation to make sure cm gets propagated in the cluster
* Raise not found error if configmap was not found
* Happy new year!
* :pushpin: Automatic update of dependency mypy from 0.760 to 0.761
* :pushpin: Automatic update of dependency argo-workflows from 2.1.3 to 2.1.4
* :pushpin: Automatic update of dependency argo-workflows from 2.1.2 to 2.1.3
* :pushpin: Automatic update of dependency mypy from 0.750 to 0.760
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* :pushpin: Automatic update of dependency openshift from 0.10.0 to 0.10.1
* Release of version 0.9.22
* Correct bug in one function
* Add Thamos documentation
* Add is_s2i flag to adviser scheduling
* Point documentation to other libraries
* Introduce a generic logger adjustment
* Add Google Analytics
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.4 to 0.13.5
* Change Sphinx theme
* Release of version 0.9.21
* Sentry's aiohttp integration is supported only for Python 3.7+
* Release of version 0.9.20
* Updated randbits to fix #568
* Use 8 random digits in the ID instead of 16
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* Inspection Workflow template is stored in amun infra
* Fixed ResourceNotUniqueError in get_solver_names
* Fixed accessor to amun_infra_namespace attribute
* Allow for different workflow and template namespaces
* :pushpin: Automatic update of dependency mypy from 0.740 to 0.750
* Release of version 0.9.19
* Fix testsuite
* Library fixes
* Release of version 0.9.18
* Release of version 0.9.17
* :pushpin: Relock
* Make workflow management publicly consumable
* Propagate document id into templates
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.3 to 0.13.4
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency argo-workflows from 2.1.1 to 2.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.2 to 0.13.3
* Add configuration of ignored loggers
* Imlicitly assign workflow ID to the workflow name
* Sanitize workflow before submitting
* Process inspection template before retrieval
* Added methods to submit inspection workflows
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* Add few notes about logging to the README file
* Print integrations to log
* Update README file
* Enable Sentry integrations
* :pushpin: Automatic update of dependency argo-workflows from 2.1.0 to 2.1.1
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* Fix error due to ambiguous template resources
* Move data related files to tests/data dir
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Move workflows tests to the tests/ folder
* fixed W391 blank line at end of file
* Generate workflow ID by the unified `generate_id`
* Refactorings
* Fixed typing issues
* Reduce complexity of _submit_workflow method
* Return Workflow ID on submission
* Fix coala issues
* :pushpin: Lock dependencies for Argo
* Added missing flexmock dependency to the Pipfile
* Sanitize for serialization and validate by default
* Added deserialization of Workflow
* Implement Workflow.from_file method
* Syntactic sugar to load Workflow from a file
* Namespace is no longer optional
* Added configuration property to OpenShift instance
* Moved Workflow management to a separate module
* Added Argo client to the OpenShift class
* Release of version 0.9.16
* Do not propagate private property on to_dict()
* Enable running pytest for testsuite implementation
* Release of version 0.9.15
* Provide a method to check if the given environment is fully specified
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* Fix boolean types in mypy.ini
* :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* Start using mypy for type checking
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0
* Release of version 0.9.14
* Fix method name to comply with other methods
* Propagate is_external flag to package-extract runs
* relocked dependencies, cleaned up the coala deps
* Release of version 0.9.13
* Release of version 0.9.12
* Add warnings when there is something fishy in environment configuration for logging
* Always log in UTC to be consistent with team members all over the world
* Fix missing bracket
* Refactor out scheduling graph syncs
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Drop subgraph check
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* Release of version 0.9.11
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* Improve error message shown when getting cluster resources
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* Release of version 0.9.10
* Hotfix for errors when getting solver templates
* Release of version 0.9.9
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* Be consistent with solver type labels
* Release of version 0.9.8
* Do not pin to a specific Kubernetes release
* Release of version 0.9.7
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste
* Release of version 0.9.6
* Add template as optional param
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* New function to count jobs per status per label
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* Release of version 0.9.5
* :sunrise: Modified the names to standard convention
* Release of version 0.9.4
* openshift scheduler job for package analyzer
* Changed env variable names
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* Release of version 0.9.3
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Broke up run and schedule for stable api
* Release of version 0.9.2
* Fix wrong argument handling
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* Copy paste remnants
* :arrow_double_up: Increase the limit for file line size
* Increase maximum lines
* Conditional statement
* Subcommand env
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* Introduce graph sync multiple
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* Coala fixes
* Release of version 0.9.1
* Provide method for scheduling graph-refresh on demand
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* Release of version 0.9.0
* New function for all ConfigMaps
* Logic to run and schedule kebechet builds
* Fix retrieving pod logs - use OpenShift API
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* Release of version 0.8.11
* Fix solver temlate handling
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* Release of version 0.8.10
* :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* Implement Sentry environment
* Supply environment variable for registry and infra namespace for inspections
* minor fix of error msg
* :bug: minor fix for correct namespace
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.13.10 (2020-06-10T12:51:45)
* Properly serialize metadata
* Release of version 0.13.9
* :pushpin: Automatic update of dependency pylint from 2.5.2 to 2.5.3
* Introudce method for verifying Kebechet inputs
* Reformat code using black
* :sparkles: standard pre-commit-config
* :pushpin: Automatic update of dependency mypy from 0.770 to 0.780
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* wrong function name and use enum.name
* remove coala from zuul
* added a 'tekton trigger tag_release pipeline issue'
* Release of version 0.13.8
* add missing import
* adjust config
* Be consistent
* use strings to indicate futures
* move import to fix circular dependency issue
* move type: ignore
* only change pre-commit config
* rename base test
* typing checks, docstrings, test renamed
* Release of version 0.13.7
* make output in solve optional
* Missing self in methods
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* Release of version 0.13.6
* rename method
* Missing self
* Release of version 0.13.5
* Introduce logic for solver
* Release of version 0.13.4
* Add missing parameters
* Correct docstring
* New check method for Qeb-HWt inputs
* remove method
* Use name
* Add check for Thoth integration
* Add exception for integrations
* import auto
* Add exception for integrations
* Use solvers ConfigMap
* remove is_s2i flag
* Adjust enums
* Add enum to init
* Add TODO
* Add source type for Thoth adviser integrations
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.3 to 0.14.4
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* :pushpin: Automatic update of dependency pylint from 2.5.0 to 2.5.2
* Release of version 0.13.3
* all the github standard templates
* :pushpin: Automatic dependency re-locking
* :pushpin: Automatic dependency re-locking
* Quote unknown configuration entries
* Release of version 0.13.2
* :pushpin: Automatic update of dependency jsonformatter from 0.1.4 to 0.2.1
* Add status analysis and make label selector optional
* Little adjustments
* Adjust name of method
* New methods to monitor Argo workflows
* Changed parameter type
* Moved json serialization
* Release of version 0.13.1
* Renamed to kebechet
* :pushpin: Automatic update of dependency pylint from 2.4.4 to 2.5.0
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.1 to 0.6.2
* Release of version 0.13.0
* Added workflow functions
* Release of version 0.12.10
* Provide platform in Thoth's runtime environment config option
* Release of version 0.12.9
* Remove assignment of the Dockerfile
* Remove parallelism and allowed failures configuration
* Propagate requests and limits for inspection run and build
* Release of version 0.12.8
* :nut_and_bolt: provide imagestream name while processing template
* Release of version 0.12.7
* Correct default and typo
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.0 to 0.6.1
* Release of version 0.12.6
* Set default loglevel to WARNING
* Lazily initialize the WorkflowManager
* Release of version 0.12.5
* Initial dependency lock
* Delete Pipfile.lock
* Lock down kubernetes version to 0.10.0 due to CVE-2017-18342
* Propagate THOTH_ADVISER_DEV parameter to adviser runs
* Release of version 0.12.4
* Adjust id for qeb-hwt workflow
* Force JSON logger for all registered loggers
* Release of version 0.12.3
* We don't use threads, do not log info about them
* Remove warning produced by jsonformatter
* Release of version 0.12.2
* Fix requirements parsing
* Stopping bots
* Remove TODO for bot creating issues
* Release of version 0.12.1
* added the missing jsonformatter
* Release of version 0.12.0
* Release of version 0.11.0
* Implement structured logging for cluster deployments
* Removed coala bear
* add re_run metadata for qeb-hwt app
* Increase mypy timeout
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.2 to 0.14.3
* Release of version 0.10.12
* remove unused env variables
* Add empty env template
* :pushpin: Automatic update of dependency pytest from 5.3.5 to 5.4.1
* :pushpin: Automatic update of dependency pytest-mypy from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency pyyaml from 5.3 to 3.13
* :pushpin: Automatic update of dependency openshift from 0.10.2 to 0.10.3
* Remove again lines
* Reintroduce wf id
* Adjust solver workflows ID
* Fix issue with returning None instead of workflow id
* Add warning
* Modify logic of get_solver_names not to depend on Openshift template
* Removed unnecessary assignment
* Fix multiple spaces after operator
* Refactor get_workflow
* Allow to get_workflow by name
* Do not implicitly modify Workflow name
* Return adviser_id instead of workflow_id
* Move env variables to right place
* Remove old methods to schedule inspections
* Introduce Schedule inspection method in Openshift Class
* :pushpin: Automatic update of dependency mypy from 0.761 to 0.770
* Release of version 0.10.11
* Introduce method to assign workflow parameters
* Add variables for Ceph for adviser workflows
* Generalize variables for Ceph storage for workflow
* Add method to check workflow parameters
* Generalize variables for Ceph storage for workflow
* Adjust .thoth.yaml
* Adjust Pipfile and Pipfile.lock
* Release of version 0.10.10
* Adjust inputs for solvers
* Release of version 0.10.9
* Migrate method to be used for Argo
* Release of version 0.10.8
* Correct datatype
* Added get_workflow_status method
* Handle debug parameter for adviser in argo workflows
* Changed `nodes` -> `pods` in job status report
* Changed Job status report according to Amun API
* Openshift methods for inspection workflows
* Missing metadata parameters
* Release of version 0.10.7
* Always use Argo for thamos workflow
* Release of version 0.10.6
* Fix check for default value in workflow template
* Return directly result
* Simplfiy condition, do not use nested if
* Simplify dictionary handling with dict instantiation
* Propagate missing is_s2i flag to adviser metadata
* Simplify dictionary handling with inlined dict
* Add locked application stack optionally
* Fix confusion with lowercase decision type
* Add templates for releases
* Update .thoth.yaml
* Update .thoth.yaml
* Release of version 0.10.5
* Remove revision
* Release of version 0.10.4
* Change template name for Argo migration
* add missing parameter to advise method
* Release of version 0.10.3
* Adjust parameter for Thamos Workflos
* Add method to retrieve image streams
* Make decision type and recommendation type lowercase
* Release of version 0.10.2
* Remove prefix to avoid error in Thoth components
* Release of version 0.10.1
* Add host parameter for Thamos GitHub App
* function to sync build analyzers report
* :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.10.0
* Extend parameters for Adviser
* :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* Changed string formatting
* Added log error
* Added minor changes
* Modified documentation
* Reverted back autoindent
* Removed dummy files
* Modified function for init to handle env variables
* Release of version 0.9.31
* Do not cache fully specified environment check
* Adjust exception for thamos advise workflow
* Modify method to accept None
* Release of version 0.9.30
* :sparkles: added pre-commit and did a little bit of coala cleanup
* Thamos workflow for GitHub App Qeb-Hwt
* added xml coverage report
* Added missing return
* Fixed coala errors
* Added suggested changes
* Added suggested changes
* Fixed the spelling mistake causing issue
* Added readme back
* Delete .env
* Added to read me.
* Added to read me.
* Fixed Coala errors
* Added modified filter function
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.0 to 0.14.1
* Added before send filter
* Experiment logging
* Experiment logging
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* Release of version 0.9.29
* Rename template used by workload opeartor
* Correct solver id input
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* Release of version 0.9.28
* Use thoth.common as a root logger for logging information
* Release of version 0.9.27
* Try to avoid timing issues between job and configmap creation
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* Solver runs with Argo workflows
* Release of version 0.9.26
* remove wrong default value to run Dependency Monkey
* Release of version 0.9.25
* Enable providing pipeline configuration to Dependency Monkey
* Release of version 0.9.24
* Fix decision type environment variable name
* Add missing argument to dependency monkey runs
* Pass OpenShift instance instead of dynamic client to workflow manager
* I had to do it... it was so annoying
* Fix relative import issue
* adjust-code
* Add env variable to select type of scheduling
* Migrate to workflow for Adviser
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.5 to 0.14.0
* Release of version 0.9.23
* correct namespace use
* Schedule adviser workflow
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Be more aggressive with busy wait
* Busy wait on configmap creation to make sure cm gets propagated in the cluster
* Raise not found error if configmap was not found
* Happy new year!
* :pushpin: Automatic update of dependency mypy from 0.760 to 0.761
* :pushpin: Automatic update of dependency argo-workflows from 2.1.3 to 2.1.4
* :pushpin: Automatic update of dependency argo-workflows from 2.1.2 to 2.1.3
* :pushpin: Automatic update of dependency mypy from 0.750 to 0.760
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* :pushpin: Automatic update of dependency openshift from 0.10.0 to 0.10.1
* Release of version 0.9.22
* Correct bug in one function
* Add Thamos documentation
* Add is_s2i flag to adviser scheduling
* Point documentation to other libraries
* Introduce a generic logger adjustment
* Add Google Analytics
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.4 to 0.13.5
* Change Sphinx theme
* Release of version 0.9.21
* Sentry's aiohttp integration is supported only for Python 3.7+
* Release of version 0.9.20
* Updated randbits to fix #568
* Use 8 random digits in the ID instead of 16
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* Inspection Workflow template is stored in amun infra
* Fixed ResourceNotUniqueError in get_solver_names
* Fixed accessor to amun_infra_namespace attribute
* Allow for different workflow and template namespaces
* :pushpin: Automatic update of dependency mypy from 0.740 to 0.750
* Release of version 0.9.19
* Fix testsuite
* Library fixes
* Release of version 0.9.18
* Release of version 0.9.17
* :pushpin: Relock
* Make workflow management publicly consumable
* Propagate document id into templates
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.3 to 0.13.4
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency argo-workflows from 2.1.1 to 2.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.2 to 0.13.3
* Add configuration of ignored loggers
* Imlicitly assign workflow ID to the workflow name
* Sanitize workflow before submitting
* Process inspection template before retrieval
* Added methods to submit inspection workflows
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* Add few notes about logging to the README file
* Print integrations to log
* Update README file
* Enable Sentry integrations
* :pushpin: Automatic update of dependency argo-workflows from 2.1.0 to 2.1.1
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* Fix error due to ambiguous template resources
* Move data related files to tests/data dir
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Move workflows tests to the tests/ folder
* fixed W391 blank line at end of file
* Generate workflow ID by the unified `generate_id`
* Refactorings
* Fixed typing issues
* Reduce complexity of _submit_workflow method
* Return Workflow ID on submission
* Fix coala issues
* :pushpin: Lock dependencies for Argo
* Added missing flexmock dependency to the Pipfile
* Sanitize for serialization and validate by default
* Added deserialization of Workflow
* Implement Workflow.from_file method
* Syntactic sugar to load Workflow from a file
* Namespace is no longer optional
* Added configuration property to OpenShift instance
* Moved Workflow management to a separate module
* Added Argo client to the OpenShift class
* Release of version 0.9.16
* Do not propagate private property on to_dict()
* Enable running pytest for testsuite implementation
* Release of version 0.9.15
* Provide a method to check if the given environment is fully specified
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* Fix boolean types in mypy.ini
* :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* Start using mypy for type checking
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0
* Release of version 0.9.14
* Fix method name to comply with other methods
* Propagate is_external flag to package-extract runs
* relocked dependencies, cleaned up the coala deps
* Release of version 0.9.13
* Release of version 0.9.12
* Add warnings when there is something fishy in environment configuration for logging
* Always log in UTC to be consistent with team members all over the world
* Fix missing bracket
* Refactor out scheduling graph syncs
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Drop subgraph check
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* Release of version 0.9.11
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* Improve error message shown when getting cluster resources
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* Release of version 0.9.10
* Hotfix for errors when getting solver templates
* Release of version 0.9.9
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* Be consistent with solver type labels
* Release of version 0.9.8
* Do not pin to a specific Kubernetes release
* Release of version 0.9.7
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste
* Release of version 0.9.6
* Add template as optional param
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* New function to count jobs per status per label
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* Release of version 0.9.5
* :sunrise: Modified the names to standard convention
* Release of version 0.9.4
* openshift scheduler job for package analyzer
* Changed env variable names
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* Release of version 0.9.3
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Broke up run and schedule for stable api
* Release of version 0.9.2
* Fix wrong argument handling
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* Copy paste remnants
* :arrow_double_up: Increase the limit for file line size
* Increase maximum lines
* Conditional statement
* Subcommand env
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* Introduce graph sync multiple
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* Coala fixes
* Release of version 0.9.1
* Provide method for scheduling graph-refresh on demand
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* Release of version 0.9.0
* New function for all ConfigMaps
* Logic to run and schedule kebechet builds
* Fix retrieving pod logs - use OpenShift API
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* Release of version 0.8.11
* Fix solver temlate handling
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* Release of version 0.8.10
* :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* Implement Sentry environment
* Supply environment variable for registry and infra namespace for inspections
* minor fix of error msg
* :bug: minor fix for correct namespace
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.13.11 (2020-06-10T20:44:50)
* Add sesheta as a maintainer
* Fixed mypy and black
* Fixed type
* added serialize before json dump
* Remove repo name from workflow-id
* Remove slash from repo name
* Release of version 0.13.10
* Add docstring to repository param
* Change parameter to single repo
* Edit namespace check
* Add schedule srcopsmetrics workflow method
* Properly serialize metadata
* Add submit srcopsmetrics workflow
* Release of version 0.13.9
* :pushpin: Automatic update of dependency pylint from 2.5.2 to 2.5.3
* Introudce method for verifying Kebechet inputs
* Reformat code using black
* :sparkles: standard pre-commit-config
* :pushpin: Automatic update of dependency mypy from 0.770 to 0.780
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* wrong function name and use enum.name
* remove coala from zuul
* added a 'tekton trigger tag_release pipeline issue'
* Release of version 0.13.8
* add missing import
* adjust config
* Be consistent
* use strings to indicate futures
* move import to fix circular dependency issue
* move type: ignore
* only change pre-commit config
* rename base test
* typing checks, docstrings, test renamed
* Release of version 0.13.7
* make output in solve optional
* Missing self in methods
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* Release of version 0.13.6
* rename method
* Missing self
* Release of version 0.13.5
* Introduce logic for solver
* Release of version 0.13.4
* Add missing parameters
* Correct docstring
* New check method for Qeb-HWt inputs
* remove method
* Use name
* Add check for Thoth integration
* Add exception for integrations
* import auto
* Add exception for integrations
* Use solvers ConfigMap
* remove is_s2i flag
* Adjust enums
* Add enum to init
* Add TODO
* Add source type for Thoth adviser integrations
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.3 to 0.14.4
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* :pushpin: Automatic update of dependency pylint from 2.5.0 to 2.5.2
* Release of version 0.13.3
* all the github standard templates
* :pushpin: Automatic dependency re-locking
* :pushpin: Automatic dependency re-locking
* Quote unknown configuration entries
* Release of version 0.13.2
* :pushpin: Automatic update of dependency jsonformatter from 0.1.4 to 0.2.1
* Add status analysis and make label selector optional
* Little adjustments
* Adjust name of method
* New methods to monitor Argo workflows
* Changed parameter type
* Moved json serialization
* Release of version 0.13.1
* Renamed to kebechet
* :pushpin: Automatic update of dependency pylint from 2.4.4 to 2.5.0
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.1 to 0.6.2
* Release of version 0.13.0
* Added workflow functions
* Release of version 0.12.10
* Provide platform in Thoth's runtime environment config option
* Release of version 0.12.9
* Remove assignment of the Dockerfile
* Remove parallelism and allowed failures configuration
* Propagate requests and limits for inspection run and build
* Release of version 0.12.8
* :nut_and_bolt: provide imagestream name while processing template
* Release of version 0.12.7
* Correct default and typo
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.0 to 0.6.1
* Release of version 0.12.6
* Set default loglevel to WARNING
* Lazily initialize the WorkflowManager
* Release of version 0.12.5
* Initial dependency lock
* Delete Pipfile.lock
* Lock down kubernetes version to 0.10.0 due to CVE-2017-18342
* Propagate THOTH_ADVISER_DEV parameter to adviser runs
* Release of version 0.12.4
* Adjust id for qeb-hwt workflow
* Force JSON logger for all registered loggers
* Release of version 0.12.3
* We don't use threads, do not log info about them
* Remove warning produced by jsonformatter
* Release of version 0.12.2
* Fix requirements parsing
* Stopping bots
* Remove TODO for bot creating issues
* Release of version 0.12.1
* added the missing jsonformatter
* Release of version 0.12.0
* Release of version 0.11.0
* Implement structured logging for cluster deployments
* Removed coala bear
* add re_run metadata for qeb-hwt app
* Increase mypy timeout
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.2 to 0.14.3
* Release of version 0.10.12
* remove unused env variables
* Add empty env template
* :pushpin: Automatic update of dependency pytest from 5.3.5 to 5.4.1
* :pushpin: Automatic update of dependency pytest-mypy from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency pyyaml from 5.3 to 3.13
* :pushpin: Automatic update of dependency openshift from 0.10.2 to 0.10.3
* Remove again lines
* Reintroduce wf id
* Adjust solver workflows ID
* Fix issue with returning None instead of workflow id
* Add warning
* Modify logic of get_solver_names not to depend on Openshift template
* Removed unnecessary assignment
* Fix multiple spaces after operator
* Refactor get_workflow
* Allow to get_workflow by name
* Do not implicitly modify Workflow name
* Return adviser_id instead of workflow_id
* Move env variables to right place
* Remove old methods to schedule inspections
* Introduce Schedule inspection method in Openshift Class
* :pushpin: Automatic update of dependency mypy from 0.761 to 0.770
* Release of version 0.10.11
* Introduce method to assign workflow parameters
* Add variables for Ceph for adviser workflows
* Generalize variables for Ceph storage for workflow
* Add method to check workflow parameters
* Generalize variables for Ceph storage for workflow
* Adjust .thoth.yaml
* Adjust Pipfile and Pipfile.lock
* Release of version 0.10.10
* Adjust inputs for solvers
* Release of version 0.10.9
* Migrate method to be used for Argo
* Release of version 0.10.8
* Correct datatype
* Added get_workflow_status method
* Handle debug parameter for adviser in argo workflows
* Changed `nodes` -> `pods` in job status report
* Changed Job status report according to Amun API
* Openshift methods for inspection workflows
* Missing metadata parameters
* Release of version 0.10.7
* Always use Argo for thamos workflow
* Release of version 0.10.6
* Fix check for default value in workflow template
* Return directly result
* Simplfiy condition, do not use nested if
* Simplify dictionary handling with dict instantiation
* Propagate missing is_s2i flag to adviser metadata
* Simplify dictionary handling with inlined dict
* Add locked application stack optionally
* Fix confusion with lowercase decision type
* Add templates for releases
* Update .thoth.yaml
* Update .thoth.yaml
* Release of version 0.10.5
* Remove revision
* Release of version 0.10.4
* Change template name for Argo migration
* add missing parameter to advise method
* Release of version 0.10.3
* Adjust parameter for Thamos Workflos
* Add method to retrieve image streams
* Make decision type and recommendation type lowercase
* Release of version 0.10.2
* Remove prefix to avoid error in Thoth components
* Release of version 0.10.1
* Add host parameter for Thamos GitHub App
* function to sync build analyzers report
* :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* Release of version 0.10.0
* Extend parameters for Adviser
* :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* Changed string formatting
* Added log error
* Added minor changes
* Modified documentation
* Reverted back autoindent
* Removed dummy files
* Modified function for init to handle env variables
* Release of version 0.9.31
* Do not cache fully specified environment check
* Adjust exception for thamos advise workflow
* Modify method to accept None
* Release of version 0.9.30
* :sparkles: added pre-commit and did a little bit of coala cleanup
* Thamos workflow for GitHub App Qeb-Hwt
* added xml coverage report
* Added missing return
* Fixed coala errors
* Added suggested changes
* Added suggested changes
* Fixed the spelling mistake causing issue
* Added readme back
* Delete .env
* Added to read me.
* Added to read me.
* Fixed Coala errors
* Added modified filter function
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.0 to 0.14.1
* Added before send filter
* Experiment logging
* Experiment logging
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* Release of version 0.9.29
* Rename template used by workload opeartor
* Correct solver id input
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* Release of version 0.9.28
* Use thoth.common as a root logger for logging information
* Release of version 0.9.27
* Try to avoid timing issues between job and configmap creation
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* Solver runs with Argo workflows
* Release of version 0.9.26
* remove wrong default value to run Dependency Monkey
* Release of version 0.9.25
* Enable providing pipeline configuration to Dependency Monkey
* Release of version 0.9.24
* Fix decision type environment variable name
* Add missing argument to dependency monkey runs
* Pass OpenShift instance instead of dynamic client to workflow manager
* I had to do it... it was so annoying
* Fix relative import issue
* adjust-code
* Add env variable to select type of scheduling
* Migrate to workflow for Adviser
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.5 to 0.14.0
* Release of version 0.9.23
* correct namespace use
* Schedule adviser workflow
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* Be more aggressive with busy wait
* Busy wait on configmap creation to make sure cm gets propagated in the cluster
* Raise not found error if configmap was not found
* Happy new year!
* :pushpin: Automatic update of dependency mypy from 0.760 to 0.761
* :pushpin: Automatic update of dependency argo-workflows from 2.1.3 to 2.1.4
* :pushpin: Automatic update of dependency argo-workflows from 2.1.2 to 2.1.3
* :pushpin: Automatic update of dependency mypy from 0.750 to 0.760
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* :pushpin: Automatic update of dependency openshift from 0.10.0 to 0.10.1
* Release of version 0.9.22
* Correct bug in one function
* Add Thamos documentation
* Add is_s2i flag to adviser scheduling
* Point documentation to other libraries
* Introduce a generic logger adjustment
* Add Google Analytics
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.4 to 0.13.5
* Change Sphinx theme
* Release of version 0.9.21
* Sentry's aiohttp integration is supported only for Python 3.7+
* Release of version 0.9.20
* Updated randbits to fix #568
* Use 8 random digits in the ID instead of 16
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* Inspection Workflow template is stored in amun infra
* Fixed ResourceNotUniqueError in get_solver_names
* Fixed accessor to amun_infra_namespace attribute
* Allow for different workflow and template namespaces
* :pushpin: Automatic update of dependency mypy from 0.740 to 0.750
* Release of version 0.9.19
* Fix testsuite
* Library fixes
* Release of version 0.9.18
* Release of version 0.9.17
* :pushpin: Relock
* Make workflow management publicly consumable
* Propagate document id into templates
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.3 to 0.13.4
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency argo-workflows from 2.1.1 to 2.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.2 to 0.13.3
* Add configuration of ignored loggers
* Imlicitly assign workflow ID to the workflow name
* Sanitize workflow before submitting
* Process inspection template before retrieval
* Added methods to submit inspection workflows
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* Add few notes about logging to the README file
* Print integrations to log
* Update README file
* Enable Sentry integrations
* :pushpin: Automatic update of dependency argo-workflows from 2.1.0 to 2.1.1
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* Fix error due to ambiguous template resources
* Move data related files to tests/data dir
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* Move workflows tests to the tests/ folder
* fixed W391 blank line at end of file
* Generate workflow ID by the unified `generate_id`
* Refactorings
* Fixed typing issues
* Reduce complexity of _submit_workflow method
* Return Workflow ID on submission
* Fix coala issues
* :pushpin: Lock dependencies for Argo
* Added missing flexmock dependency to the Pipfile
* Sanitize for serialization and validate by default
* Added deserialization of Workflow
* Implement Workflow.from_file method
* Syntactic sugar to load Workflow from a file
* Namespace is no longer optional
* Added configuration property to OpenShift instance
* Moved Workflow management to a separate module
* Added Argo client to the OpenShift class
* Release of version 0.9.16
* Do not propagate private property on to_dict()
* Enable running pytest for testsuite implementation
* Release of version 0.9.15
* Provide a method to check if the given environment is fully specified
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* Fix boolean types in mypy.ini
* :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* Start using mypy for type checking
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0
* Release of version 0.9.14
* Fix method name to comply with other methods
* Propagate is_external flag to package-extract runs
* relocked dependencies, cleaned up the coala deps
* Release of version 0.9.13
* Release of version 0.9.12
* Add warnings when there is something fishy in environment configuration for logging
* Always log in UTC to be consistent with team members all over the world
* Fix missing bracket
* Refactor out scheduling graph syncs
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* Drop subgraph check
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* Release of version 0.9.11
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* Improve error message shown when getting cluster resources
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* Release of version 0.9.10
* Hotfix for errors when getting solver templates
* Release of version 0.9.9
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* Be consistent with solver type labels
* Release of version 0.9.8
* Do not pin to a specific Kubernetes release
* Release of version 0.9.7
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste
* Release of version 0.9.6
* Add template as optional param
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* New function to count jobs per status per label
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* Release of version 0.9.5
* :sunrise: Modified the names to standard convention
* Release of version 0.9.4
* openshift scheduler job for package analyzer
* Changed env variable names
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* Release of version 0.9.3
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Broke up run and schedule for stable api
* Release of version 0.9.2
* Fix wrong argument handling
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* Copy paste remnants
* :arrow_double_up: Increase the limit for file line size
* Increase maximum lines
* Conditional statement
* Subcommand env
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* Introduce graph sync multiple
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* Coala fixes
* Release of version 0.9.1
* Provide method for scheduling graph-refresh on demand
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* Release of version 0.9.0
* New function for all ConfigMaps
* Logic to run and schedule kebechet builds
* Fix retrieving pod logs - use OpenShift API
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* Release of version 0.8.11
* Fix solver temlate handling
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* Release of version 0.8.10
* :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* Implement Sentry environment
* Supply environment variable for registry and infra namespace for inspections
* minor fix of error msg
* :bug: minor fix for correct namespace
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* Provide default for limit latest versions
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Minor fix to display correct release in title of docs html
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* Add missing requests library to requirements
* Release of version 0.8.5
* Fix inspection and inspect bad interpretation
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Release of version 0.8.3
* fixed the log message
* fixed some coala errors
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Release of version 0.8.2
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Use safe_load() instead of load()
* Release of version 0.8.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Do not consider nested none values in output if with_none is false
* Introduce limit latest versions parameter
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Update .coafile
* Propagate origin as metadata
* Add getter to default datetime format
* Add format_datetime method to convert datetimes
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Introduce runtime environment abstractions
* Introduce method for scheduling adviser graph syncs
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* A temporary workaround for workload management
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Parse requests for build workload
* Make run methods optional
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Assing memory and cpu requests when getting template
* Fix issues when template does not request any resources
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Serialize parameters into JSON when adding to ConfigMap
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Release of version 0.5.0
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Dependency monkey can accept a serialized JSON representing Pipfile
* Fix env variable typo
* Propagate count to dependency monkey runs
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Solver now accepts subgraph check API parameter
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Release of version 0.4.7
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Propagate index urls into solver runs
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Introduce method for gathering buildconfigs
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Introduce count and limit for adviser
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Use api version from template
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Release of version 0.4.0
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* Report error if sentry initialization fails
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Release of version 0.3.14
* refactor methods into pythonic way
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* add InClusterConfigLoader to load SA and cert
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* using the correct api
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Release of version 0.3.12
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* added get_jobs(), it will be used for thoth-metrics
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Default to now if no datetime was provided
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Return None if there are no pod logs yet
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Fix undefined name error
* Raise appropriate not found exception exception
* Release of version 0.3.7
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
* Release of version 0.3.6
* fixed another typo
* fixed a few typos
* Release of version 0.3.5
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

## Release 0.13.12 (2020-06-16T23:35:49)
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.4 to 1.4.1
* remove default index
* move Lazy to common helpers from python helpers
* mypy typing error introduced in another commit
* No default package index
* Ignore unused import
* use middletier namespace
* add submit and schedule methods for SI's
* Setup Sentry traces sample rate

## Release 0.13.13 (2020-06-25T17:13:22)
* Fixed precommit
* Source type enum fix
* Update OWNERS
* Adjust signature - return value
* some reformatting
* :pushpin: Automatic update of dependency mypy from 0.781 to 0.782
* :ambulance: some reformatting
* Make pipeline configuration optional
* The schedule method of dependency monkey now accepts only Pipfile
* Remove report output, it is placed on Ceph by Argo
* Schedule Dependency Monkey using Argo workflows
* pre-commit
* Remove variable not required
* Remove build dependencies component
* :pushpin: Automatic update of dependency mypy from 0.780 to 0.781
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.4 to 0.15.1
* :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0
* Accept alternative datetime format string used by PyPI
* Correct serialization of Enum
* :pushpin: Automatic update of dependency pytest-cov from 2.9.0 to 2.10.0

## Release 0.14.0 (2020-07-01T09:45:47)
* Always supply pipeline configuration for dependency monkey (#897)
* Package extract now does not need output to result-api (#896)
* Update OWNERS
* Update OWNERS
* Drop remaning workload-operator bits
* Drop legacy workload operator, use only Argo workflows
* Update OWNERS
* Remove kebechet jobs they are now part of workflows
* Remove package analyzer job
* Introduce provenance-checker Argo workflow
* Use Argo workflows for package-extract
* Reformat using black
* Introduce build analysis workflow
* Remove graph sync jobs

## Release 0.14.1 (2020-07-03T08:50:13)
* Use singular (#901)
* Add methods to schedule SI workflow (#900)

## Release 0.14.2 (2020-07-15T21:57:46)
* Make methods static (#909)
* Parsing solver names can be a class method (#908)
* Introduce reverse solver workflow (#907)
* Add parameter to trigger reverse solver run (#906)

## Release 0.15.0 (2020-07-28T18:38:04)
* Added workflow status wrapper (#919)
* Do not limit latest versions on adviser runs (#917)
* Remove unused env variable (#916)
