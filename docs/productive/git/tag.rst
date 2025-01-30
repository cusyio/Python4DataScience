.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git tags
========

Git tags are references that point to specific commits in the Git history. This
allows certain points in the history to be marked for a particular version, for
example :samp:`v3.9.16`. Tags are like :doc:`branch` that do not change, so have
no further history of commits.

``git tag``
-----------

:samp:`$ git tag {TAGNAME}`
    creates a tag, where :samp:`{TAGNAME}` is a semantic label for the current
    state of the Git repository. Git distinguishes between two different types
    of tags: annotated and lightweight tags. They differ in the amount of
    associated metadata.

    Annotated tags
        They store not only the :samp:`{TAGNAME}`, but also additional metadata
        such as the name and email address of the person who created the tag and
        the date. In addition, annotated tags have messages, similar to commits.
        You can create such tags, for example with :samp:`git tag -a {v3.9.16}
        -m '{Python 3.9.16}'`. You can then display this additional metadata for
        example with :samp:`git show {v3.9.16}`.
    Lightweight tags
        Lightweight tags can be created, for example, with :samp:`git tag
        {v3.9.16}` without the :samp:`-a`, :samp:`-s` or :samp:`-m` options.
        They create a tag checksum that are stored in the :file:`.git/`
        directory of your repo.

:samp:`$ git tag`
    lists the tags of your repo, for example:

    .. code-block:: console

       0.1.0
       0.1.1
       0.1.10
       0.1.11
       0.1.12
       0.1.2
       …

    .. _tag-sort:

    .. tip::
       However, the order of the tags does not correspond to what we would
       actually expect: After ``0.1.1``, we expect ``0.1.2`` and not ``0.1.10``.
       To achieve this, we can configure Git as follows:

       .. code-block:: console

          git config --global tag.sort version:refname

    :samp:`$ git tag -l '{REGEX}'`
        lists only tags that match a regular expression.

:samp:`$ git tag -a {TAGNAME} {COMMIT-SHA}`
    creates a tag for a previous commit.

    The previous examples create tags for implicit commits that reference
    ``HEAD``. Alternatively, :samp:`git tag` can be passed the reference to a
    specific commit that you get with :doc:`review`.

    However, if you try to create a tag with the same identifier as an existing
    tag, Git will give you an error message, for example :samp:`Fatal: tag
    'v3.9.16' already exists`. If you try to tag an older commit with an
    existing tag, Git will give the same error.

    In case you need to update an existing tag, you can use the ``-f`` option,
    for example:

    .. code-block:: console

        $ git tag -af v3.9.16 595f9ccb0c059f2fb5bf13643bfc0cdd5b55a422 -m 'Python 3.9.16'
        Tag 'v3.9.16' updated (was 4f5c5473ea)

:samp:`$ git push origin {TAGNAME}`
    Sharing tags is similar to pushing branches: by default, :samp:`git push`
    does not share tags, but they must be explicitly passed to :samp:`git push
    for example`:

    .. code-block:: console

        $ git tag -af v3.9.16 -m 'Python 3.9.16'
        $ git push origin v3.9.16
        Counting objects: 1, done.
        Writing objects: 100% (1/1), 161 bytes, done.
        Total 1 (delta 0), reused 0 (delta 0)
        To git@github.com:python/cpython.git
         * [new tag]         v3.9.16 -> v3.9.16

    To send tags to the server, you can use the :samp:`--tags` option for the
    :samp:`git push` command. Others receive the tags with :samp:`git clone`,
    :samp:`git pull` or :samp:`git fetch` of the repo.

    With ``git push --follow-tags`` you can also share the corresponding
    annotated tags with a commit.

    .. note::
       ``--follow-tags`` works for annotated tags, not for lightweight tags.

    If you want to use ``--follow-tags`` for all future pushes, you can
    configure this with

    .. code-block:: console

       $ git config --global push.followTags true

    .. seealso::
       * `git push --follow-tags
         <https://git-scm.com/docs/git-push#Documentation/git-push.txt---follow-tags>`_
       * `git config push.followTags
         <https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushfollowTags>`_

:samp:`$ git checkout {TAGNAME}`
    switches to the state of the repo with this tag and detaches ``HEAD``. This
    means that any changes made now will not update the tag, but will end up in
    a detached commit that cannot be part of a branch and will only be directly
    accessible via the SHA hash of the commit. Therefore, a new branch is
    usually created when such changes are to be made, for example with
    :samp:`git checkout -b v3.9.17 v3.9.16`.

:samp:`$ git tag -d {TAGNAME}`
    deletes a tag, for example:

    .. code-block:: console

        $ git tag -d v3.9.16
        $ git push origin --delete v3.9.16

    .. _prune-tags:

    If tags that have been deleted on the server should also be deleted locally,
    you can use :samp:`git fetch --prune-tags`. Alternatively, you can also
    adjust the global configuration with:

    .. code-block:: console

       $ git config --global fetch.pruneTags true

``git describe``
----------------

The :samp:`git describe {SH}` command finds the most recent tag that can be
reached from a commit. If the tag points to the commit, only the tag is
displayed, otherwise the number of additional commits is appended to the tag
name. The result is an object name that can be used by other Git commands to
identify the commit. Assuming you have a commit SHA and want to know in which
version it was first published, you can use the following command:

.. code-block:: console

   $ git describe --contains 39ff38d | sed -E 's/[~^][0-9]*//g'
   24.1.0
