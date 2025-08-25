.. SPDX-FileCopyrightText: 2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Ruff
====

`Ruff <https://docs.astral.sh/ruff/>`_ is an extremely fast Python linter and
code formatter written in Rust that can enforce the rules of :doc:`flake8`,
:doc:`isort`, :doc:`/performance/perflint`, :doc:`black`, :ref:`Bandit
<bandit>`, and others. In total, Ruff can `check over 800 rules
<https://docs.astral.sh/ruff/rules/>`_.

Installation
------------

.. code-block:: console

    $ uv add --dev ruff

Check
-----

You can then check the installation with

.. code-block:: console

    $ uv run ruff check /PATH/TO/YOUR/SOURCE/FILE

Shell auto-completion
---------------------

Ruff supports autocompletion for most shells. A shell-specific script can be
generated with :samp:`uv run ruff generate-shell-completion {SHELL}`, where
:samp:`{SHELL}` is either ``bash``, ``elvish``, ``fig``, ``fish``,
``powershell`` or ``zsh``, for example

.. tab:: Bash

   .. code-block:: console

      $ ruff generate-shell-completion zsh >> ~/.bash_completion

.. tab:: Zsh

   .. code-block:: console

      % ruff generate-shell-completion zsh > ~/.zfunc/_ruff

   Then, the following lines must be added to your :file:`~/.zshrc` file, if
   they are not already there:

   .. code-block:: zsh

      fpath+=~/.zfunc
      autoload -Uz compinit && compinit

.. tab:: Oh My Zsh

   .. code-block:: console

      % mkdir $ZSH_CUSTOM/plugins/ruff
      % ruff generate-shell-completion zsh > $ZSH_CUSTOM/plugins/ruff/_ruff

.. seealso::
   `Shell autocompletion
   <https://docs.astral.sh/ruff/configuration/#shell-autocompletion>`_

Configuration
-------------

Unlike :doc:`black`’s default formatting of 88 characters, I prefer a line
length of 79 characters. To do this, you can enter the following in the
:file:`pyproject.toml` file:

.. code-block:: toml

    [tool.ruff]
    line-length = 79

.. tip::
   Usually, we first add all rules to ``ruff lint`` before excluding individual
   ones, for example:

   .. code-block:: toml

      [tool.ruff.lint]
      select = ["ALL"]
      ignore = [
          "A",       # Shaddowing is fine
      ]

Ruff also supports monorepos with different rules through `hierarchical and
cascading configurations
<https://docs.astral.sh/ruff/configuration/#config-file-discovery>`_.

.. seealso::
   For more information on configuring ruff in the :file:`pyproject.toml` file,
   see `Configuring Ruff <https://docs.astral.sh/ruff/configuration/>`_.

Integration
-----------

Jupyter Notebooks
~~~~~~~~~~~~~~~~~

Ruff supports linting and formatting :doc:`Jupyter Notebooks
<jupyter-tutorial:notebook/index>` with :ref:`nbQA <nbqa>`. With `jupyter-ruff,
<https://github.com/leotaku/jupyter-ruff>`_ you can also use Ruff in your
notebooks.

IDE
~~~

Integration with other editors such as Visual Studio Code, PyCharm or Vim is
also possible, see `Editor Integrations
<https://docs.astral.sh/ruff/editors/>`_.

pre-commit
~~~~~~~~~~

Ruff can be used as a :doc:`pre-commit hook
</productive/git/advanced/hooks/pre-commit>` via `ruff-pre-commit
<https://github.com/astral-sh/ruff-pre-commit>`_:

.. code-block:: yaml

   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.12.10
       hooks:
       - id: ruff-check
         args: [--fix, --exit-non-zero-on-fix]
         exclude: docs
       - id: ruff-format
