.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Separating environments
=======================

Current best practice is to separate different environments depending on what is
to be done in each one. For example, in our `cusy.tasks
<https://github.com/cusyio/cusy.tasks>`_ application, a distinction is made
between the following environments:

.. code-block:: toml
   :caption: pyproject.toml

   [project]

   dependencies = [
     "rich",
     "tinydb",
     "typer",
   ]

   [dependency-groups]
   dev = [
     "pre-commit",
     "reuse",
     "tox-uv",
     "watchgha",
     { include-group = "docs" },
     { include-group = "tests" },
   ]
   docs = [
     "furo",
     "interrogate",
     "matplotlib",
     "sphinx-copybutton",
     "sphinx-inline-tabs",
     "sphinxcontrib-napoleon",
     "sphinxext-opengraph",
   ]
   tests = [
     "coverage[toml]",
     "faker",
     "pytest",
     "pytest-cov",
   ]

This means that when the application is running, only the dependencies required
for that purpose are installed; additional dependencies are only installed when
testing or deploying the documentation. Only the development environment
contains all dependencies.

Just as your Python environment should be kept up to date with immutable
references, your :doc:`../git/advanced/hooks/checks` and GitHub Actions should
also be updated regularly.

In the :file:`.pre-commit-config.yaml` file, the versions of the checks and
their hashes should be updated regularly, for example using:

.. code-block:: console

   $ uv run prek update --freeze --cooldown-days 7
   https://github.com/pre-commit/pre-commit-hooks
     updating rev `v6.0.0` -> `3e8a8703264a2f4a69428a0aa4dcb512790b2c8c` (frozen: v6.0.0)

.. seealso::
   :doc:`../git/advanced/hooks/prek`

.. _pinact:

Check your GitHub Actions
-------------------------

For GitHub Actions, you can use `pinact
<https://github.com/suzuki-shunsuke/pinact>`_, for example with:

.. code-block:: console

   $ pinact run -u --min-age 7

`zizmor <https://docs.zizmor.sh>`_ is a static analysis tool that detects
security vulnerabilities in GitHub Actions workflows – including template
injection, unpinned actions, excessive permissions, credential exposure and
`more than 30 other checks <https://docs.zizmor.sh/audits/>`_. zizmor identifies
vulnerabilities such as those exploited through :ref:`token exfiltration
<token-exfiltration>`.

.. seealso::
   * :ref:`zizmorcore`
