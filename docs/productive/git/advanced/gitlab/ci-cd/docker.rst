.. SPDX-FileCopyrightText: 2024–2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Building Docker containers
==========================

We use :doc:`index`, to create our Python Docker containers.

#. First, we define the Python version in our :ref:`pyproject-toml` file of the
   project:

   .. code-block:: toml

      [project]
      name = "my-app"
      requires-python = "==3.12.*"

#. We then extract this string in our :file:`.gitlab-ci.yml` file and pass it as
   a build argument to ``docker build``:

   .. code-block:: yaml

      build:
        stage: build
        only: [main]
        script:
          - export PY=$(sed -nE 's/^requires-python = "==(3\.[0-9]+)\.*"$/python\1/p' pyproject.toml)
          - >
            docker build
            --build-arg PY=$PY

#. Finally, we can use the extracted version in the Dockerfile to create a
   virtual environment in the build phase and install the Python version in the
   ``application`` stage:

   .. code-block:: docker
      :emphasize-lines: 3, 6

      FROM your-docker/build-image as build

      ARG PY
      RUN --mount=type=cache,target=/root/.cache \
          set -ex \
          && virtualenv --python $PY /app
      …
      FROM your-docker/app-image
      …
      RUN set -ex \
          && apt-get update -qy \
          && apt-get install -qy \
              -o APT::Install-Recommends=false \
              -o APT::Install-Suggests=false \
      …
      COPY --from=build --chown=app /app /app
