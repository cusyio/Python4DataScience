.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Quick start
===========

.. _badges:

Status
------

.. image:: https://img.shields.io/github/contributors/cusyio/python4datascience.svg
   :alt: Contributors
   :target: https://github.com/cusyio/python4datascience/graphs/contributors
.. image:: https://img.shields.io/github/license/cusyio/Python4DataScience.svg
   :alt: License
   :target: https://github.com/cusyio/python4datascience/blob/main/LICENSE
.. image:: https://results.pre-commit.ci/badge/github/cusyio/Python4DataScience/main.svg
   :target: https://results.pre-commit.ci/repo/github/649815375
   :alt: pre-commit.ci status
.. image:: https://readthedocs.org/projects/python4datascience/badge/?version=latest
   :alt: Docs
   :target: https://www.python4data.science/en/latest/
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo..14031392.svg
   :target: https://doi.org/10.5281/zenodo.14031392
.. image:: https://img.shields.io/badge/dynamic/json?label=Mastodon&query=totalItems&url=https%3A%2F%2Fmastodon.social%2F@Python4DataScience%2Ffollowers.json&logo=mastodon
   :alt: Mastodon
   :target: https://mastodon.social/@Python4DataScience

.. _first-steps:

Overview
--------

This repository contains a data management and analysis tutorial using Python.
The folders contain:

- ``data/`` - data for an example project
- ``docs/`` - the actual tutorial docs
- ``fastapi/`` - example web server providing data


Installation
------------

#. Download and unpack:

   .. code-block:: console

    $ curl -O https://codeload.github.com/cusyio/python4datascience/zip/main
    $ unzip main
    Archive:  main
    …
       creating: python4datascience-main/
    …

#. Install Python packages:

   .. code-block:: console

    $ cd python4datascience-main
    $ python3 -m venv .venv
    $ . .venv/bin/activate
    $ python -m pip install -e ".[dev]"

#. Install the `Jupyter Notebook Extensions
   <https://jupyter-contrib-nbextensions.readthedocs.io/>`_ Javascript and CSS
   files:

   .. code-block:: console

    $ jupyter contrib nbextension install --user
    jupyter contrib nbextension install --user
    Installing jupyter_contrib_nbextensions nbextension files to jupyter data directory
    …
    Successfully installed jupyter-contrib-core-0.3.3 jupyter-contrib-nbextensions-0.5.1
    jupyter-highlight-selected-word-0.2.0 jupyter-latex-envs-1.4.6
    jupyter-nbextensions-configurator-0.4.1
    …
    $ jupyter nbextension enable latex_envs --user --py
    Enabling notebook extension latex_envs/latex_envs...
          - Validating: OK

#. Create HTML documentation:

   Note that pandoc has to be installed. On Debian/Ubuntu you can just run

   .. code-block:: console

    $  sudo apt-get install pandoc

   To create the HTML documentation run these commands:

    $ cd docs
    $ make html

#. Create a PDF:

   For the creation of a PDF file you need additional packages.

   For Debian/Ubuntu you get them with the following command:

   .. code-block:: console

    $ sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   or for macOS with:

   .. code-block:: console

    $ brew cask install mactex
    …
    🍺  mactex was successfully installed!
    $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
    $ sudo texlua install-getnonfreefonts
    …
    mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
    mktexlsr: Done.

   Then you can generate a PDF with:

   .. code-block:: console

    $ make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   You can find the PDF at ``docs/_build/latex/jupytertutorial.pdf``.

#. Install and run ale to check spelling

   You can install Vale with:

   .. code-block:: console

    $ brew install vale

   You can install the parser for reStructuredText with:

   .. code-block:: console

    $ brew install docutils

   .. seealso::
      * `Vale installation <https://docs.errata.ai/vale/install>`_
      * `Vale formats <https://docs.errata.ai/vale/scoping#formats>`_

   Now you can check the reStructuredText files with:

   .. code-block:: console

    $ vale .
    ✔ 0 errors, 0 warnings and 0 suggestions in 201 files.

.. _follow-us:

Follow us
---------

* `GitHub <https://github.com/cusyio/python4datascience>`_
* `Mastodon <https://mastodon.social/@Python4DataScience>`_

Pull-Requests
-------------

If you have suggestions for improvements and additions, we recommend that you
create a `Fork <https://github.com/cusyio/python4datascience/fork>`_ of our
`GitHub Repository <https://github.com/cusyio/python4datascience/>`_ and make
your changes there. You are also welcome to make a *pull request*. If the
changes contained therein are small and atomic, we will be happy to look at your
suggestions.

The following guidelines help us to maintain the German translation of the
tutorial:

* Write commit messages in English
* Start commit messages with a `Gitmoji <https://gitmoji.dev/>`__
* Stick to English names of files and folders.
