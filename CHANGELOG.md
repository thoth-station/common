# Changelog for the Thoth common module

## Release 0.36.5 (2022-07-20T12:17:36)
* e0636bc Release of version 0.36.4
* 29b2653 Update OWNERS
* 0750c76 Release of version 0.36.3
* e0b56ea :recycle: HouseKeeping: Updated OWNERS and pre-commit changes (#1267)
* 0564012 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment (#1266)
* fcd6755 🥹 moving @fridex in the OWNERS file, thanks for all the great work!!! (#1265)
* f177706 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 2a5d90b adding openshift function and schedule workflow for sync-job (#1260)
* 35e798c :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 898a361 bump kubernetes version for common image
* 1f0cfe5 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 3362110 Release of version 0.36.2
* f60c5ce Replace slash with dash in repo slug [scheduling mi workflows] (#1249)
* cc06aad Moving out the mypy as separate check
* d2b808b Update mypy config python version to 3.8
* 54c810c Fix pre-commit version to be ==2.15.0
* 53b4441 Update prow image tags
* 9c87ab5 Autoupdate pre-commit
* 11c303f :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* e0dc247 Send messages based on template defaults, do not hardcode (#1231)
* a2a9cbe Release of version 0.36.1
* 70063d0 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 4239319 Remove rfc5424-logging-handler from dependencies
* 676250c Release of version 0.36.0
* 4d3bd3d Add username to maintainers
* 16ff4e9 Remove [mypy-rfc5424logging] from mypy.ini
* c3a313e Drop rfc5424logging and syslog
* 140413f Remove venv import
* 03e9544 Make pre-commit happy
* b05fe9a Remove blank line:
* bd6b480 Add create_knowledge parameter, change workflow name
* fc05165 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* d4e0104 Release of version 0.35.0
* 1fe2cd5 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* e9b945d Increase test timeout
* 639ccad Allow passing dependency indexes to be checked for solver
* 448f504 Release of version 0.34.1
* 541f8d8 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment (#1222)
* 8aaaab5 Fix parsing solver name for Python 3.10
* a8b60ad :fire: Fix the send_message assignment with default
* b126ad1 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* cef84cd Enable TLS verification
* e37f984 Release of version 0.34.0
* 4c42ccc :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 333d0e8 if slug is None then param should not be passed
* 72291f4 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 1aa5f4c :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 45a5e1e common project repo is not built into container image
* a54bb31 Release of version 0.33.1
* b37e553 Runtime environment entries can have labels associated
* 6c32131 Release of version 0.33.0
* f6dd77a :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* f9b9b49 Fix typing for CPU and GPU properties
* dbacb31 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* cee0150 add kebechet to crossroads in docs
* 0ed4777 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* f49ceae increase pytest timeout
* b46ed63 add method to schedule thoth-repo-init workflow
* c3049e6 Move variables closer to each other
* 7984478 Assign empty string if None
* ed9c121 Add merge path to schedule mi workflows
* 96079d6 :arrow_up: Automatic update of dependencies by Kebechet
* 1318474 :arrow_up: Automatic update of dependencies by Kebechet
* f17edbc Adjust exceptions
* fdd1cdd Introduce method to expose cache expiration
* b7f9bbf Release of version 0.32.0
* 6db1d35 get update info from kebechet meta
* d3f45b0 :arrow_up: Automatic update of dependencies by Kebechet
* 262817e Release of version 0.31.0
* 928f379 :arrow_up: Automatic update of dependencies by Kebechet
* 8590912 use numbers in enums
* 0ec26f4 Use explicit values for enums
* c11702a Remove from adviser method
* 0063887 Remove qeb-hwt and github-app bits
* ed38297 add function argument to add value to template parameter for update advises
* a88ee9b :medal_sports: set badges for easy access to content (#1175)
* 213d3a2 :arrow_up: updating the pytest fixes
* 4fa2818 :arrow_up: Automatic update of dependencies by Kebechet (#1168)
* a3404c2 Release of version 0.30.0 (#1169)
* 777341a add priority/critical-urgent label to all bot related issue templates
* aa4b7b2 Add thoth.common to mypy.ini
* 501e931 Provide force_sync to solver schedule methods
* 1429d9d :hatched_chick: update the prow resource limits (#1163)
* 706aa76 Release of version 0.29.1 (#1160)
* 5764125 Run purge workflows in middletier namespace (#1158)
* 9e0b5a4 Release of version 0.29.0 (#1157)
* 42e3f3e Introduce methods for scheduling purge workflow (#1152)
* daa6e95 Make graph namespace available to the OpenShift adapter (#1155)
* f3ee976 :arrow_up: Automatic update of dependencies by Kebechet (#1154)
* 7bf5b8e Mi/feature/merge (#1153)
* 1a6d581 Minor improvements to docs (#1151)
* 70f6598 Release of version 0.28.0 (#1150)
* 2da86cf Allow running authenticated provenance check (#1147)
* d0ece90 :arrow_up: Automatic update of dependencies by Kebechet (#1148)
* 354d862 Provide an argument to run authenticated advises (#1146)
* 83c5668 Release of version 0.27.0 (#1145)
* 419c6a2 Be consistent with env vars supplied (#1143)
* 85da648 :arrow_up: Automatic update of dependencies by Kebechet (#1142)
* f8e821a Add additional configuration as parameter (#1141)
* 5b96cd3 Release of version 0.26.0 (#1138)
* 517b979 thoth-adviser metadata
* 8f7333e Release of version 0.25.0 (#1134)
* 3751c0f pass slug to kebechet workflow (#1125)
* be31377 add metadata to relevant schedule methods (#1103)
* 014556c :arrow_up: Automatic update of dependencies by Kebechet (#1131)
* 17bab45 Add knowledge_path as parameter for schedule_mi_workflow (#1129)
* ca5454b :sparkles: reconfgured CI/CD to use prow and aicoe-ci
* 4f77a26 Release of version 0.24.2
* f2bb414 Pin openshift to help Pipenv resolve the stack (#1126)
* f9c5449 :arrow_up: Automatic update of dependencies by Kebechet
* 3595be3 Release of version 0.24.1
* 335f8a4 Add empty commit to trigger a new release for thoth-common
* 43fda68 Release of version 0.24.0
* 999d9e0 Fix parsing runtime environment entries
* cc82140 Add flag to optionally sync results of package-extract
* 5b55519 Fix obtaining pod status for workflows (#1113)
* 35ba322 :arrow_up: Automatic update of dependencies by Kebechet (#1114)
* d5b4201 Do not propagate request data via messaging (#1109)
* 4aff3b4 :arrow_up: Automatic update of dependencies by Kebechet (#1112)
* 31a9027 Thoth application#398 (#1111)
* 22a9184 :arrow_up: Automatic update of dependencies by Kebechet (#1110)
* fd6775d Thoth application#398 (#1107)
* be74fc6 Release of version 0.23.0 (#1106)
* a56dacd run dependency monkey workload on the amun-inspection namespace (#1104)
* e9b1cf9 Release of version 0.22.1 (#1102)
* c584b6e Fix package-extract job id propagation (#1100)
* 7439543 :arrow_up: Automatic update of dependencies by kebechet. (#1099)
* 552e6f1 add enum for internal triggers (#1098)
* a40d960 :arrow_up: Automatic update of dependencies by kebechet. (#1097)
* ca650d1 :arrow_up: Automatic update of dependencies by kebechet. (#1095)
* c2ea600 Release of version 0.22.0 (#1096)
* ff70011 Extend Thamos configuration file (#1072)
* 4fed76e Revisit generating id to avoid hash collisions (#1093)
* 1ce8b7e :sparkles: add kind/ labels to feature and bug template (#1091)
* e5cded7 :arrow_up: Automatic update of dependencies by kebechet. (#1090)
* cd271a0 Add is_external flag to build analysis (#1088)
* 4049cdb Release of version 0.21.4
* 8fb9467 Provide additional build-analysis metadata so documents are traceable (#1085)
* eb00072 Provide image metadata for package-extract (#1083)
* e743b5e Add method to schedule graph-update-schema job (#1052)
* 138b2b1 removed bissenbay, thanks for your contributions!
* 9ed3126 Version 0.21.3
* 532c325 Extend parameters supplied to build analysis (#1076)
* 67d7702 Propagate build log document id to build analysis workflow (#1073)
* 4d8e125 Increase random bits used to distinguish workflows (#1069)
* fe5aacc Release of version 0.21.1 (#1068)
* c2d1641 Remove AttrDict from requirements (#1066)
* d9ade2f Release of version 0.21.0 (#1065)
* c6ed30b :arrow_up: Automatic update of dependencies by kebechet. (#1063)
* 5051d78 Move normalization functions to helpers (#1060)
* 0531b6c Bump black version
* da1fb80 Add submit and schedule kebechet methods (#1054)
* 008b303 included issue template to release missing module (#1055)
* 46c64cb add .aicoe-ci.yaml
* 574dae7 bump python version
* 355a1ff Release of version 0.20.6 (#1049)
* 8837849 Release of version 0.20.5 (#1041)
* 75332e3 Pin argo-workflows to a version before 4 (#1043)
* 1121596 :pushpin: Automatic update of dependency argo-workflows from 3.5.1 to 3.6.0 (#1038)
* dc968f8 Move openshift related code from mi-scheduler (#1037)
* 0bbbfa6 :pushpin: Automatic update of dependency pytest-mypy from 0.7.0 to 0.8.0 (#1035)
* c3126b4 :pushpin: Automatic update of dependency sentry-sdk from 0.19.2 to 0.19.3 (#1034)
* bf740ac :pushpin: Automatic update of dependency requests from 2.24.0 to 2.25.0 (#1033)
* cc762f7 schedule graph sync workflow (#1028)
* 07070a7 :pushpin: Automatic update of dependency daiquiri from 2.1.1 to 3.0.0 (#1032)
* fdbe842 :pushpin: Automatic update of dependency attrs from 20.2.0 to 20.3.0 (#1030)
* b8a4ba0 :pushpin: Automatic update of dependency sentry-sdk from 0.19.1 to 0.19.2 (#1029)
* 4c2fdfa get workflow node status (#1007)
* d711442 Release of version 0.20.4 (#1027)
* 96ca6c1 :pushpin: Automatic update of dependency pytest from 6.1.1 to 6.1.2 (#1026)
* d18f7f4 Turn missing env variable warning into an error (#1024)
* 467eb49 Release of version 0.20.3 (#1023)
* dd9cac5 Added method to call kebechet admin workflow (#1021)
* 7fac11b Release of version 0.20.2 (#1020)
* 3c83534 :pushpin: Automatic update of dependency sentry-sdk from 0.19.0 to 0.19.1 (#1018)
* e953cb9 check if workflow has started (#1017)
* ebcdf8b Added method to initiate kebechet run-url workflow (#1013)
* d3e0ebf :pushpin: Automatic update of dependency mypy from 0.782 to 0.790 (#1016)
* 23189e4 :pushpin: Automatic update of dependency sentry-sdk from 0.18.0 to 0.19.0 (#1015)
* e5d8a12 Release of version 0.20.1 (#1012)
* 2cdc4a0 Qebhwt needs deployment name (#1010)
* 0239923 :pushpin: Automatic update of dependency pytest from 6.0.2 to 6.1.1 (#1008)
* 6626c69 :pushpin: Automatic update of dependency pytest from 6.0.2 to 6.1.1 (#1006)
* eba6918 :pushpin: Automatic update of dependency sentry-sdk from 0.17.8 to 0.18.0 (#1005)
* fd12293 Release of version 0.20.0 (#1003)
* cfea886 :pushpin: Automatic update of dependency sentry-sdk from 0.17.7 to 0.17.8 (#1002)
* 94d3905 Update versions for compatibility between Argo, Kuberneter and Openshift (#998)
* 5aa48e6 Rely on S2I specific environment variable, no OpenShift build env vars (#994)
* 59404a7 :pushpin: Automatic update of dependency sentry-sdk from 0.17.5 to 0.17.6 (#995)
* 0b1fe6f fix pre-commit for common (#996)
* dc73941 Improve message logged when obtaining wf node log from cluster fails
* c3bf680 Release of version 0.19.0 (#991)
* 977d58d :pushpin: Automatic update of dependency sentry-sdk from 0.17.4 to 0.17.5 (#989)
* 446d09b Fix predictor config propagation when scheduling adviser
* 5c88c40 only get pending workflows
* e143522 Release of version 0.18.3 (#985)
* 122e7e9 :pushpin: Automatic update of dependency pytest from 6.0.1 to 6.0.2 (#984)
* 4d53e6c add option to pass job_id so we can return it in user-api (#982)
* 12412f1 No need to provide html suffix (#981)
* 52bc443 Release of version 0.18.2 (#980)
* dfaabe5 thamos->qebhwt for workflow name (#978)
* 2b33828 Release of version 0.18.1
* d197108 Make links to justifications shorter so they fit to terminal output (#975)
* 1cfe5bf Release of version 0.18.0 (#974)
* 12a6570 :pushpin: Automatic update of dependency sentry-sdk from 0.17.3 to 0.17.4 (#973)
* ff9e0cc Provide a method for obtaining a link to justification description (#971)
* 48220ec :pushpin: Automatic update of dependency attrs from 20.1.0 to 20.2.0 (#969)
* 0bdccdd :pushpin: Automatic update of dependency sentry-sdk from 0.17.2 to 0.17.3 (#968)
* 75f9047 Release of version 0.17.3
* 88be0ab Do not propagate private attribute in to_doct() method
* 9f260a2 Provenance checks should be scheduled in backend namespace
* 6484e8d Add more information related to invalid response size (#962)
* dea1864 Hide default predictor name (#963)
* 6ccb47d Add Thoth's template for PRs (#964)
* a5300d2 Release of version 0.17.2 (#961)
* 1f799e7 Allow users to pick predictor to be used (#959)
* 8889505 Release of version 0.17.1 (#958)
* dc7100e :pushpin: Automatic update of dependency sentry-sdk from 0.16.5 to 0.17.2 (#957)
* b83cbe7 Introduce a way to parametrize adviser's predictor (#955)
* ab00017 make count a simple library call
* ebf7cd1 Provide cached Python package version tuple (#918)
* 62428aa Fix typing
* 387b511 Release of version 0.17.0
* 34f99ba add sleep
* 864d0d6 Add a routine for obtaining logs from workflow nodes
* f084cf5 add optional limit for workflows
* d0c0eb1 :pushpin: Automatic update of dependency pytest-mypy from 0.6.2 to 0.7.0 (#946)
* 4a39387 :pushpin: Automatic update of dependency pylint from 2.5.3 to 2.6.0 (#945)
* 9d4a313 :pushpin: Automatic update of dependency attrs from 19.3.0 to 20.1.0 (#944)
* f267725 :pushpin: Automatic update of dependency attrs from 19.3.0 to 20.1.0 (#943)
* 982b67c Remove IMAGE_STREAM_NAMESPACE env (#941)
* aa5fb4b Release of version 0.16.1 (#940)
* bcba785 :pushpin: Automatic update of dependency sentry-sdk from 0.16.3 to 0.16.5 (#937)
* a9dd47c :pushpin: Automatic update of dependency pytest-cov from 2.10.0 to 2.10.1 (#938)
* 4038c17 Introduce raw specification parameter to be used when storing on Ceph (#936)
* 3d08288 Add long_description_content_type (#935)
* 6ee544a set source_type_enum None when soure_type not set (#932)
* 79c263e :pushpin: Automatic update of dependency pytest from 6.0.0 to 6.0.1 (#934)
* 73e552f :pushpin: Automatic update of dependency sentry-sdk from 0.16.2 to 0.16.3 (#933)
* 3d7e3a9 :arrow_down: removed the files as they are no longer required
* bcb5d85 Release of version 0.16.0 (#929)
* 54f3de1 :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.0 (#927)
* 2831758 Rename srcopsmetrics to mi (#926)
* 8417273 Release of version 0.15.0 (#923)
* d579472 :pushpin: Automatic update of dependency jsonformatter from 0.2.3 to 0.3.0 (#922)
* c43d661 :pushpin: Automatic update of dependency sentry-sdk from 0.16.1 to 0.16.2 (#921)
* 49987d8 Added workflow status wrapper (#919)
* 4152294 Do not limit latest versions on adviser runs (#917)
* e0c9f26 Remove unused env variable (#916)
* 3876c4e Release of version 0.14.2 (#913)
* 1ae52bf :pushpin: Automatic update of dependency pytest-timeout from 1.4.1 to 1.4.2 (#912)
* 3c565f9 :pushpin: Automatic update of dependency sentry-sdk from 0.16.0 to 0.16.1 (#911)
* a46e9c3 Make methods static (#909)
* 06a80fd Parsing solver names can be a class method (#908)
* 8b34840 Introduce reverse solver workflow (#907)
* e175a2a Add parameter to trigger reverse solver run (#906)
* a302c35 Release of version 0.14.1 (#904)
* 2a0bc40 :pushpin: Automatic update of dependency sentry-sdk from 0.15.1 to 0.16.0 (#903)
* 6a057e9 Use singular (#901)
* fc576e6 Add methods to schedule SI workflow (#900)
* dc5d1ed Release of version 0.14.0 (#899)
* 453149d Always supply pipeline configuration for dependency monkey (#897)
* 9a481df Package extract now does not need output to result-api (#896)
* 2217d3f Update OWNERS
* 1605b3e Update OWNERS
* 6ca22ab Drop remaning workload-operator bits
* a58216f Drop legacy workload operator, use only Argo workflows
* 2d8ceab Update OWNERS
* de24419 Remove kebechet jobs they are now part of workflows
* 4deb77d Remove package analyzer job
* aa03835 Introduce provenance-checker Argo workflow
* 34c2fee Use Argo workflows for package-extract
* bc10f51 Reformat using black
* 348241b Introduce build analysis workflow
* 600af7d Remove graph sync jobs
* 957a614 Release of version 0.13.13
* 0effd3d Fixed precommit
* befe0c0 Source type enum fix
* d249301 Update OWNERS
* c8e8111 Adjust signature - return value
* f5788e2 some reformatting
* 8170e9b :pushpin: Automatic update of dependency mypy from 0.781 to 0.782
* 2f38a5e :ambulance: some reformatting
* 29ec12a Make pipeline configuration optional
* 03197b3 The schedule method of dependency monkey now accepts only Pipfile
* b788ad9 Remove report output, it is placed on Ceph by Argo
* adf33b7 Schedule Dependency Monkey using Argo workflows
* 2d50991 pre-commit
* d4f9541 Remove variable not required
* 4360558 Remove build dependencies component
* 3bc4dc4 :pushpin: Automatic update of dependency mypy from 0.780 to 0.781
* 64fc8e8 :pushpin: Automatic update of dependency sentry-sdk from 0.14.4 to 0.15.1
* 0aebd53 :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0
* b2dbaf0 Accept alternative datetime format string used by PyPI
* 0e0ea7f Correct serialization of Enum
* ae1d759 :pushpin: Automatic update of dependency pytest-cov from 2.9.0 to 2.10.0
* af1755b Release of version 0.13.12
* 368190f :pushpin: Automatic update of dependency pytest-timeout from 1.3.4 to 1.4.1
* 63f0fb6 remove default index
* d14469a move Lazy to common helpers from python helpers
* 8cbc973 Release of version 0.13.11
* b39d932 Add sesheta as a maintainer
* 62f5e88 Fixed mypy and black
* 8479b64 Fixed type
* 61b6018 added serialize before json dump
* c8f82b5 Remove repo name from workflow-id
* 27d1f4c Remove slash from repo name
* b041a15 Release of version 0.13.10
* 5459233 Add docstring to repository param
* d4fd4ef Change parameter to single repo
* 0aab36b Edit namespace check
* ce7de3d Add schedule srcopsmetrics workflow method
* 6fdbfe8 Properly serialize metadata
* 53dcef0 Add submit srcopsmetrics workflow
* bcf90db mypy typing error introduced in another commit
* e32c693 No default package index
* b4d0b88 Release of version 0.13.9
* 880ed6e :pushpin: Automatic update of dependency pylint from 2.5.2 to 2.5.3
* b171073 Ignore unused import
* 0d8f2e4 use middletier namespace
* ceb75ea add submit and schedule methods for SI's
* e861de9 Introudce method for verifying Kebechet inputs
* 30f1694 Reformat code using black
* 365c075 :sparkles: standard pre-commit-config
* 3d3c827 Setup Sentry traces sample rate
* 8619485 :pushpin: Automatic update of dependency mypy from 0.770 to 0.780
* c202ccb :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* 9c3e408 wrong function name and use enum.name
* ce507bf remove coala from zuul
* be20bb1 added a 'tekton trigger tag_release pipeline issue'
* bf3b7a8 Release of version 0.13.8
* 5f4995b add missing import
* e08a67a adjust config
* 6c4cc16 Be consistent
* 55b5822 use strings to indicate futures
* e099879 move import to fix circular dependency issue
* 3230d37 move type: ignore
* 41a4d38 only change pre-commit config
* 0d9cffb rename base test
* 8dec902 typing checks, docstrings, test renamed
* 46bb9f8 Release of version 0.13.7
* e9b9481 make output in solve optional
* 53ee33b Missing self in methods
* 910aec7 :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* 1c36cba Release of version 0.13.6
* af794d4 rename method
* 6ae8e4a Missing self
* 1d8ff5d Release of version 0.13.5
* 29a5fd7 Introduce logic for solver
* 84bc017 Release of version 0.13.4
* e06dc6e Add missing parameters
* 5e1b442 Correct docstring
* f863228 New check method for Qeb-HWt inputs
* 78a5aba remove method
* c9af691 Use name
* b6a4fd1 Add check for Thoth integration
* aaa51f8 Add exception for integrations
* 66f6f84 import auto
* e6f1b90 Add exception for integrations
* 5560d84 Use solvers ConfigMap
* 2a7ac4b remove is_s2i flag
* 3fbd03e Adjust enums
* 7c8260c Add enum to init
* 1d14b27 Add TODO
* 211c2b3 Add source type for Thoth adviser integrations
* ff96f00 :pushpin: Automatic update of dependency sentry-sdk from 0.14.3 to 0.14.4
* 698766b :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* 676c758 :pushpin: Automatic update of dependency pylint from 2.5.0 to 2.5.2
* 28557e4 Release of version 0.13.3
* 0f7682a all the github standard templates
* b6b938a :pushpin: Automatic dependency re-locking
* ca00a4a :pushpin: Automatic dependency re-locking
* ac134ff Quote unknown configuration entries
* 4b2f372 Release of version 0.13.2
* 6569bbe :pushpin: Automatic update of dependency jsonformatter from 0.1.4 to 0.2.1
* 6c53fe6 Add status analysis and make label selector optional
* 5d67847 Little adjustments
* 1d99fea Adjust name of method
* 86c5b80 New methods to monitor Argo workflows
* a98c545 Changed parameter type
* 07c523b Moved json serialization
* 454a8d5 Release of version 0.13.1
* 06dfe3d Renamed to kebechet
* e2be95e :pushpin: Automatic update of dependency pylint from 2.4.4 to 2.5.0
* ada321d :pushpin: Automatic update of dependency pytest-mypy from 0.6.1 to 0.6.2
* b280b98 Release of version 0.13.0
* 2fdced9 Added workflow functions
* b5f1df3 Release of version 0.12.10
* 55d9743 Provide platform in Thoth's runtime environment config option
* 7fbc72b Release of version 0.12.9
* ed91d1b Remove assignment of the Dockerfile
* 55aff78 Remove parallelism and allowed failures configuration
* 7c33ed8 Propagate requests and limits for inspection run and build
* 1943c85 Release of version 0.12.8
* bb62861 :nut_and_bolt: provide imagestream name while processing template
* 855bab8 Release of version 0.12.7
* 5148b38 Correct default and typo
* cf59fd9 :pushpin: Automatic update of dependency pytest-mypy from 0.6.0 to 0.6.1
* 71b0f46 Release of version 0.12.6
* 9ce67d4 Set default loglevel to WARNING
* ac759ee Lazily initialize the WorkflowManager
* 613a0c5 Release of version 0.12.5
* a7093d6 Initial dependency lock
* 1871185 Delete Pipfile.lock
* eb5a480 Lock down kubernetes version to 0.10.0 due to CVE-2017-18342
* c007f6b Propagate THOTH_ADVISER_DEV parameter to adviser runs
* 1193820 Release of version 0.12.4
* cce29ff Adjust id for qeb-hwt workflow
* 9ea5878 Force JSON logger for all registered loggers
* cc56a77 Release of version 0.12.3
* 67058ef We don't use threads, do not log info about them
* c8ce484 Remove warning produced by jsonformatter
* 89a54f6 Release of version 0.12.2
* 61913b0 Fix requirements parsing
* 78ceaee Stopping bots
* d2367dc Remove TODO for bot creating issues
* b352188 Release of version 0.12.1
* e030c80 added the missing jsonformatter
* b1bf508 Release of version 0.12.0
* f7ac0fc Release of version 0.11.0
* fdcc833 Implement structured logging for cluster deployments
* 97aaa90 Removed coala bear
* 3ca33fb add re_run metadata for qeb-hwt app
* 4b3e477 Increase mypy timeout
* 9ae9cf5 :pushpin: Automatic update of dependency sentry-sdk from 0.14.2 to 0.14.3
* 56bb7e7 Release of version 0.10.12
* 76212f7 remove unused env variables
* 65caac2 Add empty env template
* 780cd96 :pushpin: Automatic update of dependency pytest from 5.3.5 to 5.4.1
* e2a493f :pushpin: Automatic update of dependency pytest-mypy from 0.5.0 to 0.6.0
* bc866f4 :pushpin: Automatic update of dependency pyyaml from 5.3 to 3.13
* 3585e5a :pushpin: Automatic update of dependency openshift from 0.10.2 to 0.10.3
* 231fece Remove again lines
* a7dd9ba Reintroduce wf id
* c8d4a35 Adjust solver workflows ID
* 852febf Fix issue with returning None instead of workflow id
* dba35be Add warning
* dfdc649 Modify logic of get_solver_names not to depend on Openshift template
* be70738 Removed unnecessary assignment
* f3982df Fix multiple spaces after operator
* 965c322 Refactor get_workflow
* cdd4d3d Allow to get_workflow by name
* 4ce9f5a Do not implicitly modify Workflow name
* 76e3a82 Return adviser_id instead of workflow_id
* 739db3e Move env variables to right place
* 1c9fd83 Remove old methods to schedule inspections
* 74a7bd0 Introduce Schedule inspection method in Openshift Class
* f100c0f :pushpin: Automatic update of dependency mypy from 0.761 to 0.770
* 331bf98 Release of version 0.10.11
* 2490a85 Introduce method to assign workflow parameters
* d4455a6 Add variables for Ceph for adviser workflows
* e0ed4ac Generalize variables for Ceph storage for workflow
* d433293 Add method to check workflow parameters
* a095ed7 Generalize variables for Ceph storage for workflow
* 5cbf075 Adjust .thoth.yaml
* 54bfced Adjust Pipfile and Pipfile.lock
* 82005a7 Release of version 0.10.10
* c747c06 Adjust inputs for solvers
* 886e1a8 Release of version 0.10.9
* 199370e Migrate method to be used for Argo
* 5ded87f Release of version 0.10.8
* 0344410 Correct datatype
* cd7cbb8 Added get_workflow_status method
* b70ffb2 Handle debug parameter for adviser in argo workflows
* 0aded2d Changed `nodes` -> `pods` in job status report
* 28caa49 Changed Job status report according to Amun API
* 3d4a9df Openshift methods for inspection workflows
* a8b2da0 Missing metadata parameters
* b7538b6 Release of version 0.10.7
* 74d60f1 Always use Argo for thamos workflow
* b8b2547 Release of version 0.10.6
* ef3f5f9 Fix check for default value in workflow template
* f7e7e59 Return directly result
* 4a991a1 Simplfiy condition, do not use nested if
* 81e459a Simplify dictionary handling with dict instantiation
* 1e24b2b Propagate missing is_s2i flag to adviser metadata
* a6c2ae6 Simplify dictionary handling with inlined dict
* 86081bd Add locked application stack optionally
* da957cf Fix confusion with lowercase decision type
* f3c3562 Add templates for releases
* 156bb3b Update .thoth.yaml
* 543920f Update .thoth.yaml
* 7054428 Release of version 0.10.5
* e35464b Remove revision
* cbfb4f1 Release of version 0.10.4
* bacdd7e Change template name for Argo migration
* d9c24cf add missing parameter to advise method
* 3ceb1ff Release of version 0.10.3
* 818b263 Adjust parameter for Thamos Workflos
* d1bd8bf Add method to retrieve image streams
* 5b07d1e Make decision type and recommendation type lowercase
* 9bd039f Release of version 0.10.2
* 2c159f2 Remove prefix to avoid error in Thoth components
* 36d5fe9 Release of version 0.10.1
* 68be594 Add host parameter for Thamos GitHub App
* 764e197 function to sync build analyzers report
* f8d5236 :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* 94aa465 :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* 9b67365 Release of version 0.10.0
* e4d9a1e Extend parameters for Adviser
* 28a0aa5 :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* 69a4da6 Changed string formatting
* 826b7a6 Added log error
* 6e14a54 Added minor changes
* 79692f6 Modified documentation
* 432f6ba Reverted back autoindent
* 3a5bceb Removed dummy files
* 4f72303 Modified function for init to handle env variables
* 71c158a Release of version 0.9.31
* 174502f Do not cache fully specified environment check
* dcf5e97 Adjust exception for thamos advise workflow
* 68de3d3 Modify method to accept None
* 3f899de Release of version 0.9.30
* 9f8f374 :sparkles: added pre-commit and did a little bit of coala cleanup
* 3a80e76 Thamos workflow for GitHub App Qeb-Hwt
* ec75648 added xml coverage report
* 892590e Added missing return
* d4d91a6 Fixed coala errors
* f115f49 Added suggested changes
* 6ce2539 Added suggested changes
* 668da2e Fixed the spelling mistake causing issue
* 85d8713 Added readme back
* c2b2fbf Delete .env
* 7562a42 Added to read me.
* 305cc47 Added to read me.
* 63d491c Fixed Coala errors
* 1e463cd Added modified filter function
* d8005a1 :pushpin: Automatic update of dependency sentry-sdk from 0.14.0 to 0.14.1
* 706b2c0 Added before send filter
* ce1e7ae Experiment logging
* bfc2b71 Experiment logging
* f76d141 :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* f39be5e Release of version 0.9.29
* b3e4f93 Rename template used by workload opeartor
* 04597f2 Correct solver id input
* 7555e46 :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* 20b9df8 Release of version 0.9.28
* 7925a55 Use thoth.common as a root logger for logging information
* 327e902 Release of version 0.9.27
* 3b7d039 Try to avoid timing issues between job and configmap creation
* 5e363ce :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* ccf18a3 Solver runs with Argo workflows
* b8be16f Release of version 0.9.26
* 17b6601 remove wrong default value to run Dependency Monkey
* 8530ee7 Release of version 0.9.25
* a24aafd Enable providing pipeline configuration to Dependency Monkey
* 123a61c Release of version 0.9.24
* b0e0f3d Fix decision type environment variable name
* 9ec51fe Add missing argument to dependency monkey runs
* c62935c Pass OpenShift instance instead of dynamic client to workflow manager
* eae703d I had to do it... it was so annoying
* 3c1788d Fix relative import issue
* 8ae0408 adjust-code
* a60bf21 Add env variable to select type of scheduling
* 86e28ac Migrate to workflow for Adviser
* ac9f3e1 :pushpin: Automatic update of dependency sentry-sdk from 0.13.5 to 0.14.0
* 95071dc Release of version 0.9.23
* 54222ec correct namespace use
* 1bdef81 Schedule adviser workflow
* fe5f97b :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* f8eefd7 :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* 1d92b01 Be more aggressive with busy wait
* 083daec Busy wait on configmap creation to make sure cm gets propagated in the cluster
* b8a8b9a Raise not found error if configmap was not found
* 6e5bd8c Happy new year!
* f8483a6 :pushpin: Automatic update of dependency mypy from 0.760 to 0.761
* 910de40 :pushpin: Automatic update of dependency argo-workflows from 2.1.3 to 2.1.4
* 082e6e6 :pushpin: Automatic update of dependency argo-workflows from 2.1.2 to 2.1.3
* 897e0aa :pushpin: Automatic update of dependency mypy from 0.750 to 0.760
* 4df92b6 :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* f5f7e81 :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* 6de58d1 :pushpin: Automatic update of dependency openshift from 0.10.0 to 0.10.1
* 4813ebd Release of version 0.9.22
* af0feb2 Correct bug in one function
* 5597476 Add Thamos documentation
* d947a22 Add is_s2i flag to adviser scheduling
* 1a0386a Point documentation to other libraries
* 17879d0 Introduce a generic logger adjustment
* 8cb0cb7 Add Google Analytics
* df68ee0 :pushpin: Automatic update of dependency sentry-sdk from 0.13.4 to 0.13.5
* 020126e Change Sphinx theme
* ae95689 Release of version 0.9.21
* 2695017 Sentry's aiohttp integration is supported only for Python 3.7+
* 34c6e4a Release of version 0.9.20
* 97a87ab Updated randbits to fix #568
* c3996df Use 8 random digits in the ID instead of 16
* cc3fdf6 :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* 267fe98 Inspection Workflow template is stored in amun infra
* a59a42e Fixed ResourceNotUniqueError in get_solver_names
* a0482fb Fixed accessor to amun_infra_namespace attribute
* d193198 Allow for different workflow and template namespaces
* 391431d :pushpin: Automatic update of dependency mypy from 0.740 to 0.750
* e255f1a Release of version 0.9.19
* 774a682 Fix testsuite
* 56b66ab Library fixes
* a112d7c Release of version 0.9.18
* cab6098 Release of version 0.9.17
* f603267 :pushpin: Relock
* fd3c314 Make workflow management publicly consumable
* 3875d3d Propagate document id into templates
* a0f9bf5 :pushpin: Automatic update of dependency sentry-sdk from 0.13.3 to 0.13.4
* 58585f6 :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* 25c174a :pushpin: Automatic update of dependency argo-workflows from 2.1.1 to 2.1.2
* 14c3ae2 :pushpin: Automatic update of dependency sentry-sdk from 0.13.2 to 0.13.3
* 0c5411b Add configuration of ignored loggers
* 5db1ef0 Imlicitly assign workflow ID to the workflow name
* ceadc5e Sanitize workflow before submitting
* d544753 Process inspection template before retrieval
* 9e1d06b Added methods to submit inspection workflows
* 9454e42 :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* eea9da3 Add few notes about logging to the README file
* c186588 Print integrations to log
* f02475c Update README file
* ac1c0b8 Enable Sentry integrations
* 488678e :pushpin: Automatic update of dependency argo-workflows from 2.1.0 to 2.1.1
* b9fd371 :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* fb45727 Fix error due to ambiguous template resources
* fc5c06f Move data related files to tests/data dir
* c71a4f3 :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* 6243803 Move workflows tests to the tests/ folder
* 69b420c fixed W391 blank line at end of file
* 7cb36cb Generate workflow ID by the unified `generate_id`
* 99438c1 Refactorings
* 173d171 Fixed typing issues
* 5796875 Reduce complexity of _submit_workflow method
* a45e303 Return Workflow ID on submission
* ce79515 Fix coala issues
* 6cf6af1 :pushpin: Lock dependencies for Argo
* c370ea3 Added missing flexmock dependency to the Pipfile
* 64de0d3 Sanitize for serialization and validate by default
* ae2bfeb Added deserialization of Workflow
* 50611da Implement Workflow.from_file method
* b02ff05 Syntactic sugar to load Workflow from a file
* c7548ab Namespace is no longer optional
* 6d3f656 Added configuration property to OpenShift instance
* 1ef3967 Moved Workflow management to a separate module
* 9b2699a Added Argo client to the OpenShift class
* a9cfb5a Release of version 0.9.16
* 3345832 Do not propagate private property on to_dict()
* 27c392f Enable running pytest for testsuite implementation
* d206703 Release of version 0.9.15
* e1d44f7 Provide a method to check if the given environment is fully specified
* 4083ce7 :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* 0073d31 Fix boolean types in mypy.ini
* 5086861 :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* b7ab1c7 Start using mypy for type checking
* a117ed0 :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* 9e6ad3a :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* 2c23203 :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* eda42ff :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0
* e740e52 Release of version 0.9.14
* 87bc7f7 Fix method name to comply with other methods
* c4944e7 Propagate is_external flag to package-extract runs
* 0d44e62 relocked dependencies, cleaned up the coala deps
* 780ba3a Release of version 0.9.13
* bf01651 Release of version 0.9.12
* 914aede Add warnings when there is something fishy in environment configuration for logging
* 081a8f2 Always log in UTC to be consistent with team members all over the world
* 3c29523 Fix missing bracket
* c95fd9e Refactor out scheduling graph syncs
* 2c5a8cb :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* ae5f076 :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* 11ad119 :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* 5ce632f Drop subgraph check
* 51d4bbb :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* 8f738b5 Release of version 0.9.11
* 8d91e30 :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* 2a8925a :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* 57a7720 :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* 68eae52 :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* 89dc2e1 Improve error message shown when getting cluster resources
* 6750b86 :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* 807be15 :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* 4e51367 :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* 267511d :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* 6088ca8 Release of version 0.9.10
* b610d13 Hotfix for errors when getting solver templates
* 9a3b813 Release of version 0.9.9
* d27babb :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* 984fdb6 Schedule solvers without transitive flag being set
* ae104f2 Add dry-run to package-analyzer
* 9ad4f79 :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* 855849b :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* 5d464c1 :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* 3deb56c :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* 9af0635 :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* 6a55976 :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* 6e3eda1 Be consistent with solver type labels
* 281cf14 Release of version 0.9.8
* fe45e92 Do not pin to a specific Kubernetes release
* 4bb24bf Release of version 0.9.7
* a0881f9 As we use Thoth to resolve dependencies, stop using extras
* d2fdc50 Leftover parameter from copy paste
* 56cd8a8 Release of version 0.9.6
* 2a6e909 Add template as optional param
* 45a62e4 :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* e3f3cdd New function to count jobs per status per label
* 0189cca :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* 23420bc Release of version 0.9.5
* 09528b5 :sunrise: Modified the names to standard convention
* 949f0a2 Release of version 0.9.4
* 8dcea2a openshift scheduler job for package analyzer
* 2ce2673 Changed env variable names
* 08c4206 :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* f0f04a7 Release of version 0.9.3
* a31ffb4 Increase maximum lines per file
* 7817354 :sunglasses: Support for build analysers scheduling
* 58b3dc9 Broke up run and schedule for stable api
* fe3ca6c Release of version 0.9.2
* 8eeb82c Fix wrong argument handling
* 5217b4a :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* d6083f7 Copy paste remnants
* 66ba385 :arrow_double_up: Increase the limit for file line size
* b19c5e0 Increase maximum lines
* 0f33558 Conditional statement
* 3c58f1e Subcommand env
* a744206 :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* d0be843 :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* 74c9639 Introduce graph sync multiple
* e55de0b :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* 118c27a :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* d86edfb :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* 2878fa1 :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* 0964829 Coala fixes
* 7ed7424 Release of version 0.9.1
* 458cb46 Provide method for scheduling graph-refresh on demand
* fc3e7e2 :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* 445445a :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* ce306b3 Release of version 0.9.0
* 44e3e34 New function for all ConfigMaps
* 58d0a50 Logic to run and schedule kebechet builds
* 7f14fcc Fix retrieving pod logs - use OpenShift API
* cfcfc87 :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* 5d6e560 :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* 175a9a3 Release of version 0.8.11
* 820894f Fix solver temlate handling
* 19fdb78 :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* bc30631 Release of version 0.8.10
* 8cc5f12 :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* bfe9b35 Implement Sentry environment
* 35b7c03 Supply environment variable for registry and infra namespace for inspections
* bc0a905 minor fix of error msg
* e3db8d9 :bug: minor fix for correct namespace
* 0322590 :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* 85f5ec1 :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* b35455a :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* 7037db9 Release of version 0.8.9
* c6014e3 Release of version 0.8.8
* d8492e7 Release of version 0.8.7
* e1c823e :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* d68d799 Provide default for limit latest versions
* 82813d0 :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* e894612 Release of version 0.8.6
* e82338c Ensure recommendation type is in upper case
* 1c46603 Propagate library usage to adviser runs
* 89318bf Minor fix to display correct release in title of docs html
* a793269 :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* b5b4167 :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* 9d5136d :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* 6313c88 :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* 7029938 :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* 9c7c073 :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* b257762 :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* f1dd114 Add missing requests library to requirements
* a350a96 Release of version 0.8.5
* 3fbddd0 Fix inspection and inspect bad interpretation
* 51abff2 :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* 26f14c7 Release of version 0.8.4
* 0d13048 Obtain templates from Amun infra for Amun specific templates
* f8329f8 Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* f32d13a Release of version 0.8.3
* 2af0607 fixed the log message
* 010c2a7 fixed some coala errors
* 0f671c6 :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* 590ab50 Release of version 0.8.2
* 297eb08 Automatic update of dependency pytest from 4.3.1 to 4.4.0
* 064babf Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* 9a802dd Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* 3f04b53 Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* f7b787e Add Thoth's configuration file
* 9171247 Fix serialization of runtime environment
* 43dd6ff Propagate metadata about runtime and buildtime environment
* 31f04cd Release of version 0.8.1
* 26f2db4 Finding the right OpenShift version
* 9a67979 Lock Kubernetes and OpenShift to specific version
* 2a2d84b Adjust heading
* c0bb9aa Use Sphinx for documentation
* 65fca69 Automatic update of dependency pyyaml from 3.13 to 5.1
* f9c7549 Automatic update of dependency pylint from 2.3.0 to 2.3.1
* eec368a Automatic update of dependency pytest from 4.3.0 to 4.3.1
* 67f8ed6 Automatic update of dependency attrs from 18.2.0 to 19.1.0
* 2bacacc Use safe_load() instead of load()
* 82453ac Release of version 0.8.0
* 31f44b7 Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* f4110a3 Do not consider nested none values in output if with_none is false
* 29bad61 Introduce limit latest versions parameter
* 5a76335 Automatic update of dependency pylint from 2.2.2 to 2.3.0
* 1446e54 Automatic update of dependency pytest from 4.2.1 to 4.3.0
* ad51e87 Automatic update of dependency openshift from 0.8.5 to 0.8.6
* 6e2ba95 Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* b976784 Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* 348517e Update .coafile
* 18ddfe0 Propagate origin as metadata
* e3976c1 Add getter to default datetime format
* 5f35065 Add format_datetime method to convert datetimes
* c4c0c6a Automatic update of dependency openshift from 0.8.4 to 0.8.5
* d1b5865 Release of version 0.7.1
* 6011ea4 Add missing MANIFEST.in
* 109b886 Release of version 0.7.0
* c3c98e4 Graph syncs are unique per document id, no need to have long ids
* 2862aba Do not pin down openshift and kubernetes, let consumers do it if needed
* d61445c Propagate document ID into graph-sync job name
* 6dc1dd6 Address coala complains
* db6f2d5 Check for ConfigMap presence to report registered workload to user
* 7d6e8de Automatic update of dependency pytest from 4.2.0 to 4.2.1
* 444e26e Runtime environment can be set to None
* ebf1719 Add check for runtime environment name
* 68d740c Optionally provide dict representation without none values
* 955d6bd Load runtime environment transparently from YAML/JSON file
* 6f69c9b Also install the missing config module
* b6c394a Remove unused entry
* 53fe82a Introduce name and rename hardware_information to hardware
* d820104 Automatic update of dependency pytest from 4.1.1 to 4.2.0
* a05690e Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* 84cb57f Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* a3f4b06 Introduce runtime environment abstractions
* bd067d5 Introduce method for scheduling adviser graph syncs
* 7acce6a Release of version 0.6.0
* dc96286 Revert "A temporary workaround for workload management"
* 00a034a A temporary workaround for workload management
* 071bd74 Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* 4a216fc Disable urllib3 warnings
* 16955f0 Fix seed environment name typo
* d883488 Provide sugar methods for scheduling graph sync
* 112f10a Parse requests for build workload
* 49cdf2f Make run methods optional
* da59ccf Label workload to allow type specific queries
* 60358e9 Fix in template gathering for inspection build
* 16e2233 Treat builds as workload
* 9bae885 Propagate graph-sync job id into template
* f6be033 Explicitly assign inspection requests
* b17e4da Assing memory and cpu requests when getting template
* 10b5625 Fix issues when template does not request any resources
* 9b700f1 Fix how amun and thoth infra namespace is handled
* e27195e Fix more coala issues
* fc59d83 Fix coala errors
* 9339da4 Fix incorrect namespace usage one more time
* 073c16f Fix incorrect use of infra namespace
* 67d2418 Amun does not use Thoth's infra namespace
* 1854c94 Add routine for scheduling all registered solvers
* fc1bd36 Check running workload based on quota
* 4268349 Add routines for workload operator
* d26d26f Enable local development for OpenShift client
* 918eb31 Reformat using black
* ebf4b91 Add missing guards for scheduling routines
* 50b7658 Move Amun specific pieces to OpenShift class
* 0c7b3d6 Workload operator expects method, not method_name
* 8193575 Serialize parameters into JSON when adding to ConfigMap
* 1782cef Remove self from propagated parameters to configmap
* ea0c055 Introduce schedule methods for workload operator
* 6c54227 Reformant using black
* 0d6528f Extend log messages with a line number
* b6b18db Report template parameters in debug mode
* aad6930 Make limit and count optional parameters for adviser template
* 564d934 Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* bcdcc72 Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* 64c1edf Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* 0a9b415 Automatic update of dependency pytest from 4.0.1 to 4.0.2
* 7097f68 Release of version 0.5.0
* cb15c82 Automatic update of dependency requests from 2.20.1 to 2.21.0
* b294a0b Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* 36ca1cd Dependency monkey can accept a serialized JSON representing Pipfile
* cde8d18 Fix env variable typo
* 40c523f Propagate count to dependency monkey runs
* abaf9fd Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* 989fefb Solver now accepts subgraph check API parameter
* 5aa88d6 Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* 32bf896 Release of version 0.4.7
* 7191c3e Automatic update of dependency pylint from 2.2.1 to 2.2.2
* 0077751 Automatic update of dependency pylint from 2.2.0 to 2.2.1
* 828868c Propagate index urls into solver runs
* 7ffac3e Automatic update of dependency pylint from 2.1.1 to 2.2.0
* 76a20ed Automatic update of dependency pytest from 4.0.0 to 4.0.1
* 7207d60 Add long description for PyPI
* 8d55f49 Supply whitelisted sources to provenance checks
* e68460f Adjust force sync to respect implementation
* 26fe000 Release of version 0.4.6
* c64c495 Runtime environment is now a dict
* 2ca0416 Release of version 0.4.5
* f8e5da5 Introduce method for gathering buildconfigs
* bb8aa31 Release of version 0.4.4
* aa8cb2a Fix CI
* c7961fe Rename dependency monkey limit to respect its semantics
* 8305831 Introduce count and limit for adviser
* 152ad7d Release of version 0.4.3
* 4cec185 Introduce method for getting build in a namespace
* 8c87c84 Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* 3fe0105 Release of version 0.4.2
* 8d68879 Add count parameter to dependency monkey
* 6634724 Release of version 0.4.1
* 3d882d5 Propagate dependency monkey parameters to template
* 6da9bf2 Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* 14fee6b Automatic update of dependency pytest from 3.10.1 to 4.0.0
* ccaade8 Use api version from template
* 6fa992c Automatic update of dependency pytest from 3.10.0 to 3.10.1
* 6b10e7e Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* 3222fdf Automatic update of dependency requests from 2.20.0 to 2.20.1
* cafd2c4 Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* 3545977 Release of version 0.4.0
* 7808397 Automatic update of dependency pytest from 3.9.3 to 3.10.0
* 6ddf28d Introduce method for creating datetime from timestamp
* e51181a Release of version 0.3.16
* f638e86 Fix missing import
* 01347d9 Make CI happy again
* b397be3 Release of version 0.3.15
* d773fc8 Make all datetimes timezone aware
* 3444a5d Report error if sentry initialization fails
* c6c0723 using thoht-* jobs now
* 241eca0 Do not propagate force to actual package-extract run
* 2798136 Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* c398e3c Release of version 0.3.14
* 74092c9 refactor methods into pythonic way
* 306c4bd Release of version 0.3.13
* 8f88eca added parameter force:bool, why was it missing?
* 5e60ee8 Automatic update of dependency pytest from 3.9.2 to 3.9.3
* de3c01f add InClusterConfigLoader to load SA and cert
* aa31d2f Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* f668d11 using the correct api
* 8bd41e8 Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* 02c6901 Automatic update of dependency pytest from 3.9.1 to 3.9.2
* f4f646d Release of version 0.3.12
* 91f8a52 Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* 29c95f4 added get_jobs(), it will be used for thoth-metrics
* a9264ca Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* 7bae13c Automatic update of dependency requests from 2.19.1 to 2.20.0
* 5149e9b Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* 4b496ee Automatic update of dependency pytest from 3.8.2 to 3.9.1
* 6f433d8 Default to now if no datetime was provided
* c11d345 Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* 15bbbb8 Release of version 0.3.11
* 80bfe58 Fix syntax error
* 4bf4760 Release of version 0.3.10
* 7d4228d Return None if there are no pod logs yet
* a17dd21 Add message to translate table
* 605ef7c Release of version 0.3.9
* 17a576e Release of version 0.3.8
* 0540a1c Fix gathering pod id from job name
* dd088a9 Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* 77eb1da Fix undefined name error
* 1159ce4 Raise appropriate not found exception exception
* f294a27 Release of version 0.3.7
* 5bbc7b4 Automatic update of dependency sentry-sdk from 0.3.9 to 0.3.11
* c4f47ee Add routines for jobs handling
* 5e0a857 Gather build logs from OpenShift
* 885d544 Allow explicitly specifying the logging configuration prefix
* 146aeac Make reusable methods public
* ae3fc31 Introduce methods for running dependency monkey
* 9087883 Automatic update of dependency sentry-sdk from 0.3.8 to 0.3.9
* 5535bc5 Automatic update of dependency pytest from 3.8.1 to 3.8.2
* 098d511 Automatic update of dependency sentry-sdk from 0.3.7 to 0.3.8
* 7d68e85 Automatic update of dependency sentry-sdk from 0.3.6 to 0.3.7
* 10f8ae2 Release of version 0.3.6
* 4dab35c fixed another typo
* 25739c8 fixed a few typos
* 35ba58e Release of version 0.3.5
* 7548de3 Release of version 0.3.4
* e5a42c0 Release of version 0.3.3
* 757f344 fixed the typo, this closes #114
* 2bf8f10 Automatic update of dependency sentry-sdk from 0.3.5 to 0.3.6
* ef34a95 Release of version 0.3.2
* 8c246c9 Initial dependency lock
* 005960e Add Sentry support
* d17b4b8 Report scheduling status if pod was not initialized yet
* 055bf7b Report back empty pod status is pod is being scheduled
* 974ddd9 Automatic update of dependency pytest from 3.8.0 to 3.8.1
* bafe0c1 Automatic update of dependency rfc5424-logging-handler from 1.1.2 to 1.2.1
* 0e19dc7 Unify pod status reports
* e68e248 Treat None parameter values as empty values
* e05602a Release of version 0.3.1
* 06d0048 added github configuration
* 9e6da3f Automatic update of dependency pytest from 3.7.4 to 3.8.0
* e40f73c Fix built-in type shadowing
* 50599ad Release of version 0.3.0
* 91ecb4b Let's reuse adviser env var names
* 8c46b27 Issue warning on suspicious parameter expansion in templates
* d461b85 Fix propagating debug flag to package-extract
* a2fce27 Fix gathering pod logs for default middletier namespace
* c5aad21 Fix gathering pod status for default middletier namespace
* fe45d41 Automatic update of dependency pytest-cov from 2.5.1 to 2.6.0
* e4fbbe8 Release of version 0.2.7
* 28ff96e Fix default TLS verification behavior
* 3f80f09 Introduce routine for running provenance checker
* 713a82a Release of version 0.2.6
* 9e86f32 Initial dependency lock
* df29ccf change the queue
* dad8282 change the queue
* 972fd90 Fix TLS/SSL certification verification configuration
* 06729e4 Release of version 0.2.5
* 4767e4e Configure SSL/TLS correctly when communicating with master
* a4fafdd Initial dependency lock
* 757b902 Release of version 0.2.4
* 2bf1618 Pin down Kubernetes and OpenShift clients to specific versions
* 6ea251c Release of version 0.2.3
* f410b14 Initial dependency lock
* 09e5f15 Fix over-intended block
* ef26aff Remove Pipfile.lock for initial lock from Kebechet
* d46cd55 Add TODO comment based on review
* 2fdd8b0 Allow passing configuration via env vars
* 0b6fe33 Place all the OpenShift related logic at one place
* da12cfe Automatic update of dependency pytest-timeout from 1.3.1 to 1.3.2
* 6676ce4 Automatic update of dependency pytest from 3.7.1 to 3.7.3
* 52a8196 Automatic update of dependency pylint from 2.1.0 to 2.1.1
* d785775 Automatic update of dependency pytest from 3.7.0 to 3.7.1
* a1199c5 Automatic update of dependency pylint from 2.0.1 to 2.1.0
* 851d6cc Automatic update of dependency pytest from 3.6.4 to 3.7.0
* 219d64d Automatic update of dependency pytest from 3.6.3 to 3.6.4
* 940e64d Update .zuul.yaml
* 59a7e66 Release of version 0.2.2
* 2d570bf Automatic update of dependency pylint from 1.9.2 to 2.0.1
* 84ee06c Automatic update of dependency pytest-timeout from 1.3.0 to 1.3.1
* f30b50b Allow completely suppressing logs
* 9251de5 Automatic update of dependency daiquiri from 1.3.0 to 1.5.0
* 12dcd92 releasing 0.2.1
* 752e763 Fix syntax error in logging
* 4901a5d Initial dependency lock
* 434c5dc Delete Pipfile.lock for relocking dependencies
* 29f8c7a preparing release 0.2.0
* 6439904 using logger.exception()
* feda091 catching and logging a "[Errno -2] Name or service not known"
* 9bb5f64 Remove pydocstyle from Pipfile
* e7346b3 releasing 0.1.0
* cadbb17 Introduce a function for getting service account token
* d5d5074 releasing 0.0.9
* a826bf8 Change in var name
* a3c6dfd fixed trailing space issue
* c4604ff added the gate pipeline to the core queue
* 70b1aba releasing 0.0.8
* 77d62f3 uploading to production pypi now... using sesheta account
* 14ea1ea trigger
* a55aade fixed some coala errors
* 38ba8c0 preparing release 0.0.8: Zuul
* 4c0850f Version 0.0.7
* fb0547a Change in Indentation
* e7f2fe4 Change in Indentation and variable names
* 5dd6def Generic wrappers to define verbose level on every method
* 5ff870d Fix logging issues
* 3fd1494 added daiquiri
* d791d9f Disable annoying unverified HTTPS warnings
* c655ea4 Fix typo in docstring
* 8786ff7 Setup logging for root logger
* d21a4b0 Remove a temporary dependency for kebechet testing
* 8afdd3f Automatic update of dependency thoth-storages from 0.0.26 to 0.0.28
* 8e41b14 Automatic update of dependency rfc5424-logging-handler from 1.1.0 to 1.1.2
* eab2725 Testing dependencies
* f14fa45 A temporary dependency downgrade to test kebechet
* 41d82cb Version 0.0.6
* 6d5db91 Add support for rsyslog logging endpoint
* b568d7d Run coala in non-interactive mode
* b844675 Run coala in CI
* 3e989ff Create OWNERS
* 72bb3d3 Remove dependencies.yml
* d64a64b Add missing headers to files
* db56f0b Use coala for code checks
* 7224b07 Use GPLv3 in setup.py
* 32f43b7 Use GPLv3
* 3010d9a Add missing import
* 336c818 Version 0.0.5
* 088bcbc Convert a timestamp to datetime string
* 5649d77 Version 0.0.4
* 99e46c5 Argument 2 to isinstance has to be a type
* b86ab68 Add README file
* 5779773 Version 0.0.3
* 0a1eb48 Add datetime2datetime_str conversion function
* e3732df Version 0.0.2
* 685ca55 Abstract manipulation with datetime
* b4f1ede Add space so Sphinx interpret docstrings correctly
* b2507c8 Respect double dash as module separator
* 68d8578 Version 0.0.1
* e82d2fb Provide version information properly
* 5db5410 Add init_logging function
* 5526b44 Fix package name
* c84b29a Create initial dependencies.yml config
* 9e8ab84 Initial project import

## Release 0.36.4 (2022-07-20T12:10:17)
* 29b2653 Update OWNERS

## Release 0.36.3 (2022-07-11T17:04:39)
* e0b56ea :recycle: HouseKeeping: Updated OWNERS and pre-commit changes (#1267)
* 0564012 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment (#1266)
* fcd6755 🥹 moving @fridex in the OWNERS file, thanks for all the great work!!! (#1265)
* f177706 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 2a5d90b adding openshift function and schedule workflow for sync-job (#1260)
* 35e798c :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* 898a361 bump kubernetes version for common image
* 1f0cfe5 :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 0.36.2 (2022-04-12T14:30:11)
* f60c5ce Replace slash with dash in repo slug [scheduling mi workflows] (#1249)
* cc06aad Moving out the mypy as separate check
* d2b808b Update mypy config python version to 3.8
* 54c810c Fix pre-commit version to be ==2.15.0
* 53b4441 Update prow image tags
* 9c87ab5 Autoupdate pre-commit
* 11c303f :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* e0dc247 Send messages based on template defaults, do not hardcode (#1231)

## Release 0.36.1 (2022-03-14T15:17:12)
* Remove rfc5424-logging-handler from dependencies
* Remove venv import
* Make pre-commit happy
* Remove blank line:
* Add create_knowledge parameter, change workflow name

## Release 0.36.0 (2022-03-10T17:22:54)
* Add username to maintainers
* Remove [mypy-rfc5424logging] from mypy.ini
* Drop rfc5424logging and syslog
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment

## Release 0.35.0 (2022-02-11T09:41:07)
* Increase test timeout
* Allow passing dependency indexes to be checked for solver

## Release 0.34.1 (2022-02-09T06:05:03)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment (#1222)
* Fix parsing solver name for Python 3.10
* :fire: Fix the send_message assignment with default
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* Enable TLS verification

## Release 0.34.0 (2022-01-12T11:49:13)
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* if slug is None then param should not be passed
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* common project repo is not built into container image

## Release 0.33.1 (2022-01-05T14:28:46)
* Runtime environment entries can have labels associated

## Release 0.33.0 (2021-11-29T16:11:43)
* Fix typing for CPU and GPU properties
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* add kebechet to crossroads in docs
* :arrow_up: Automatic update of dependencies by Kebechet for the ubi8 environment
* increase pytest timeout
* add method to schedule thoth-repo-init workflow
* Move variables closer to each other
* Assign empty string if None
* Add merge path to schedule mi workflows
* :arrow_up: Automatic update of dependencies by Kebechet

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

## Release 0.16.0 (2020-07-30T08:22:35)
* :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.0 (#927)
* Rename srcopsmetrics to mi (#926)

## Release 0.16.1 (2020-08-17T19:56:11)
* Introduce raw specification parameter to be used when storing on Ceph (#936)
* Add long_description_content_type (#935)
* set source_type_enum None when soure_type not set (#932)
* :pushpin: Automatic update of dependency pytest from 6.0.0 to 6.0.1 (#934)
* :pushpin: Automatic update of dependency sentry-sdk from 0.16.2 to 0.16.3 (#933)
* :arrow_down: removed the files as they are no longer required

## Release 0.17.0 (2020-08-27T18:27:21)
### Features
* Add a routine for obtaining logs from workflow nodes
* Remove IMAGE_STREAM_NAMESPACE env (#941)
### Automatic Updates
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.2 to 0.7.0 (#946)
* :pushpin: Automatic update of dependency pylint from 2.5.3 to 2.6.0 (#945)
* :pushpin: Automatic update of dependency attrs from 19.3.0 to 20.1.0 (#944)
* :pushpin: Automatic update of dependency attrs from 19.3.0 to 20.1.0 (#943)

## Release 0.17.1 (2020-09-01T13:34:45)
### Features
* Introduce a way to parametrize adviser's predictor (#955)
* Provide cached Python package version tuple (#918)
### Automatic Updates
* :pushpin: Automatic update of dependency sentry-sdk from 0.16.5 to 0.17.2 (#957)

## Release 0.17.2 (2020-09-01T14:42:25)
### Features
* Allow users to pick predictor to be used (#959)

## Release 0.17.3 (2020-09-08T13:00:16)
### Features
* Do not propagate private attribute in to_doct() method
* Provenance checks should be scheduled in backend namespace
* Hide default predictor name (#963)
* Add Thoth's template for PRs (#964)
### Improvements
* Add more information related to invalid response size (#962)

## Release 0.18.0 (2020-09-10T08:58:20)
### Features
* Provide a method for obtaining a link to justification description (#971)
### Automatic Updates
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.3 to 0.17.4 (#973)
* :pushpin: Automatic update of dependency attrs from 20.1.0 to 20.2.0 (#969)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.2 to 0.17.3 (#968)

## Release 0.18.1 (2020-09-10T14:00:08)
### Features
* Make links to justifications shorter so they fit to terminal output (#975)

## Release 0.18.2 (2020-09-11T14:22:22)
### Features
* thamos->qebhwt for workflow name (#978)

## Release 0.18.3 (2020-09-11T23:08:54)
### Features
* add option to pass job_id so we can return it in user-api (#982)
* No need to provide html suffix (#981)

## Release 0.19.0 (2020-09-15T08:48:51)
### Features
* Fix predictor config propagation when scheduling adviser
* only get pending workflows
* make count a simple library call
* add sleep
* add optional limit for workflows

## Release 0.20.0 (2020-09-23T19:47:43)
### Features
* Update versions for compatibility between Argo, Kuberneter and Openshift (#998)
* Rely on S2I specific environment variable, no OpenShift build env vars (#994)
* Improve message logged when obtaining wf node log from cluster fails
### Bug Fixes
* fix pre-commit for common (#996)
### Automatic Updates
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.5 to 0.17.6 (#995)

## Release 0.20.1 (2020-10-09T15:31:44)
### Features
* Qebhwt needs deployment name (#1010)
### Automatic Updates
* :pushpin: Automatic update of dependency pytest from 6.0.2 to 6.1.1 (#1008)
* :pushpin: Automatic update of dependency pytest from 6.0.2 to 6.1.1 (#1006)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.8 to 0.18.0 (#1005)

## Release 0.20.2 (2020-10-20T09:30:52)
### Features
* check if workflow has started (#1017)
* Added method to initiate kebechet run-url workflow (#1013)
### Automatic Updates
* :pushpin: Automatic update of dependency sentry-sdk from 0.19.0 to 0.19.1 (#1018)
* :pushpin: Automatic update of dependency mypy from 0.782 to 0.790 (#1016)
* :pushpin: Automatic update of dependency sentry-sdk from 0.18.0 to 0.19.0 (#1015)

## Release 0.20.3 (2020-10-23T15:23:15)
### Features
* Added method to call kebechet admin workflow (#1021)

## Release 0.20.4 (2020-10-29T17:48:45)
### Bug Fixes
* Turn missing env variable warning into an error (#1024)

## Release 0.20.5 (2020-11-23T08:43:46)
### Features
* schedule graph sync workflow (#1028)
* get workflow node status (#1007)
### Other
* Move openshift related code from mi-scheduler (#1037)
### Automatic Updates
* :pushpin: Automatic update of dependency argo-workflows from 3.5.1 to 3.6.0 (#1038)
* :pushpin: Automatic update of dependency pytest-mypy from 0.7.0 to 0.8.0 (#1035)
* :pushpin: Automatic update of dependency sentry-sdk from 0.19.2 to 0.19.3 (#1034)
* :pushpin: Automatic update of dependency requests from 2.24.0 to 2.25.0 (#1033)
* :pushpin: Automatic update of dependency daiquiri from 2.1.1 to 3.0.0 (#1032)
* :pushpin: Automatic update of dependency attrs from 20.2.0 to 20.3.0 (#1030)
* :pushpin: Automatic update of dependency sentry-sdk from 0.19.1 to 0.19.2 (#1029)

## Release 0.20.6 (2020-11-30T18:26:00)
### Features
* Release of version 0.20.5 (#1041)

## Release 0.21.0 (2021-01-05T17:17:53)
### Features
* :arrow_up: Automatic update of dependencies by kebechet. (#1063)
* Move normalization functions to helpers (#1060)
* Bump black version
* included issue template to release missing module (#1055)
* add .aicoe-ci.yaml
* bump python version
### Improvements
* Add submit and schedule kebechet methods (#1054)

## Release 0.21.1 (2021-01-05T19:08:30)
### Features
* Remove AttrDict from requirements (#1066)

## Release 0.21.4 (2021-01-14T09:12:03)
### Features
* Provide additional build-analysis metadata so documents are traceable (#1085)
* Provide image metadata for package-extract (#1083)
* Add method to schedule graph-update-schema job (#1052)
* Version 0.21.3
* Extend parameters supplied to build analysis (#1076)
* Propagate build log document id to build analysis workflow (#1073)
* Increase random bits used to distinguish workflows (#1069)
* Release of version 0.21.1 (#1068)
* Remove AttrDict from requirements (#1066)
* Release of version 0.21.0 (#1065)
* :arrow_up: Automatic update of dependencies by kebechet. (#1063)
* Move normalization functions to helpers (#1060)
* Bump black version
* included issue template to release missing module (#1055)
* add .aicoe-ci.yaml
* bump python version
* Release of version 0.20.6 (#1049)
* Release of version 0.20.5 (#1041)
* Pin argo-workflows to a version before 4 (#1043)
* schedule graph sync workflow (#1028)
* get workflow node status (#1007)
* Release of version 0.20.4 (#1027)
* Release of version 0.20.3 (#1023)
* Added method to call kebechet admin workflow (#1021)
* Release of version 0.20.2 (#1020)
* check if workflow has started (#1017)
* Added method to initiate kebechet run-url workflow (#1013)
* Release of version 0.20.1 (#1012)
* Qebhwt needs deployment name (#1010)
* Release of version 0.20.0 (#1003)
* Update versions for compatibility between Argo, Kuberneter and Openshift (#998)
* Rely on S2I specific environment variable, no OpenShift build env vars (#994)
* Improve message logged when obtaining wf node log from cluster fails
* Release of version 0.19.0 (#991)
* Fix predictor config propagation when scheduling adviser
* only get pending workflows
* Release of version 0.18.3 (#985)
* add option to pass job_id so we can return it in user-api (#982)
* No need to provide html suffix (#981)
* Release of version 0.18.2 (#980)
* thamos->qebhwt for workflow name (#978)
* Release of version 0.18.1
* Make links to justifications shorter so they fit to terminal output (#975)
* Release of version 0.18.0 (#974)
* Provide a method for obtaining a link to justification description (#971)
* Release of version 0.17.3
* Do not propagate private attribute in to_doct() method
* Provenance checks should be scheduled in backend namespace
* Hide default predictor name (#963)
* Add Thoth's template for PRs (#964)
* Release of version 0.17.2 (#961)
* Allow users to pick predictor to be used (#959)
* Release of version 0.17.1 (#958)
* Introduce a way to parametrize adviser's predictor (#955)
* make count a simple library call
* Provide cached Python package version tuple (#918)
* Fix typing
* Release of version 0.17.0
* add sleep
* Add a routine for obtaining logs from workflow nodes
* add optional limit for workflows
* Remove IMAGE_STREAM_NAMESPACE env (#941)
* Release of version 0.16.1 (#940)
* Add long_description_content_type (#935)
* Release of version 0.16.0 (#929)
* Rename srcopsmetrics to mi (#926)
* Release of version 0.15.0 (#923)
* Added workflow status wrapper (#919)
* Do not limit latest versions on adviser runs (#917)
* Release of version 0.14.2 (#913)
* Parsing solver names can be a class method (#908)
* Introduce reverse solver workflow (#907)
* Add parameter to trigger reverse solver run (#906)
* Release of version 0.14.1 (#904)
* Use singular (#901)
* Add methods to schedule SI workflow (#900)
* Release of version 0.14.0 (#899)
* Always supply pipeline configuration for dependency monkey (#897)
* Package extract now does not need output to result-api (#896)
* Update OWNERS
* Update OWNERS
* Drop remaning workload-operator bits
* Update OWNERS
* Remove package analyzer job
* Introduce provenance-checker Argo workflow
* Use Argo workflows for package-extract
* Reformat using black
* Introduce build analysis workflow
* Remove graph sync jobs
* Release of version 0.13.13
* Fixed precommit
* Update OWNERS
* Adjust signature - return value
* some reformatting
* :ambulance: some reformatting
* Make pipeline configuration optional
* The schedule method of dependency monkey now accepts only Pipfile
* Schedule Dependency Monkey using Argo workflows
* pre-commit
* Remove variable not required
* Remove build dependencies component
* Accept alternative datetime format string used by PyPI
* Correct serialization of Enum
* Release of version 0.13.12
* move Lazy to common helpers from python helpers
* Release of version 0.13.11
* Add sesheta as a maintainer
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
* Ignore unused import
* add submit and schedule methods for SI's
* :sparkles: standard pre-commit-config
* Setup Sentry traces sample rate
* added a 'tekton trigger tag_release pipeline issue'
* Release of version 0.13.8
* add missing import
* adjust config
* Be consistent
* move type: ignore
* only change pre-commit config
* Release of version 0.13.7
* make output in solve optional
* Release of version 0.13.6
* Missing self
* Release of version 0.13.5
* Introduce logic for solver
* Release of version 0.13.4
* Add missing parameters
* Correct docstring
* New check method for Qeb-HWt inputs
* Use name
* Add check for Thoth integration
* Add exception for integrations
* import auto
* Add exception for integrations
* Use solvers ConfigMap
* Adjust enums
* Add enum to init
* Add TODO
* Release of version 0.13.3
* all the github standard templates
* :pushpin: Automatic dependency re-locking
* :pushpin: Automatic dependency re-locking
* Quote unknown configuration entries
* Release of version 0.13.2
* Little adjustments
* Changed parameter type
* Moved json serialization
* Release of version 0.13.1
* Renamed to kebechet
* Release of version 0.13.0
* Added workflow functions
* Release of version 0.12.10
* Provide platform in Thoth's runtime environment config option
* Release of version 0.12.9
* Remove assignment of the Dockerfile
* Remove parallelism and allowed failures configuration
* Release of version 0.12.8
* :nut_and_bolt: provide imagestream name while processing template
* Release of version 0.12.7
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
* Release of version 0.10.12
* Add empty env template
* Remove again lines
* Reintroduce wf id
* Adjust solver workflows ID
* Add warning
* Removed unnecessary assignment
* Refactor get_workflow
* Allow to get_workflow by name
* Do not implicitly modify Workflow name
* Return adviser_id instead of workflow_id
* Move env variables to right place
* Introduce Schedule inspection method in Openshift Class
* Release of version 0.10.11
* Introduce method to assign workflow parameters
* Add variables for Ceph for adviser workflows
* Generalize variables for Ceph storage for workflow
* Add method to check workflow parameters
* Generalize variables for Ceph storage for workflow
* Adjust .thoth.yaml
* Release of version 0.10.10
* Adjust inputs for solvers
* Release of version 0.10.9
* Migrate method to be used for Argo
* Release of version 0.10.8
* Correct datatype
* Changed `nodes` -> `pods` in job status report
* Changed Job status report according to Amun API
* Missing metadata parameters
* Release of version 0.10.7
* Release of version 0.10.6
* Fix check for default value in workflow template
* Return directly result
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
* Release of version 0.10.2
* Release of version 0.10.1
* Add host parameter for Thamos GitHub App
* function to sync build analyzers report
* Release of version 0.10.0
* Extend parameters for Adviser
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
* Added before send filter
* Experiment logging
* Experiment logging
* Release of version 0.9.29
* Rename template used by workload opeartor
* Correct solver id input
* Release of version 0.9.28
* Use thoth.common as a root logger for logging information
* Release of version 0.9.27
* Solver runs with Argo workflows
* Release of version 0.9.26
* remove wrong default value to run Dependency Monkey
* Release of version 0.9.25
* Enable providing pipeline configuration to Dependency Monkey
* Release of version 0.9.24
* Fix decision type environment variable name
* Add missing argument to dependency monkey runs
* Pass OpenShift instance instead of dynamic client to workflow manager
* Fix relative import issue
* adjust-code
* Add env variable to select type of scheduling
* Migrate to workflow for Adviser
* Release of version 0.9.23
* Schedule adviser workflow
* Be more aggressive with busy wait
* Busy wait on configmap creation to make sure cm gets propagated in the cluster
* Happy new year!
* Release of version 0.9.22
* Add Thamos documentation
* Add is_s2i flag to adviser scheduling
* Point documentation to other libraries
* Introduce a generic logger adjustment
* Add Google Analytics
* Change Sphinx theme
* Release of version 0.9.21
* Sentry's aiohttp integration is supported only for Python 3.7+
* Release of version 0.9.20
* Use 8 random digits in the ID instead of 16
* Inspection Workflow template is stored in amun infra
* Fixed ResourceNotUniqueError in get_solver_names
* Fixed accessor to amun_infra_namespace attribute
* Allow for different workflow and template namespaces
* Release of version 0.9.19
* Fix testsuite
* Release of version 0.9.18
* Release of version 0.9.17
* :pushpin: Relock
* Make workflow management publicly consumable
* Propagate document id into templates
* Add configuration of ignored loggers
* Imlicitly assign workflow ID to the workflow name
* Sanitize workflow before submitting
* Process inspection template before retrieval
* Add few notes about logging to the README file
* Print integrations to log
* Update README file
* Enable Sentry integrations
* Move data related files to tests/data dir
* Generate workflow ID by the unified `generate_id`
* Refactorings
* Fixed typing issues
* Return Workflow ID on submission
* Fix coala issues
* :pushpin: Lock dependencies for Argo
* Added missing flexmock dependency to the Pipfile
* Added deserialization of Workflow
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
* Fix boolean types in mypy.ini
* Release of version 0.9.14
* Propagate is_external flag to package-extract runs
* Release of version 0.9.13
* Release of version 0.9.12
* Add warnings when there is something fishy in environment configuration for logging
* Always log in UTC to be consistent with team members all over the world
* Fix missing bracket
* Refactor out scheduling graph syncs
* Drop subgraph check
* Release of version 0.9.11
* Release of version 0.9.10
* Hotfix for errors when getting solver templates
* Release of version 0.9.9
* Schedule solvers without transitive flag being set
* Add dry-run to package-analyzer
* Be consistent with solver type labels
* Release of version 0.9.8
* Do not pin to a specific Kubernetes release
* Release of version 0.9.7
* As we use Thoth to resolve dependencies, stop using extras
* Leftover parameter from copy paste
* Release of version 0.9.6
* Add template as optional param
* New function to count jobs per status per label
* Release of version 0.9.5
* :sunrise: Modified the names to standard convention
* Release of version 0.9.4
* openshift scheduler job for package analyzer
* Release of version 0.9.3
* Increase maximum lines per file
* :sunglasses: Support for build analysers scheduling
* Release of version 0.9.2
* Fix wrong argument handling
* Copy paste remnants
* Increase maximum lines
* Conditional statement
* Subcommand env
* Introduce graph sync multiple
* Release of version 0.9.1
* Provide method for scheduling graph-refresh on demand
* Release of version 0.9.0
* Release of version 0.8.11
* Fix solver temlate handling
* Release of version 0.8.10
* Implement Sentry environment
* Release of version 0.8.9
* Release of version 0.8.8
* Release of version 0.8.7
* Provide default for limit latest versions
* Release of version 0.8.6
* Ensure recommendation type is in upper case
* Propagate library usage to adviser runs
* Add missing requests library to requirements
* Release of version 0.8.5
* Release of version 0.8.4
* Obtain templates from Amun infra for Amun specific templates
* Release of version 0.8.3
* Release of version 0.8.2
* Add Thoth's configuration file
* Fix serialization of runtime environment
* Propagate metadata about runtime and buildtime environment
* Release of version 0.8.1
* Finding the right OpenShift version
* Lock Kubernetes and OpenShift to specific version
* Adjust heading
* Use Sphinx for documentation
* Use safe_load() instead of load()
* Release of version 0.8.0
* Introduce limit latest versions parameter
* Update .coafile
* Propagate origin as metadata
* Add format_datetime method to convert datetimes
* Release of version 0.7.1
* Add missing MANIFEST.in
* Release of version 0.7.0
* Propagate document ID into graph-sync job name
* Address coala complains
* Check for ConfigMap presence to report registered workload to user
* Runtime environment can be set to None
* Add check for runtime environment name
* Optionally provide dict representation without none values
* Load runtime environment transparently from YAML/JSON file
* Also install the missing config module
* Introduce runtime environment abstractions
* Release of version 0.6.0
* Revert "A temporary workaround for workload management"
* Parse requests for build workload
* Label workload to allow type specific queries
* Fix in template gathering for inspection build
* Treat builds as workload
* Propagate graph-sync job id into template
* Explicitly assign inspection requests
* Fix how amun and thoth infra namespace is handled
* Fix more coala issues
* Fix coala errors
* Amun does not use Thoth's infra namespace
* Add routine for scheduling all registered solvers
* Check running workload based on quota
* Add routines for workload operator
* Enable local development for OpenShift client
* Reformat using black
* Add missing guards for scheduling routines
* Move Amun specific pieces to OpenShift class
* Workload operator expects method, not method_name
* Remove self from propagated parameters to configmap
* Introduce schedule methods for workload operator
* Reformant using black
* Extend log messages with a line number
* Report template parameters in debug mode
* Make limit and count optional parameters for adviser template
* Release of version 0.5.0
* Dependency monkey can accept a serialized JSON representing Pipfile
* Propagate count to dependency monkey runs
* Solver now accepts subgraph check API parameter
* Release of version 0.4.7
* Add long description for PyPI
* Supply whitelisted sources to provenance checks
* Adjust force sync to respect implementation
* Release of version 0.4.6
* Runtime environment is now a dict
* Release of version 0.4.5
* Release of version 0.4.4
* Fix CI
* Rename dependency monkey limit to respect its semantics
* Release of version 0.4.3
* Introduce method for getting build in a namespace
* Release of version 0.4.2
* Add count parameter to dependency monkey
* Release of version 0.4.1
* Propagate dependency monkey parameters to template
* Use api version from template
* Release of version 0.4.0
* Introduce method for creating datetime from timestamp
* Release of version 0.3.16
* Fix missing import
* Make CI happy again
* Release of version 0.3.15
* Make all datetimes timezone aware
* using thoht-* jobs now
* Do not propagate force to actual package-extract run
* Release of version 0.3.14
* Release of version 0.3.13
* added parameter force:bool, why was it missing?
* add InClusterConfigLoader to load SA and cert
* using the correct api
* Release of version 0.3.12
* added get_jobs(), it will be used for thoth-metrics
* Default to now if no datetime was provided
* Release of version 0.3.11
* Fix syntax error
* Release of version 0.3.10
* Add message to translate table
* Release of version 0.3.9
* Release of version 0.3.8
* Fix gathering pod id from job name
* Release of version 0.3.7
* Add routines for jobs handling
* Gather build logs from OpenShift
* Allow explicitly specifying the logging configuration prefix
* Release of version 0.3.6
* Release of version 0.3.5
* Release of version 0.3.4
* Release of version 0.3.3
* Release of version 0.3.2
* Initial dependency lock
* Add Sentry support
* Unify pod status reports
* Treat None parameter values as empty values
* Release of version 0.3.1
* added github configuration
* Fix built-in type shadowing
* Release of version 0.3.0
* Issue warning on suspicious parameter expansion in templates
* Fix gathering pod status for default middletier namespace
* Release of version 0.2.7
* Fix default TLS verification behavior
* Introduce routine for running provenance checker
* Release of version 0.2.6
* Initial dependency lock
* change the queue
* change the queue
* Fix TLS/SSL certification verification configuration
* Release of version 0.2.5
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
* Update .zuul.yaml
* Release of version 0.2.2
* Allow completely suppressing logs
* releasing 0.2.1
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
* added the gate pipeline to the core queue
* releasing 0.0.8
* uploading to production pypi now... using sesheta account
* trigger
* preparing release 0.0.8: Zuul
* Version 0.0.7
* Change in Indentation
* Fix logging issues
* added daiquiri
* Setup logging for root logger
* Testing dependencies
* Version 0.0.6
* Add support for rsyslog logging endpoint
* Run coala in non-interactive mode
* Run coala in CI
* Create OWNERS
* Remove dependencies.yml
* Add missing headers to files
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
### Bug Fixes
* Turn missing env variable warning into an error (#1024)
* fix pre-commit for common (#996)
* Introduce raw specification parameter to be used when storing on Ceph (#936)
* set source_type_enum None when soure_type not set (#932)
* Source type enum fix
* Remove report output, it is placed on Ceph by Argo
* mypy typing error introduced in another commit
* move import to fix circular dependency issue
* Fix issue with returning None instead of workflow id
* Modify logic of get_solver_names not to depend on Openshift template
* Fix multiple spaces after operator
* Remove prefix to avoid error in Thoth components
* Raise not found error if configmap was not found
* Correct bug in one function
* Updated randbits to fix #568
* Library fixes
* Fix error due to ambiguous template resources
* fixed W391 blank line at end of file
* Improve error message shown when getting cluster resources
* Coala fixes
* minor fix of error msg
* :bug: minor fix for correct namespace
* Minor fix to display correct release in title of docs html
* fixed the log message
* fixed some coala errors
* Do not consider nested none values in output if with_none is false
* Fix issues when template does not request any resources
* Report error if sentry initialization fails
* Fix undefined name error
* Raise appropriate not found exception exception
* fixed another typo
* fixed a few typos
* fixed the typo, this closes #114
* Report scheduling status if pod was not initialized yet
* Report back empty pod status is pod is being scheduled
* Configure SSL/TLS correctly when communicating with master
* Fix syntax error in logging
* fixed trailing space issue
* fixed some coala errors
### Improvements
* removed bissenbay, thanks for your contributions!
* Add submit and schedule kebechet methods (#1054)
* Add more information related to invalid response size (#962)
* :arrow_down: removed the files as they are no longer required
* Remove unused env variable (#916)
* Make methods static (#909)
* Drop legacy workload operator, use only Argo workflows
* Remove kebechet jobs they are now part of workflows
* remove default index
* Fixed mypy and black
* No default package index
* use middletier namespace
* Introudce method for verifying Kebechet inputs
* wrong function name and use enum.name
* use strings to indicate futures
* rename base test
* typing checks, docstrings, test renamed
* rename method
* Add source type for Thoth adviser integrations
* Add status analysis and make label selector optional
* Adjust name of method
* New methods to monitor Argo workflows
* Propagate requests and limits for inspection run and build
* Correct default and typo
* We don't use threads, do not log info about them
* remove unused env variables
* Remove old methods to schedule inspections
* Adjust Pipfile and Pipfile.lock
* Added get_workflow_status method
* Handle debug parameter for adviser in argo workflows
* Openshift methods for inspection workflows
* Always use Argo for thamos workflow
* Simplfiy condition, do not use nested if
* Make decision type and recommendation type lowercase
* :sparkles: added pre-commit and did a little bit of coala cleanup
* Try to avoid timing issues between job and configmap creation
* I had to do it... it was so annoying
* correct namespace use
* Added methods to submit inspection workflows
* Move workflows tests to the tests/ folder
* Reduce complexity of _submit_workflow method
* Sanitize for serialization and validate by default
* Implement Workflow.from_file method
* Start using mypy for type checking
* Fix method name to comply with other methods
* relocked dependencies, cleaned up the coala deps
* Changed env variable names
* Broke up run and schedule for stable api
* :arrow_double_up: Increase the limit for file line size
* New function for all ConfigMaps
* Logic to run and schedule kebechet builds
* Fix retrieving pod logs - use OpenShift API
* Supply environment variable for registry and infra namespace for inspections
* Fix inspection and inspect bad interpretation
* :recycle: refactored retrieval of template to OpenShift._get_template(label_selector)
* Add getter to default datetime format
* Graph syncs are unique per document id, no need to have long ids
* Do not pin down openshift and kubernetes, let consumers do it if needed
* Remove unused entry
* Introduce name and rename hardware_information to hardware
* Introduce method for scheduling adviser graph syncs
* A temporary workaround for workload management
* Disable urllib3 warnings
* Fix seed environment name typo
* Provide sugar methods for scheduling graph sync
* Make run methods optional
* Assing memory and cpu requests when getting template
* Fix incorrect namespace usage one more time
* Fix incorrect use of infra namespace
* Serialize parameters into JSON when adding to ConfigMap
* Fix env variable typo
* Propagate index urls into solver runs
* Introduce method for gathering buildconfigs
* Introduce count and limit for adviser
* refactor methods into pythonic way
* Return None if there are no pod logs yet
* Make reusable methods public
* Introduce methods for running dependency monkey
* Let's reuse adviser env var names
* Fix propagating debug flag to package-extract
* Fix gathering pod logs for default middletier namespace
* Change in Indentation and variable names
* Generic wrappers to define verbose level on every method
* Disable annoying unverified HTTPS warnings
* Fix typo in docstring
* A temporary dependency downgrade to test kebechet
### Non-functional
* Remove a temporary dependency for kebechet testing
### Other
* Move openshift related code from mi-scheduler (#1037)
* Reformat code using black
* remove coala from zuul
* Missing self in methods
* remove method
* remove is_s2i flag
* Use coala for code checks
### Automatic Updates
* :pushpin: Automatic update of dependency argo-workflows from 3.5.1 to 3.6.0 (#1038)
* :pushpin: Automatic update of dependency pytest-mypy from 0.7.0 to 0.8.0 (#1035)
* :pushpin: Automatic update of dependency sentry-sdk from 0.19.2 to 0.19.3 (#1034)
* :pushpin: Automatic update of dependency requests from 2.24.0 to 2.25.0 (#1033)
* :pushpin: Automatic update of dependency daiquiri from 2.1.1 to 3.0.0 (#1032)
* :pushpin: Automatic update of dependency attrs from 20.2.0 to 20.3.0 (#1030)
* :pushpin: Automatic update of dependency sentry-sdk from 0.19.1 to 0.19.2 (#1029)
* :pushpin: Automatic update of dependency pytest from 6.1.1 to 6.1.2 (#1026)
* :pushpin: Automatic update of dependency sentry-sdk from 0.19.0 to 0.19.1 (#1018)
* :pushpin: Automatic update of dependency mypy from 0.782 to 0.790 (#1016)
* :pushpin: Automatic update of dependency sentry-sdk from 0.18.0 to 0.19.0 (#1015)
* :pushpin: Automatic update of dependency pytest from 6.0.2 to 6.1.1 (#1008)
* :pushpin: Automatic update of dependency pytest from 6.0.2 to 6.1.1 (#1006)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.8 to 0.18.0 (#1005)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.7 to 0.17.8 (#1002)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.5 to 0.17.6 (#995)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.4 to 0.17.5 (#989)
* :pushpin: Automatic update of dependency pytest from 6.0.1 to 6.0.2 (#984)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.3 to 0.17.4 (#973)
* :pushpin: Automatic update of dependency attrs from 20.1.0 to 20.2.0 (#969)
* :pushpin: Automatic update of dependency sentry-sdk from 0.17.2 to 0.17.3 (#968)
* :pushpin: Automatic update of dependency sentry-sdk from 0.16.5 to 0.17.2 (#957)
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.2 to 0.7.0 (#946)
* :pushpin: Automatic update of dependency pylint from 2.5.3 to 2.6.0 (#945)
* :pushpin: Automatic update of dependency attrs from 19.3.0 to 20.1.0 (#944)
* :pushpin: Automatic update of dependency attrs from 19.3.0 to 20.1.0 (#943)
* :pushpin: Automatic update of dependency sentry-sdk from 0.16.3 to 0.16.5 (#937)
* :pushpin: Automatic update of dependency pytest-cov from 2.10.0 to 2.10.1 (#938)
* :pushpin: Automatic update of dependency pytest from 6.0.0 to 6.0.1 (#934)
* :pushpin: Automatic update of dependency sentry-sdk from 0.16.2 to 0.16.3 (#933)
* :pushpin: Automatic update of dependency pytest from 5.4.3 to 6.0.0 (#927)
* :pushpin: Automatic update of dependency jsonformatter from 0.2.3 to 0.3.0 (#922)
* :pushpin: Automatic update of dependency sentry-sdk from 0.16.1 to 0.16.2 (#921)
* :pushpin: Automatic update of dependency pytest-timeout from 1.4.1 to 1.4.2 (#912)
* :pushpin: Automatic update of dependency sentry-sdk from 0.16.0 to 0.16.1 (#911)
* :pushpin: Automatic update of dependency sentry-sdk from 0.15.1 to 0.16.0 (#903)
* :pushpin: Automatic update of dependency mypy from 0.781 to 0.782
* :pushpin: Automatic update of dependency mypy from 0.780 to 0.781
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.4 to 0.15.1
* :pushpin: Automatic update of dependency requests from 2.23.0 to 2.24.0
* :pushpin: Automatic update of dependency pytest-cov from 2.9.0 to 2.10.0
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.4 to 1.4.1
* :pushpin: Automatic update of dependency pylint from 2.5.2 to 2.5.3
* :pushpin: Automatic update of dependency mypy from 0.770 to 0.780
* :pushpin: Automatic update of dependency pytest from 5.4.2 to 5.4.3
* :pushpin: Automatic update of dependency pytest-cov from 2.8.1 to 2.9.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.3 to 0.14.4
* :pushpin: Automatic update of dependency pytest from 5.4.1 to 5.4.2
* :pushpin: Automatic update of dependency pylint from 2.5.0 to 2.5.2
* :pushpin: Automatic update of dependency jsonformatter from 0.1.4 to 0.2.1
* :pushpin: Automatic update of dependency pylint from 2.4.4 to 2.5.0
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.1 to 0.6.2
* :pushpin: Automatic update of dependency pytest-mypy from 0.6.0 to 0.6.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.2 to 0.14.3
* :pushpin: Automatic update of dependency pytest from 5.3.5 to 5.4.1
* :pushpin: Automatic update of dependency pytest-mypy from 0.5.0 to 0.6.0
* :pushpin: Automatic update of dependency pyyaml from 5.3 to 3.13
* :pushpin: Automatic update of dependency openshift from 0.10.2 to 0.10.3
* :pushpin: Automatic update of dependency mypy from 0.761 to 0.770
* :pushpin: Automatic update of dependency pre-commit from 2.0.0 to 2.0.1
* :pushpin: Automatic update of dependency pytest from 5.3.4 to 5.3.5
* :pushpin: Automatic update of dependency pre-commit from 1.21.0 to 2.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.14.0 to 0.14.1
* :pushpin: Automatic update of dependency pytest from 5.3.3 to 5.3.4
* :pushpin: Automatic update of dependency pytest from 5.3.2 to 5.3.3
* :pushpin: Automatic update of dependency daiquiri from 1.6.1 to 2.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.5 to 0.14.0
* :pushpin: Automatic update of dependency pytest-timeout from 1.3.3 to 1.3.4
* :pushpin: Automatic update of dependency pyyaml from 5.2 to 5.3
* :pushpin: Automatic update of dependency mypy from 0.760 to 0.761
* :pushpin: Automatic update of dependency argo-workflows from 2.1.3 to 2.1.4
* :pushpin: Automatic update of dependency argo-workflows from 2.1.2 to 2.1.3
* :pushpin: Automatic update of dependency mypy from 0.750 to 0.760
* :pushpin: Automatic update of dependency daiquiri from 1.6.0 to 1.6.1
* :pushpin: Automatic update of dependency pytest from 5.3.1 to 5.3.2
* :pushpin: Automatic update of dependency openshift from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.4 to 0.13.5
* :pushpin: Automatic update of dependency pyyaml from 5.1.2 to 5.2
* :pushpin: Automatic update of dependency mypy from 0.740 to 0.750
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.3 to 0.13.4
* :pushpin: Automatic update of dependency pytest from 5.3.0 to 5.3.1
* :pushpin: Automatic update of dependency argo-workflows from 2.1.1 to 2.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.2 to 0.13.3
* :pushpin: Automatic update of dependency pytest from 5.2.4 to 5.3.0
* :pushpin: Automatic update of dependency argo-workflows from 2.1.0 to 2.1.1
* :pushpin: Automatic update of dependency pytest from 5.2.3 to 5.2.4
* :pushpin: Automatic update of dependency pytest from 5.2.2 to 5.2.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.1 to 0.13.2
* :pushpin: Automatic update of dependency pytest-mypy from 0.4.1 to 0.4.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.13.0 to 0.13.1
* :pushpin: Automatic update of dependency pytest from 5.2.1 to 5.2.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.3 to 0.13.0
* :pushpin: Automatic update of dependency attrs from 19.2.0 to 19.3.0
* :pushpin: Automatic update of dependency pytest from 5.2.0 to 5.2.1
* :pushpin: Automatic update of dependency pytest-cov from 2.8.0 to 2.8.1
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.2 to 0.12.3
* :pushpin: Automatic update of dependency attrs from 19.1.0 to 19.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.1 to 2.4.2
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.0
* :pushpin: Automatic update of dependency pylint from 2.4.0 to 2.4.1
* :pushpin: Automatic update of dependency pylint from 2.3.1 to 2.4.0
* :pushpin: Automatic update of dependency pytest from 5.1.2 to 5.1.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.1 to 0.12.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.12.0 to 0.12.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.2 to 0.12.0
* :pushpin: Automatic update of dependency pytest from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.1 to 0.11.2
* :pushpin: Automatic update of dependency pytest from 5.1.0 to 5.1.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.11.0 to 0.11.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.2 to 0.11.0
* :pushpin: Automatic update of dependency pytest from 5.0.1 to 5.1.0
* :pushpin: Automatic update of dependency daiquiri from 1.5.0 to 1.6.0
* :pushpin: Automatic update of dependency pyyaml from 5.1.1 to 5.1.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.1 to 0.10.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.10.0 to 0.10.1
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.5 to 0.10.0
* :pushpin: Automatic update of dependency pytest from 5.0.0 to 5.0.1
* :pushpin: Automatic update of dependency pytest from 4.6.3 to 5.0.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.4 to 0.9.5
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.3 to 0.9.4
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.2 to 0.9.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.1 to 0.9.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.9.0 to 0.9.1
* :pushpin: Automatic update of dependency pytest from 4.6.2 to 4.6.3
* :pushpin: Automatic update of dependency pyyaml from 5.1 to 5.1.1
* :pushpin: Automatic update of dependency pytest from 4.5.0 to 4.6.2
* :pushpin: Automatic update of dependency sentry-sdk from 0.8.0 to 0.9.0
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.2 to 1.4.3
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.14 to 0.8.0
* :pushpin: Automatic update of dependency requests from 2.21.0 to 2.22.0
* :pushpin: Automatic update of dependency pytest from 4.4.2 to 4.5.0
* :pushpin: Automatic update of dependency pytest from 4.4.1 to 4.4.2
* :pushpin: Automatic update of dependency pytest-cov from 2.7.0 to 2.7.1
* :pushpin: Automatic update of dependency pytest-cov from 2.6.1 to 2.7.0
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.13 to 0.7.14
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.12 to 0.7.13
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.11 to 0.7.12
* :pushpin: Automatic update of dependency sentry-sdk from 0.7.10 to 0.7.11
* :pushpin: Automatic update of dependency pytest from 4.4.0 to 4.4.1
* :pushpin: Automatic update of dependency rfc5424-logging-handler from 1.4.1 to 1.4.2
* Automatic update of dependency sentry-sdk from 0.7.9 to 0.7.10
* Automatic update of dependency pytest from 4.3.1 to 4.4.0
* Automatic update of dependency sentry-sdk from 0.7.8 to 0.7.9
* Automatic update of dependency sentry-sdk from 0.7.7 to 0.7.8
* Automatic update of dependency sentry-sdk from 0.7.6 to 0.7.7
* Automatic update of dependency pyyaml from 3.13 to 5.1
* Automatic update of dependency pylint from 2.3.0 to 2.3.1
* Automatic update of dependency pytest from 4.3.0 to 4.3.1
* Automatic update of dependency attrs from 18.2.0 to 19.1.0
* Automatic update of dependency sentry-sdk from 0.7.4 to 0.7.6
* Automatic update of dependency pylint from 2.2.2 to 2.3.0
* Automatic update of dependency pytest from 4.2.1 to 4.3.0
* Automatic update of dependency openshift from 0.8.5 to 0.8.6
* Automatic update of dependency sentry-sdk from 0.7.2 to 0.7.4
* Automatic update of dependency rfc5424-logging-handler from 1.4.0 to 1.4.1
* Automatic update of dependency openshift from 0.8.4 to 0.8.5
* Automatic update of dependency pytest from 4.2.0 to 4.2.1
* Automatic update of dependency pytest from 4.1.1 to 4.2.0
* Automatic update of dependency sentry-sdk from 0.6.9 to 0.7.2
* Automatic update of dependency rfc5424-logging-handler from 1.3.0 to 1.4.0
* Automatic update of dependency sentry-sdk from 0.6.6 to 0.6.9
* Automatic update of dependency sentry-sdk from 0.6.4 to 0.6.5
* Automatic update of dependency sentry-sdk from 0.6.3 to 0.6.4
* Automatic update of dependency sentry-sdk from 0.6.2 to 0.6.3
* Automatic update of dependency pytest from 4.0.1 to 4.0.2
* Automatic update of dependency requests from 2.20.1 to 2.21.0
* Automatic update of dependency sentry-sdk from 0.6.1 to 0.6.2
* Automatic update of dependency sentry-sdk from 0.6.0 to 0.6.1
* Automatic update of dependency sentry-sdk from 0.5.5 to 0.6.0
* Automatic update of dependency pylint from 2.2.1 to 2.2.2
* Automatic update of dependency pylint from 2.2.0 to 2.2.1
* Automatic update of dependency pylint from 2.1.1 to 2.2.0
* Automatic update of dependency pytest from 4.0.0 to 4.0.1
* Automatic update of dependency pytest-timeout from 1.3.2 to 1.3.3
* Automatic update of dependency sentry-sdk from 0.5.4 to 0.5.5
* Automatic update of dependency pytest from 3.10.1 to 4.0.0
* Automatic update of dependency pytest from 3.10.0 to 3.10.1
* Automatic update of dependency sentry-sdk from 0.5.3 to 0.5.4
* Automatic update of dependency requests from 2.20.0 to 2.20.1
* Automatic update of dependency sentry-sdk from 0.5.2 to 0.5.3
* Automatic update of dependency pytest from 3.9.3 to 3.10.0
* Automatic update of dependency sentry-sdk from 0.5.1 to 0.5.2
* Automatic update of dependency pytest from 3.9.2 to 3.9.3
* Automatic update of dependency sentry-sdk from 0.5.0 to 0.5.1
* Automatic update of dependency sentry-sdk from 0.4.3 to 0.5.0
* Automatic update of dependency pytest from 3.9.1 to 3.9.2
* Automatic update of dependency rfc5424-logging-handler from 1.2.1 to 1.3.0
* Automatic update of dependency sentry-sdk from 0.4.2 to 0.4.3
* Automatic update of dependency requests from 2.19.1 to 2.20.0
* Automatic update of dependency sentry-sdk from 0.4.1 to 0.4.2
* Automatic update of dependency pytest from 3.8.2 to 3.9.1
* Automatic update of dependency sentry-sdk from 0.4.0 to 0.4.1
* Automatic update of dependency sentry-sdk from 0.3.11 to 0.4.0
* Automatic update of dependency sentry-sdk from 0.3.9 to 0.3.11
* Automatic update of dependency sentry-sdk from 0.3.8 to 0.3.9
* Automatic update of dependency pytest from 3.8.1 to 3.8.2
* Automatic update of dependency sentry-sdk from 0.3.7 to 0.3.8
* Automatic update of dependency sentry-sdk from 0.3.6 to 0.3.7
* Automatic update of dependency sentry-sdk from 0.3.5 to 0.3.6
* Automatic update of dependency pytest from 3.8.0 to 3.8.1
* Automatic update of dependency rfc5424-logging-handler from 1.1.2 to 1.2.1
* Automatic update of dependency pytest from 3.7.4 to 3.8.0
* Automatic update of dependency pytest-cov from 2.5.1 to 2.6.0
* Automatic update of dependency pytest-timeout from 1.3.1 to 1.3.2
* Automatic update of dependency pytest from 3.7.1 to 3.7.3
* Automatic update of dependency pylint from 2.1.0 to 2.1.1
* Automatic update of dependency pytest from 3.7.0 to 3.7.1
* Automatic update of dependency pylint from 2.0.1 to 2.1.0
* Automatic update of dependency pytest from 3.6.4 to 3.7.0
* Automatic update of dependency pytest from 3.6.3 to 3.6.4
* Automatic update of dependency pylint from 1.9.2 to 2.0.1
* Automatic update of dependency pytest-timeout from 1.3.0 to 1.3.1
* Automatic update of dependency daiquiri from 1.3.0 to 1.5.0
* Automatic update of dependency thoth-storages from 0.0.26 to 0.0.28
* Automatic update of dependency rfc5424-logging-handler from 1.1.0 to 1.1.2

## Release 0.22.0 (2021-01-21T08:00:59)
### Features
* Extend Thamos configuration file (#1072)
* Revisit generating id to avoid hash collisions (#1093)
* :sparkles: add kind/ labels to feature and bug template (#1091)
* :arrow_up: Automatic update of dependencies by kebechet. (#1090)

## Release 0.22.1 (2021-02-02T22:28:54)
### Features
* Fix package-extract job id propagation (#1100)
* :arrow_up: Automatic update of dependencies by kebechet. (#1099)
* add enum for internal triggers (#1098)
* :arrow_up: Automatic update of dependencies by kebechet. (#1097)
* :arrow_up: Automatic update of dependencies by kebechet. (#1095)

## Release 0.23.0 (2021-02-05T07:24:32)
### Features
* run dependency monkey workload on the amun-inspection namespace (#1104)

## Release 0.24.0 (2021-02-22T13:15:53)
### Features
* Fix parsing runtime environment entries
* Fix obtaining pod status for workflows (#1113)
* :arrow_up: Automatic update of dependencies by Kebechet (#1114)
* Do not propagate request data via messaging (#1109)
* :arrow_up: Automatic update of dependencies by Kebechet (#1112)
* Thoth application#398 (#1111)
* :arrow_up: Automatic update of dependencies by Kebechet (#1110)
* Thoth application#398 (#1107)
### Improvements
* Add flag to optionally sync results of package-extract

## Release 0.24.1 (2021-02-24T11:03:04)
### Features
* Add empty commit to trigger a new release for thoth-common

## Release 0.24.2 (2021-03-01T20:46:19)
### Features
* Pin openshift to help Pipenv resolve the stack (#1126)
* :arrow_up: Automatic update of dependencies by Kebechet

## Release 0.25.0 (2021-03-04T19:02:56)
### Features
* pass slug to kebechet workflow (#1125)
* add metadata to relevant schedule methods (#1103)
* :arrow_up: Automatic update of dependencies by Kebechet (#1131)
* Add knowledge_path as parameter for schedule_mi_workflow (#1129)
### Improvements
* :sparkles: reconfgured CI/CD to use prow and aicoe-ci

## Release 0.26.0 (2021-03-08T19:40:01)
### Features
* thoth-adviser metadata

## Release 0.27.0 (2021-03-26T12:19:01)
### Features
* Be consistent with env vars supplied (#1143)
* :arrow_up: Automatic update of dependencies by Kebechet (#1142)
* Add additional configuration as parameter (#1141)

## Release 0.28.0 (2021-03-31T18:28:38)
### Features
* Allow running authenticated provenance check (#1147)
* :arrow_up: Automatic update of dependencies by Kebechet (#1148)
* Provide an argument to run authenticated advises (#1146)

## Release 0.29.0 (2021-05-05T19:22:28)
### Features
* Make graph namespace available to the OpenShift adapter (#1155)
* :arrow_up: Automatic update of dependencies by Kebechet (#1154)
* Mi/feature/merge (#1153)
### Improvements
* Introduce methods for scheduling purge workflow (#1152)
### Non-functional
* Minor improvements to docs (#1151)

## Release 0.29.1 (2021-05-05T19:52:59)
### Features
* Run purge workflows in middletier namespace (#1158)

## Release 0.30.0 (2021-06-10T20:33:52)
### Features
* Add thoth.common to mypy.ini
* Provide force_sync to solver schedule methods
* :hatched_chick: update the prow resource limits (#1163)

## Release 0.31.0 (2021-07-01T18:51:47)
### Features
* Remove from adviser method
* :medal_sports: set badges for easy access to content (#1175)
* :arrow_up: Automatic update of dependencies by Kebechet (#1168)
### Bug Fixes
* :arrow_up: updating the pytest fixes
### Improvements
* use numbers in enums
* Use explicit values for enums
* Remove qeb-hwt and github-app bits

## Release 0.32.0 (2021-07-08T13:57:35)
### Features
* get update info from kebechet meta
* :arrow_up: Automatic update of dependencies by Kebechet
* add function argument to add value to template parameter for update advises
