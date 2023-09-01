.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Psycopg
=======

`Psycopg <https://www.psycopg.org/>`_ is a PostgreSQL adapter based on the C
library for PostgreSQL `libpq
<https://www.postgresql.org/docs/current/libpq.html>`_. Among other things, it
offers:

* DB API 2.0 compatibility
* Multithreading with thread safety
* `Connections pooling <https://www.psycopg.org/docs/pool.html>`_
  to be able to use a cache of existing database connections for queries.
* `Asynchronous
  <https://www.psycopg.org/docs/advanced.html#asynchronous-support>`_ and
  `Coroutines support
  <https://www.psycopg.org/docs/advanced.html#support-for-coroutine-libraries>`_
* `Adaptation of the Python types in SQL
  <https://www.psycopg.org/docs/usage.html#adaptation-of-python-values-to-sql-types>`_

Install
-------

With Spack you can provide psycopg2 in your kernel, e.g. with

.. code-block:: console

    $ spack env activate python-311
    $ spack install py-psycopg2
