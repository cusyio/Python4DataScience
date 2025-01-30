.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Supported git hooks
===================

The hooks managed by the pre-commit framework are not limited to being executed
before commits; they can also be used for other Git hooks:

* :ref:`commit-msg <commit-msg-hook>`
* :ref:`post-checkout <post-checkout-hook>`
* :ref:`post-commit <post-commit-hook>`
* :ref:`post-merge <post-merge-hook>`
* :ref:`post-rewrite <post-rewrite-hook>`
* :ref:`pre-merge-commit <pre-merge-commit-hook>`
* :ref:`pre-push <pre-push-hook>`
* :ref:`pre-rebase <pre-rebase-hook>`
* :ref:`prepare-commit-msg <prepare-commit-msg-hook>`

.. _commit-msg-hook:

``commit-msg``
    `commit-msg <https://git-scm.com/docs/githooks#_commit_msg>`_ can be used
    with:

    .. code-block:: console

       $ uv run pre-commit install --hook-type commit-msg
       pre-commit installed at .git/hooks/commit-msg

    The ``commit-msg`` hook can be configured with ``stages: [commit-msg]``,
    passing the name of a file containing the current contents of the commit
    message that can be checked.

.. _post-checkout-hook:

``post-checkout``
    The `post-checkout <https://git-scm.com/docs/githooks#_post_checkout>`_ hook
    is called when ``git checkout`` or ``git switch`` is executed.

    The ``post-checkout`` hook can be used for example for

    * checking repositories
    * viewing differences from the previous ``HEAD``
    * changing the metadata of the working directory.

    In pre-commit it can be used with:

    .. code-block:: console

        $ uv run pre-commit install --hook-type post-checkout
        pre-commit installed at .git/hooks/post-checkout

    Since ``post-checkout does`` not act on files, ``always_run`` must be set
    for all ``post-checkout`` scripts, for example:

    .. code-block:: yaml

        - repo: local
          hooks:
          - id: post-checkout-local
            name: Post checkout
            always_run: true
            stages: [post-checkout]
            # …

    There are three environment variables that correspond to the three arguments
    of ``post-checkout``:

    ``$PRE_COMMIT_FROM_REF``
        returns the reference of the previous ``HEAD``
    ``$PRE_COMMIT_TO_REF``
        returns the reference of the new ``HEAD``, which may or may not have
        changed.
    ``$PRE_COMMIT_CHECKOUT_TYPE``
        returns ``Flag=1`` if it was a branch checkout and ``Flag=0`` if it was
        a file checkout.

.. _post-merge-hook:

``post-merge``
    As of version 2.11.0, the framework can also execute scripts for the
    `post-merge <https://git-scm.com/docs/githooks#_post_merge>`_ hook:

    .. code-block:: console

        $ uv run pre-commit install --hook-type post-merge
        pre-commit installed at .git/hooks/post-merge

    With ``$PRE_COMMIT_IS_SQUASH_MERGE`` you can find out if it was a squash
    merge.

.. _post-rewrite-hook:

``post-rewrite``
    `post-rewrite <https://git-scm.com/docs/githooks#_post_rewrite>`_ is called
    when commits are rewritten, for example from ``git commit --amend`` or from
    ``git rebase``.

    .. code-block:: console

        $ uv run pre-commit install --hook-type post-rewrite
        pre-commit installed at .git/hooks/post-rewrite

    Since ``post-rewrite`` does not affect files, ``always_run: true`` must be
    set.

    Git tells the ``post-rewrite`` hook which command triggered the rewrite.
    ``pre-commit`` outputs this as ``$PRE_COMMIT_REWRITE_COMMAND``.

.. _pre-merge-commit-hook:

``pre-merge-commit``
    As of Git 2.24, there is a `pre-merge-commit
    <https://git-scm.com/docs/githooks#_pre_merge_commit>`_ hook that is
    triggered after a merge is successful but before the merge commit is
    created. You can use it with the pre-commit framework with:

    .. code-block:: console

        $ uv run pre-commit install --hook-type pre-merge-commit
        pre-commit installed at .git/hooks/pre-merge-commit

.. _pre-push-hook:

``pre-push``
    To use the `pre-push <https://git-scm.com/docs/githooks#_pre_push>`_ hook
    with the pre-commit framework, enter the following:

    .. code-block:: console

        $ uv run pre-commit install --hook-type pre-push
        pre-commit installed at .git/hooks/pre-push

    The following environment variables are provided for this purpose:

    ``$PRE_COMMIT_FROM_REF``
        The remote revision that was pushed to.
    ``$PRE_COMMIT_TO_REF``
        The local revision that was pushed to the remote revision.
    ``$PRE_COMMIT_REMOTE_NAME``
        The local revision that was pushed to the remote revision, for example
        :samp:`origin`.
    ``$PRE_COMMIT_REMOTE_URL``
        The URL of the remote repository that was pushed to, for example
        :samp:`git@github.com:veit/python4datascience`
    ``$PRE_COMMIT_REMOTE_BRANCH``
        The name of the remote branch that was pushed to, for example
        :samp:`refs/heads/{TARGET_BRANCH}`.
    ``$PRE_COMMIT_LOCAL_BRANCH``
        The name of the local branch that was pushed to the remote branch, for
        example :samp:`{HEAD}`.

.. _pre-rebase-hook:

``pre-rebase``
    Since version 3.2.0, the framework also supports `pre-rebase
    <https://git-scm.com/docs/githooks#_pre_rebase>`_ hooks:

    .. code-block:: console

       $ uv run pre-commit install --hook-type pre-rebase
       pre-rebase installed at .git/hooks/pre-rebase

    ``pre-rebase`` hooks cannot be applied to files, and therefore they must be
    set as ``always_run: true``, otherwise they will always be skipped.

.. _post-commit-hook:

``post-commit``
    As of version 2.4.0, the framework can also execute `post-commit
    <https://git-scm.com/docs/githooks#_post_commit>`_ hooks with:

    .. code-block:: console

       $ uv run pre-commit install --hook-type post-commit
       pre-commit installed at .git/hooks/post-commit

    However, since ``post-commit`` does not work on files, all these hooks must
    set ``always_run``:

    .. code-block:: yaml

        - repo: local
          hooks:
          - id: post-commit-local
            name: post commit
            always_run: true
            stages: [post-commit]
            # …

.. _prepare-commit-msg-hook:

``prepare-commit-msg``
    `prepare-commit-msg
    <https://git-scm.com/docs/githooks#_prepare_commit_msg>`_ can be used with
    pre-commit with:

    .. code-block:: console

        $ uv run pre-commit install --hook-type prepare-commit-msg
        pre-commit installed at .git/hooks/prepare-commit-msg

    The ``prepare-commit-msg`` hook is configured with ``stages:
    [prepare-commit-msg]``, passing the name of a file that contains the initial
    commit message, for example from :samp:`git commit -m "{COMMIT-MESSAGE}"` to
    create a dynamic template from it that is displayed in the editor. Finally,
    the hook should check that no editor is started with ``GIT_EDITOR=:``.
