.. SPDX-FileCopyrightText: 2026 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

cProfile/profiling.tracing
==========================

Usually, a profile is created in the command line with `cProfile
<https://docs.python.org/3.14/library/profile.html#module-cProfile>`_ or, from
Python 3.15 onwards, with :mod:`profiling.tracing`, which then displays its
profile statistics. However, this can quickly become very tedious, especially
when reading extensive profiles or sorting the data. A more flexible approach is
to save the profile data in a file instead, which can then be read with the
:mod:`pstats` module:

#. :samp:`uv run python -m cProfile -o {PROFILE} ({SCRIPT} | {-m {MODULE})`
   runs `cProfile
   <https://docs.python.org/3.14/library/profile.html#module-cProfile>`_ to
   profile your script or module and saves the results in a file specified by
   the ``-o`` option.

#. :samp:`uv run python -m (cProfile | profiling.tracing) -o profile ({SCRIPT} |
   -m {MODULE}) <<< $'sort cumtime\nstats 100' | less` passes the following two
   commands to the :mod:`pstats` module using the ``$`` syntax.

   ``sort cumtime``
       sorts the output by cumulative time, starting with the largest.

       To sort by other metrics, simply replace ``cumtime`` with a value from
       :meth:`pstats.Stats.sort_stats`.

   ``stats 100``
       displays the first 100 lines of the profile.

   The output is passed to ``less`` so you can view the results. Press :kbd:`q`
   to exit when you are finished.

#. Before and after optimisation can be easily compared, for example with:

   .. code-block:: console

      $ uv run python -m cProfile -o before.profile main.py
      $ git switch -c main_optimisation
      ...
      $ uv run python -m cProfile -o after.profile main.py
