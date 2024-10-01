.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Environment variables
=====================

``pipenv`` environment variables
--------------------------------

``pipenv --envs`` outputs options of the environment variables.

For more information, see `Configuration With Environment Variables
<https://docs.pipenv.org/advanced/#configuration-with-environment-variables>`_.

:file:`.env` file
-----------------

If an :file:`.env` file exists in your virtual environment, ``$ pipenv shell``
and ``$ pipenv run`` will automatically load it:

.. code-block:: console

    $ cat .env
    USERNAME=veit

    $ pipenv run python
    Loading .env environment variables...
    …

.. code-block:: pycon

    >>> import os
    >>> os.environ["USERNAME"]
    'veit'

The credentials of the version management, can also be specified in the
:file:`Pipfile`, for example:

.. code-block:: ini

    [[source]]
    url = "https://$USERNAME:${PASSWORD}@ce.cusy.io/api/v4/projects/$PROJECT_ID/packages/pypi/simple"
    verify_ssl = true
    name = "gitlab"

.. note::
   ``pipenv`` hashes the :file:`pipfile` before determining the environment
   variables, and the environment variables from the :file:`pipfile.lock` are
   also replaced so that no credentials need to be stored in the version
   management.

You can also save the :file:`.env` file outside your virtual environment. You
then only have to specify the path to this file in ``PIPENV_DOTENV_LOCATION``:

.. code-block:: console

    $ PIPENV_DOTENV_LOCATION=/PATH/TO/.env pipenv shell

You can also prevent ``pipenv`` from using an existing :file:`.env` file with:

.. code-block:: console

    $ PIPENV_DONT_LOAD_ENV=1 pipenv shell
