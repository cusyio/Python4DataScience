.. SPDX-FileCopyrightText: 2024 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Changelog
=========

All significant changes to this project are documented in this file.

The format is based on `Keep a Changelog
<https://keepachangelog.com/en/1.0.0/>`_ and this project adheres to `Calendar
Versioning <https://calver.org>`_.

The first number of the version is the year. The second number is incremented
with each version, starting at 1 for each year. The third number is for
emergencies when we need to start branches for older versions.

.. _changelog

`Unreleased <https://github.com/cusyio/Python4DataScience/compare/26.1.0...HEAD>`_
----------------------------------------------------------------------------------

Changed
~~~~~~~

* 👷🔧📝 Switch to prek

  * Remove pre-commit
  * Fix Python syntax

`26.1.0 <https://github.com/cusyio/Python4DataScience/compare/24.3.0...26.1.0>`_: 2026-07-08
--------------------------------------------------------------------------------------------

Added
~~~~~

* 📝 Add bandit rules to security
* 📝 Add jsonata-python
* 📝 Add Memray as a profile tool
* 📝 Add Git’s data and storage model
* 📝 New features in Python 3.15

  * profiling.tracing and profiling.sampling
  * Tachyon
  * Python JIT compiler

* 📝 Add tdda detect_df
* 🔧 Add dependabot cooldown and group dependabot updates
* 📝 Check and change data types
* 📝 Indexing with Boolean DataFrame and bitwise operators
* 📝 🔧 Check and format pyproject.toml

  * Add pyproject-fmt and validate-pyproject

* 📝 fsck as a last resort to restore changes
* 📝 Add Claude and Cursor config for uv
* 📝 Add comparison between pandas, Polars, Dask and DuckDB
* 📝 Add geopython libs

  pygeoapi, OWSLib, pycsw and pygeometa

* 📝 Add project templates
* 📝 Add file formats for geodata
* 📝 Add GitLab CI/CD examples
* 📝 Add csv.Sniffer methods
* 📝 Add the removal of git lfs
* 📝 Add deal recommendation for the licensing of open access publications
* 📝 Fill with mean values
* 🔧 Add OpenGraph tag for mastodon

Changed
~~~~~~~

* 📝 Switch from uv-secure to uv audit
* 🔧 Switch to ruff

  * Variables not shadowing Python builtins (A001)
  * Not used loop control variable renamed with a leading underscore (B007)
  * Raise with from inside except (B904)
  * Add explicit ``strict=`` parameter to ``zip()`` (B905)
  * Call datetime.now and datetime.strptime with timezone (DTZ005, DTZ007)
  * Assign a ``def`` instead of a ``lambda`` expression (E731)
  * Replace legacy ``np.random.randn`` with ``np.random.Generator`` (NPY002)
  * Use ``.merge`` method instead of ``pd.merge`` function (PD015)
  * ``open()`` is replaced by ``Path.open()`` (PTH123)

* 📄 Update licence information

  * Copyright belongs to cusy GmbH
  * Move LICENSE file to LICENSES/

* 📝 Update git section

  * Add git history and config-based hooks
  * Add links to Sourcegraph to find pre-commit hooks

* 📝 Update security

  * Add references to Securing the release workflow, zizmor and 2FA
  * Add anchor for GitHub Actions

* 📝 Update dtype conversion
* 📝 Update open data

  * Organise open data by topic
  * Add link to Authors Alliance
  * Add lots of new data sources
  * Move geodata sources to open data
  * Add NFDI4DS Portal
  * Add link to Authors Alliance
  * Fix internal link to geodata

* 📝 Update performance measurements section

  * Add cProfile/profiling.tracing
  * Add tprof
  * Add performance metrics

* 📝 Update FastAPI Extensions

  * Add AuthTuna
  * Postpone dormant projects

* 🔧 Use PEP 639 licence expression

  Remove deprecated Trove classifier

* 📝 Update git pre-commit section

  * Add pyproject-fmt pre-commit scripts

* 📝 Update dvc section
* 📝 Add ruff formatter
* 📝 Add JSON tools
* 📝 Update licensing
* 💚 Switch to uv for the GitHub workflow
* 📝 Update licence action

  * Update hardware licences
  * Add ML models licences

* 📝 Switch from pipenv to uv
* 📝 Update performance section

  * Add Installation and usage of perflint
  * Add perflint pre-commit hook
  * Add link to cProfile

* 📝 Update git section
* 📝 Switch form safety to uv-secure
* 📝 Switch from git checkout to git switch
* 📝 Update GitLab pipeline with uv
* 📝 Move logging to Python basics
* 📝 Update dedupe section
* 📝 Remove axis as option for pandas groupby
* 🔧 Switch to the PyViz tutorial in English

`24.3.0 <https://github.com/cusyio/Python4DataScience/compare/24.2.0...24.3.0>`_: 2024-11-03
--------------------------------------------------------------------------------------------

Added
~~~~~

* 🔧 Add vale

  * Fix spelling mistakes

* 🔧 Add codespell

  * Add pre-commit check
  * Fix spelling

* 👷 Build docs and check links

  * Configure linkcheck
  * Fix external links

* 📝 Add the series of tutorials and trainings
* 📝 Add automatic building of Docker containers
* 📝 Add edgy, zopyx-fastapi-auth, and FastAPI Utilities to FastAPI extensions

Removed
~~~~~~~

* 📝 Move logging to Python basics
* ✏️ Remove link to Objectivity/DB
* 📝 Move SOLID principles to Python Basics

Changed
~~~~~~~

* 📝 Update GitLab pipeline with uv
* ⬆️ Update to Python 3.13, NumPy 2.1 and pandas 2.2

  * Replace dataframe.applymap with dataframe.apply
  * Replace pandas.value_counts with pandas.Series(obj).value_counts()
  * Replace as_index=False for groupby() with reset_index(drop=True)
  * Add include_groups=False for DataFrameGroupBy.apply

* 🍱 Update git workflow graphic
* 📝 Switch to the pre-commit framework for gitleaks

* 📝 Switch from pipenv to uv

  * Remove pipenv
  * Add pre-commit-uv
  * Add CI/CD-Pipelines
  * Add dependency bot
  * Update security

* 🔧 Update gitignore

* 🔧 Add blacken-docs

  * Fix Python syntax

* 📝 Update the file system libraries

* 🔧 Switch to pyproject.toml

* 👷 Update pre-commit github workflow
* 📝 Update geodata libs

`24.2.0 <https://github.com/cusyio/Python4DataScience/compare/24.1.0...24.2.0>`_: 2024-06-29
--------------------------------------------------------------------------------------------

Added
~~~~~

* Git

  * 📝 Add zdiff3 as git merge conflict style
  * 📝 Update meaningful commit messages
  * 🍱 Update git cheatsheet
  * 📝 Add git batch processing
  * 📝 Add warning for git keep
  * 🎨 Improve structure of the git section

* 🌱 Add matplotlib for social cards

Changed
~~~~~~~

* 🎨 Improve structure of the code quality section
* 🎨 Improve structure of the cite software section

`24.1.0 <https://github.com/cusyio/Python4DataScience/compare/v1.0.0...24.1.0>`_: 2024-04-02
--------------------------------------------------------------------------------------------

Added
~~~~~

* Code smells

  * 📝 Add SOLID principles
  * 📝 Add the recognition of code smells
  * 📝 Add intro to code smells
  * 🎨 Rearrange code reduction with dataclasses and attrs
  * 📝 Update itertools filterfalse

* 📄 Add SPDX classifier

Changed
~~~~~~~

* 📝 Update redis licenses, add hint to Redict and Valkey

* Git

  * 📝 Add ‘Change commits for a clean log’
  * 📝 Update git’s database internals
  * 📝 Rearrange advanced git section
  * 📝 Extend the git notes section
  * 📝 Simplify secret detection
  * 📝 Add more git commands and options
  * 📝 Extend the git bisect section
  * 🎨 Rearrange the git section
  * 📝 Update log and reflog
  * 📝 Improve the Git configuration
  * 📝 Add reference for common reset commands
  * 📝 Update git reset
  * 📝 Expand section on meaningful commit messages
  * 📝 Update git section
  * 📝 Update the section Undo commit in the wrong branch
  * 📝 Add description of workspaces

* Data serialisation

  * 📝 Update xml example
  * 📝 Update data serialisation
  * 📝 Simplify the json example

* 📝 Switch from the requests lib to httpx
