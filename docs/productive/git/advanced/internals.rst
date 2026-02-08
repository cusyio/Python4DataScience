.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git Internals
=============

So far, we have looked at how you can use Git to manage the different states of
your code. Now we want to show you the :ref:`data <git-data-model>` and
:ref:`storage models <git-storage-model>` that underlie Git.

Data Model
----------

You will be able to use Git more effectively once you understand the data model.
Git manages four types of data:

Objects
~~~~~~~

.. include:: ../glossary.rst
   :start-after: start-object
   :end-before: end-object

Commit
::::::

.. include:: ../glossary.rst
   :start-after: start-commit
   :end-before: end-commit

Tree
::::

.. include:: ../glossary.rst
   :start-after: start-tree
   :end-before: end-tree

Blob
::::

.. include:: ../glossary.rst
   :start-after: start-blob
   :end-before: end-blob

Tag
:::

.. include:: ../glossary.rst
   :start-after: start-tag
   :end-before: end-tag

References
~~~~~~~~~~

.. include:: ../glossary.rst
   :start-after: start-refs
   :end-before: end-refs

Index
~~~~~

.. include:: ../glossary.rst
   :start-after: start-index
   :end-before: end-index

Reflog
~~~~~~

.. include:: ../glossary.rst
   :start-after: start-reflog
   :end-before: end-reflog

.. _git-storage-model:

Storage model
-------------

.. seealso::
   * Git’s database internals

     * `Part I: packed object store
       <https://github.blog/open-source/git/gits-database-internals-i-packed-object-store/>`_
     * `Part II: commit history queries
       <https://github.blog/open-source/git/gits-database-internals-ii-commit-history-queries/>`_
     * `Part III: file history queries
       <https://github.blog/open-source/git/gits-database-internals-iii-file-history-queries/>`_
     * `Part IV: distributed synchronization
       <https://github.blog/open-source/git/gits-database-internals-iv-distributed-synchronization/>`_
     * `Part V: scalability
       <https://github.blog/open-source/git/gits-database-internals-v-scalability/>`_

Packfiles
~~~~~~~~~

.. include:: ../glossary.rst
   :start-after: start-packfile
   :end-before: end-packfile
