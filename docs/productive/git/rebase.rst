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


Delete commits with rebase
--------------------------

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
