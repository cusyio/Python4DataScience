.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Working with Git
================

Start working on a project
--------------------------

.. _git-init:

Start your own project
~~~~~~~~~~~~~~~~~~~~~~

:samp:`$ git init [{PROJECT}]`
    creates a new, local git repository.

    :samp:`[{PROJECT}]`
        if the project name is given, Git creates a new directory and
        initializes it.

        If no project name is given, the current directory is initialised.

    .. tip::
       The default branch in Git is ``master``. However, as `this term is
       offensive to some people
       <https://sfconservancy.org/news/2020/jun/23/gitbranchname/>`_, the
       default branch name can be configured in Git ≥ 2.28:

       .. code-block:: console

          $ git config --global init.defaultBranch main

    Most Git hosts also use *main* as the standard for new repositories.

Work on a project
~~~~~~~~~~~~~~~~~

:samp:`$ git clone {SOURCE}`
    downloads a project with all branches and the entire history from the remote
    repository, for example:

    .. code-block:: console

       $ git clone https://github.com/cusyio/Python4DataScience.git

    or

    .. code-block:: console

       $ git clone git@github.com:cusyio/Python4DataScience.git

    ``git clone --depth``
        indicates the number of commits to be downloaded.

    ``git clone -b``
        specifies the name of the remote branch to be downloaded.

Work on a project
-----------------

``$ git status``
    shows the status of the current branch in the working directory with new,
    changed and files already marked for commit.

    ``git status -v``
        shows the changes in the stage area as a diff.
    ``git status -vv``
        also shows the changes in the working directory as a second diff.

    .. seealso::
       `git status -v
       <https://git-scm.com/docs/git-status#Documentation/git-status.txt--v>`_

    ``git status -s|--short``
        shows the status in short format, for example

        .. code-block:: console

           $ git status -s
            M docs/productive/git/work.rst
           ?? Python4DataScience.txt

        The preceding letters indicate the status of the file.

    ``git status`` gives a lot of advice on what to do with the files in the
    individual states:

    .. code-block:: console

       $ git status
       On branch main
       Your branch and 'origin/main' have diverged,
       and have 1 and 1 different commits each, respectively.
         (use "git pull" if you want to integrate the remote branch with yours)

       Changes not staged for commit:
         (use "git add <file>..." to update what will be committed)
         (use "git restore <file>..." to discard changes in working directory)
           modified:   docs/productive/git/work.rst
       Untracked files:
         (use "git add <file>..." to include in what will be committed)
           Python4DataScience.txt

       no changes added to commit (use "git add" and/or "git commit -a")

    .. _git-statushints:

    If you are familiar with Git, you may find these hints unnecessary. Then you
    can deactivate these messages with the ``advice.statusHints`` option:

    .. code-block:: console

       $ git config --global advice.statusHints false

    From now on, calling ``git status`` will no longer display any hints:

    .. code-block:: console

       $ git status
       On branch main
       Your branch and 'origin/main' have diverged,
       and have 1 and 1 different commits each, respectively.

       Changes not staged for commit:
           modified:   docs/productive/git/work.rst

       Untracked files:
           Python4DataScience.txt

       no changes added to commit (use "git add" and/or "git commit -a")

    Also when calling ``git-switch`` and ``git-checkout`` as well as when
    writing commit messages, no more hints are displayed.

    .. tip::
       Although there are many other `advice.*
       <https://git-scm.com/docs/git-config#Documentation/git-config.txt-advice>`_
       options, most of them are quite insignificant, so they should only be
       excluded when they start to interfere.

:samp:`$ git add {PATH}`
    adds one or more files to the stage area.

    :samp:`git add -p`
        adds parts of one or more files to the stage area.
    :samp:`git add -e`
        the changes to be adopted can be edited in the standard editor.

:samp:`$ git diff [{PATH}]`
    shows differences between working and stage areas, for example:

    .. code-block:: console

       $ git diff docs/productive/git/work.rst
       diff --git a/docs/productive/git/work.rst b/docs/productive/git/work.rst
       index e2a5ea6..fd84434 100644
       --- a/docs/productive/git/work.rst
       +++ b/docs/productive/git/work.rst
       @@ -46,7 +46,7 @@

        :samp:`$ git diff {FILE}`
       -    shows differences between work and stage areas.
       +    shows differences between work and stage areas, for example:

    By default, Git adds the prefixes ``a/`` and ``b/`` in front of the file
    paths to the diff format.

    .. tip::
       These prefixes are intended to mark the paths as * old*  and * new* , but
       they prevent the file paths from being easily copied – some terminals
       also allow you to click on file paths to open them – but the prefixes
       prevent this. You can change this with a new function in Git 2.45:

       .. code-block:: console

          $ git config --global diff.srcPrefix './'
          $ git config --global diff.dstPrefix './'

    ``index e2a5ea6..fd84434 100644`` displays some internal Git metadata that
    you will probably never need. The numbers correspond to the hash
    identifiers of the git object versions.

    The rest of the output is a list of diff chunks whose header is enclosed in
    ``@@`` symbols. Each chunk shows changes made in a file. In our
    example, 7 lines were extracted starting at line 46 and 7 lines were added
    starting at line 46.

    By default, ``git diff`` performs the comparison against ``HEAD``. If you
    use ``git diff HEAD docs/productive/git/work.rst`` in the example above, it
    will have the same effect.

    ``git diff`` can be passed Git references. Besides ``HEAD``, some other
    examples of references are tags and branch names, for example :samp:`git
    diff {MAIN}..{FEATURE_BRANCH}`. The dot operator in this example indicates
    that the diff input is the tips of the two branches. The same effect occurs
    if the dots are omitted and a space is used between the branches. In
    addition, there is a three-dot operator: :samp:`git diff
    {MAIN}...{FEATURE_BRANCH}`, which initiates a diff where the first input
    parameter :samp:`MAIN` is changed so that the reference is the common
    ancestor of :samp:`{MAIN}` and :samp:`{FEATURE}`.

    Every commit in Git has a commit ID, which you can get by running ``git
    log``. You can then also pass this commit ID to ``git diff``:

    .. code-block:: console

        $ git log --pretty=oneline
        af1a395a08221ffa83b46f562b6823cf044a108c (HEAD -> main, origin/main, origin/HEAD) :memo: Add some git diff examples
        d650de52306b63b93e92bba4f15be95eddfea425 :memo: Add „Debug .gitignore files“ to git docs
        …
        $ git diff af1a395a08221ffa83b46f562b6823cf044a108c d650de52306b63b93e92bba4f15be95eddfea425

    ``git diff --staged``, ``--cached``
        shows differences between the stage area and the repository.
    ``git diff --word-diff``
        shows the changed words.

    .. seealso::
       * :ref:`git-name-only`

:samp:`$ git restore {FILE}`
    changes files in the working directory to a state previously known to Git. By
    default, Git checks out ``HEAD``, the last commit of the current branch.

    .. note::

        In Git < 2.23, ``git restore`` is not yet available. In this case you
        still need to use ``git checkout``:

        :samp:`$ git checkout {FILE}`

``$ git commit``
    makes a new commit with the added changes.

    ``git commit -m 'COMMIT MESSAGE'``
        writes a commit message directly from the command line.
    ``git commit --dry-run --short``
        shows what would be committed with the status in short format.
    :samp:`git commit -m '{FILE}'`
        passes file names or `globbing
        <https://en.wikipedia.org/wiki/Glob_(programming)>`_ patterns to ``git
        commit`` to commit changes to these files, skipping any changes that
        already exist in the staging area with git add.

:samp:`$ git reset [--hard|--soft] [{TARGET_REFERENCE}]`
    resets the history to an earlier commit.
:samp:`$ git rm {PATH}`
    removes a file from the work and stage areas.

.. _git-stash:

``$ git stash``
    moves the current changes from the workspace to a stash.

    To be able to distinguish your hidden changes as well as possible, the
    following two options are recommended:

    ``git stash -p|--patch``
        allows you to partially hide changes, for example:

        .. code-block:: console

           $ git stash -p
           diff --git a/docs/productive/git/work.rst b/docs/productive/git/work.rst
           index cff338e..1988ab2 100644
           --- a/docs/productive/git/work.rst
           +++ b/docs/productive/git/work.rst
           @@ -83,7 +83,16 @@
                ``list``
                    lists the hidden changes.
                ``show``
           -        shows the changes in the hidden files.
           +        shows the changes in the hidden files, for example
           …
           (1/1) Stash this hunk [y,n,q,a,d,e,?]? y

        With ``?`` you get a complete list of options. The most common are:

        +---------------+-----------------------------------------------+
        | Command       | Description                                   |
        +===============+===============================================+
        | ``y``         | Hide this change                              |
        +---------------+-----------------------------------------------+
        | ``n``         | Do not apply this change                      |
        +---------------+-----------------------------------------------+
        | ``q``         | All changes already selected will be hidden   |
        +---------------+-----------------------------------------------+
        | ``a``         | Apply this and all subsequent changes         |
        +---------------+-----------------------------------------------+
        | ``e``         | Edit this change manually                     |
        +---------------+-----------------------------------------------+
        | ``?``         | Help                                          |
        +---------------+-----------------------------------------------+

        .. _git-singlekey:

        .. tip::
           Usually you have to press the :kbd:`↩︎` key after every command with a
           letter. However, you can switch off this overhead:

           .. code-block:: console

              $ git config --global interactive.singleKey true

        .. _git-autostash:

        You can also automatically apply stash for merge and rebase:

        .. code-block:: console

           $ git config --global merge.autoStash true
           $ git config --global rebase.autoStash true

    :samp:`git stash branch {BRANCHNAME}`
        creates a branch from hidden files, for example:

        .. code-block :: console

            $ git stash branch stash-example stash@{0}
            On branch stash-example
            Changes marked for commit:
              (use "git restore --staged <file>..." to remove from staging area).
                new file: docs/productive/git/work.rst

            Changes not marked for commit:
              (use "git add <file>..." to mark the changes for commit).
              (use "git restore <file>..." to discard the changes in the working directory)
                changed: docs/productive/git/index.rst

            stash@{0} (6565fdd1cc7dff9e0e6a575e3e20402e3881a82e) gelöscht

    :samp:`git stash save {MESSAGE}`
        adds a message to the changes.
    ``git stash -u UNTRACKED_FILE``
        hides unversioned files.
    ``git stash list``
        lists the various stashes.

        :samp:`git stash list --date=relative|default`
            also displays the relative or absolute date.

    ``git stash show``
        shows the changes in the stashed files.
    ``git stash pop``
        transfers the changes from the stash to the workspace and empties the
        stash, for example:

        .. code-block:: console

           $ git stash pop stash 2

    ``git stash drop``
        empties a specific stash, for example:


        .. code-block:: console

            $ git stash drop stash 1
            stash@{1} (defcf56541b74a1ccfc59bc0a821adf0b39eaaba) deleted


    ``git stash clear``
        delete all your hiding places.
