.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

pandas
======

`pandas <https://pandas.pydata.org/>`_ is a Python library for data analysis
that has become very popular in recent years. On the website, pandas is
described thus:

    „pandas is a fast, powerful, flexible and easy to use open source data
    analysis and manipulation tool, built on top of the Python programming
    language.“

More specifically, pandas is an in-memory analysis tool that offers SQL-like
constructs, as well as statistical and analytical tools. In doing so, pandas
builds on Cython and NumPy, making it less memory intensive and faster than pure
Python code. Mostly pandas is used to

* replace :doc:`/data-processing/serialisation-formats/excel` and `Power BI
  <https://www.microsoft.com/en-us/power-platform/products/power-bi/>`_
* implement an `ETL <https://en.wikipedia.org/wiki/Extract,_transform,_load>`_
  process
* process :doc:`/data-processing/serialisation-formats/csv/index` or
  :doc:`/data-processing/serialisation-formats/json/index` data
* prepare machine learning

.. tip::
   `Analysing data with pandas
   <https://cusy.io/en/our-training-courses/analysing-data-with-pandas.html>`_

.. seealso::
    * `Home
      <https://pandas.pydata.org/>`_
    * `User guide
      <https://pandas.pydata.org/docs/user_guide/index.html>`_
    * `API reference
      <https://pandas.pydata.org/docs/reference/index.html>`_
    * `GitHub
      <https://github.com/pandas-dev/pandas/>`_

pandas vs. Polars vs. Dask and DuckDB
-------------------------------------

The choice between pandas, `Polars <https://pola.rs>`_,
:doc:`/performance/dask`, and `DuckDB <https://duckdb.org>`_ depends on the type
of workload:

pandas
    is the canonical Python DataFrame library for analysis on a single machine.
Polars
    is written in Rust and allows for powerful analysis on a single node or when
    `lazy evaluation <https://en.wikipedia.org/wiki/Lazy_evaluation>`_ and
    `expressions API
    <https://docs.pola.rs/api/python/stable/reference/expressions/index.html>`_
    are important.
Dask
    is a Python library for parallel computing that scales familiar APIs,
    including pandas and `Scikit-Learn <https://scikit-learn.org/stable/>`_, to
    clusters.
DuckDB
    is an in-process `OLAP
    <https://en.wikipedia.org/wiki/Online_analytical_processing>`_ database for
    analysis and SQL over **local** files, which often complements pandas
    DataFrames as it is excellent for in-process analysis and SQL tasks.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    data-structures.ipynb
    python-data-structures.ipynb
    indexing.ipynb
    date-time.ipynb
    select-filter.ipynb
    transforming.ipynb
    string-manipulation.ipynb
    arithmetic.ipynb
    descriptive-statistics.ipynb
    sorting-ranking.ipynb
    discretisation.ipynb
    combining-merging.ipynb
    group-operations.ipynb
    aggregation.ipynb
    apply.ipynb
    pivoting-crosstab.ipynb
    convert-dtypes.ipynb
