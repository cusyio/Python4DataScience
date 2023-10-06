.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Workspaces
==========

.. figure:: git-workspaces.png
   :alt: Git workspaces

``git add``
    adds files from the working directory to the staging area.
``git reset HEAD``
    restores a file in the work area from the stage area.
``git stash``
    moves files from the workspace to a stash.
``git stash pop``
    brings files from the stash to the work area.
``git commit``
    writes changes from the staging area to the local repository.
``git pull``
    copies changes from the remote to the local repository and updates the work area.
``git push``
    copies changes from the local repository to the remote repository.

    :samp:`git push -u {UPSTREAM} {BRANCHNAME}`
        ``-u`` (long form ``--set-upstream``)
          allows to specify the remote repository and a branch in it.

        :samp:`{UPSTREAM}`
            the name of the remote repository, typically ``origin``.

        :samp:`{BRANCHNAME}`
            the name of a branch in the remote repository,
            typically the same as in the local repository.
