.. SPDX-FileCopyrightText: 2021 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

CodeMeta
========


`CodeMeta <https://codemeta.github.io/>`__ provides a common metadata vocabulary
for software that supports research, citation and interoperability across
platforms. It is currently being used in major initiatives such as
`FAIRCORE4EOSC <https://faircore4eosc.eu>`_ to make research software FAIR
(Findable, Accessible, Interoperable, Reusable).

Using existing standards such as the Schema.org types `SoftwareApplication
<https://schema.org/SoftwareApplication>`_ and `SoftwareSourceCode
<https://schema.org/SoftwareSourceCode>`_, as well as JSON for Linking Data
(`JSON-LD <https://json-ld.org/>`_), CodeMeta identifies precisely the version
used in scientific and other research, thereby enabling the reproducibility of
results.

A :file:`codemeta.json` file is expected in the root directory of the software
repository. The file might look like this, for example:

.. code-block:: javascript

   {
       "@context": "https://w3id.org/codemeta/3.0",
       "type": "SoftwareSourceCode",
       "applicationCategory": "Universal",
       "author": [
           {
               "id": "http://orcid.org/0000-0002-1825-0097",
               "type": "Person",
               "affiliation": {
                   "type": "Organization",
                   "name": "Department of Research Software Engineering"
               },
               "email": "veit.schiele@example.org",
               "familyName": "Schiele",
               "givenName": "Veit"
           },
           {
               "type": "Role",
               "schema:author": "http://orcid.org/0000-0002-1825-0097",
               "roleName": "Developer"
           }
       ],
       "codeRepository": "git+https://github.com/cusy/my-research-tool.git",
       "dateCreated": "2026-09-07",
       "dateModified": "2026-09-07",
       "datePublished": "2026-09-07",
       "description": "My research tool reliably answers every question with 42.",
       "license": "https://spdx.org/licenses/BSD-3-Clause",
       "name": "My Research Tool",
       "operatingSystem": [
           "Linux",
           "Windows",
           "MacOS"
       ],
       "programmingLanguage": "Python",
       "releaseNotes": "Change log: this and that",
       "review": {
           "type": "Review",
           "reviewBody": "Review about my tool."
       },
       "softwareRequirements": "https://www.python.org/downloads/release/python-3147/",
       "version": "2026.1.0",
       "developmentStatus": "active",
       "issueTracker": "https://github.com/cusy/my-research-tool/issues",
       "referencePublication": "https://doi.org/10.1000/xyz123"
   }

.. seealso::
   * `The Research Software MetaData Guidelines for End-Users
     <https://fair-impact.github.io/RSMD-guidelines/>`_
   * `CodeMeta generator <https://codemeta.github.io/codemeta-generator/>`_
   * `Codemeta Terms <https://codemeta.github.io/terms/>`_
   * `GitHub Repository <https://github.com/codemeta/codemeta-generator/>`_
