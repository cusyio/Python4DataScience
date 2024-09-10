.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Find regressions with ``git bisect``
====================================

``git bisect`` allows you to quickly find a git commit that has introduced a
regression. The name *bisect* comes from the `binary search
<https://en.wikipedia.org/wiki/Binary_search_algorithm>`_ that the command uses.
The list of commits is repeatedly halved until the relevant commit is found.
This means that only log₂(n+1) commits need to be tested.

#. To do this, start the search with ``git bisect start``. You can then use
   :samp:`git bisect new [{COMMIT}]` and :samp:`git bisect old [{COMMIT}]` to
   narrow down the area in which an error was introduced. Alternatively, the
   short form :samp:`git bisect start [{BAD COMMIT}] [{GOOD COMMIT}]` can also
   be used. ``git bisect`` then checks out a commit in the middle and asks you
   to test it, for example:

   .. code-block:: console

    $ git bisect start v2.6.27 v2.6.25
    Bisecting: 10928 revisions left to test after this (roughly 14 steps)
    [2ec65f8b89ea003c27ff7723525a2ee335a2b393] x86: clean up using max_low_pfn on 32-bit

#. The search can now be continued manually or automatically with a script.
   Manually, you can use ``git bisect new`` and ``git bisect old`` to narrow
   down the area in which an error was introduced. If this commit is found, the
   output may look like this, for example:

   .. code-block:: console

    $ git bisect new
    2ddcca36c8bcfa251724fe342c8327451988be0d is the first bad commit
    commit 2ddcca36c8bcfa251724fe342c8327451988be0d
    Author: Linus Torvalds <torvalds@linux-foundation.org>
    Date:   Sat May 3 11:59:44 2008 -0700

        Linux 2.6.26-rc1

    :100644 100644 5cf82581... 4492984e... M      Makefile

#. We then use ``git show HEAD`` to check what changes have been made in this
   commit:

   .. code-block:: console

    $ git show HEAD
    commit 2ddcca36c8bcfa251724fe342c8327451988be0d
    Author: Linus Torvalds <torvalds@linux-foundation.org>
    Date: Sat May 3 11:59:44 2008 -0700

        Linux 2.6.26-rc1

    diff --git a / Makefile b / Makefile
    index 5cf8258 ..4492984 100644
    --- a / Makefile
    +++ b / Makefile
    @@ -1,7 +1,7 @@
     VERSION = 2
     PATCHLEVEL = 6
    -SUBLEVEL = 25
    -EXTRAVERSION =
    + SUBLEVEL = 26
    + EXTRAVERSION = -rc1
     NAME = Funky Weasel is Jiggy with it

     # * DOKUMENTATION *

#. Finally, you can use ``git bisect reset`` to return to the branch you were in
   before the bisect search:

   .. code-block:: console

      $ git bisect reset
      Checking out files: 100% (21549/21549), done.
      Previous HEAD position was 2ddcca3... Linux 2.6.26-rc1
      Switched to branch 'master'

Mark non-testable commits with ``git bisect skip``
--------------------------------------------------

Sometimes with ``git bisect`` you end up with a commit that you can’t test
because there’s another problem. Usually this is due to an error that prevents
you from running your code or seeing the test result, for example a syntax
error. In this case, you should not mark the commit as ``old`` or ``new``, as
you will not be able to determine the behaviour due to the error. Instead, you
should skip the commit with ``git bisect skip``. ``git bisect`` checks out a
neighbouring commit for testing instead. If this works, continue testing and
executing ``new`` or ``old`` as usual. If not, run ``git bisect skip`` again. If
you know that there is a range of untestable commits, instruct ``git bisect`` to
skip this entire area with :samp:`git bisect skip {COMMIT1}..{COMMIT2}`.

.. seealso::
   * `Avoiding testing a commit
     <https://git-scm.com/docs/git-bisect#_avoiding_testing_a_commit>`_

Automatic testing with ``git bisect run``
-----------------------------------------

It is often possible to automate the test of whether a commit shows ``old`` or
``new`` behaviour. This speeds up the use of ``git bisect`` massively, as you no
longer have to make an entry at every step. It also makes the process less
error-prone, as you won’t accidentally execute the wrong ``old`` and ``new``
subcommand. Automated tests are also advantageous if your test process takes a
while, for example if you have a long compilation step. The search will not be
interrupted to wait for your input, and you can work on something else in the
meantime.

To start automatic tests, use ``git bisect`` run with your test command and
optional arguments. You may need to create a short test script that runs the
affected part of your code and checks what behaviour is present. ``git bisect``
runs the specified command at each step of the binary search loop and uses its
results to call ``old``, ``new`` or ``skip`` as needed.

You can find an example of this in the issue `fetch_california_housing fails in
CI on master <https://github.com/scikit-learn/scikit-learn/issues/14956>`_ from
scikit-learn:

.. code-block:: console

   $ git bisect run pytest sklearn/utils/tests/test_multiclass.py -k test_unique_labels_non_specific

Automated testing of performance regressions
--------------------------------------------

With a little extra effort, you can use automated tests to search for more
complicated changes in behaviour. For performance tests, we need a test
programme that can perform multiple runs and determine the minimum time while
eliminating possible noise:

.. code-block:: python

   from subprocess import run
   from time import perf_counter


   times = []
   for _ in range(10):
       start = perf_counter()
       run(
           [./perftest, PARAM],
           check=True,
           capture_output=True,
       )
       elapsed = perf_counter() - start
       times.append(elapsed)
   if min(times) > X.0:
       print("Too slow")
       raise SystemExit(1)
   else:
       print("Fast enough")
       raise SystemExit(0)

The programme executes :samp:`python perftest.py {PARAM}` ten times and measures
the time for each execution. It then compares the minimum execution time with a
limit value of ``X`` seconds. If the minimum time is above the limit value, it
outputs *Too slow* and exits with the exit code ``1``, otherwise it outputs
*Fast enough* and exits with the exit code ``0``:

.. code-block:: console

   $ python perftest.py PARAM
   Fast enough
   $ echo $? 0

Reproducing the binary search with ``git bisect log`` and ``git bisect replay``
-------------------------------------------------------------------------------

The scikit-learn issue also shows how you can communicate the results of your
bisect search to others in a reproducible way using ``git bisect log``:

.. code-block::

   $ git bisect log
   81f2d3a0e *   massich/multiclass_type_of_target Merge branch 'master' into multiclass_type_of_target
           |\
   15f24f25d | * bad DOC Cleaning for what's new
   fbb2c7c70 | * good-fbb2c7c7007dc373c462e39ab273a183a8823d58 @ ENH Adds _MultimetricScorer for Optimized Scoring  (#14593)
   …

With ``git bisect log > bisect_log.txt`` you can also save your search for
others to reproduce:

.. code-block:: console

   $ git bisect replay bisect_log.txt
