Remove Git LFS
==============

Services such as GitHub offer `Git LFS <https://git-lfs.com>`_ for their
repositories, but these may not exceed the additional storage of 1 GiB.
Purchasing additional quotas from GitHub is then quite expensive.

.. seealso::
   * `About storage and bandwidth usage
     <https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage>`_

But how do you get rid of Git LFS in such a repository?

The following steps allow you to get rid of Git LFS:

#. Use ``git lfs ls-files`` to get a list of all files managed by Git LFS.
#. Next, we make sure that we have checked out all large files with  

   .. code-block:: console

      $ git lfs fetch --all
      $ git lfs checkout

#. Remove the Git LFS filters:

   #. To do this, you must first remove entries such as ::samp:`*.{png}
      filter=lfs diff=lfs merge=lfs -text` from your  :file:`.gitattributes`
      file.
   #. You can then stop Git tracking for each deleted entry in the
      :file:`.gitattributes` file, for example with :samp:`git lfs untrack
      '*.{png}'`. 

      Alternatively, you can also use ``cut -f 1 < .gitattributes | xargs "git
      lfs untrack {}"`` for all files managed with Git LFS.

   #. Finally, the line ends should be normalised with ``git add --renormalize
      .``.

#. Now Git LFS can be uninstalled with ``git lfs uninstall``.
#. Finally, the changes must be transferred to the server.

Now you can switch to Manage data with :doc:`DVC <../../dvc/index>`, for
example, to manage large files in a versioned manner.
