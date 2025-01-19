.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git branches
============

:samp:`$ git branch [-a] [-l "{GLOB_PATTERN}"]`
    shows all local branches in a repository.

    ``-a``
        also shows all removed branches.
    ``-l``
        restricts the branches to those that correspond to a specific pattern.

:samp:`$ git branch --sort=-committerdate`
    sorts the branches according to the commit date.

    You can also use :samp:`git config --global branch.sort -committerdate` to
    make this setting your default setting.

:samp:`$ git branch {BRANCH_NAME}`
    creates a new branch based on the current ``HEAD``.

:samp:`$ git switch [-c] {BRANCH_NAME}`
    switches between branches.

    ``-c``
        creates the branch to switch to.

:samp:`$ git switch -`
    alternates between the last two branches. This makes it much easier to jump
    back and forth between branches.

    .. note::

       In Git < 2.23, ``git switch`` is not yet available. In this case you
       still need to use ``git checkout``:

       :samp:`$ git checkout [-b] [{BRANCH_NAME}]`
           changes the working directory to the specified branch.

           ``-b``
               creates the specified branch if it does not already exist.

:samp:`$ git merge {FROM_BRANCH_NAME}`
    connects the specified branch with the branch you are currently in, for
    example:

    .. code-block:: console

       $ git switch main
       $ git merge hotfix
       Updating f42c576..3a0874c
       Fast forward
        setup.py |    1 -
        1 files changed, 0 insertions(+), 1 deletions(-)

    ``Fast forward``
        means that the new commit immediately followed the original commit and
        so the branch pointer only had to be continued.

        In other cases the output can look like this:

        .. code-block:: console

           $ git switch main
           $ git merge 'my-feature'
           Merge made by recursive.
            setup.py |    1 +
            1 files changed, 1 insertions(+), 0 deletions(-)

    ``recursive``
        is a merge strategy that is used when the merge is only to be done to
        ``HEAD``.

.. _merge-conflicts:

Merge conflicts
---------------

Occasionally, however, Git runs into issues with merging, such as:

.. code-block:: console

   $ git merge 'my-feature'
   Auto-merging setup.py
   CONFLICT (content): Merge conflict in setup.py
   Automatic merge failed; fix conflicts and then commit the result.

The history can then look like this, for example:

.. code-block:: console

   *   49770a2 (HEAD -> main) Fix merge conflict with my-feature
   |\
   | * 9412467 (my-feature) My feature
   * | 46ab1a2 Hotfix directly in main
   |/
   * 0c65f04 Initial commit

.. seealso::

   * `Git Branching - Basic Branching and Merging
     <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging>`_
   * `Git Tools - Advanced Merging
     <https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging>`_

Improved conflict display with zdiff3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git normally displays merge conflicts as follows:

.. code-block:: console

   <<<<<<< HEAD
   This line has been changed by feature one.
   This line has also been changed by feature one.
   This line will be changed by feature two.
   =======
   This line is changed by feature one.
   This line has been changed by feature two.
   This line has also been changed by feature two.
   >>>>>>> feature_two

The lines of the merge target are located between the markers ``<<<<<<<`` and
``=======``. The lines between the markers ``=======`` and ``>>>>>>>`` are the
lines of the merge source. The labels after the arrow markers name the commit
references that are merged.

This is often sufficient to resolve a conflict. But it can also be unnecessarily
challenging because the original lines from which both sides started are
missing. The common ground from which both sides started creates clarity about
the context in which both changes arose.

If you set `merge.conflictStyle
<https://git-scm.com/docs/git-config#Documentation/git-config.txt-mergeconflictStyle>`_
to ``zdiff3``, you can also display the common basis:

.. code-block:: console

   $ git config --global merge.conflictStyle zdiff3

Here is the same merge with this style:

.. code-block:: console

   <<<<<<< HEAD
   This line has been changed by feature one.
   This line has also been changed by feature one.
   This line will be changed by feature two.
   ||||||| 45d92bd
   This line is changed by feature one.
   This line will be changed by feature one and feature two.
   This line will be changed by feature two.
   =======
   This line is changed by feature one.
   This line has been changed by feature two.
   This line has also been changed by feature two.

The common base is now displayed between the markers ``|||||||`` and
``=======`` with the SHA value of the common base. This additional context is
often useful for resolving a conflict.

``rerere`` to reuse recorded conflict resolutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:abbr:`rerere (reuse recorded resolutions)` makes it easier for you to have to
resolve the same merge conflicts again and again. This can happen, for example,
if you merge a commit into several branches or if you have to rebase a branch
repeatedly. Resolving merge conflicts requires concentration and energy, and it
is a waste to resolve the same conflict again and again. `git rerere
<https://git-scm.com/docs/git-rerere>`_ is rarely called directly, however, but
is usually activated globally. It is then automatically used by ``git merge``,
``git rebase`` and ``git commit``. Its most important effect is that it adds
some messages to the output of these commands. You can activate it with:

.. code-block:: console

   $ git config --global rerere.enabled true

Let’s look at an example of ``git rerere`` in action. Suppose you attempt a
merge and run into conflicts:

.. code-block:: console

   % git merge rerere-example
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Recorded preimage for 'README.md'
   Automatic merge failed; fix conflicts and then commit the result.

``git rerere`` wrote the third line, ``Preimage for 'README.md'``, meaning that
the conflict was recorded before we fixed it. If we fix the conflict now, we can
proceed with the merge, in our example with:

.. code-block:: console

   $ git add README.md
   $ git merge --continue
   Recorded resolution for 'README.md'.
   [main 5935d00] Merge branch 'rerere-example'

``git rerere`` now reports ``conflict resolution recorded for 'README.md'.``,
meaning that it has saved how we resolved the conflicts in this file. Suppose
you undo this merge because you realise that it was not finished:

.. code-block:: console

   $ git reset --keep @~

Later you repeat the merging process:

.. code-block:: console

   $ git merge rerere-example
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   Resolved 'README.md' using previous resolution.
   Automatic merge failed; fix conflicts and then commit the result.
   When finished, apply stashed changes with `git stash pop`

``git rerere`` solved the conflict using the previous solution, which means it
reused your previous merge. Now check that the file is correct and then
continue:

.. code-block:: console

   $ git add README.md
   $ git merge --continue
   [main c922b21] Merge branch 'rerere-example'

``git rerere`` saves its data within the :file:`.git` directory of your Git
repository in an :file:`rr-cache` directory. You should note two things here:

#. The rerere cache is local. It is not shared when you perform a ``git push``,
   so your team colleagues cannot reuse the merges you have performed.
#. Git’s automatic garbage collection deletes entries from the :file:`rr-cache`.
   It is controlled by two configuration options:

   `gc.rerereResolved <https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrerereResolved>`_
       determines how long entries for resolved conflicts are kept. The default
       value is 60 days. And with git ``config gc.rerereResolved`` you can
       change the default values for your project.
   `gc.rerereUnresolved <https://git-scm.com/docs/git-config#Documentation/git-config.txt-gcrerereUnresolved>`_
       determines how long entries for unresolved conflicts are kept. The
       default value is 15 days.

Delete branches
---------------

:samp:`$ git branch -d [{BRANCH_NAME}]`
    deletes the selected branch if it has already been transferred to another.

    ``-D`` instead of ``-d`` forcing the deletion.

.. seealso::
   * `Git Branching - Branches in a Nutshell
     <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`_

Remote branches
---------------

So far, these examples have all shown local branches. However, the git branch
command also works with remote branches. To work with remote branches, a remote
repository must first be configured and added to the local repository
configuration:

:samp:`$ git remote add origin https://ce.cusy.io/veit/{NEWREPO}.git`

Add remote branches
~~~~~~~~~~~~~~~~~~~

Now the branch can also be added to the remote repository:

:samp:`$ git push origin [{BRANCH_NAME}]`

With ``git branch -d`` you delete the branches locally only. To delete them on
the remote server as well, you can type the following:

:samp:`$ git push --set-upstream origin [{BRANCH_NAME}]`

If you want to add all branches of a local repository to the remote repo, you
can do this with:

:samp:`$ git push --set-upstream origin --all`

You can configure the following so that this happens automatically for branches
without a tracking upstream:

.. code-block:: console

   $ git config --global push.autoSetupRemote true

Delete remote branches
~~~~~~~~~~~~~~~~~~~~~~

To remove remote branches locally, you can run ``git fetch`` with the
``--prune`` or ``-p`` option. You can also make this the default behaviour by
enabling ``fetch.prune``:

.. code-block:: console

   $ git config --global fetch.prune true

.. seealso::
   `PRUNING <https://git-scm.com/docs/git-fetch#_pruning>`_

Rename branches
---------------

You can rename branches, for example with

.. code-block:: console

   $ git branch --move master main

This changes your local ``master`` branch to ``main``. In order for others to
see the new branch, you must push it to the remote server. This will make the
``main`` branch available on the remote server:

.. code-block:: console

   $ git push origin main

The current state of your repository may now look like this:

.. code-block:: console

   $ git branch -a
   * main
     remotes/origin/HEAD -> origin/master
     remotes/origin/main
     remotes/origin/master

* Your local ``master`` branch has disappeared because it has been replaced by
  the ``main`` branch.
* The ``main`` branch is also present on the remote computer.
* However, the ``master`` branch is also still present on the remote server. So
  presumably others will continue to use the the ``master`` branch for their
  work until you make the following changes:

  * For all projects that depend on this project, the code and/or configuration
    must be updated.
  * The test-runner configuration files may need to be updated.
  * Build and release scripts need to be adjusted.
  * The settings on your repository server, such as the default branch of the
    repository, merge rules and others, need to be adjusted.
  * References to the old branch in the documentation need to be updated.
  * Any pull or merge requests that target the ``master`` branch should be
    closed.

After you have done all these tasks and are sure that the ``main`` branch works
the same as the ``master`` branch, you can delete the ``master`` branch:

.. code-block:: console

   $ git push origin --delete master

Team members can delete their locally still existing references to the
``master`` branch with

.. code-block:: console

   $ git fetch origin --prune
