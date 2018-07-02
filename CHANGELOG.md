# Changelog for the Thoth common module

## [0.0.9] - 2018-Jun-28 - goern

### Fixed

* argument name in logger_setup() see https://github.com/thoth-station/common/pull/31

## [0.0.8] - 2018-Jun-25 - goern

### Added

Starting with this release we have a Zuul-CI pipeline that:

* lints on Pull Requrest and gate/merge
* uploads to pypi (test) on tag
