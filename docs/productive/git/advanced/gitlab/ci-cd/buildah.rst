.. SPDX-FileCopyrightText: 2022–2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Multi-arch images with Buildah
==============================

`Buildah <https://buildah.io>`_ allows you to create container images without
the need for a full container runtime. Buildah is an open-source Linux-based
tool that can create `Docker <https://www.docker.com>`_ and
`Kubernetes <https://kubernetes.io>`_-compatible images. In addition, Buildah
can not only create working containers from scratch, but also from an existing
Dockerfile. Finally, it can be easily integrated into scripts and build
pipelines.

First steps
-----------

#. Set up environment variables

   ``DEPLOY_USER``
       Name of the account.
   ``DEPLOY_KEY_FILE``
       Path to a private SSH key that is to be used for authentication against
       the server.
   ``DEPLOY_HOST``
       Host name or IP address of the server to be deployed to.

#. Setting up the CI/CD pipeline

   .. code-block:: yaml
      :caption: .gitlab-ci.yml
      :linenos:

      stages:
        - build
        - deploy

      build_docker:
        stage: build
        variables:
          DOCKER_STEM: $CI_REGISTRY_IMAGE
        image: quay.io/buildah/stable:v1.27
        script:
          - apk add --no-cache openssh
          - chmod 0600 "$DEPLOY_KEY_FILE"
          - ./build.sh

      deploy_app:
        stage: deploy
        image: alpine
        environment:
          name: app
          deployment_tier: staging
        when: manual
        script:
          - apk add --no-cache openssh
          - chmod 0600 "$DEPLOY_KEY"
          - ./deploy.sh

#. Building the Docker container

   .. code-block:: sh
      :caption: build.sh
      :linenos:
      :emphasize-lines: 2, 5, 8

      # Registry login
      echo "$CI_REGISTRY_PASSWORD" | buildah login -u "$CI_REGISTRY_USER" --password-stdin "$CI_REGISTRY"

      # Set docker tag
      if [ "$CI_COMMIT_BRANCH" == main ]; then export DOCKER_TAG="latest"; else export DOCKER_TAG="${CI_COMMIT_TAG:-$CI_COMMIT_REF_SLUG}"; fi; export DOCKER_TAG_FULL="$DOCKER_STEM:$DOCKER_TAG"; echo "DOCKER_TAG_FULL=$DOCKER_TAG_FULL"

      # Build and push
      buildah build --isolation chroot --storage-driver vfs --jobs 2 --platform linux/amd64,linux/arm/v7 --manifest "$DOCKER_TAG_FULL" && buildah --storage-driver vfs images && buildah manifest push --storage-driver vfs --format v2s2 --all "$DOCKER_TAG_FULL" "docker://$DOCKER_TAG_FULL"

   Line 2
       logs in to the :doc:`../package-registry`.
   Line 5
       identifies the images by their branch or tag names with the exception of
       ``main``, which is labelled with ``latest``.
   Line 8
       builds the images and deploys them with the `VFS
       <https://docs.docker.com/engine/storage/drivers/vfs-driver/>`_ driver.

#. Deploy

   .. code-block:: sh
      :caption: deploy.sh
      :linenos:

      # Set docker tag
      if [ "$CI_COMMIT_BRANCH" == main ]; then export DOCKER_TAG="latest"; else export DOCKER_TAG="${CI_COMMIT_TAG:-$CI_COMMIT_REF_SLUG}"; fi; export DOCKER_TAG_FULL="$DOCKER_STEM:$DOCKER_TAG"; echo "DOCKER_TAG_FULL=$DOCKER_TAG_FULL"

      echo "$CI_REGISTRY $DEPLOY_USER $DEPLOY_PASSWORD MYAPP $DOCKER_TAG" | ssh -o 'BatchMode yes' -o 'StrictHostKeyChecking accept-new' -i "$DEPLOY_KEY" root@$DEPLOY_HOST
