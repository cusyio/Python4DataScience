.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git best practices
==================

Commit early
------------

Make your first commit after you’ve finished the initial installation and
before you make your first changes. For a cookie cutter template, for example,
proceed as follows:

.. code-block:: console

   $ pipenv run cookiecutter https://github.com/veit/cookiecutter-namespace-template.git
   full_name [Veit Schiele]:
   email [veit@cusy.io]:
   github_username [veit]:
   project_name [cusy.example]:
   …

These initial changes can then be checked in with:

.. code-block:: console

   $ cd cusy.example
   $ git init
   $ git add *
   $ git add .gitignore
   $ git commit -m 'Initial commit'
   $ git remote add origin ssh://git@github.com:veit/cusy.example.git
   $ git push -u origin main

Exclude undesired files
-----------------------

Temporary files, jupyter checkpoint folders and builds have no business in a git
repository. Credentials do not either. The :file:`.gitignore` file contains a
list of paths that git will not add unless you ask for it explicitly.

You can find a template ``.gitignore`` file for Python projects in the
`dotfiles <https://github.com/veit/dotfiles>`_ repository.
The `gitignore.io  <https://gitignore.io/>`_ website contains :file:`.gitignore`
files for other programming languages.
The :file:`.gitignore` file itself should be checked in, too:

.. code-block:: console

   $ git add .gitignore
   $ git commit -m 'add .gitignore file'

If you have accidentally checked undesired files into your Git repository, you
can remove them again with:

.. code-block:: console

   $ git rm -r .ipynb_checkpoints/

Write a README
--------------

Each repository should also have a :file:`README.rst` file that describes the
deployment and the basic structure of the code.

Commit often
------------

Each completed task and subtask should be immediately followed by a commit.
Incomplete work also may be stored on git. As a rule of thumb you should commit
at least daily before leaving work. In busy times it is common to commit every
10 minutes.

Frequent commits make it easier for you to:

* isolate errors
* understand the code
* maintain the code in the future

If you have made several changes to a file, you can split them up into several
commits later with:

.. code-block:: console

  $ git add -p my-changed-file.py

Don’t change the published history
----------------------------------

Even if you later find out that a commit that has already been published with
``git push`` contains one or more errors, you should never try to undo this
commit. Rather, you should fix the error that have occurred through further
commits.

.. warning::

   Workflows with ``git rebase`` are a reasonable exception to this rule.

Choose a Git workflow
---------------------

Choose a workflow that fits best to your project. Projects are by no means
identical and a workflow that fits one project does not necessarily have to
fit in another project. A different workflow can be recommended initially than
in the further progress of the project.

Write meaningful commit messages
--------------------------------

By creating insightful and descriptive commit messages, you make working in a
team a lot easier. They allow others to understand your changes. They are also
helpful at a later point in time to understand which goal should be achieved
with the code.

Usually short messages, 50–72 characters long, should be specified and
displayed on one line, eg with ``git log --oneline``.

With ``git blame`` you can later specify for each line in which revision and
by which author the change was made. You can find more information on this in
the Git documentation: `git-blame <https://git-scm.com/docs/git-blame>`_.

If you use gitmojis in your commit messages, you can easily see the intent of
the commit later.

.. note::

   * `gitmoji.dev <https://gitmoji.dev/>`_
   * `github.com/carloscuesta/gitmoji
     <https://github.com/carloscuesta/gitmoji>`_
   * `github.com/carloscuesta/gitmoji-cli
     <https://github.com/carloscuesta/gitmoji-cli>`_
   * `Visual Studio Code Extension
     <https://marketplace.visualstudio.com/items?itemName=seatonjiang.gitmoji-vscode>`_

GitLab also interprets certain commit messages as links, for example:

.. code-block:: console

   $ git commit -m "Awesome commit message (Fix #21 and close group/otherproject#22)"

* links to issues: :samp:`#{NUMBER}`
* links to issues in other projects: :samp:`{GROUP/PROJECT}#{NUMBER}`
* links to merge requests: :samp:`!{NUMBER}`
* links to snippets: :samp:`${NUMBER}`

There should be at least one ticket for each commit that should provide more
detailed information about the changes.

There should be at least one ticket for each commit, which should contain more
detailed information about the changes. Alternatively, you can also write
multi-line commit messages containing this information, for example with:

.. code-block:: console

   $ git commit -m 'Expand section on meaningful commit messages' -m 'Fix the serious problem'

Or, if you just enter :samp:`git commit`, your editor will open, for example
with the following text:

.. code-block:: ini

   # Please enter the commit message for your changes. Lines starting
   # with '#' will be ignored, and an empty message aborts the commit.
   #
   # On branch main

Git expects you to insert your commit message at the beginning of the file.
After you have finished editing the file, Git reads its contents and continues.
It cleans up the file by removing lines commented with ``#`` and subsequent
empty lines. If the message is empty after cleaning up, Git cancels the commit –
this is useful if you realise that you have forgotten something. Otherwise, the
commit is created with the remaining content. However, GitLab uses ``#`` as a
prefix for the number of an item. This double meaning of ``#`` can lead to
confusion if you write a commit message that refers to an item:

.. code-block:: ini

   Expand section on meaningful commit messages
   #21: Add multi-line commit messages
   # Please enter the commit message for your changes. Lines starting
   # with '#' will be ignored, and an empty message aborts the commit.
   #
   # On branch main
   # Changes to be committed:
   #       modified:   productive/git/best-practices.rst
   #

Git usually removes the line starting with #21 so that the message looks like
this:

.. code-block:: ini

   Expand section on meaningful commit messages

Avoid this mishap by using an alternative clean-up mode called *Scissors*. You
can activate it globally with:

.. code-block:: console

   $ git config --global commit.cleanup scissors

Git then starts each new commit message with the *Scissorsr* line:

.. code-block:: ini

   # ------------------------ >8 ------------------------
   # Do not modify or remove the line above.
   # Everything below it will be ignored.
   #
   # On branch main
   # ...
   #

Specify co-authors
~~~~~~~~~~~~~~~~~~

If you are working on a commit with a team member, it’s good to acknowledge
their contribution with the ``co-authored-by`` trailer. Trailers are additional
metadata at the end of the commit message that use a :samp:`{KEY}: {VALUE}`
syntax and can be repeated to list multiple values:

.. code-block:: ini

   Expand section on meaningful commit messages
   #21: Add multi-line commit messages
   co-authored-by: Kristian Rother <kristian.rother@cusy.io>
   co-authored-by: Frank Hofmann <frank.hofmann@cusy.io>

GitLab analyses the ``co-authored-by`` lines to display all avatars of the
commit and also to update the profile statistics of the co-authors, :abbr:`etc.
(et cetera)`.

Maintain your repository regularly
----------------------------------

You should perform the following maintenance work regularly:

Validate the repo
~~~~~~~~~~~~~~~~~

The command ``git fsck`` checks whether all objects in the internal
datastructure of git are consistently connected with each other.

Compresses the repo
~~~~~~~~~~~~~~~~~~~

Save storage space with the command ``git gc`` or ``git gc --aggressive``.

.. seealso::
    * `git gc <https://git-scm.com/docs/git-gc>`_
    * `Git Internals - Maintenance and Data Recovery
      <https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery>`_

Clean up remote tracking branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unused branches on a server can be removed with ``git remote update --prune``.
It is even better if you change the default setting so that remotely deleted
branches are also deleted locally with ``git fetch`` and ``git pull``. You
can achieve this with:

.. code-block:: console

    $ git config --global fetch.prune true

Check forgotten work
~~~~~~~~~~~~~~~~~~~~

Display a list of saved stashes with ``git stash list``. They can be removed
with ``git stash drop``.

Check your repositories for unwanted files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With `Gitleaks <https://github.com/zricethezav/gitleaks>`_ you can regularly
check your repositories for unintentionally saved access data.

You can also run Gitleaks automatically as a GitLab action. To do this, you need
to include the `Secret-Detection.gitlab-ci.yml
<https://gitlab.com/gitlab-org/gitlab/-/blob/master/lib/gitlab/ci/templates/Jobs/Secret-Detection.gitlab-ci.yml>`_
template, for example, in a stage called ``secrets-detection`` in your
:file:`.gitlab-ci.yml` file:

.. code-block:: yaml

    stages:
      - secrets-detection

    gitleaks:
      stage: secrets-detection
      include:
        - template: Security/Secret-Detection.gitlab-ci.yml

The template creates secret detection jobs in your CI/CD pipeline and searches
the source code of your project for secrets. The results are saved as a `Secret
Detection Report Artefakt
<https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportssecret_detection>`_
that you can download and analyse later.

.. seealso::

    * `GitLab Secret Detection
      <https://docs.gitlab.com/ee/user/application_security/secret_detection/>`_

With :ref:`git-filter-repo <git-filter-repo>` you can remove unwanted files from
your Git history.
