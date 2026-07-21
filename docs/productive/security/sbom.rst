.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Software Bill of Materials (SBOM)
=================================

A Software Bill of Materials (SBOM) is a document used to exchange information
about software and its composition. This format is primarily used in the
security field to check software and its dependencies for vulnerabilities using
vulnerability databases such as `CVE <https://www.cve.org/>`_ and `OSV
<https://osv.dev/>`_. The SBOM format used by the CPython project is `SPDX
<https://spdx.github.io/spdx-spec/v3.0.1/model/Software/Classes/Sbom/>`_, which
can be converted to other formats as needed. The SBOM file for the dependencies
included in CPython is maintained at `Misc/sbom.spdx.json
<https://github.com/python/cpython/blob/main/Misc/sbom.spdx.json>`_. The file is
generated using `Tools/build/generate_sbom.py
<https://github.com/python/cpython/blob/main/Tools/build/generate_sbom.py>`_.

Generating an SBOM File
-----------------------

… with uv
~~~~~~~~~

:term:`uv` provides an easy way to generate an SBOM file in the CycloneDX v1.5
format using:

.. code-block:: console

   $ uv export --format='cyclonedx1.5' > sbom.cdx.json

However, the file contains only very basic information; for example, for
`cusy.tasks <https://github.com/cusyio/cusy.tasks>`_:

.. code-block:: json

    "component": {
      "type": "library",
      "bom-ref": "cusy-tasks-1@26.2.0",
      "name": "cusy-tasks",
      "version": "26.2.0",
      "properties": [
        {
          "name": "uv:package:is_project_root",
          "value": "true"
        }
      ]
    }

Using ``uv export --all-groups --format='cyclonedx1.5' > sbom.cdx.json``, you
can also include all dependency groups in the SBOM file.

… using CycloneDX Python
~~~~~~~~~~~~~~~~~~~~~~~~

The output from `CycloneDX Python
<https://cyclonedx-bom-tool.readthedocs.io/en/latest/index.html>`_ is
considerably more comprehensive:

.. code-block:: json

    {
      "bom-ref": "cusy-tasks==26.2.0",
      "description": "",
      "externalReferences": [
        {
          "comment": "PackageSource: Local",
          "type": "distribution",
          "url": "file:///Users/veit/cusy/prj/cusy.tasks"
        },
        {
          "comment": "from packaging metadata Project-URL: Documentation",
          "type": "documentation",
          "url": "https://tasks.cusy.io/"
        },
        {
          "comment": "from packaging metadata Project-URL: Mastodon",
          "type": "other",
          "url": "https://mastodon.social/@Python4DataScience"
        },
        {
          "comment": "from packaging metadata Project-URL: GitHub",
          "type": "vcs",
          "url": "https://github.com/cusyio/cusy.tasks"
        }
      ],
      "licenses": [
        {
          "license": {
            "acknowledgement": "declared",
            "id": "BSD-3-Clause"
          }
        }
      ],
      "name": "cusy-tasks",
      "type": "library",
      "version": "26.2.0"
    }

The command to generate the file is:

.. code-block:: console

   $ uvx --from cyclonedx-bom cyclonedx-py environment .venv --output-file sbom.cdx.json

.. warning::
   CycloneDX Python generates the SBOM file from the current :file:`.venv`
   directory. So if you run ``cyclonedx-bom`` in your development environment,
   you will also find all your development tools listed in your SBOM file.

… with sbomify
~~~~~~~~~~~~~~

sbomify provides a GitHub Action for generating the SBOM file, which uses
CycloneDX Python under the bonnet. The file can then be attested using
`actions/attest-sbom <https://github.com/actions/attest-sbom>`_:

.. literalinclude:: sbomify.yml
   :caption: .github/workflows/sbomify.yml
   :language: yaml

In GitLab CI, you can use sbomify as follows:

.. literalinclude:: .gitlab-ci.yml
   :caption: .gitlab-ci.yml
   :language: yaml
   :lines: 1-12, 32-

You can also integrate dependency scanning:

.. literalinclude:: .gitlab-ci.yml
   :caption: .gitlab-ci.yml
   :language: yaml
   :lines: 13-30

.. seealso::
   * `SBOM Generation in CI/CD Pipelines <https://sbomify.com/guides/ci-cd/>`_
   * `Dependency scanning by using SBOM
     <https://docs.gitlab.com/user/application_security/dependency_scanning/dependency_scanning_sbom/>`_

PEP 770 – SBOMs in Python packages
----------------------------------

:pep:`770` standardises the inclusion of SBOMs in Python wheels via the
:file:`.dist-info/sboms/` directory. If you publish Python packages on
:term:`PyPI`, this means that your users will automatically receive the SBOM
file when they install your package, for example:

.. code-block:: console

   myapp-26.2.0.dist-info
   ├── METADATA
   ├── RECORD
   └── sboms/
       └── myapp.cdx.json

Build backends such as Hatchling ≥ 1.28 already support this via the
``sbom-files`` configuration:

.. code-block:: toml
   :caption: pyproject.toml

   [tool.hatch.build.targets.wheel]
   sbom-files = ["myapp.cdx.json"]

Instead of generating the SBOM file from scratch during the build, a minimal
CycloneDX SBOM file can be checked into the repository:

.. code-block:: json

   {
     "bomFormat": "CycloneDX",
     "specVersion": "1.6",
     "version": 1,
     "metadata": {
       "component": {
         "type": "library",
         "name": "mylib",
         "version": "0.0.0-placeholder"
       }
     },
     "components": []
   }

In the :term:`CI` workflow, the placeholder SBOM file is then checked out along
with the code. sbomify then enriches it with the latest information. Hatchling
subsequently builds the wheel using the latest SBOM file, and finally the :term:`wheel` is published to :term:`PyPI`.

Analysis
--------

There are numerous tools available for security and licence checks, each
focusing on different problem areas. Two open-source tools for SBOM analysis are
`Dependency Track <https://dependencytrack.org>`_ and `GUAC <https://guac.sh>`_.
With ``sbomify-action``, you can upload SBOMs directly from the :term:`CI`
pipeline to your Dependency Track instance using:

.. code-block:: yaml

   UPLOAD_DESTINATIONS=dependency-track
