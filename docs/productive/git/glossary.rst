.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git glossary
============

.. glossary::

    Branch
        A branch is a development line. The last commit on a branch is called
        the tip of the branch, which is referenced by a ``head`` and which moves
        on as more development is done on the branch. A single Git repository
        can have any number of branches, but its :term:`Working Tree` is
        associated with only one of them – the current or checked-out branch –
        and :term:`HEAD` points to that branch.

    Cache
        iObsolete for :term:`Index`.

    Clone
        Local version of a repository including all commits and branches.

    Commit
        A snapshot of the entire Git repository, compressed in a `SHA
        <https://en.wikipedia.org/wiki/Secure_Hash_Algorithms>`_.

    Fork
        A copy of a repository on GitLab that belongs to another user or group.

    Git
        Git is a distributed version control system.

    GitLab
        Web application for version management based on :term:`git`. RGitlab CI,
        a system for continuous integration, GitLab Runner, container registry
        and much more were added later.

    ``HEAD``
        The ``HEAD`` pointer represents your current working directory and can
        be moved to different branches, tags or commits using git switch.

    Index
        A collection of files with status information whose content is saved as
        objects. The index is a saved version of your :term:`Working Tree`.

    ``origin``
        The usual upstream repository. Most projects have at least one upstream
        project that they track. By default, ``origin`` is used for this
        purpose. New upstream updates are fetched into branches named
        :samp:`origin/{NAME_OF_UPSTREAM_BRANCH}`, which you can see with ``git
        branch -r``.

    Remote repository
        A repository that is used to track a shared project but is located
        elsewhere.

    ``remote``
        shared repository, for example on GitLab, for exchanging changes in a
        team

    ``fork``
        Copy of a repository on GitLab that belongs to another user

    Merge request
        Place to compare and discuss the changes introduced in a branch with
        ratings, comments, tests etc.; see also `Merge requests
        <https://docs.gitlab.com/ee/user/project/merge_requests/>`_.

    Trunk-Based Development
    TBD
         Git workflow with short-lived topic branches that are quickly merged
         into a single ``main`` branch.

         .. seealso::
            * `Trunk Based Development <https://trunkbaseddevelopment.com/>`_


    Working Tree
        The tree of the files actually checked out. The working tree normally
        contains the content of the :term:`HEAD` commit tree as well as all
        local changes that you have made but not yet transferred.
