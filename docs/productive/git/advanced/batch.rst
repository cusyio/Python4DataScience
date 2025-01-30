Batch processing
================

All files in a repository
-------------------------

Occasionally, you may want to change all files in your repository or those that
match a pattern. This is possible with the combination of `git ls-files
<https://git-scm.com/docs/git-ls-files>`_ and `xargs
<https://linux.die.net/man/1/xargs>`_:

:samp:`$ git ls-files -z | xargs -0 {COMMAND}`
    change all files in a repository.
:samp:`$ git ls-files -z -- "*.SUFFIX" | xargs -0 {COMMAND}`
    only changes the files with a specific file extension.

    ``-z``, ``-0``
        uses the zero-byte separator.

Example
~~~~~~~

:samp:`$ git ls-files -z -- ‘*.py’ | xargs -0 git update-index --chmod=+x`
    changes the permissions for all files with the suffix ``.py`` from
    ``100644`` to ``100755``, if necessary, so that they become executable.

.. _git-name-only:

All files changed in the working or staging area
------------------------------------------------

:samp:`git diff --name-only`
    outputs the files that are managed by Git and have been changed in the
    working area.
:samp:`git diff --staged --name-only`
    outputs the files added to the staging area.
:samp:`git diff --staged --name-only "*.{SUFFIX}"`
    also filters for a specific file extension.

.. _list-changed:

:samp:`git diff --name-only --diff-filter d`
    excludes deleted files.

    This is the most common case for me, which is why I have created a
    ``list-changed`` alias for this: ``git config --global alias.list-changed
    'diff --name-only --diff-filter d'``.

Example
~~~~~~~

To execute commands for the changed file list, you can use the shell `Command
Substitution
<https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html>`_:

:samp:`$ uv run codespell $(git list-changed '*.py')`
    The shell executes the ``git list-changed`` in brackets and inserts its
    output into the outer command. ``codespell`` therefore receives the list of
    changed text files as an argument.
:samp:`uv run pytest $(git diff --staged --name-only "tests/*test_*.py")`
    calls :doc:`python-basics:test/pytest/index` to execute only those test
    modules that have been changed in the working directory.
