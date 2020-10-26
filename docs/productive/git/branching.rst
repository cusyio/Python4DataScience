Git branches
============

``$ git branch [-a]``
    shows all local branches in a repository.

    ``-a``
        also shows all removed branches.

``$ git branch [branch_name]``
    creates a new branch based on the current ``HEAD``.
``$ git checkout [-b] [branch_name]``
    changes the working directory to the specified branch.

    ``-b``
        creates the specified branch if it does not already exist.
``$ git merge [from name]``
    connects the given branch with the current branch you are currently in, e.g.

    .. code-block:: console

        $ git checkout master
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

            $ git checkout master
            $ git merge #42
            Merge made by recursive.
             setup.py |    1 +
             1 files changed, 1 insertions(+), 0 deletions(-)

    ``recursive``
        is a merge strategy that is used when the merge is only to be done to
        ``HEAD``.

Merge conflict
--------------

Occasionally, however, Git runs into issues with merging, such as:

    .. code-block:: console

        $ git merge #17
        Auto-merging setup.py
        CONFLICT (content): Merge conflict in setup.py
        Automatic merge failed; fix conflicts and then commit the result.

    .. seealso::

        * `Git Branching - Einfaches Branching und Merging
          <https://git-scm.com/book/de/v2/Git-Branching-Einfaches-Branching-und-Merging>`_
        * `Git Tools - Fortgeschrittenes Merging
          <https://git-scm.com/book/de/v2/Git-Tools-Fortgeschrittenes-Merging>`_

Branches
--------

``$ git branch -d [name]``
    deletes the selected branch if it has already been transferred to another.

    ``-D`` instead of ``-d`` forcing the deletion.

.. seealso::
    * `Git Branching - Branches in a Nutshell
      <https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell>`_
