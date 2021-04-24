Performance measurement and optimisation
========================================

Performance measurement
-----------------------

However, once you have worked with your code, it can be useful to examine its
efficiency more closely. The :doc:`ipython-profiler` or :doc:`scalene` can be
used for this.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ipython-profiler.ipynb
    scalene

Parallel programming
--------------------

Three examples of :doc:`Threading <threading-example>`, :doc:`Multiprocessing
<multiprocessing>` and :doc:`Async <async-example>` illustrate the rules and
best practices for parallel programming.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    concurrency.ipynb
    threading-example.ipynb
    multiprocessing.ipynb
    threading-forking-combined.ipynb
    async-example.ipynb
    parallelise-pandass
    ipyparallel/index.rst

.. seealso::
    * `Faster CPython <https://faster-cpython.readthedocs.io/>`_
    * `Python Speed Center <https://speed.python.org/>`_
    * `Tracing the Python GIL <https://www.maartenbreddels.com/perf/jupyter/python/tracing/gil/2021/01/14/Tracing-the-Python-GIL.html>`_
