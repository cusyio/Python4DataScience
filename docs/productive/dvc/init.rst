.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Create project
==============

DVC can be easily initialised with:

.. code-block:: console

    $ uv init --package dvc-example
    $ cd dvc-example
    $ git init
    $ git add --all
    $ git commit -m ':tada: Initial commit'
    $ uv add dvc
    $ uv run dvc init
    $ git add pyproject.toml .dvc .dvcignore
    $ git commit -m ":heavy_plus_sign: Add and initialise DVC"

``uv run dvc init``
    creates a :file:`.dvc/` directory with :file:`config`, :file:`.gitignore`
    and :file:`cache/` directory.

    The first time you run ``dvc init``, you will be informed that DVC collects
    and transmits anonymised usage statistics. If you want to disable this, you
    can do so with the command ``dvc config``:

    .. code-block:: console

       $ uv run dvc config core.analytics false

    This will disable it for the project. Alternatively, you can use the
    ``--global`` or ``--system`` options of dvc config to disable analytics for
    the active account or for all accounts in the system.

``git add pyproject.toml .dvc .dvcignore``
    places :file:`.dvc/config`, :file:`.dvc/.gitignore` and the updated
    :file:`pyproject.toml` under Git version control.

Configure remote storage
------------------------

.. _dvc-remote:

Before using DVC, remote storage should be set up. This should be accessible to
everyone who needs to access the data or model. It is similar to using a Git
server. However, this is often also an NFS mount, which can be integrated as
follows, for example:

.. code-block:: console

    $ mkdir ~/dvc-storage
    $ uv run dvc remote add -d local ~/dvc-storage
    Setting 'local' as a default remote.
    $ git commit .dvc/config -m ":wrench: Configure local remote"
    [main 3e0c8fb] :wrench: Configure local remote
     1 file changed, 4 insertions(+)

``-d``, ``--default``
    Default value for remote storage space
``local``
    Name of remote storage space
:file:`~/dvc-storage`
    URL of remote storage space

    Other protocols are also supported and can be prefixed to the path,
    including ``ssh:``, ``hdfs:``, ``https:``.

This means that another remote data storage location can easily be added, for
example with:

.. code-block:: console

    $ uv run dvc remote add webserver https://dvc.cusy.io/dvc-example

The corresponding configuration file :file:`.dvc/config` then looks like this:

.. code-block:: ini

   [core]
       remote = local
   ['remote "local"']
       url = /Users/veit/dvc-storage
   ['remote "webserver"']
       url = https://dvc.cusy.io/dvc-example

.. seealso::
   `Remote Storage
   <https://dvc.org/doc/user-guide/data-management/remote-storage>`_

Configure pre-commit
--------------------

You can check the data managed by DVC with the pre-commit framework before every
``git commit`` and ``git push``, as well as after every ``git checkout``. With
``dvc config --use-pre-commit-tool``, the :file:`.pre-commit-config.yaml` file
receives the following checks:

.. code-block:: yaml

    - repo: https://github.com/iterative/dvc
      rev: 3.63.0
      hooks:
      - id: dvc-pre-commit
        additional_dependencies:
        - .[all]
        language_version: python3
        stages:
        - pre-commit
      - id: dvc-pre-push
        additional_dependencies:
        - .[all]
        language_version: python3
        stages:
        - pre-push
      - id: dvc-post-checkout
        additional_dependencies:
        - .[all]
        language_version: python3
        stages:
        - post-checkout
        always_run: true

To ensure that not only the ``pre-commit`` hook is used, you must also activate
the ``pre-push`` and ``post-checkout`` hooks:

.. code-block:: console

   $ pre-commit install --hook-type pre-commit --hook-type pre-push --hook-type post-checkout
   pre-commit installed at .git/hooks/pre-commit
   pre-commit installed at .git/hooks/pre-push
   pre-commit installed at .git/hooks/post-checkout
