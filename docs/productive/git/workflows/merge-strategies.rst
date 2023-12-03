.. SPDX-FileCopyrightText: 2023 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Merge strategies: merge vs. squash vs. rebase
=============================================

I use :samp:`git merge`, :samp:`git merge squash` and :samp:`git rebase`
depending on the situation. They all have their merits, but their use depends
very much on the context.

:samp:`git merge`
    adds a new commit when the branches are merged.

    This has the advantage that it best represents the true history. You can see
    the merge and all the :abbr:`WIP (work in progress)` commits that were run
    during development. If necessary, you can simply undo the merge with
    :samp:`git revert {-m|--mainline} {1|2} {MERGE-COMMIT_SHA}`.

    ``-m 1``
        takes you back to the behaviour of the parent element from the branch to
        which you have applied the changes.
    ``-m 2``
        takes you back to the behaviour of the parent element from the branch
        from which you have applied the changes.

    .. tip::
       More commits also make :doc:`git bisect <../advanced/bisect>` better, as
       long as a build can be created for each commit. With a hundred or at
       most a thousand lines that have changed, I still have a chance of finding
       the bug in a reasonable amount of time.

    .. seealso::
       * `Advanced Merging
         <https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging>`_

:samp:`git merge --squash`
    allows you to merge all changes from a branch into a single commit above the
    current branch.

    This is useful if you have many small :abbr:`WIP (work in progress)` commits
    that are really all aimed at one feature. When squashing, I make sure to
    rewrite the commit message so that it is as meaningful as possible. The
    usual squash commit message created by Git, :doc:`../advanced/gitlab/index`
    :abbr:`etc. (et cetera)` is usually not sufficient and simply adds all
    squash commit messages together, possibly a series of :abbr:`WIP (work in
    progress)` commit messages.

:samp:`git rebase`
    moves a sequence of commits to a new base commit. With :samp:`git rebase`,
    the advantage to find a bug quickly using :doc:`git bisect
    <../advanced/bisect>` remains. In addition, however, it is now easier to
    recognise the context in which the bug occurred.

    .. tip::
       With a large diff and many :abbr:`WIP (work in progress)` commits,
       :samp:`git rebase` can be used interactively to selectively choose
       commits for the squash option and rearrange the commits. However, it only
       does one thing at a time:

       * merge commits with the ``squash`` option or
       * change the order of the commits or
       * edit the commits.

       Do not try to make all changes at once.

    .. tip::
       If you don’t feel safe with :samp:`git rebase`, then don’t do it! You can
       use :samp:`git merge` or :samp:`git commit --amend` instead.

    .. seealso::
       * :doc:`../rebase`
       * `Rewriting History: Squashing Commits
         <https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#_squashing>`_
       * `Rewriting History: Reordering Commits
         <https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#_reordering_commits>`_
