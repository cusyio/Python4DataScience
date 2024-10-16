.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Citation File Format
====================

`Citation File Format <https://citation-file-format.github.io/>`_ is a scheme
for software citation metadata in machine-readable
:doc:`/data-processing/serialisation-formats/yaml/index` format.

A file ``CITATION.cff`` should be stored in the root directory of the software
repository.

The content of the file can look like this:

.. code-block::

    cff-version: "1.1.0"
    message: "If you use this tutorial, please cite it as below."
    authors:
      -
        family-names: Schiele
        given-names: Veit
        orcid: "https://orcid.org/https://orcid.org/0000-0002-2448-8958"
    identifiers:
      -
        type: doi
        value: "10.5281/zenodo.4147287"
    keywords:
      - "data-science"
      - jupyter
      - "jupyter-notebooks"
      - "jupyter-kernels"
      - ipython
      - pandas
      - spack
      - uv
      - ipywidgets
      - "ipython-widget"
      - dvc
    title: "Jupyter tutorial"
    version: "0.8.0"
    date-released: 2020-10-08
    license: "BSD-3-Clause"
    repository-code: "https://github.com/veit/jupyter-tutorial"

You can easily adapt the example above to create your own ``CITATION.cff`` file
or use the `cffinit
<https://citation-file-format.github.io/cff-initializer-javascript/>`_ website.

With `cff-validator <https://github.com/marketplace/actions/cff-validator>`_ you
have a GitHub action that checks ``CITATION.cff`` files with the R package
``V8``.
