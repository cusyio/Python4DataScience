.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

HERMES
======

`HERMES <https://project.software-metadata.pub>`_ simplifies the publication of
research software by continuously retrieving existing metadata in :doc:`cff`,
:doc:`codemeta` and :doc:`Git <../../git/index>`. Subsequently, the metadata is
also compiled appropriately for `InvenioRDM
<https://invenio-software.org/products/rdm/>`_ and `Dataverse
<https://dataverse.org/>`_. Finally, :doc:`CITATION.cff <cff>` and
:doc:`codemeta.json <codemeta>` are also updated for the publication
repositories.

#. Add ``.hermes/`` to the :ref:`.gitignore <gitignore>` file
#. Provide :doc:`CITATION.cff <cff>` file with additional metadata

   .. important::
      Make sure  ``license`` is defined in the :doc:`CITATION.cff <cff>` file;
      otherwise, your release will not be accepted as open access by the
      :doc:`Zenodo <doi>` sandbox.

#. Configure HERMES workflow

   The HERMES workflow is configured in the file
   :doc:`/data-processing/serialisation-formats/toml/index`, where each step
   gets its own section.

   If you want to configure HERMES to use the metadata from :doc:`Git
   <../../git/index>` and :doc:`CITATION.cff <cff>`, and to file in the Zenodo
   sandbox built on InvenioRDM, the :file:`hermes.toml` file looks like this:

   .. literalinclude:: hermes.toml
      :caption: hermes.toml
      :name: hermes.toml

#. Access token for Zenodo Sandbox

   In order for GitHub Actions to publish your repository in the `Zenodo Sandbox
   <https://sandbox.zenodo.org/>`_, you need a personal access token. To do
   this, you need to log in to Zenodo Sandbox and then create a `personal access
   token
   <https://sandbox.zenodo.org/account/settings/applications/tokens/new/>`_ in
   your user profile with the name :samp:`HERMES workflow` and the scopes
   :guilabel:`deposit:actions` und :guilabel:`deposit:write`:

   .. image:: zenodo-personal-access-token.png
      :alt: Zenodo: Neues persönliches Zugangstoken

#. Copy the newly created token to a new `GitHub secret
   <https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository>`_
   named :samp:`ZENODO_SANDBOX` in your repository: `Settings --> Secrets and
   Variables --> Actions --> New repository secret`:

   .. image:: github-new-action-secret.png
      :alt: GitHub: Neues Action-Secret

#. Configure the GitHub action

   The HERMES project provides templates for continuous integration in a special
   repository: `hermes-hmc/ci-templates
   <https://github.com/hermes-hmc/ci-templates>`_. Copy the template file
   `TEMPLATE_hermes_github_to_zenodo.yml
   <https://github.com/hermes-hmc/ci-templates/blob/main/TEMPLATE_hermes_github_to_zenodo.yml>`_
   into the :file:`.github/workflows/` directory of your repository and rename
   it, for example to :file:`hermes_github_to_zenodo.yml`.

   Then you should go through the file and look for comments marked :samp:`#
   ADAPT`. Modify the file to suit your needs.

   Finally, add the workflow file to version control and push it to the GitHub
   server:

   .. code-block:: console

      $ git add .github/workflows/hermes_github_to_zenodo.yml
      $ git commit -m ":construction_worker: GitHub action for automatic publication with HERMES"
      $ git push

#. GitHub actions should be allowed to create pull requests in your repository

   The HERMES workflow will not publish metadata without your approval. Instead,
   it will create a pull request so that you can approve or change the metadata
   that is stored. To enable this, go to :menuselection:`Settings --> Actions
   --> General` in your repository and in the :guilabel:`Workflow permissions`
   section, enable :guilabel:`Allow GitHub Actions to create and approve pull
   requests`.
