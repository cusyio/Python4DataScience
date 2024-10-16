Python Docker Container with ``uv``
===================================

We divide our Docker workflow into different layers. This allows us to provide
new builds more quickly. We start with the layers that change the least so that
we can cache the artefacts for as long as possible. This is also the reason why
we keep the installations of the dependencies from :file:`uv.lock` and the
installation of our :doc:`application <python-basics:apps>` strictly separate –
our code probably changes faster than that of the dependencies.

.. seealso::
   * `Order your layers
     <https://docs.docker.com/build/cache/optimize/#order-your-layers>`_

#. First, we build an initial build container that prevents us from having to
   deliver our build tools.

   .. seealso::
      * `Multi-stage builds
        <https://docs.docker.com/build/building/multi-stage/>`_

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 4

      # syntax=docker/dockerfile:1.9
      FROM ubuntu:noble AS build

      SHELL ["sh", "-exc"]

      RUN <<EOT
      apt update -qy
      apt install -qyy \
          -o APT::Install-Recommends=false \
          -o APT::Install-Suggests=false \
          build-essential \
          ca-certificates \
          python3-setuptools \
          python3.12-dev
      EOT

   Line 4:
       If you are using `Podman <https://podman.io>`_, you should use the Docker
       compatibility mode.
   Line 6:
       If necessary, you can also prefix each ``RUN`` script with ``set -ex``,
       which makes troubleshooting easier.

       .. seealso::
          * https://github.com/containers/podman/issues/8477

#. We then build a :ref:`virtual Python environment <venv>` with our application
   in the :file:`/app` directory and copy it to our runtime container. One of
   the advantages of this is that the same base container can be used for
   different Python versions and :ref:`virtual environments <venv>`. With
   :doc:`/productive/envs/uv/index` 0.4.4 this has become much easier thanks to
   the environment variable ``UV_PROJECT_ENVIRONMENT``:

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 1, 3, 4, 6, 7

      COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

      ENV UV_LINK_MODE=copy \
          UV_COMPILE_BYTECODE=1 \
          UV_PYTHON_DOWNLOADS=never \
          UV_PYTHON=python3.12 \
          UV_PROJECT_ENVIRONMENT=/app

   Line 1:
       Safety-conscious organisations should check and pack ``uv`` themselves.

   Line 3:
       This prevents :doc:`/productive/envs/uv/index` from complaining about not
       being able to use hardlinks.
   Line 4:
       The Python packages are byte-compiled to shorten the start times of the
       container.
   Line 6:
       Select Python version.
   Line 7:
       Declare :file:`/app` as target for ``uv sync``.

#. Now we create the ``app`` Dockerfile:

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 1-2, 6-9, 14

      COPY pyproject.toml /_lock/
      COPY uv.lock /_lock/

      RUN --mount=type=cache,target=/root/.cache <<EOT
      cd /_lock
      uv sync \
          --locked \
          --no-dev \
          --no-install-project
      EOT

      COPY . /src
      RUN --mount=type=cache,target=/root/.cache \
          cd /src && uv sync --locked --no-dev --no-editable

   Lines 1–2:
       The :file:`lock` files are moved to a directory that is not in the
       runtime container. The slash at the end ensures that ``COPY``
       automatically creates :file:`/_lock/`.

   Line 4:
       For example, the build cache mount prevents all :term:`wheels <Wheel>`
       from having to be rebuilt if the layer with your dependencies has to be
       rebuilt.

       .. seealso::
          * `Use cache mounts
            <https://docs.docker.com/build/cache/optimize/#use-cache-mounts>`_


   Lines 6–9:
       The dependencies are synchronised without the application itself. This
       layer is cached until the :ref:`uv_lock` file or :file:`pyproject.toml`
       changes.
   Line 14:
       ``myapp`` is installed from :file:`/src` without any dependencies.

#. Finally, we create the runtime container:

   .. code-block:: docker
      :linenos:
      :emphasize-lines: 4, 6-9, 13, 20-21, 29-30, 32, 37-41


      FROM python:3.12-slim
      SHELL ["sh", "-exc"]

      ENV PATH=/app/bin:$PATH

      RUN <<EOT
      groupadd -r app
      useradd -r -d /app -g app -N app
      EOT

      ENTRYPOINT ["/docker-entrypoint.sh"]

      STOPSIGNAL SIGINT

      RUN <<EOT
      apt update -qy
      apt install -qyy \
          -o APT::Install-Recommends=false \
          -o APT::Install-Suggests=false \
          python3.12 \
          libpython3.12 \
          libpcre3 \
          libxml2

      apt clean
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
      EOT

      COPY docker-entrypoint.sh /
      COPY . /app/

      COPY --from=build --chown=app:app /app /app

      USER app
      WORKDIR /app

      RUN <<EOT
      python -V
      python -Im site
      python -Ic 'import myapp'
      EOT

   Line 4:
       Optional: Adds the :ref:`virtual environment <venv>` to the search path.

   Lines 6–9:
       Runs the application as a service user ``app``.

   Line 13:
       In the Python ecosystem, it is not necessarily common for your
       application to respond to a ``SIGTERM``. ``STOPSIGNAL SIGINT`` is an easy
       way to work around this.

       .. seealso::
          * `Why Your Dockerized Application Isn’t Receiving Signals
            <https://hynek.me/articles/docker-signals>`_

   Lines 20–21:
       Note that the dependencies at runtime are different from the dependencies
       at build time. Also, there is no ``uv``.

   Lines 29–30:
       If your application is not a :doc:`Python package
       <python-basics:libs/distribution>` installed with ``uv sync``, you must
       copy your application into the container here.

   Line 32:
       This copies the pre-built directory :file:`/app` into the runtime
       container and changes the permissions on the service user ``app`` and the
       group ``app`` in one step.

   Lines 37–41:
       Optional: I usually use this introspection for a smoke test, which
       ensures that the application can actually be imported.
