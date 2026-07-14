.. SPDX-FileCopyrightText: 2020 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

prek in CI pipelines
====================

Pre-commit can also be used for :abbr:`CI (continuous integration)`.

.. _gh-action-prek-example:

Example for GitHub Actions
--------------------------

:file:`.github/workflows/pre-commit.yml`
    Alternative configuration as a GitHub workflow, for example:

.. code-block:: yaml
   :caption: .github/workflows/prek.yml

   name: prek

   on:
     pull_request:
     push:
       branches: [main]

   concurrency:
     group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
     cancel-in-progress: true

   permissions: {}

   jobs:
     prek:
       name: prek
       # External pull requests should be checked, but not our own internal pull
       # requests again, as these are already checked by the push on the branch.
       # Without this if condition, the checks would be performed twice, as
       # internal pull requests correspond to both the push and pull_request
       # events.
       if:
         github.event_name == 'push' ||
         github.event.pull_request.head.repo.full_name != github.repository
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
         with:
           persist-credentials: false
       - uses: j178/prek-action@e98a699c41eb69ab013a45817a0406469a748f8d # v2.0.5

.. _prek-in-gitlab-ci:

Example for GitLab Actions
--------------------------

.. code-block:: yaml

   :caption: .gitlab-ci.yml

   stages:
     - validate

   prek:
     stage: validate
     image:
       name: python:3.14
     only:
       refs:
         - merge_requests
         - tags
         - main
     script:
       - uvx prek run --all-files

.. seealso::

   For more information on fine-tuning caching, see `Good caching practices
   <https://docs.gitlab.com/ci/caching/#good-caching-practices>`_.
