.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git rebase
==========

The commands ``git rebase`` and ``git merge`` allow you to merge
:doc:`branch`. While ``git merge`` is always a moving forward change approach,
``git rebase`` has powerful history rewrite functions.
Here we take a look at its configuration, use cases and pitfalls.

In doing so, ``git rebase`` moves a sequence of commits to a new base commit and
can be useful for :doc:`workflows/feature-branches` workflows. Internally, Git
achieves this by creating new commits and applying them to the specified base;
so the same-looking commits from branches are entirely new commits.

The main reason for ``git rebase`` is to maintain a linear project progression.
If the main branch has evolved since you started working on a feature branch,
you might want to keep the latest updates to the main branch in your feature
branch, but keep the history of your branch clean. This would have the advantage
that you could later do a clean ``git merge`` of your functional branch into the
main branch. This *clean history* also makes it easier for you to find a
regression with :doc:`advanced/bisect`. A more realistic scenario would be the
following:

#. An error is found in the main branch in a function that once worked without
   errors.
#. With the *clean history* of the main branch, :doc:`log` should allow for
   quick conclusions.
#. If :doc:`log` does not lead to the desired result, :doc:`git bisect
   <advanced/bisect>` will probably help. In this case, the clean Git history
   helps ``git bisect`` in the search for the regression.

.. warning::
   The published history should only be changed in very rare exceptional cases,
   as the old commits would be replaced by new ones and it would look as if
   this part of the project history had suddenly disappeared.

.. seealso::
   `git rebase: what can go wrong?
   <https://jvns.ca/blog/2023/11/06/rebasing-what-can-go-wrong-/#undoing-a-rebase-is-hard>`_

.. note::
   ``git rebase`` is also covered briefly in :doc:`advanced/jupyter-notebooks`
   and :doc:`workflows/feature-branches`.

Rebasing dependent branches with ``–update-refs``
-------------------------------------------------

When you are working on a large feature, it is often helpful to spread the work
over several branches that build on each other.

However, these branches can be cumbersome to manage if you need to overwrite the
history in an earlier branch. Since each branch depends on the previous
branches, rewriting commits in one branch will result in subsequent branches no
longer being connected to the history.

Git 2.38 ships with a new ``--update-refs`` option for ``git rebase`` that will
perform such updates for you without you having to manually update each branch
and without subsequent branches losing their history.

If you want to use this option on every rebase, you can run ``git config
--global rebase.updateRefs true`` to make Git behave as if the ``--update-refs``
option is always specified.

.. seealso::
   `rebase: add --update-refs option
   <https://lore.kernel.org/git/3ec2cc922f971af4e4a558188cf139cc0c0150d6.1657631226.git.gitgitgadget@gmail.com/>`_


Delete commits with ``git rebase``
----------------------------------

This can also be easily realised with ``git rebase``, whereby you do not have to
delete the line in your editor but replace the line ``pick`` with ``r``
(*reword*).

.. code-block:: console

   $ git rebase -i SHA origin/main

``-i``
   Interactive mode, in which your standard editor is opened and a list of
   all commits after the commit with the hash value :samp:`{SHA}` to be
   removed is displayed, for example

.. code-block:: console

   pick d82199e Update readme
   pick 410266e Change import for the interface
   …

If you now remove a line, this commit will be deleted after saving and
closing the editor. Then the remote repository can be updated with:

.. code-block:: console

   $ git push origin HEAD:main -f

Modify a commit message with rebase
-----------------------------------

This can also be easily with ``rebase``  by not deleting the line in your
editor but replace ``pick`` with  ``r`` (*reword*).

``rebase`` as standard ``git pull`` strategy
--------------------------------------------

Normally, ``git pull`` fetches and merges new remote commits without any
problems. Usually only new commits from the remote branch are added, a so-called
fast-forward merge. However, if both the local and remote branches have new
commits, the branches will diverge. You must then somehow harmonise the
different histories. By default, as of Git 2.33.1, any discrepancy will cause
``git pull`` to stop and display the following message:

.. code-block:: console

   $ git pull
   hint: You have divergent branches and need to specify how to reconcile them.
   hint: You can do so by running one of the following commands sometime before
   hint: your next pull:
   hint:
   hint:   git config pull.rebase false  # merge
   hint:   git config pull.rebase true   # rebase
   hint:   git config pull.ff only       # fast-forward only
   hint:
   hint: You can replace "git config" with "git config --global" to set a default
   hint: preference for all repositories. You can also pass --rebase, --no-rebase,
   hint: or --ff-only on the command line to override the configured default per
   hint: invocation.
   fatal: Need to specify how to reconcile divergent branches.

The notes allow three options:

``git config pull.rebase false``
    merges the local and remote commits. Before Git 2.33.1, Git always used this
    merge.
``git config pull.rebase true``
    The local commits are transferred to the remote commits.
``git config pull.ff only``
    always leads to an error with divergent branches. You can then decide on a
    case-by-case basis with ``--no-rebase`` (which means ``merge``) or
    ``--rebase`` whether you want to merge or rebase.

.. tip::
   I recommend ``git config pull.rebase true``, as merging can be confusing.
   Rebasing the local commits to the remote ones makes the story linear, which
   is more understandable.

Make ``rebase`` part of your standard strategy:

.. code-block:: console

   $ git config --global pull.rebase interactive

If ``git pull`` then encounters divergent local and remote branches, it will
perform a ``rebase``:

.. code-block:: console

   $ git pull
   Auto-merging README.md
   CONFLICT (content): Merge conflict in README.md
   error: could not apply e50dfe5...
   hint: Resolve all conflicts manually, mark them as resolved with
   hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
   hint: You can instead skip this commit: run "git rebase --skip".
   hint: To abort and get back to the state before "git rebase", run "git rebase --
   ,→abort".
   Could not apply e50dfe5...
