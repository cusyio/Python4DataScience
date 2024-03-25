Change commits for a clean log
==============================

With ``git commit --fixup`` and ``git rebase --autosquash`` you can correct a
series of commits relatively easily. To demonstrate this with an example, I
present the following scenario:

#. We have two commits in our ``my-feature`` branch: one for the actual
   function, the other for the associated tests:

   .. code-block:: console

      $ git log --oneline my-feature ^origin/main
      a4587fa (my-feature) Add test for my new feature
      56e34e9 Add new feature

#. During the *merge* or *pull request*, we receive feedback on both our
   function and our tests, which we would like to integrate into our existing
   commits. To do this, we first create temporary commits:

   .. code-block:: console

      $ git commit -m "Feedback on the tests from my function"
      $ git commit -m "Feedback on my function"
      $ git log --oneline my-feature ^origin/main
      556c1e8 (my-feature) Feedback on my function
      8780db6 Feedback on the tests from my function
      a4587fa Add test for my new feature
      56e34e9 Add new feature

… with ``git rebase``
---------------------

3. With ``git rebase -i`` we can interactively rearrange the ``pick`` lines:

   .. code-block:: console

      $ git rebase -i origin/main

   This opens our editor:

   .. code-block:: console

      pick 56e34e9 Add new feature
      pick a4587fa Add test for my new feature
      pick 8780db6 Feedback on the tests from my function
      pick 556c1e8 Feedback on my function

   We can then change the lines, for example to:

   .. code-block:: console

      pick 56e34e9 Add new feature
      squash 556c1e8 Feedback on my function
      pick a4587fa Add test for my new feature
      squash 8780db6 Feedback on the tests from my function

   Now we have two commits again:

   .. code-block:: console

      $ git log --oneline my-feature ^origin/main
      31a140a (my-feature) Add test for my new feature
      132ae9b Add new feature

#. The changes can now be sent to our remote branch with ``git push -f``.

…with ``git commit --fixup`` and ``git rebase --autosquash``
------------------------------------------------------------

In Git, however, there is an even easier way to correct a previous commit: with
``git commit--fixup`` and ``git rebase --autosquash``.

5. We create two temporary commits again, but this time with ``git
   commit--fixup``:

   .. code-block:: console

      # Further changes to the tests
      $ git commit --fixup=31a140a
      [my-feature dd0c0d1] fixup! Add test for my new feature
       1 file changed, 1 insertion(+)
      # Further changes to my function
      $ git commit --fixup=132ae9b
      [my-function bc2298a] fixup! Add new feature
       1 file changed, 1 insertion(+)
      $ git log --oneline my-feature ^origin/main
      bc2298a (my-feature) fixup! Add new feature
      dd0c0d1 fixup! Add test for my new feature
      31a140a Add test for my new feature
      132ae9b Add new feature

   For commits with the :samp:`--fixup={SHA}` option, Git writes a specially
   formatted commit message that can be read as *this commit corrects that
   commit*.

#. Instead of using ``git rebase -i`` to manually specify the
   ``Pick``/``Squash`` lines, we can now simply run ``git rebase --autosquash``:

   .. code-block:: console

      $ git rebase --autosquash origin/main
      Successfully rebased and updated refs/heads/my-feature.
      $ git log --oneline my-feature ^origin/main
      694cb48 (my-feature) Add test for my new feature
      55cbe9b Add new feature

   ``git rebase --autosquash`` automates what we have just done manually with
   ``git rebase -i`` – but it does not open an editor in which we have to move
   the commits manually.

   .. tip::
      The ``--fixup`` option also contains the ``amend`` and ``reword`` options
      to reformulate the commit message, for example :samp:`git commit
      --fixup:amend={SHA}`.

      Further options can be found in the `Git commit documentation
      <https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---fixupamendrewordltcommitgt>`_.
