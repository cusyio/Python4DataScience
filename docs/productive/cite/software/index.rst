.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Cite software
=============

James Howison and Julia Bullard listed the following examples in descending
reputations in their 2016 article `Software in the scientific literature
<https://doi.org/10.1002/asi.23538>`_:

#. citing publications that describe the respective software
#. citing operating instructions
#. citing the software project website
#. link to a software project website
#. mention the software name

The situation remains unsatisfactory for the authors of software, especially if
they differ from the authors of the software description. Conversely, research
software is unfortunately not always well suited to being cited. For example,
others will hardly be able to cite your software directly if you send it to
them as an email attachment. Even a download link is not really useful here. It
is better to provide a `persistent identifier (PID)
<https://en.wikipedia.org/wiki/Persistent_identifier>`_ to ensure the long-term
availability of your software. Both `Zenodo <https://zenodo.org/>`__ and
`figshare <https://figshare.com/>`_ repositories accept source code including
binaries and provide `Digital Object Identifiers (DOI)
<https://en.wikipedia.org/wiki/Digital_object_identifier>`_ for them. The same
applies to `CiteAs <https://citeas.org/>`_, which can be used to retrieve
citation information for software.

.. seealso::
   * `Should I cite? <https://mr-c.github.io/shouldacite/index.html>`_
   * `How to cite software “correctly”
     <https://cite.research-software.org/>`_
   * Daniel S. Katz: `Compact identifiers for software: The last missing link in
     user-oriented software citation?
     <https://danielskatzblog.wordpress.com/2018/02/06/compact-identifiers-for-software-the-last-missing-link-in-user-oriented-software-citation/>`_
   * `Neil Chue Hong: How to cite software: current best practice
     <https://zenodo.org/records/2842910>`_
   * `Recognizing the value of software: a software citation guide
     <https://f1000research.com/articles/9-1257/v2>`_
   * Stephan Druskat, Radovan Bast, Neil Chue Hong, Alexander Konovalov, Andrew
     Rowley, Raniere Silva: `A standard format for CITATION files
     <https://www.software.ac.uk/blog/standard-format-citation-files>`_
   * `Module-5-Open-Research-Software-and-Open-Source
     <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source/blob/master/content_development/README.md/>`_
   * Software Heritage: `Save and reference research software
     <https://www.softwareheritage.org/save-and-reference-research-software/>`_
   * `Mining software metadata for 80 M projects and even more
     <https://www.softwareheritage.org/2019/05/28/mining-software-metadata-for-80-m-projects-and-even-more/>`_
   * `Extensions to schema.org to support structured, semantic, and executable
     documents <https://github.com/stencila/schema>`_
   * `Guide to Citation File Format schema
     <https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md>`_
   * `schema.json
     <https://github.com/citation-file-format/citation-file-format/blob/main/schema.json>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    doi

Metadata formats
----------------

The `FORCE11 <https://force11.org/group/software-citation-working-group>`_
working group has published a paper in which the principles of scientific
software citation are presented: `FORCE11 Software Citation Working Group
<https://peerj.com/articles/cs-86/>`_ by Arfon Smith, Daniel Katz and Kyle
Niemeyer 2016. Two projects are currently emerging for structured metadata:

:doc:`codemeta`
    is an exchange scheme for general software metadata and reference
    implementation for JSON for Linking Data
    (`JSON-LD <https://json-ld.org/>`_).
:doc:`cff`
    is a scheme for software citation metadata in machine-readable
    :doc:`/data-processing/serialisation-formats/yaml/index` format.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    codemeta
    cff

Tools
-----

:doc:`git2prov`
    generates PROV data from the information in a Git repository.
:doc:`hermes`
    simplifies the publication of research software by continuously retrieving
    existing metadata in :doc:`cff`, :doc:`codemeta` and :doc:`Git
    <../../git/index>`.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    git2prov
    hermes
