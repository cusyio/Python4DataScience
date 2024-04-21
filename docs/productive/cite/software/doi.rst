.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Create a DOI with Zenodo
========================

`Zenodo <https://zenodo.org/>`__ enables software to be archived and a DOI to be
provided for it. In the following I will show which steps are required on the
example of the Jupyter tutorial:

#. If you haven’t already, `create an account on Zenodo
   <https://zenodo.org/signup/>`_, preferably with GitHub.

#. In :menuselection:`Upload --> New Upload` under :guilabel:`Basic information`
   activate the button :guilabel:`Reserve DOI` to reserve a :abbr:`DOI (Digital
   Object Identifier)` for your upload. Leave the form open to upload your
   software later.

#. Create or modify the :doc:`codemeta`- und :doc:`cff` files in your software
   directory.

#. Include the badge in the :file:`README` file of your software:

   Markdown:

   .. code-block:: md

      [![DOI](https://zenodo.org/badge/307380211.svg)](https://zenodo.org/badge/latestdoi/307380211)

   reStructedText:

   .. code-block:: rst

      .. image:: https://zenodo.org/badge/307380211.svg
         :target: https://zenodo.org/badge/latestdoi/307380211

#. Now select the repository that you want to archive:

   .. figure:: zenodo-github.png
      :alt: Enable repositories for Zenodo

#. Check whether Zenodo has created a webhook in your repository for the
   *Releases* event:

   .. figure:: zenodo-webhook.png
      :alt: Zenodo webhook

#. Create a new release:

   .. figure:: github-release.png
      :alt: Github releases
