.. SPDX-FileCopyrightText: 2024 Veit Schiele
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

`Unreleased <https://github.com/cusyio/Python4DataScience/compare/24.3.0...HEAD>`_
------------------------------------------------------------------------------------

Added
~~~~~

* 📝 Add csv.Sniffer methods
* 📝 Add the removal of git lfs

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
