.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Advanced Git
============

:doc:`git cherry-pick <cherry-pick>`
    allows you to append any Git commit to the current ``HEAD`` based on its
    hash value.
:doc:`git bisect <bisect>`
    allows you to quickly find a Git commit that has introduced a regression.
:doc:`git notes <notes>`
    adds text notes to commits, tags and other objects.
:doc:`hooks/index`
    are scripts that are automatically executed when certain events occur in a
    Git repository.
:doc:`Jupyter Notebooks <jupyter-notebooks>`
    can lead to problems when managing with Git.
:doc:`Binärdateien <binary-files>`
    can be configured in Git so that meaningful diffs are displayed.
:doc:`batch`
    can process files from a Git repository together.
:doc:`vs-code/index`
    can use an existing Git installation to provide the corresponding
    functionalities.
:doc:`gitlab/index`
    is a web application for version management based on Git.
:doc:`git-big-picture`
    visualises Git repositories as :abbr:`DAGs (directed acyclic graph)`.
:doc:`etckeeper`
    is a collection of tools that can be used to manage the :file:`/etc`
    directory in a Git repository.
:doc:`internals`
    refers to articles on Git’s database internals.

.. toctree::
   :hidden:

   cherry-pick
   bisect
   notes
   hooks/index
   jupyter-notebooks
   binary-files
   batch
   lfs
   vs-code/index
   gitlab/index
   git-big-picture
   etckeeper
   internals
