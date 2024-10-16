Dependency bot
==============

It is good practice to update dependencies regularly to avoid vulnerabilities,
limit incompatibilities between dependencies and avoid complex upgrades when
upgrading from a version that is too old. A variety of tools can help you stay
up to date. :term:`uv` is supported by `Renovate
<https://docs.renovatebot.com/>`_.

Renovate uses the :ref:`uv_lock` file to detect that ``uv`` is being used to
manage dependencies and suggests updates for project dependencies, optional
dependencies and development dependencies. Renovate updates both the
:file:`pyproject.toml` and :file:`uv.lock` files.

Installation and configuration
------------------------------

The Renovate CLI tool can be installed with

.. code-block:: console

   $ npm install renovate

.. tip::
   The Renovate bot should run under its own service user. We therefore
   recommend creating and using a separate account, ``renovate-bot``, for the
   bot. Then create and save an access token for this account.

You can now configure Renovate for your
:doc:`/productive/git/advanced/gitlab/index` server. Renovate looks for a
:file:`config.js` file in the current working directory by default. However, you
can override this by defining the environment variable ``RENOVATE_CONFIG_FILE``.
The configuration can then look like this, for example:

.. code-block:: js
   :caption: config.js

   module.exports = {
     endpoint: 'https://ce.cusy.io/api/v4/',
     token: 'GITLAB_TOKEN',
     platform: 'gitlab',
     onboardingConfig: {
       extends: ['config:recommended'],
     },
     repositories: ['USERNAME/REPO', 'ORGNAME/REPO'],
   };

.. note::
   Changes the paths to the repositories to something suitable. Also replace the
   GitLab token value with the value created in the previous step.

.. seealso::
   * `Renovate configuration overview
     <https://docs.renovatebot.com/config-overview/>`_

If you now want to regularly update the :file:`uv.lock` file in your repository,
you should use the `lockFileMaintenance
<https://docs.renovatebot.com/configuration-options/#lockfilemaintenance>`_
option in the :file:`renovate.json5` file in your repository, for example:

.. code-block:: json5
   :caption: renovate.json5

   {
     $schema: "https://docs.renovatebot.com/renovate-schema.json",
     lockFileMaintenance: {
       enabled: true,
     },
   }

However, Renovate does not automatically recognise files with
:ref:`inline-script-metadata`. You must explicitly specify these Python scripts
with `fileMatch
<https://docs.renovatebot.com/configuration-options/#filematch>`_, for example
with:

.. code-block:: json5
   :caption: renovate.json5
   :emphasize-lines: 4-5

   {
     $schema: "https://docs.renovatebot.com/renovate-schema.json",
     pep723: {
       fileMatch: [
         "app\\.py",
       ],
     },
   }

.. seealso::
   * `lockFileMaintenance
     <https://docs.renovatebot.com/configuration-options/#lockfilemaintenance>`_

Finally, the timing of Renovate should be planned, for example with `cron
<https://en.wikipedia.org/wiki/Cron>`_:

.. code-block:: bash

   #!/bin/bash

   export PATH="/home/renovate-bot/.node_modules/.bin/renovate:$PATH"
   export RENOVATE_CONFIG_FILE="/home/renovate-bot/config.js"
   export RENOVATE_TOKEN="GITLAB_TOKEN"

   0 * * * * renovate

CI/CD pipeline
--------------

Renovate can also be integrated into :doc:`cicd`:

* `GitHub Action <https://github.com/renovatebot/github-action>`_
* `GitLab Runner <https://gitlab.com/renovate-bot/renovate-runner/>`_
