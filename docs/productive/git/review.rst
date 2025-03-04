.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Review
======

``log``
-------

.. seealso::
   * `Git’s Database Internals III: File History Queries
     <https://github.blog/open-source/git/gits-database-internals-iii-file-history-queries/>`_

Filter and sort
~~~~~~~~~~~~~~~

:samp:`$ git log [-n {COUNT}]`
   lists the commit history of the current branch.

   ``-n``
       limits the number of commits to the specified number.

:samp:`$ git log [--after="{YYYY-MM-DD}"] [--before="{YYYY-MM-DD}"]`
   Commit history filtered by date.

   Relative specifications such as ``1 week ago`` or ``yesterday`` are also
   permitted.

:samp:`$ git log --author="{VEIT}"`
   filters the commit history by author.

   It is also possible to search for several authors at the same time, for
   example:

   :samp:`$ git log --author="{VEIT\|VSC}"`

:samp:`$ git log --grep="{TERM}" [-i]`
   filters the commit history for regular expressions in the commit message.

   ``-i``
       ignores upper and lower case.

:samp:`$ git log -S"{FOO}" [-i]`
   filters commits for specific lines in the source code.

   ``-i``
       ignores upper and lower case.

:samp:`$ git log -G"{BA*}"`
   filters commits for regular expressions in the source code.

:samp:`$ git log -- {PATH}`
   filters the commit history for specific files.

:samp:`$ git log {MAIN}..{FEATURE}`
   filters for different commits in different branches, in our case between
   the :samp:`MAIN` and :samp:`FEATURE` branches.

   However, this is not the same as :samp:`git log {FEATURE}..{MAIN}`. Let’s
   take the following example:

   .. code-block::

      A - B main
       \
        C - D feature

   :samp:`$ git log {MAIN}..{FEATURE}`
       shows changes in :samp:`{FEATURE}` that are not contained in
       :samp:`{MAIN}`, that is, commits ``C`` and ``D``.
   :samp:`$ git log {FEATURE}..{MAIN}`
       shows changes in :samp:`{MAIN}` that are not contained in
       :samp:`{FEATURE}`, that is, commit ``B``.
   :samp:`$ git log {MAIN}...{FEATURE}`
       shows the changes on both sides, that is, commits ``B``, ``C`` and
       ``D``.

:samp:`$ git log --follow {PATH/TO/FILE}`
   This ensures that the log shows changes to a single file, even if it has
   been renamed or moved.

   You can activate ``--follow`` for individual file calls by default by
   activating the ``log.follow`` option in your global configuration:

   .. code-block:: console

      $ git config --global log.follow true

   Then you no longer have to enter ``--follow``, but only the file name.

``$ git log -L``
   With the `-L
   <https://git-scm.com/docs/git-log#Documentation/git-log.txt--Lltstartgtltendgtltfilegt>`_
   option, you can perform a refined search by checking the log of only part
   of a file:

   * :samp:`$ git log -L {LINE_START_INT|LINE_START_REGEX},{LINE_END_INT|LINE_END_REGEX}:{PATH/TO/FILE}`
   * :samp:`$ git log -L :{FUNCNAME_REGEX}:{PATH/TO/FILE}`

   This function allows you to thoroughly search through the history of a single
   function, class or other code block. It is ideal for finding out when
   something was created and how it was changed so that you can correct,
   refactor or delete it with confidence.

   For more comprehensive investigations, you can also track multiple blocks.
   You can use multiple ``-L`` options at once.

:samp:`$ git log --reverse`
   The log usually displays the latest commit first. You can reverse this
   with ``--reverse``. This is particularly useful if you are analysing with
   the ``-S`` and ``-G`` options already mentioned. By reversing the order
   of the commits, you can quickly find the first commit that added a
   specific string to the codebase.

View
~~~~

:samp:`$ git log --stat --patch|-p`
   ``--stat``
       A summary of the number of changed lines per file is added to the
       usual metadata.
   ``--patch|-p``
       adds the complete commit diff to the output.

:samp:`$ git log --oneline --decorate --graph --all|{FEATURE}`
   display the history graph with references, one commit per line.

   ``--oneline``
       One commit per line.
   ``--decorate``
       The prefixes ``refs/heads/``, ``refs/tags/`` and  ``refs/remotes/``
       are not output.
   ``--graph``
       The log usually smoothes historical branches and displays commits one
       after the other. This hides the parallel structure of the history
       when merging branches. ``--graph`` displays the history of the
       branches in ASCII format.

   :samp:`--all|{FEATURE}`
       ``--all`` shows the log for all branches; :samp:`{FEATURE}` only
       shows the commits of this branch.

.. _reflog:

``reflog``
----------

With `git reflog <https://git-scm.com/docs/git-reflog>`_, your Git repository is
not checked a second time. Instead, it displays the reference log, a record of
all commits made. The reflog not only tracks changes to a branch, it also
records changes to the current commit, branch changes, rebasing, :abbr:`etc. (et
cetera)` You can use it to find all unreachable commits, even those on deleted
branches. This allows you to undo many otherwise destructive actions.

Let’s look at the basics of using reflog and some typical use cases.

.. warning::
   The reflog is only part of your local repository. If you delete a repository
   and clone it again, the new clone will have a fresh, empty reflog.

Show the reflog for ``HEAD``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:samp:`$ git reflog`
    If no options are specified, the command displays the reflog for ``HEAD`` by
    default. It is short for ``git reflog show HEAD``. git reflog has other
    subcommands to manage the log, but show is the default command if no
    subcommand is passed.

.. code-block:: console
   :linenos:

   $ git reflog
   12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{0}: merge my-feature-branch: Fast-forward
   900844a HEAD@{1}: checkout: moving from my-feature-branch to main
   12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{2}: commit (amend): Add my feature and more
   982d93a HEAD@{3}: commit: Add my feature
   900844a HEAD@{4}: checkout: moving from main to my-feature-branch
   900844a HEAD@{5}: commit (initial): Initial commit

* The output is quite dense.
* Each line is a reflog entry, the most recent first.
* The lines start with the abbreviated SHA of the corresponding commit, for
  example ``12bc4d4``.
* The first entry is what ``HEAD`` currently refers to: ``(HEAD -> main,
  my-feature)``.
* The names ``HEAD@\{N}`` are alternative references for the specified commits.
  ``N`` is the number of returning reflog entries.
* remaining text describes the change. Above you can see several types of
  entries:

  * :samp:`commit: {MESSAGE}` for commits
  * :samp:`commit (amend): {MESSAGE}` for a commit change
  * :samp:`checkout: moving from {SRC} TO {DST}` for a branch change

There are many other possible types of entries. The text should be descriptive
enough that you can understand the process without looking it up in the
documentation. In most cases, you will want to look through such reflog entries
to find the corresponding commit SHA.

Show the reflog for a branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can focus on entries for a single branch by using the explicit subcommand
``show`` and the branch name:

.. code-block:: console

   $ git reflog show my-feature-branch
   12bc4d4 (HEAD -> main, my-feature-branch) my-feature-branch@{0}: commit (amend): Add my feature and more
   982d93a my-feature-branch@{1}: commit: Add my feature
   900844a my-feature-branch@{2}: branch: Created from HEAD

Show timestamps of the entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to distinguish between similarly titled changes, the timestamps can
help. For relative timestamps you can use ``--date=relative``:

.. code-block:: console

   $ git reflog --date=relative
   12bc4d4 (HEAD -> main, my-feature) HEAD@{37 minutes ago}: merge my-feature-branch: Fast-forward
   900844a HEAD@{37 minutes ago}: checkout: moving from my-feature-branch to main
   12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{37 minutes ago}: commit (amend): Add my feature and more
   982d93a HEAD@{38 minutes ago}: commit: Add my feature
   900844a HEAD@{39 minutes ago}: checkout: moving from main to my-feature-branch
   900844a HEAD@{40 minutes ago}: commit (initial): Initial commit

And for absolute timestamps you can also use ``--date=iso``:

.. code-block:: console

    $ git reflog --date=iso
    12bc4d4 (HEAD -> main, my-feature) HEAD@{2024-01-11 15:26:53 +0100}: merge my-feature-branch: Fast-forward
    900844a HEAD@{2024-01-11 15:26:47 +0100}: checkout: moving from my-feature-branch to main
    12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{2024-01-11 15:26:11 +0100}: commit (amend): Add my feature and more
    982d93a HEAD@{2024-01-11 15:25:38 +0100}: commit: Add my feature
    900844a HEAD@{2024-01-11 15:24:37 +0100}: checkout: moving from main to my-feature-branch
    900844a HEAD@{2024-01-11 15:23:56 +0100}: commit (initial): Initial commit

Passes all options that ``git log`` supports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``git reflog show`` has the same options as ``git log``. For example, you can
use ``--grep`` to search for commit messages that mention :samp:`{my feature}`
without case-sensitivity:

.. code-block:: console

    $ git reflog -i --grep 'my feature'
    12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{0}: merge my-feature: Fast-forward
    12bc4d4 (HEAD -> main, my-feature-branch) HEAD@{2}: commit (amend): Add my feature and more
    982d93a HEAD@{3}: commit: Add my feature

Note the expiry of entries
~~~~~~~~~~~~~~~~~~~~~~~~~~

Reflog entries expire after a certain time when Git runs the automatic :abbr:`gc
(garbage collection)` process for your repository. This expiration time is
controlled by two ``gc.*`` options:

``gc.reflogExpire``
    The general expiration time, which is set to 90 days by default.
``gc.reflogExpireUnreachable``
    The expiry time for entries relating to commits that can no longer be
    reached is set to 30 days by default.

You can increase these options to a longer time frame, but this is rarely
useful.
