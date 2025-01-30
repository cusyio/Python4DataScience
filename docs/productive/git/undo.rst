.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Undo changes
============

With Git 2.23, ``git restore`` was added for undoing file changes. Previously,
this task was performed by ``git reset``, which also has other tasks:

:samp:`$ git restore`
    changes files in the working directory to a state that was previously known
    to Git. By default, Git ``HEAD`` checks out the last commit of the current
    branch.

    .. note::

        In Git < 2.23, ``git restore`` is not yet available. In this case, you
        still need to use ``git checkout``:

       :samp:`$ git checkout {FILE}`

    :samp:`$ git restore [-S|--staged] {PATH/TO/FILE}`
        undoes the addition of files. The changes are retained in your workspace
        so that you can change and add them again if necessary.

        The command is equivalent to :samp:`$ git reset {PATH/TO/FILE}`.

    :samp:`$ git restore [-SW] {FILE}`
        undoes the addition and changes in the workspace.
    :samp:`$ git restore [-s|--source] {BRANCH} {FILE}`
        restores a change to the version in the :samp:`{BRANCH}`.
    :samp:`$ git restore [-s|--source] @~ {FILE}`
        restores a change to the previous commit.
    :samp:`$ git restore [-p|--patch]`
        lets you select the changes to be undone individually.

:samp:`$ git reset [--hard | --mixed | --soft | --keep] {TARGET_REFERENCE}`
    resets the history to an earlier commit.

    .. warning::
        The risk with ``reset`` is that work can be lost. Although commits are
        not deleted immediately, they can become orphaned so that there is no
        longer a direct path to them. They must then be found and restored
        promptly with :ref:`reflog` as Git usually deletes all orphaned commits
        after 30 days.

    .. code-block:: console

        $ git reset @~

    ``@~``
        cancels the last commit, whereby its changes are now transferred back to
        the stage area.

        If there are changes in the stage area, these are moved to the work
        area, for example:

        .. code-block:: console

            $ echo 'My first repo' > README.rst
            $ git add README.rst
            $ git status
            On branch main
            Changes marked for commit:
              (use "git rm --cached <Datei>..." to remove from staging area)
                New file:     README.rst
            $ git reset
            $ git status
            On branch main
            Unversioned files:
              (use "git add <file>...", to mark the changes for commit)
                README.rst

    ``@~3``
        takes back the last three commits.
    ``'@{u}'``
        takes the remote version (*upstream*) of the current branch.
    ``--hard``
        discards the changes in the staging and working area as well.

        .. code-block:: console

            $ git status
            On branch main
            Changes marked for commit:
              (use "git rm --cached <Datei>..." to remove from staging area)
                New file:     README.rst
            $ git reset --hard
            $ git status
            On branch main
            nothing to commit (create/copy files and use "git add" to version)

    ``--mixed``
        resets the stage area, but not the work area, so that the changed files
        are retained but not marked for commit.

        .. tip::
           I usually prefer ``--soft`` over ``--mixed``: it keeps the undone
           changes separate so that any additional changes are explicit. This is
           especially useful if you have changes to the same file in the stage
           and workspace.

    ``--soft``
        takes back the commits, but leaves the stage and workspace unchanged.

    ``--keep``
        resets the stage area and updates the files in the work area that differ
        between :samp:`COMMIT` and ``HEAD``, but retains those that differ
        between stage and work area, these are files with changes that have not
        yet been added. If a file that differs between :samp:`COMMIT` and stage
        area has unadded changes, ``reset`` will be cancelled.

        You can then deal with your uncommitted changes, perhaps undoing them
        with ``git restore`` or hiding them with ``git stash``, before trying
        again.

        .. tip::
           Many other guides recommend ``--hard`` for this task, probably
           because this mode has been around for a while. However, this mode is
           riskier because it irrevocably discards the changes not included in
           the commit without asking questions. However, I use ``--keep`` and if
           I want to discard all uncommitted changes before the ``reset``, I use
           ``git restore -SW``.

:samp:`$ git revert {COMMIT_SHA}`
    creates a new commit and reverts the changes of the specified commit so that
    the changes are inverted.
:samp:`$ git fetch --prune {REMOTE}`
    Remote refs are removed when they are removed from the remote repository.
:samp:`$ git commit --amend`
    updates and replaces the last commit with a new commit that combines all
    deployed changes with the contents of the previous commit. If nothing is
    provided, only the previous commit message is rewritten.

    ``--no-edit``
        skips the editing of the commit message.
    ``--date now``
        updates the commit date.

Reference for common reset commands
-----------------------------------

Undo all local changes to a branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ git reset --keep '@{u}'

Undo all commits in the current branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`git merge-base <https://git-scm.com/docs/git-merge-base>`_ selects the commit
where two branches have split. Pass ``@`` and ``main`` to select the commit
where the current branch is forked from ``main``. Reset it to undo all commits
on the local branch with:

.. code-block:: console

    $ git reset --soft $(git merge-base @ main)

Undo all changes in the current branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ git reset --keep main

Undo commit in the wrong branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have accidentally committed to an existing branch instead of creating a
new branch first, you can change this in the following three steps:

#. create a new branch with :samp:`$ git branch {NEW_BRANCH}`
#. Resets the last commit in your active branch with :samp:`$ git reset --keep
   @~`
#. Apply the changes to the new branch with :samp:`$ git switch {NEW_BRANCH}`

Restoring a deleted branch
~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have accidentally deleted an unmerged branch, you can recreate the
branch with the corresponding SHA:

.. code-block:: console

   $ git branch -D new-feature
   Branch new-feature entfernt (war d53e431).

The output contains the SHA commit to which the branch pointed. You can recreate
the branch with this SHA:

.. code-block:: console

   $ git branch new-feature d53e431

But what if you have deleted the branch and the corresponding terminal history
has been lost? To find the SHA again, you can pass the :ref:`reflog` output to
``grep``:

.. code-block:: console

   $ git reflog | grep -A 1 new-feature
   12bc4d4 HEAD@{0}: checkout: moving from new-feature to main
   d53e431 HEAD@{1}: commit: Add new feature
   12bc4d4 HEAD@{2}: checkout: moving from main to new-feature
   12bc4d4 HEAD@{3}: merge my-feature: Fast-forward

``-A 1`` displays an additional line after each hit. The output shows several
:ref:`reflog` entries that refer to the branch. The first entry shows a change
from ``new-feature`` to ``main``, with the commit SHA on ``main``. The entry
before it is the last change to ``new-feature`` with the SHA to restore:

.. code-block:: console

   $ git branch triceratops-enclosure 43f66f9

By default, you can save such a branch within 30 days after deleting the branch,
as ``gc.reflogExpireUnreachable`` is usually set to do so.

Undoing a commit change
~~~~~~~~~~~~~~~~~~~~~~~

Let’s return to the introductory example. Imagine you have made a commit and
changed it later. Then you realise that the change should be undone. How can you
proceed? If you can still see the original Git commit output in your terminal
history, you can retrieve the SHA from there and undo the change. But if this is
no longer possible, it’s time for the :ref:`reflog`. Check the reflog for the
branch:

.. code-block:: console

   $ git reflog my-feature-branch
   12bc4d4 (HEAD -> main, my-feature-branch) my-feature-branch@{0}: commit (amend): Add my feature and more
   982d93a my-feature-branch@{1}: commit: Add my feature
   900844a my-feature-branch@{2}: branch: Created from HEAD

The first entry, ``commit (amend)``, shows the creation of the amended commit.
The second entry shows the original commit, which we now want to return to with
a hard reset:

.. code-block:: console

   $ git reset --hard 982d93a

You may then want to restore the content of the changed commit in order to
correct it and change it again. Do this with git ``restore`` from the changed
commit SHA, which is at the top of the previous :ref:`reflog` output:

.. code-block:: console

   $ git restore -s 12bc4d4

Undoing a faulty rebase
~~~~~~~~~~~~~~~~~~~~~~~

Imagine you are working on a ``new-feature`` branch with three commits, of which
you want to undo the middle one:

.. code-block:: console

   $ git rebase -i main

.. code-block:: diff

    pick d53e431 Add new feature
   -pick 329271a More performant implementation for the new feature
   -pick 1d6c477 Add API docs

However, you have now inadvertently deleted the last commit. If you can no
longer see the SHA value in the terminal history, you can pass the :ref:`reflog`
output to ``grep`` again:

.. code-block:: console

   $ git reflog| grep 'API docs'
   1d6c477 HEAD@{2}: commit: Add API docs

With this SHA, the commit can now be restored with :doc:`advanced/cherry-pick`:

.. code-block:: console

   $ git cherry-pick 1d6c477

.. _git-filter-repo:

Remove a file from the history
------------------------------

A file can be completely removed from the current branches Git history. This is
necessary if, for example, you have accidentally added passwords or a very large
file to the repository.

To do this, you need to install `git-filter-repo
<https://github.com/newren/git-filter-repo>`__, for example with ``uv add
git-filter-repo``. Then you can delete your file, for example with
:samp:`{PATH/SOMEFILE}`:

.. code-block:: console

   $ git filter-repo --invert-paths --path PATH/SOMEFILE
   $ git push --no-verify --mirror

.. note::
   Inform the team members that they should create a clone of the repository
   again.

Remove a string from the history
--------------------------------

.. code-block:: console

    $ git filter-repo --message-callback 'return re.sub(b"^git-svn-id:.*\n", b"", message, flags=re.MULTILINE)'

.. seealso::
    * `git-filter-repo — Man Page <https://www.mankier.com/1/git-filter-repo>`_
    * `git-reflog <https://git-scm.com/docs/git-reflog>`_
    * `git-gc <https://git-scm.com/docs/git-gc>`_
