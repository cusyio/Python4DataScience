.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git installation and configuration
==================================

Installation
------------

For ix distributions, Git should be in the standard repository.

.. tab:: Debian/Ubuntu

   The `git-all <https://packages.debian.org/stable/git-all>`_ package provides
   a complete Git working environment. Install it with:

   .. code-block:: console

      $ sudo apt install git-all

   To install only Git the `git <https://packages.debian.org/stable/git>`_
   package suffices:

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

Save the global configuration in :file:`~/.config/git/`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git uses three levels of configuration files, which are applied in this order:

``system``
    applies to all users on your computer, but it’s unlikely you’ll ever use
    this.
``global``
    applies to all repositories of a single user and we will look at this in
    more detail here.
``local``
    applies to a single repository and is only suitable for a few
    repository-specific options.

Git searches for a global configuration file in two places: :file:`~/.config/git/config` and :file:`~/.gitconfig`. The first location is the default location
for configuration files while the second is the legacy option.

.. note::
   On Linux machines, :file:`~/.config` can sometimes be a different path set by
   the environment variable ``XDG_CONFIG_HOME``. This behaviour is part of the
   `X Desktop Group (XDG) specification
   <https://wiki.archlinux.org/title/XDG_Base_Directory#Specification>`_. You
   can get the other path with:

   .. code-block:: ini

      $ echo $XDG_CONFIG_HOME

   If this does not result in anything, then your system will use
   :file:`~/.config`, otherwise it will use the path shown. For the sake of
   simplicity, we will only refer to :file:`~/.config` from now on.

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

.. note::
   You can find a comprehensive example of a configuration file in my `dotfiles
   <https://github.com/veit/dotfiles/>`_  repository: `.gitconfig
   <https://github.com/veit/dotfiles/blob/main/.config/git/config>`_.

.. _migrate-git-config:

Migrate from :file:`~/.gitconfig` to :file:`~/.config/git/config`
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

If you are currently using the old file name :file:`~/.gitconfig`, you can move
it to the :file:`~/.config` directory in just a few steps:

#. Make sure that the :file:`~/.config` directory exists.
#. Move your existing configuration file to its place:

   .. code-block:: console

      $ mv ~/.gitconfig ~/.config/git/config

#. Check whether Git can still read the configuration file by asking for your
   user name:

   .. code-block:: console

      $ git config --global user.name
      Veit Schiele

#. You may then have to move other files, for example :file:`~/.gitattributes`
   and :file:`~/.gitignore`. You can check whether these files are available
   with

   .. code-block:: console

      $ git config --global core.excludesFile
      ~/.gitignore
      $ git config --global core.attributesFile
      ~/.gitattributes

   You must then move the files and delete the associated configuration entries:

   .. code-block:: console

      $ mv ~/.gitignore_global ~/.config/git/ignore
      $ git config --global --unset core.excludesFile
      $ mv ~/.gitattributes ~/.config/git/attributes
      $ git config --global --unset core.attributesFile

Read and write configuration entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we have already seen above, configuration entries can be read with `git
config <https://git-scm.com/docs/git-config>`_, for example:

.. code-block:: console

   $ git config --global user.name
   Veit Schiele

… and to change it

.. code-block:: console

   $ git config --global user.name 'veit'

You can also edit the configuration file directly by calling ``git config`` with
the ``-e|--edit`` option:

.. code-block:: console

   $ git config --global -e

This opens the :file:`~/.config/git/config` file in your default editor:

.. code-block:: ini

   [user]
       name = veit
       email = veit@cusy.io

Git saves its configuration in `INI <https://en.wikipedia.org/wiki/INI_file>`_
files.

The default editor for Git is defined in the ``GIT_EDITOR`` environment variable
or in Git’s ``core.editor`` option or in the ``VISUAL`` or ``EDITOR``
environment variable. You can query the values with

.. code-block:: console

   $ echo $GIT_EDITOR
   $ git config core.editor
   $ echo $VISUAL
   $ echo $EDITOR

Normally you always want to use the same editor and therefore the ``EDITOR``
environment variable should be set. To do this, you can enter the following in
:file:`~/.bash_profile` or :file:`~/.zprofile`, for example:

.. code-block:: sh

   export EDITOR='C:\Program Files (x86)\Microsoft VS Code\code.exe --wait'

.. note::
   On macOS, you must first start Visual Studio Code, then open the command
   palette with :kbd:`⌘+⇧-p` and finally execute the *Install 'code' command in
   PATH*.

or

.. code-block:: sh

   export EDITOR='vim'

.. _basic-git-config:

Basic configuration
~~~~~~~~~~~~~~~~~~~

Git commits have two mandatory fields that refer to employees: the author who
wrote the code change and the committer who submitted the code to the
repository. For most workflows, this is the same person.  With the options
``user.name`` and ``user.email`` you can configure information for the ``author`` and ``committer``.

:samp:`$ git config --global user.name "{NAME}"`
    defines the name :samp:`{NAME}` associated with your commit transactions.
:samp:`$ git config --global user.email "{EMAIL-ADDRESS}"`
    defines the email address :samp:`{EMAIL-ADDRESS}` that will be linked to
    your commit transactions.

.. seealso::
   * `user.name
     <https://git-scm.com/docs/git-config#Documentation/git-config.txt-username>`_

.. tip::
   Git hosts, such as `GitHub <https://github.com>`_ or
   :doc:`advanced/gitlab/index`, link commits to your profile via the email
   address. If your configured email address does not match your profile, your
   commits will not be assigned. This makes it difficult for team members to
   determine that you have written a specific commit. Therefore, check your
   configured name and your e-mail address.

.. _includeif:

Alternative configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use other configuration files for certain working directories, for
example to distinguish between private and professional projects. You can use a
local configuration in your repository or `conditional includes
<https://git-scm.com/docs/git-config#_conditional_includes>`_ at the end of your
global configuration:

.. code-block:: ini
   :caption: ~/.config/git/config

   [includeIf "gitdir:~/private"]
   path = ~/.config/git/config-private

This construct ensures that Git includes additional configurations or overwrites
existing ones when you work in :file:`~/private`.

Now create the file :file:`~/.config/git/config-private` and define your
alternative configuration there, for example:

.. code-block:: ini
   :caption: ~/.config/git/config-private

   [user]
       email = kontakt@veit-schiele.de
   [core]
       sshCommand = ssh -i ~/.ssh/private_id_rsa

.. seealso::
   * `core.sshCommand
     <https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresshCommand>`_

.. _git-colouring:

Colouring
~~~~~~~~~

By default, Git uses your terminal’s ability to colour and format different
types of text. Such colouring allows you to analyse the output more quickly.
However, the default colours are suboptimal: for example, ``git status`` marks
changed files in red, a colour generally associated with errors; however,
changing files is not an error, but perfectly normal in any Git process. You can
use the ``color.*`` options to adjust the colours per command. I have been using
the `cheat sheet colours
<https://web.archive.org/web/20180223152317/https://cheat.errtheblog.com/s/git>`_
for a long time:

.. code-block:: ini

   [color "branch"]
       current = yellow reverse
       local = yellow
       remote = green

   [color "status"]
       added = yellow
       changed = green
       untracked = cyan

.. note::
   Later we will look at :ref:`git-delta`, a tool to better visualise
   differences. Its colouring would overwrite information from ``[colour
   ‘diff’]`` and therefore we have not added this section.

.. _git-autocorrect:

Correcting commands
~~~~~~~~~~~~~~~~~~~

If you make a mistake when entering a Git command, similar commands are listed
by default and the programme is terminated:

.. code-block:: console

   $ git comit -m ':wrench: Update git config'
   git: 'comit' is not a git command. See 'git --help'.

   The most similar command is
       commit

However, you can also configure Git with ``git config --global help.autoCorrect
immediate`` [#]_ so that the first hit is executed automatically:

.. code-block:: console

   $ git comit -m ':wrench: Update git config'
   WARNING: You called a Git command named 'comit', which does not exist.
   Continuing under the assumption that you meant 'commit'.
   [main 48cafbf5f] :wrench: Update git config

However, Git only corrects automatically if a command has a sufficiently large
match. If there are several potential matches, these are listed and the
correction is cancelled:

.. code-block:: console

   $ git co -m ':wrench: Update git config'
   git: 'co' is not a git command. See 'git --help'.

   The most similar commands are
       commit
       clone
       log

If the automatic correction of an command is too much for you, you can use the
*Prompt* mode instead:

.. code-block:: console

   $ git config --global help.autoCorrect prompt
   $ git comit -m ':wrench: Update git config'
   WARNING: You called a Git command named 'comit', which does not exist.
   Run 'commit' instead [y/N]? y
   [main 48cafbf5f] :wrench: Update git config

.. _git-pagination:

Pagination
~~~~~~~~~~

You can activate pagination by default for a command by setting the
corresponding option: :samp:`pager.{CMD} = true`. [#]_ For example, to switch
git status to pagination:

.. code-block:: console

   $ git config --global pager.status true

.. _credential-helper:

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

.. tab:: Debian/Ubuntu

   With Linux you have to select a so-called: `Credential Store
   <https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/credstores.md>`_.
   In most cases, you will opt for the *Secret Service API*, such as
   ``libsecret`` from Git, which you can select with:

   .. code-block:: console

      $ git config --global credential.credentialStore secretservice

.. tab:: macOS

   With macOS you can use ``osxkeychain`` to store the login information.
   ``osxkeychain`` requires Git version 1.7.10 or newer and can be installed in
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

   Alternatively, you can also install the `Git Credential Manager
   <https://github.com/git-ecosystem/git-credential-manager>`_ with

   .. code-block:: console

      brew install --cask git-credential-manager

.. tab:: Windows

   For Windows, `Git Credential Manager (GCM)
   <https://github.com/git-ecosystem/git-credential-manager>`_ is available. It
   is integrated in `Git for Windows <https://git-scm.com/download/win>`_ and
   is installed by default. However, there is also a standalone Installer in
   `Releases
   <https://github.com/git-ecosystem/git-credential-manager/releases>`_.

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

   Now, when cloning a repository, a *Git Credential Manager* window opens and
   asks you to enter your credentials.

   In addition, the :file:`~/.gitconfig` file is supplemented, for example by
   the following two lines:

   .. code-block:: ini

      [credential "https://ce.cusy.io"]
          provider = generic

.. seealso::
   * `Git Credential Manager: authentication for everyone
     <https://github.blog/security/application-security/git-credential-manager-authentication-for-everyone/>`_

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
| .. code-block:: console       | :file:`instance.log`,             | Usually the pattern match     |
|                               | :file:`logs/instance.log`         | files in any directory.       |
|     instance.log              |                                   |                               |
+-------------------------------+-----------------------------------+-------------------------------+
| .. code-block:: console       | :file:`instance0.log`,            | A question mark fits exactly  |
|                               | :file:`instance1.log`,            | on a character.               |
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

.. warning::
   However, this technique has several disadvantages:

   * Both :file:`.gitignore` and :file:`log/.gitkeep` must be edited.
   * When renaming the directory, it is easy to forget to change the
     :file:`.gitignore` file as well.
   * :file:`.gitkeep` is a completely normal file for Git; however, the name
     suggests that the file would be treated specially by Git.

A better option is to create a :file:`.gitignore` file with the following
content in an empty directory:

.. code-block:: ini

   # ignore everything except .gitignore
   *
   !.gitignore

.. seealso:
   * `Can I add empty directories?
     <https://git.wiki.kernel.org/index.php/GitFaq#Can_I_add_empty_directories.3F>`_

.. _excludesfile:

``excludesfile``
::::::::::::::::

However, you can also exclude files centrally for all Git repositories. For this
purpose, you can set ``excludesfile`` in the :file:`~/.config/git/config` file:

.. code-block:: ini

   [core]
       # Use custom ignore file
       excludesfile = ~/.config/git/ignore
       …

.. note::
   You can find helpful templates in my `dotfiles
   <https://github.com/veit/dotfiles/tree/main/gitignores>`__ repository or
   on the `gitignore.io <https://www.toptal.com/developers/gitignore/>`_
   website.

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
   You can omit the ``--cached`` option if you want to remove the file from both
   the repository and your local file system.

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
.. [#] `help.autoCorrect
       <https://git-scm.com/docs/git-config#Documentation/git-config.txt-helpautoCorrect>`_
.. [#] `pager.cmd <https://git-scm.com/docs/git-config#Documentation/git-config.txt-pagerltcmdgt>`_
.. [#] `git status --ignored
   <https://git-scm.com/docs/git-status#Documentation/git-status.txt---ignoredltmodegt>`_
.. [#] `git check-ignore
   <https://git-scm.com/docs/git-check-ignore>`_
.. [#] `git ls-files --ignored
   <https://git-scm.com/docs/git-ls-files#Documentation/git-ls-files.txt---ignored>`_
