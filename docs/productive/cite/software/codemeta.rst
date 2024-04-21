.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

CodeMeta
========

`CodeMeta <https://codemeta.github.io/>`__ is an exchange scheme for general
software metadata and reference implementation for JSON for Linking Data
(`JSON-LD <https://json-ld.org/>`_).

A ``codemeta.json`` file is expected in the root directory of the software
repository. The file can look like this:

.. code-block:: javascript

    {
        "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
        "@type": "SoftwareSourceCode",
        "author": [{
            "@type": "Person",
            "givenName": "Stephan",
            "familyName": "Druskat",
            "@id": "http://orcid.org/0000-0003-4925-7248"
        }],
        "name": "My Research Tool",
        "softwareVersion": "2.0",
        "identifier": "https://doi.org/10.5281/zenodo.1234",
        "datePublished": "2017-12-18",
        "codeRepository": "https://github.com/research-software/my-research-tool"
    }

.. seealso::
    * `CodeMeta generator <https://codemeta.github.io/codemeta-generator/>`_
    * `Codemeta Terms <https://codemeta.github.io/terms/>`_
    * `GitHub Repository
      <https://github.com/codemeta/codemeta-generator/>`_
