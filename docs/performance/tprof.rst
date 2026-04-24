.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

``tprof``
=========

`tprof <https://github.com/adamchainz/tprof>`_ measures from Python 3.12 onwards
the time spent executing a module in specific functions. Unlike other profilers,
it only tracks the specified functions with :mod:`sys.monitoring`, eliminating
the need for filtering.

``tprof`` supports use as a command line programme and with a Python interface:

:samp:`uv run tprof -t {MODULE}:{FUNCTION} (-m {MODULE} | {PATH/TO/SCRIPT})`
    Suppose you have determined that creating :class:`pathlib.Path` objects in
    the :mod:`main` module is slowing down your code. Here’s how you can measure
    this with ``tprof``:

    .. code-block:: console

       $ uv run tprof -t pathlib:Path.open  -m main
       🎯 tprof results:
        function            calls total mean ± σ  min … max
        pathlib:Path.open()     1  93μs 93μs     93μs … 93μs

    With the ``-x`` option, you can also compare two functions with each other:

    .. code-block:: console

       $ uv run tprof -x -t old -m main -t new -m main
       🎯 tprof results:
        function   calls total mean ± σ  min … max  delta
        main:old()     1  41μs 41μs     41μs … 41μs -
        main:new()     1  20μs 20μs     20μs … 20μs -50.67%

``tprof(*targets, label: str | None = None, compare: bool = False)``
    uses this code as a :doc:`context manager <python-basics:control-flow/with>`
    in your code to perform profiling in a specific block. The report is
    generated each time the block is run through.

    ``*targets``
        are callable elements for profiling or references to elements that are
        resolved with :func:`pkgutil.resolve_name`.
    ``label``
        is an optional string that can be added to the report as a header.
    ``compare``
        set to ``True`` activates comparison mode.

    Example:

    .. code-block:: Python

       from pathlib import Path

       from tprof import tprof

       with tprof(Path.open):
           p = Path("docs", "save-data", "myfile.txt")
           f = p.open()

    .. code-block:: console

       $ uv run python main.py
       🎯 tprof results:
        function            calls total mean ± σ  min … max
        pathlib:Path.open()     1  82μs 82μs     82μs … 82μs
