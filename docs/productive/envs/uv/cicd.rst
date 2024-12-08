CI/CD pipelines
===============

.. _uv-gitlab:

GitLab CI/CD
------------

For :doc:`GitLab CI/CD pipelines </productive/git/advanced/gitlab/ci-cd>` there
are various Docker images with pre-installed ``uv``: Available images
<https://docs.astral.sh/uv/guides/integration/docker/#available-images>`_.

.. code-block:: yaml
   :caption: .gitlab-ci.yml
   :linenos:

   variables:
     UV_VERSION: 0.4
     PYTHON_VERSION: 3.12
     BASE_LAYER: bookworm-slim


   stages:
     - build

   uv-install:
     stage: build
     image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
     variables:
       UV_CACHE_DIR: .uv-cache
     cache:
       - key:
           files:
             - uv.lock
         paths:
           - $UV_CACHE_DIR
     script:
       # YOUR UV COMMANDS
       - uv cache prune --ci

Line 23
    This reduces the cache size, see also `Caching in continuous integration
    <https://docs.astral.sh/uv/concepts/cache/#caching-in-continuous-integration>`_.

.. seealso::
   * `Using uv in GitLab CI/CD
     <https://docs.astral.sh/uv/guides/integration/gitlab/>`_

GitHub Actions
--------------

The official `astral-sh/setup-uv <https://github.com/astral-sh/setup-uv>`_
GitHub action installs uv, adds it to PATH and provides a cache for the
installed packages:

.. code-block:: yaml
   :caption: ci.yml

   name: ci

   jobs:
     test:
       name: python
       runs-on: ubuntu-latest

       steps:
         - uses: actions/checkout@v4

         - name: Install uv
           uses: astral-sh/setup-uv@v3
           with:
             version: "0.4.24"

You can then install either a single Python version or a matrix with uv:

.. code-block:: yaml
   :caption: ci.yml

        - name: Set up Python
          uses: actions/setup-python@v5
          with:
            python-version-file: "pyproject.toml"

or

.. code-block:: yaml
   :caption: ci.yml

        - name: Set up Python
          uses: actions/setup-python@v5
          with:
            python-version-file: ".python-version"

or

.. code-block:: yaml
   :caption: ci.yml

   name: ci

   strategy:
     matrix:
       python-version:
         - "3.9"
         - "3.10"
         - "3.11"
         - "3.12"
         - "3.13"

   jobs:
     test:
       name: python
       # ...
         - name: Set up Python ${{ matrix.python-version }}
           run: uv python install ${{ matrix.python-version }}

.. seealso::
   * `Using uv in GitHub Actions
     <https://docs.astral.sh/uv/guides/integration/github/>`_

``uv sync`` and ``uv run``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once uv and Python are installed, the project can be installed with ``uv sync``
and commands can be executed in the environment with ``uv run``, for example for
:doc:`python-basics:test/pytest/index`:

.. code-block:: yaml
   :caption: ci.yml

         - name: Install the project
           run: uv sync --all-extras --dev

         - name: Run tests
           run: uv run pytest tests

Caching
~~~~~~~

The uv cache improves runtimes:

.. code-block:: yaml
   :caption: ci.yml

         - name: Enable caching
           uses: astral-sh/setup-uv@v3
           with:
             enable-cache: true

Invalidates the cache if :file:`uv.lock` changes:

.. code-block:: yaml
   :caption: ci.yml

         - name: Define a cache dependency glob
           uses: astral-sh/setup-uv@v3
           with:
             enable-cache: true
             cache-dependency-glob: "uv.lock"
