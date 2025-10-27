.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git hooks
=========

Git hooks are scripts that are automatically executed when certain events occur
in a Git repository, including:

+---------------+-------------------------------------------------------+
| Command       | Hooks                                                 |
+===============+=======================================================+
| ``git commit``| `prepare-commit-msg`_, `pre-commit`_, `commit-msg`_,  |
|               | `post-commit`_                                        |
+---------------+-------------------------------------------------------+
| ``git merge`` | `pre-merge-commit`_, `commit-msg`_,  `post-merge`_    |
+---------------+-------------------------------------------------------+
| ``git rebase``| `pre-rebase`_, `post-rewrite`_                        |
+---------------+-------------------------------------------------------+
| ``git pull``  | `post-merge`_                                         |
+---------------+-------------------------------------------------------+
| ``git push``  | `pre-push`_, `pre-receive`_, `update`_,               |
|               | `post-update`_, `proc-receive`_, `post-receive`_,     |
|               | `push-to-checkout`_                                   |
+---------------+-------------------------------------------------------+

They can be located either in local or server-side repositories. This allows Git
repositories to be customised and user-defined actions to be triggered.

Git hooks are located in the :file:`.git/hooks/` directory. When a repository is
created, some sample scripts are already created there:

.. code-block:: console

   .git/hooks
   ├── applypatch-msg.sample
   ├── commit-msg.sample
   ├── fsmonitor-watchman.sample
   ├── post-update.sample
   ├── pre-applypatch.sample
   ├── pre-commit.sample
   ├── pre-merge-commit.sample
   ├── pre-push.sample
   ├── pre-rebase.sample
   ├── pre-receive.sample
   ├── prepare-commit-msg.sample
   ├── push-to-checkout.sample
   ├── sendemail-validate.sample
   └── update.sample

For the scripts to be executed, only the suffix ``.sample`` must be removed and,
if necessary, the file permission must be executable, for example with
:samp:`chmod +x .git/{PREPARE-COMMIT-MSG}`.

The integrated scripts are shell and Perl scripts, but any scripting language
can be used. The Shebang line (:samp:`#!/bin/sh`) determines how the file is to
be interpreted.

However, the scripts cannot be copied into the server-side repository.

.. seealso::
   * `Hooks <https://git-scm.com/docs/githooks#_hooks>`_

.. toctree::
    :hidden:

    pre-commit
    scripts
    hooks
    ci
    skip
    template

.. _`prepare-commit-msg`: https://git-scm.com/docs/githooks#_prepare_commit_msg
.. _`pre-commit`: https://git-scm.com/docs/githooks#_pre_commit
.. _`post-commit`: https://git-scm.com/docs/githooks#_post_commit
.. _`commit-msg`: https://git-scm.com/docs/githooks#_commit_msg
.. _`pre-merge-commit`: https://git-scm.com/docs/githooks#_pre_merge_commit
.. _`post-merge`: https://git-scm.com/docs/githooks#_post_merge
.. _`pre-rebase`: https://git-scm.com/docs/githooks#_pre_rebase
.. _`post-rewrite`: https://git-scm.com/docs/githooks#_post_rewrite
.. _`pre-push`: https://git-scm.com/docs/githooks#_pre_push
.. _`pre-receive`: https://git-scm.com/docs/githooks#pre-receive
.. _`update`: https://git-scm.com/docs/githooks#update
.. _`post-update`: https://git-scm.com/docs/githooks#post-update
.. _`proc-receive`: https://git-scm.com/docs/githooks#proc-receive
.. _`post-receive`: https://git-scm.com/docs/githooks#post-receive
.. _`push-to-checkout`: https://git-scm.com/docs/githooks#_push_to_checkout
