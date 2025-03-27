.. SPDX-FileCopyrightText: 2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

npm deployment with rsync
=========================

`npm <https://www.npmjs.com>`_ is a package manager for the JavaScript runtime
environment `Node.js <https://nodejs.org/en/>`_, and `rsync
<https://rsync.samba.org>`_ can be used to synchronise the data with the remote
server.

First steps
-----------

#. Set up environment variables

   ``DEPLOY_DIR``
       Directory on the remote server to which data is to be distributed..
   ``DEPLOY_HOST``
       Host name or IP address of the server to be deployed to.
   ``DEPLOY_KEY_FILE``
       Path to a private SSH key that is to be used for authentication against
       the server.
   ``DEPLOY_USER``
       Name of the SSH account.
   ``KNOWN_HOSTS_FILE``
       Path to a file with predefined :file:`known_hosts` entries with which
       the connection is to be checked.

#. Setting up the CI/CD pipeline

   .. code-block:: yaml
      :caption: .gitlab-ci.yml
      :emphasize-lines: 13, 14, 15

      stages:
        - deploy

      deploy-static-assets:
        stage: deploy
        rules:
          - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
        environment:
          name: prod
          deployment_tier: production
        image: node:alpine
        script:
          - apk add --no-cache git nodejs npm openssh-client-default rsync
          - chmod 0600 "$DEPLOY_KEY_FILE"
          - ./deploy.sh

   Line 13
       installs the packages required for building and uploading
   Line 14
       changes the access authorisations for the ssh key
   Line 15
       calls the :file:`deploy.sh` file

#. Moves the static files to the server

   .. code-block:: sh
      :caption: deploy.sh
      :linenos:
      :emphasize-lines: 7-13, 18, 19, 24, 25-31

      #!/bin/sh
      set -e

      # Deploy static assets to a server via rsync.

      # Create SSH config.
      cat >deploy.ssh_config <<-END
          Host deploy
              HostName $DEPLOY_HOST
              User $DEPLOY_USER
              IdentityFile $DEPLOY_KEY_FILE
              UserKnownHostsFile $KNOWN_HOSTS_FILE
      END


      # Build the JavaScript application & related files.
      cd vite-app
      npm ci
      npx vite build

      # Deploy the application and GeoJSON data.
      rsync \
          -rtlv \
          --rsh 'ssh -F ../deploy.ssh_config' \
          --rsync-path "mkdir -p \"$DEPLOY_DIR\" && rsync" \
          ../data/cusy.geojson \
          cusy.html \
          dist/cusy-map.css \
          dist/cusy-map.js \
          dist/cusy-map.js.map \
          "deploy:$DEPLOY_DIR"

   Line 7–13
       creates the ssh configuration file.

   Line 18
       installs the dependencies of the project from the
       :file:`vite-app/package.json` file.

       .. seealso::
          `npm-ci <https://docs.npmjs.com/cli/v9/commands/npm-ci>`_

   Line 19
       creates the `vite <https://vite.dev>`_ project for production.

   Line 24
       moves the ssh configuration to the server.

   Lines 25–31
       moves the application and GeoJSON data to the server.
