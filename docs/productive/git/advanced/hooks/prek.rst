.. SPDX-FileCopyrightText: 2020 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

prek
====

`prek <https://prek.j178.dev>`_ is a variant of `pre-commit
<https://pre-commit.com/>`_, written in Rust, for managing and maintaining
multilingual commit hooks.

An essential task is to make the same scripts available to the entire
development team. `pre-commit <https://pre-commit.com/>`_ by yelp manages such
hooks and distributes them to different projects and developers.

Git hooks are mostly used to automatically point out problems in the code before
code reviews, for example to check the formatting or to find debug statements.
pre-commit simplifies the sharing of hooks across projects. The language in
which a linter was written, for example, is abstracted away – ``scss-lint`` is
written in Ruby, but you can use it with pre-commit without having to add a
Gemfile to your project.

Installation
------------

Before you can execute the hooks, prek must be installed:

.. tab:: Windows

   .. code-block:: console

      > powershell -ExecutionPolicy ByPass -c "irm https://github.com/j178/prek/releases/download/v0.4.9/prek-installer.ps1 | iex"

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ curl --proto '=https' --tlsv1.2 -LsSf https://github.com/j178/prek/releases/download/v0.4.9/prek-installer.sh | sh

.. tab:: macOS

   .. code-block:: console

      $ brew install prek

.. tab:: Others

   .. code-block:: console

      $ uv add --group dev prek

Check the installation for example with

.. code-block:: console

    $ uv run prek -V
    prek 0.4.9 (42b79a57f 2026-07-11)

Configuration
-------------

After Pre-Commit is installed, the :file:`.pre-commit-config.yaml` file in the
root directory of your project can be used to configure plugins for this
project.

.. code-block:: yaml

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: 3e8a8703264a2f4a69428a0aa4dcb512790b2c8c # v6.0.0
        hooks:
        - id: trailing-whitespace
        - id: end-of-file-fixer
        - id: check-yaml
        - id: check-added-large-files

You can also generate such an initial ``.pre-commit-config.yaml`` file with

.. code-block:: console

    $ uv run prek sample-config > .pre-commit-config.yaml

If you want to apply ``check-json`` to your Jupyter notebooks, you must first
configure that the check should also be used for the file suffix ``.ipynb``:

.. code-block:: yaml
   :emphasize-lines: 7-8

    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: 3e8a8703264a2f4a69428a0aa4dcb512790b2c8c # v6.0.0
        hooks:
        …
        - id: check-json
          types: [file]
          files: \.(json|ipynb)$

.. seealso::

    For a full list of configuration options, see `Adding pre-commit plugins to
    your project
    <https://pre-commit.com/#adding-pre-commit-plugins-to-your-project>`_.

    You can also write your own hooks, see `Creating new hooks
    <https://pre-commit.com/#creating-new-hooks>`_.

Installing the git hook scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure that pre-commit is also reliably executed before each commit, the
script is installed in our project:

.. code-block:: console

    $ prek install
    prek installed at .git/hooks/pre-commit

If you want to uninstall the git hook scripts, you can do so with ``prek
uninstall``.

Run
---

:samp:`uv run prek run --all-files`
    runs all pre-commit checks independently of ``git commit``:

    .. code-block:: console

        $ uv run prek run --all-files
        Trim Trailing Whitespace.................................................Passed
        Fix End of Files.........................................................Passed
        Check Yaml...............................................................Passed
        Check for added large files..............................................Passed

:samp:`prek run {HOOK}`
    executes single prek checks, for example :samp:`prek run
    trailing-whitespace`

.. note::
   When a prek check is called for the first time, it is first downloaded and
   then installed. This may take some time, for example if a copy of ``node``
   has to be created.

:samp:`prek update [OPTIONS]`
    updates the hooks automatically:

    .. code-block:: console

       $ uv run prek update --freeze --cooldown-days 7
       https://github.com/pre-commit/pre-commit-hooks
         updating rev `v6.0.0` -> `3e8a8703264a2f4a69428a0aa4dcb512790b2c8c` (frozen: v6.0.0)

However, the hooks managed by prek are not limited to being executed before
commits; they can also be used for other Git hooks, see :doc:`hooks`.
