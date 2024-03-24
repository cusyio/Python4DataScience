.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git Notes
=========

`Git Notes <https://git-scm.com/docs/git-notes>`_ add text notes to commits,
tags and other objects. Such notes can contain all kinds of metadata, for
example comments on code review, links to bug reports, :abbr:`etc (et cetera)`:

#. Add a git note:

   .. code-block:: console

      $ git notes add -m 'Example note'

#. Display a git note:

   .. code-block:: console

      $ git log
      commit 859de540cda23f510f4ecbe0f38d07666e933f08 (HEAD -> main)
      Author: Veit Schiele <veit@cusy.io>
      Date:   Sun Mar 24 11:17:56 2024 +0100

          A commit message

      Notes:
          Example note

#. Change a git note:

   .. code-block:: console

      $ git notes edit

However, Git notes are not sent to the remote repository with ``git push`` or
``git pull`` by default; they must be synchronised with ``git push origin
'refs/notes/*'`` and ``git fetch origin 'refs/notes/*:refs/notes/*'``.

.. warning::
   Do not use ``git pull`` instead of ``git fetch``: you will not be able to
   merge ``refs/notes/commits`` with your current branch.

.. note::
   Git notes are not included in the git commit history, so they cannot be used
   for regulatory purposes where provenance, non-repudiation or tamper
   resistance must be proven. However, they can be useful for build tags and
   similar.

.. seealso::
   * `Git Notes: Git’s Coolest, Most Unloved­ Feature
     <https://tylercipriani.com/blog/2022/11/19/git-notes-gits-coolest-most-unloved-feature/>`_
   * `git-appraise <https://github.com/google/git-appraise>`_
   * `github-issues-git-notes
     <https://github.com/TomasHubelbauer/github-issues-git-notes>`_
