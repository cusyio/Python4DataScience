.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Parallelise pandas
==================

In  :doc:`pandas:user_guide/enhancingperf`, some possibilities are described for
improving the performance of pandas. However, there are also special libraries
that can parallelise the processing of data frames.

cuDF
----

cuDF is a GPU DataFrame library that implements a `pandas-like API
<https://docs.rapids.ai/api/cudf/stable/>`_.

.. seealso::

    * `Docs <https://docs.rapids.ai/api/cudf/stable/>`__
    * `GitHub <https://github.com/rapidsai/cudf>`__
    * `PyPI <https://pypi.org/project/cudf/>`_
    * `Example notebooks
      <https://github.com/rapidsai-community/notebooks-contrib>`_

Modin
-----

Modin parallelises almost the entire Pandas API. In most cases, the existing
Pandas code only needs to be extended by the following import:

.. code-block:: python

    import modin.pandas as pd

The restrictions refer to  ``pd.read_json``, which is only implemented for
``lines=True``.

.. seealso::

    * `Docs <https://modin.readthedocs.io/en/latest/>`__
    * `GitHub <https://github.com/modin-project/modin>`__

Dask
----

`Dask DataFrame
<https://www.python4data.science/en/latest/performance/dask.html#Dask-DataFrame>`_
is a large parallel DataFrame made up of multiple pandas DataFrames. Here, the
``dask.dataframe`` API is a subset of the pandas API, although there are minor
changes.

.. seealso::

    * `Home <https://docs.dask.org/en/latest/dataframe.html>`_
    * `API docs <https://docs.dask.org/en/latest/dataframe-api.html>`_
    * `Example notebook <https://examples.dask.org/dataframe.html>`_
    * `Tutorial <https://tutorial.dask.org/01_dataframe.html>`_
