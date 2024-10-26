.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-FileContributor: Modified by Kristian Rother
..
.. SPDX-License-Identifier: BSD-3-Clause

Workspaces
==========

.. figure:: git-workspaces.svg
   :alt: Git workspaces

Git manages multiple locations or **workspaces** where files are stored:

local working copy
    contains files and folders that can be edited normally.
staging area
    contains changes to files that are scheduled for writing into the version
    history.
local repository
    contains the entire history of all files in the project.
remote repository
    also contains the entire history, but is stored on a remote server.
stash
    contains changes that are temporarily stored somewhere else to move them out
    of the way.

Basic Git commands
------------------

The following basic Git commands move changes between these workspaces.

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
