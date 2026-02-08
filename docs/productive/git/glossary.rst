.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git glossary
============

.. glossary::

    Blob

        .. _start-blob

        A blob object contains the contents of a file

        With each :term:`commit`, Git stores the entire contents of each file
        you have changed as a blob. For example, if you have a commit that
        changes two files in a repository, that commit creates two new blobs, so
        commits take up relatively little storage space even in very large
        repositories.

        .. _end-blob

    Branch
        A branch is a line of development. The last :term:`commit` on a branch
        is called the tip of the branch, which is referenced by a :term:`HEAD`
        and moves forward as further development is made on the branch. A single
        Git repository can have any number of branches, but your working tree is
        only connected to one of them – the *current* or *checked-out* branch –
        and :term:`HEAD` points to that branch.

    Cache
        Obsolete for :term:`Index`.

    Clone
        Local version of a repository including all :term:`commits <commit>` and
        :term:`branches <branch>`.

    Commit
        .. _start-commit

        A commit is a snapshot of the entire Git repository that can be uniquely
        identified by a `SHA
        <https://en.wikipedia.org/wiki/Secure_Hash_Algorithms>`_ value and
        contains at least the following information:

        * Directory structure of all files in this version of the repository and
          the contents of each file, stored as the :term:`tree` ID of the
          top-level directory of the commit.
        * ID(s) of the parent commit(s). The first commit of a repository has no
          parent commits, regular commits have one parent commit, merge commits
          have two or more parent commits.
        * Author and time when the commit was created.
        * Committer and time when the commit was committed.
        * Commit message

        Example:

        .. code-block:: console

           $ git cat-file -p main
           tree 47cc0283b10bd5e4e8a0d61537d13bba3bfad916
           parent 63825a43e213ef8a7904a8994976ac86284d32bd
           author veit <veit@cusy.io> 1770370977 +0100
           committer veit <veit@cusy.io> 1770370977 +0100

           :memo: Add links to Python speed

        Like all other objects, commits cannot be changed after they have been
        created. So if you want to change a commit with ``git commit --amend``,
        a new commit with the same parent is actually created. And even if you
        display a commit with ``git show``, the diff is only calculated at that
        point in time.

        .. seealso::
           * `Commits are snapshots, not diffs
             <https://github.blog/open-source/git/commits-are-snapshots-not-diffs/>`_

        .. _end-commit

     A snapshot of the entire Git repository, compressed in a `SHA
        <https://en.wikipedia.org/wiki/Secure_Hash_Algorithms>`_.

    Fork
        A copy of a repository on :term:`GitHub` or :term:`GitLab` that belongs
        to another user or group. This enables :term:`merge requests <Merge
        request>`.

    Git
        Git is a distributed version control system.

    GitHub
        Web application for version management based on :term:`git`, which also
        enables collaboration via :term:`Forks <Fork>`. There are also `GitHub
        Actions <https://docs.github.com/de/actions>`_ and `GitHub Pages
        <https://pages.github.com>`_ extensions for continuous integration and
        static websites.

    GitLab
        Web application for version management based on :term:`git`. Later,
        :doc:`advanced/gitlab/ci-cd/index`, a system for continuous integration,
        GitLab Runner, :doc:`advanced/gitlab/package-registry`,
        :doc:`advanced/gitlab/ci-cd/pages` and many other things were added.

        .. seealso::
           * :doc:`advanced/gitlab/index`

    ``HEAD``
        The ``HEAD`` pointer represents your current working directory and can
        be moved to different :term:`branches <branch>`, :term:`tags <tag>` or
        :term: commits <commit>` using ``git switch``.

    Index
    Staging area
        .. _start-index

        List of files and their contents stored as :term:`blob`. With ``git
        add``, you can add files to the index or update the contents of a file
        in the index.

        Unlike a :term:`tree`, the index is a flat list of files. When you
        commit, Git converts the list of files in the index into a directory
        tree and uses that tree for the new commit. Each index entry has four
        fields:

        #. One of the following four file types:

           * regular file
           * executable file
           * symbolic link
           * gitlink (for submodules)

        #. Blob ID of the file or commit ID of the submodule
        #. Staging number, usually ``0``. However, in the event of a merge
           conflict, there may be multiple versions of the same file name in the
           index.
        #. File path

        .. _end-index

    ``origin``
        The usual upstream repository. Most projects have at least one upstream
        project that they track. By default, ``origin`` is used for this
        purpose. New upstream updates are fetched into branches named
        :samp:`origin/{NAME_OF_UPSTREAM_BRANCH}`, which you can see with ``git
        branch -r``.

    Merge request
        Place to compare and discuss the changes introduced in a branch with
        ratings, comments, tests :abbr:`etc. (et cetera)`.

        .. seealso::
           * :doc:`advanced/gitlab/merge-requests`
           * :ref:`Merge or pull requests <merge-pull-requests>`

    Object

        .. _start-object

        All :term:`commits <Commit>`, :term:`trees <Tree>`, :term:`blobs
        <Blob>`, and :term:`tags <Tag>` in a Git repository are stored as Git
        objects, which never change after they are created and have a unique ID,
        such as ``3a5c279ea2f5d18498b61c229571d2449305a0``. This means that you
        can use an object’s ID to restore its contents at any time, as long as
        the object has not been deleted.

        .. seealso::
           * `Git Internals - Git Objects
             <https://git-scm.com/book/en/v2/Git-Internals-Git-Objects>`_

        .. _end-object

    Packfile

        .. _start-packfile

        The format in which Git stores objects on the hard drive is called the
        *loose* object format. However, to save space, Git occasionally packs
        several of these objects into a single binary file called Packfile in
        order to save space and work more efficiently. You can also perform
        packing manually with ``git push`` or ``git gc``. This will delete most
        of your objects in :file:`.git/objects/` and create a new pair of files:

        .. code-block:: console

           $ find .git/objects -type f
           .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.pack
           .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.idx

        :file:`*.pack`
            contains the contents of all objects that have been removed from
            your file system.
        :file:`.idx`
            contains the offsets of this pack file, allowing you to quickly jump
            to a specific object.

        Any remaining objects are :term:`blobs <Blob>` that are not referenced
        by any commit, known as *dangling references* , such as files in the
        working directory that were never added to a commit.

        When Git packs objects, it looks for files with similar names and sizes
        and only stores the deltas from one version of the file to the next.
        With ``git verify-pack``, you can view the pack file and see how Git
        saved storage space:

        .. code-block:: console

           $ git verify-pack -v .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.pack
           ...
           dd1827ebf73b22d9f5828eec005eda4d79520f57 blob   147 140 389838
           0a66f9a9ab72e3a99994803de8337f523b1b93d0 blob   31 43 389978 1 dd1827ebf73b22d9f5828eec005eda4d79520f57
           ...
           .git/objects/pack/pack-e9282cda3898f806f7bd108a3675c9e4d236915c.pack: ok

        * :term:`Blob` ``0a66f9a`` refers to the following blob ``dd1827e``.
        * The third column indicates the size of the object in the packfile, so
          you can see that ``dd1827e`` takes up 147 bytes, while  ``0a66f9a``
          only takes up 31 bytes.
        * The current file is therefore stored unchanged, while the original
          version is stored as a delta. This allows faster access to the latest
          version of a file.
        * The general syntax of  ``git verify-pack -v`` is:

          :samp:`{OBJECT-ID} {TYPE} {SIZE} {SIZE-IN-PACKFILE} {OFFSET-IN-PACKFILE} [{DEPTH} {BASE-ID}]`

        .. seealso::
           * `Git Internals - Packfiles
             <https://git-scm.com/book/en/v2/Git-Internals-Packfiles>`_
           * `git verify-pack <https://git-scm.com/docs/git-verify-pack>`_

        .. _end-packfile

    Reference

        .. _start-refs

        References are a way to give commits a name that is easier to remember,
        such as for :doc:`branches <Branch>`, :doc:`tags <Tag>`,
        :ref:`remote-branches`, and so on. Git often uses ``ref`` as an
        abbreviation for such references. The most important references are:

        :samp:`.git/refs/heads/{BRANCHNAME}`
            A branch refers to the ID of the latest  :term:`commit` on that
             :term:`branch`. To retrieve the history of commits on a branch, Git
             starts with the commit ID that the branch points to and then looks
             at the parent commits. References can refer to

            * an object ID, usually a commit ID
            * another *symbolic* reference

        :samp:`.git/refs/tags/{TAGNAME}`
            A tag refers to a commit ID, a tag object ID, or another object ID.

        ``.git/HEAD``
            :term:`HEAD` is where Git stores your current branch. ``HEAD`` can
            be either

            * a symbolic reference to your current branch, for example ``ref:
              refs/heads/main``.
            * a direct reference to a commit ID if there is no current branch,
              that is, in a *detached HEAD state*.

        :samp:`.git/refs/remotes/{REMOTE}/{BRANCHNAME}`
            A remote tracking branch refers to a commit ID. You can update it
            with ``git fetch`` if necessary, and if ``git status`` outputs
            ``Your branch is up to date with 'origin/main'``, it refers to it.

            ``refs/remotes/{REMOTE}/HEAD`` is a symbolic reference to the
            default branch of the remote repository.

        .. seealso::
           * `Git Internals - Git References
             <https://git-scm.com/book/en/v2/Git-Internals-Git-References>`_

        .. _end-refs:

    Reflog

        .. _start-reflog

        Every time a :term:`branch`, a :ref:`remote tracking branch
        <remote-branches>, or :term:`HEAD` is updated, Git updates a log called
        *reflog* for that reference, for example in
        :file:`.git/logs/refs/heads/main`:

        .. code-block:: console

           0000000000000000000000000000000000000000 492e16edcf9cdb3371492be59735e517a17cc86c veit <veit@cusy.io> 1739549686 +0100  clone: from github.com:cusyio/Python4DataScience-de.git
           492e16edcf9cdb3371492be59735e517a17cc86c c40bfa2a238e824b619f760494ce5ce0769851c3 veit <veit@cusy.io> 1739549907 +0100  commit: Update git docs
           c40bfa2a238e824b619f760494ce5ce0769851c3 fa39661bb7fa93b420870845cb174529e8d62552 veit <veit@cusy.io> 1739549971 +0100  rebase (finish): refs/heads/main onto b7214df753ecbd01acd90d8f3dcd359e02441249
           ...

        Each entry in the reflog contains:

        * Commit ID
        * Commit ID of the subsequent commits
        * Author
        * Email address
        * Timestamp when the change was made
        * Log message, for example:

          * :samp:`clone: from {REMOTE-URL}`
          * :samp:`commit: {COMMIT-MESSAGE}`
          * :samp:`rebase (finish): refs/heads/main onto {BASIC-COMMIT-ID}`

        Reflogs log changes made in your local repository. However, they are not
        shared in the :term:`remote repository`.

        .. seealso::
           * :ref:`reflog`

        .. _end-reflog

    Remote repository
        shared repository, for example on :term:`GitLab`, for exchanging changes
        in a team.

    Tag object

        .. _start-tag

        Tag objects contain at least the following fields:

        *  of the object to which it refers
        * Type of the object to which it refers
        * Tag message
        * Tagger and tag date

        Example:

        .. code-block:: console

           $ git cat-file -p 24.3.0
           object aa366cc9af3497544338482f82bdeb21f1dd3c21
           type commit
           tag 24.3.0
           tagger Veit Schiele <veit@cusy.io> 1732086922 +0100

        .. _end-tag

    Tree

        .. _start-tree

        Representation of a directory in Git and can contain files or other
        trees (subdirectories). For each element in the tree, it lists the
        following:

        * File name
        * File type:

          * normal file
          * executable file
          * symbolic link
          * directory
          * gitlink (for submodules)

        * Object ID with the contents of the file, directory or gitlink

        Example:

        .. code-block:: console

           $ git cat-file -p main^{tree}
           040000 tree 2f59a223f7dc767f4776e77762d208fa72bfd343 .dvc
           040000 tree 75833fd33271db55b6f1c96915f60f98a60b51a0 .github
           100644 blob 36d2dc5a5228cbf65b8cfe913565c9be49db1a3d .gitignore
           ...
           $ git cat-file -p 2f59a223f7dc767f4776e77762d208fa72bfd343
           100644 blob 669784da1fe0818e9abb795f73b7faf393832f2e .gitignore
           100644 blob 0a66f9a9ab72e3a99994803de8337f523b1b93d0 config
           $ git cat-file -p 36d2dc5a5228cbf65b8cfe913565c9be49db1a3d
           # SPDX-FileCopyrightText: 2019 Veit Schiele
           #
           # SPDX-License-Identifier: BSD-3-Clause
           ...

        .. hint::
           The first column of a tree entry is roughly based on `Unix file
           permissions
           <https://en.wikipedia.org/wiki/File-system_permissions#UNIX_and_Unix-like_systems>`_,
           , but Git cannot actually manage Unix file permissions. Extensions
           such as :doc:`/productive/git/advanced/etckeeper` are required for
           this.

        .. _end-tree

    Trunk-Based Development
    TBD
         Git workflow with short-lived topic branches that are quickly merged
         into a single ``main`` branch.

         .. seealso::
            * :doc:`workflows/tbd`


    Working Tree
        The tree of the files actually checked out. The working tree normally
        contains the content of the :term:`HEAD` commit tree as well as all
        local changes that you have made but not yet transferred.
