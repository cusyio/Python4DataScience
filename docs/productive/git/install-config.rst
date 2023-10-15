.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git installation and configuration
==================================

Installation
------------

For iX distributions, Git should be in the standard repository.

.. tab:: Debian/Ubuntu

   The `git-all <https://packages.debian.org/stable/git-all>`_ package provides
   a complete Git working environment. Install it with:

   .. code-block:: console

      $ sudo apt install git-all

    To install only Git the `git <https://packages.debian.org/stable/git>`_ package suffices:

   .. code-block:: console

      $ sudo apt install git

   The bash autocompletion makes Git easier to use on the command line.
   The according package is called
   `bash-completion <https://packages.debian.org/stable/bash-completion>`_.
   Install it with:

   .. code-block:: console

    $ sudo apt install bash-completion

.. tab:: macOS

   There are several different ways to install Git on a Mac. Probably the
   easiest way to do is to install the Xcode Command Line Tools. For this you
   only have to call up ``git`` in the terminal for the first time:

   .. code-block:: console

      $ git --version

   ``git-completion`` you can install with `Homebrew <https://brew.sh/>`_:

   Then you have to add the following line to the file :file:`~/.bash_profile`:

   .. code-block:: bash

    [[ -r "$(brew --prefix)/etc/profile.d/bash_completion.sh" ]] && . "$(brew --prefix)/etc/profile.d/bash_completion.sh"

.. tab:: Windows

   Go to https://git-scm.com/download/win and start the download
   automatically. Further information can be found at
   https://gitforwindows.org/.

.. _git-config:

Configuration
-------------

The author of every change needs to be transparent.
Specify your name and email address as follows:


:samp:`$ git config --global user.name "{NAME}"`
    defines the name :samp:`{NAME}` associated with your commit transactions.
:samp:`$ git config --global user.email "{EMAIL-ADDRESS}"`
    defines the email address :samp:`{EMAIL-ADDRESS}` that will be linked to your commit transactions.

For better readability, activate the coloring of the command line output:

:samp:`$ git config --global color.ui auto`


The :file:`~/.gitconfig` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, the following file can be created with the commands given above:

.. code-block:: ini

    [user]
        name = veit
        email = veit@cusy.io

    [color]
        ui = auto

However, aliases can also be specified in the :file:`~/.gitconfig` file:

.. code-block:: ini

    [alias]
        st = status
        ci = commit
        br = branch
        co = checkout
        df = diff
        dfs = diff --staged

.. seealso::
   Shell-Konfiguration:

   * `oh-my-zsh <https://ohmyz.sh>`_

     * `Git plugin aliases
       <https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git#aliases>`_
     * `zsh-you-should-use
       <https://github.com/MichaelAquilina/zsh-you-should-use>`_

   * `Starship <https://starship.rs>`_

     * `git_branch-Modul <https://starship.rs/config/#git-branch>`_
     * `git_commit-Modul <https://starship.rs/config/#git-commit>`_
     * `git_state <https://starship.rs/config/#git-state>`_
     * `git_status-Modul <https://starship.rs/config/#git-status>`_

The editor can also be specified, and whitespace errors can be highlighted in ``git
diff``:

.. code-block:: ini

    [core]

        editor = vim

        # Highlight whitespace errors in git diff:
        whitespace = tabwidth=4,tab-in-indent,cr-at-eol,trailing-space

.. note::
   In addition to :file:`~/.gitconfig`, since version 1.17.12 Git also looks in
   :file:`~/.config/git/config` for a global configuration file.

   Under Linux, :file:`~/.config` can sometimes be a different path set by the
   environment variable ``XDG_CONFIG_HOME``. This behaviour is part of the `X
   Desktop Group (XDG) specification
   <https://wiki.archlinux.org/title/XDG_Base_Directory#Specification>`_. You
   can get the other path with:

   .. code-block:: ini

      $ echo $XDG_CONFIG_HOME

.. seealso::
   * `git config files <https://git-scm.com/docs/git-config#FILES>`_

Since you can set options at multiple levels, you may want to keep track of
where Git reads a particular value from. With ``git config --list`` [#]_ you can
list all the overridden options and values. You can combine this with
``--show-scope`` [#]_ to see where Git is getting the value from:

.. code-block:: console

   $ git config --list --show-scope
   system  credential.helper=osxkeychain
   global  user.name=veit
   global  user.email=veit@cusy.io
   …

You can also use ``--show-origin`` [#]_ to list the names of the configuration
files:

.. code-block:: console

   $ git config --list --show-origin
   file:/opt/homebrew/etc/gitconfig        credential.helper=osxkeychain
   file:/Users/veit/.config/git/config     user.name=veit
   file:/Users/veit/.config/git/config     user.email=veit@cusy.io
   …

Alternative configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use other configuration files for certain working directories, for
example to distinguish between private and professional projects. You can use a
local configuration in your repository or `conditional includes
<https://git-scm.com/docs/git-config#_conditional_includes>`_ at the end of your
global configuration:

.. code-block:: ini

    …
    [includeIf "gitdir:~/private"]
    path = ~/.config/git/config-private

This construct ensures that Git includes additional configurations or overwrites
existing ones when you work in :file:`~/private`.

Now create the file :file:`~/.config/git/config-private` and define your
alternative configuration there, for example:

.. code-block:: ini

   [user]
       email = kontakt@veit-schiele.de
   [core]
       sshCommand = ssh -i ~/.ssh/private_id_rsa

.. seealso::
   * `core.sshCommand
     <https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresshCommand>`_


Manage login data
~~~~~~~~~~~~~~~~~

Since Git version 1.7.9, the access data to git repositories can be managed with
`gitcredentials <https://git-scm.com/docs/gitcredentials>`_. To use this, you
can, for example, specify the following:

.. code-block:: console

    $ git config --global credential.helper Cache

This will keep your password in the cache for 15 minutes.
If necessary, the timeout can be increased, for example with:

.. code-block:: console

    $ git config --global credential.helper 'cache --timeout=3600'


.. tab:: macOS

    With macOS you can use `osxkeychain` to store the login information.
    `osxkeychain` requires Git version 1.7.10 or newer and can be installed in
    the same directory as Git with:

    .. code-block:: console

        $ git credential-osxkeychain
        git: 'credential-osxkeychain' is not a git command. See 'git --help'.
        $ curl -s -O http://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
        $ chmod u+x git-credential-osxkeychain
        $ sudo mv git-credential-osxkeychain /usr/bin/
        Password:
        git config --global credential.helper osxkeychain

    This enters the following in the :file:`~/.gitconfig` file:

    .. code-block:: ini

        [credential]
            helper = osxkeychain

.. tab:: Windows

    For Windows, `Git Credential Manager (GCM)
    <https://github.com/GitCredentialManager/git-credential-manager>`_ is
    available. It is integrated in `Git for Windows
    <https://git-scm.com/download/win>`_ and is installed by default. However,
    there is also a standalone Installer in `Releases
    <https://github.com/GitCredentialManager/git-credential-manager/releases/>`_.

    It is configured with

    .. code-block:: console

        $ git credential-manager configure
        Configuring component 'Git Credential Manager'...
        Configuring component 'Azure Repos provider'...

    This will add the ``[credential]`` section to your :file:`~.gitconfig` file:

    .. code-block:: ini

        [credential]
            helper =
            helper = C:/Program\\ Files/Git/mingw64/bin/git-credential-manager.exe

    Now, when cloning a repository, a *Git Credential Manager* window opens and asks you
    to enter your credentials.

    In addition, the :file:`~/.gitconfig` file is supplemented, for example by
    the following two lines:

    .. code-block:: ini

        [credential "https://ce.cusy.io"]
            provider = generic

.. note::
    You can find a comprehensive example of a :file:`~/.gitconfig` file in my
    `dotfiles <https://github.com/veit/dotfiles/>`__ repository: `.gitconfig
    <https://github.com/veit/dotfiles/blob/main/.config/git/config>`__.

.. seealso::
    * `Git Credential Manager: authentication for everyone
      <https://github.blog/2022-04-07-git-credential-manager-authentication-for-everyone/>`_

.. _gitignore:

The :file:`.gitignore` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the :file:`.gitignore` file you can exclude files from version management. A
typical :file:`.gitignore` file can look like this:

.. code-block:: ini

    /logs/*
    !logs/.gitkeep
    /tmp
    *.swp

In doing so, Git uses `Globbing <https://linux.die.net/man/7/glob>`_ patterns,
among others:

+-------------------------------+-----------------------------------+-------------------------------+
| Pattern                       | Example                           | Description                   |
+===============================+===================================+===============================+
| .. code-block:: console       | :file:`logs/instance.log`,        | You can put two asterisks to  |
|                               | :file:`logs/instance/error.log`,  | prefix directories anywhere.  |
|     **/logs                   | :file:`prod/logs/instance.log`    |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance.log`,        | You can put two asterisks to  |
|                               | :file:`prod/logs/instance.log`    | prefix files with their name  |
|     **/logs/instance.log      | but not                           | in a parent directory.        |
|                               | :file:`logs/prod/instance.log`    |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance.log`,             | An asterisk is a placeholder  |
|                               | :file:`error.log`,                | for null or more characters.  |
|     *.log                     | :file:`logs/instance.log`         |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`/logs/instance.log`,       | An exclamation mark in front  |
|                               | :file:`/logs/error.log`,          | of a pattern ignores it. If a |
|     /logs                     | but not                           | file matches a pattern, but   |
|     !/logs/.gitkeep           | :file:`/logs/.gitkeep` or         | also a negating one that is   |
|                               | :file:`/instance.log`             | defined later, it is not      |
|                               |                                   | ignored.                      |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`/instance.log`,            | With a preceding slash, the   |
|                               | but not                           | pattern only matches files    |
|     /instance.log             | :file:`logs/instance.log`         | in the root directory of the  |
|                               |                                   | repository.                   |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance.log`,             | Usualy the pattern match      |
|                               | :file:`logs/instance.log`         | files in any directory.       |
|     instance.log              |                                   |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance0.log`,            | A question mark fits exactly  |
|                               | :file:`instance1.log`,            | on a charater.                |
|     instance?.log             | but not                           |                               |
|                               | :file:`instance.log` or           |                               |
|                               | :file:`instance10.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance0.log`,            | Square brackets can be used   |
|                               | :file:`instance1.log`,            | to find a single character    |
|     instance[0-9].log         | but not                           | from a specific range.        |
|                               | :file:`instance.log` or           |                               |
|                               | :file:`instance10.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance0.log`,            | Square brackets match a       |
|                               | :file:`instance1.log`,            | single character from a given |
|     instance[01].log          | but not                           | set.                          |
|                               | :file:`instance2.log` or          |                               |
|                               | :file:`instance01.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance2.log`,            | An exclamation mark can be    |
|                               | but not                           | used to find any character    |
|     instance[!01].log         | :file:`instance0.log`,            | from a specified set.         |
|                               | :file:`instance1.log` or          |                               |
|                               | :file:`instance01.log`            |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs`                      | If no slash appended, the     |
|                               | :file:`logs/instance.log`         | pattern fix both files and    |
|     logs                      | :file:`prod/logs/instance.log`    | the contents of directories   |
|                               |                                   | witch this name.              |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance.log`,        | Appending a slash indicates   |
|                               | :file:`logs/prod/instance.log`,   | that the pattern is a         |
|     logs/                     | :file:`prod/logs/instance.log`    | directory. The entire         |
|                               |                                   | contents of any directory in  |
|                               |                                   | the repository that matches   |
|                               |                                   | the name – including all its  |
|                               |                                   | files and subdirectories –    |
|                               |                                   | are ignored.                  |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       |:file:`var/instance.log`,          | Two Asterisks match null or   |
|                               |:file:`var/logs/instance.log`,     | more directories.             |
|                               |but not                            |                               |
|     var/**/instance.log       |:file:`var/logs/instance/error.log`|                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance/error.log`,  | Wildcards can also be used in |
|                               | :file:`logs/instance1/error.log`  | directory names.              |
|     logs/instance*/error.log  |                                   |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`logs/instance.log`,        | Pattern, that specify a       |
|                               | but not                           | particular file in a          |
|     logs/instance.log         | :file:`var/logs/instance.log`     | directory are relative to the |
|                               | or                                | root of the repository.       |
|                               | :file:`instance.log`              |                               |
+-------------------------------+-----------------------------------+-------------------------------+

Git-commit empty folder
:::::::::::::::::::::::

In the example above you can see that with ``/logs/*`` no content of the
:file:`logs` directory should be versioned with Git, but an exception is defined
in the following line: ``!logs/.gitkeep`` allows the file :file:`.gitkeep` to be
managed with Git. The :file:`logs` directory is then also transferred to the Git
repository. This construction is necessary because empty folders cannot be
managed with Git.

Another possibility is to create a :file:`.gitignore` file in an empty folder
with the following content:

.. code-block:: ini

    # ignore everything except .gitignore
    *
    !.gitignore


.. seealso:
    * `Can I add empty directories?
      <https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F>`_

``excludesfile``
::::::::::::::::

However, you can also exclude files centrally for all Git repositories. For this
purpose, you can set ``excludesfile`` in the :file:`~/.gitconfig` file:

.. code-block:: ini

    [core]

        # Use custom `.gitignore`
        excludesfile = ~/.gitignore
        …

.. note::
    You can find helpful templates in my `dotfiles
    <https://github.com/veit/dotfiles/tree/main/gitignores>`__ repository or
    on the `gitignore.io <https://gitignore.io/>`_ website.

Ignoring a file from the repository
:::::::::::::::::::::::::::::::::::

If you want to ignore a file that has already been added to the repository in
the past, you need to delete the file from your repository and then add a
``.gitignore`` rule for it. Using the ``--cached`` option on ``git rm`` means
that the file will be deleted from the repository but will remain in your
working directory as an ignored file.

.. code-block:: console

    $ echo *.log >> .gitignore
    $ git rm --cached *.log
    rm 'instance.log'
    $ git commit -m "Remove log files"

.. note::
    You can omit the ``--cached`` option if you want to remove the file from
    both the repository and your local file system.

Commit an ignored file
::::::::::::::::::::::

It is possible to force the commit of an ignored file to the repository with the
``-f`` (or ``--force``) option on ``git add``:

.. code-block:: console

    $ cat data/.gitignore
    *
    $ git add -f data/iris.csv
    $ git commit -m "Force add iris.csv"

You might consider this if you have a general pattern (like ``*``) defined, but
want to commit a specific file. However, a better solution is usually to define
an exception to the general rule:

.. code-block:: console

    $ echo '!iris.csv' >> data/.gitignore
    $ cat data/.gitignore
    *
    !iris.csv
    $ git add data/iris.csv
    $ git commit -m "Add iris.csv"

This approach should be more obvious and less confusing for your team.

Troubleshooting :file:`.gitignore` files
::::::::::::::::::::::::::::::::::::::::

For complicated :file:`.gitignore` patterns, or patterns that are spread across
multiple :file:`.gitignore` files, it can be difficult to figure out why a
particular file is being ignored.

With ``git status --ignored=matching`` [#]_, an *Ignored Files* section is added
to the output, showing all ignored files and directories:

.. code-block:: console

   $ git status --ignored=matching
   On branch main
   Ignored Files:
     (use "git add -f <file>...", to pre-mark the changes for committing
       .DS_Store
       docs/.DS_Store
       docs/_build/doctrees/
       docs/_build/html/
       docs/clean-prep/.ipynb_checkpoints/
       …
       nothing to commit, working tree clean

You can use the ``git check-ignore`` command with the ``-v`` (or ``--verbose``)
option to determine which pattern is causing a particular file to be ignored:

.. code-block:: console

   $ git check-ignore -v data/iris.csv
   data/.gitignore:2:!iris.csv  data/iris.csv

The output shows
:samp:`{FILE_CONTAINING_THE_PATTERN}:{LINE_NUMBER_OF_THE_PATTERN}:{PATTERN}
{FILE_NAME}`

You can pass multiple filenames to ``git check-ignore`` if you like, and the
names themselves don’t even have to match the files that exist in your
repository.

You can get a complete list of all ignored files with ``git ls-files --ignored
--exclude-standard --others`` [#]_. With ``--exclude-standard`` the standard
ignored files are read and with ``--others`` the non-versioned files are
displayed instead of the versioned ones:

.. code-block:: console

   $ git ls-files --ignored --exclude-standard --others
   .DS_Store
   _build/doctrees/clean-prep/bulwark.doctree
   _build/doctrees/clean-prep/dask-pipeline.doctree
   _build/doctrees/clean-prep/deduplicate.doctree
   …

Occasionally you may want to bypass the global :file:`~/.gitignore` file to see
which files Git always ignores, regardless of your configuration. You can do
this by switching to another ``exclude`` option, ``--exclude-per-directory``,
which uses only the repository’s :file:`.gitignore` files:

.. code-block:: console

   $ git ls-files --ignored --exclude-per-directory=.gitignore --others
   docs/_build/doctrees/clean-prep/bulwark.doctree
   docs/_build/doctrees/clean-prep/dask-pipeline.doctree
   docs/_build/doctrees/clean-prep/deduplicate.doctree
   …

Note that the :file:`.DS_Store` file is no longer listed as ignored.

If you replace ``--others`` with ``--cached``, ``git ls-files`` will list files
that would be ignored unless they have already been committed:

.. code-block:: console

   $ git ls-files --ignored --exclude-per-directory=.gitignore --cached
   data/iris.csv

You may have such files because someone added them to a :file:`.gitignore` file
before the relevant patterns, or because someone added them with ``git add
--force``. Either way, if you no longer want to manage the file with Git, you
can remove it from Git management with the following one-liner, but don’t
delete it:

.. code-block:: console

   $ git ls-files --ignored --exclude-per-directory=.gitignore --cached | xargs -r git rm --cached
   rm 'data/iris.csv'

----

.. [#] `git config --list
   <https://git-scm.com/docs/git-config#Documentation/git-config.txt---list>`_
.. [#] `git config --show-scope
   <https://git-scm.com/docs/git-config#Documentation/git-config.txt---show-scope>`_
.. [#] `git config --show-origin
   <https://git-scm.com/docs/git-config#Documentation/git-config.txt---show-origin>`_
.. [#] `git status --ignored
   <https://git-scm.com/docs/git-status#Documentation/git-status.txt---ignoredltmodegt>`_
.. [#] `git check-ignore
   <https://git-scm.com/docs/git-check-ignore>`_
.. [#] `git ls-files --ignored
   <https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---ignored>`_
