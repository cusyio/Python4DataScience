.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

pgMonitor
=========

`pgMonitor <https://access.crunchydata.com/documentation/pgmonitor/latest/>`_ is
an environment to visualise the health and performance of a PostgreSQL cluster.
It combines a suite of tools to facilitate the collection of important metrics,
including:

* number of connections
* Database size
* Replication lag
* Transaction wraparround
* Extra space taken up by your tables and indexes
* CPU, memory, I/O and uptime

It combines multiple open-source software packages to create a robust PostgreSQL
monitoring environment, including:

`PostgreSQL Exporter <https://github.com/prometheus-community/postgres_exporter>`__
    an open-source data export to Prometheus that supports collecting metrics
    from any PostgreSQL server ≥ 9.1.
`Prometheus <https://prometheus.io/>`__
    an open-source metrics collector that is highly customisable.
`Grafana <https://grafana.com/>`__
    an open-source data visualiser that allows you to generate many different
    kinds of charts and graphs.

.. seealso::
   * `pgexporter <https://pgexporter.github.io/>`_

Installation and configuration
------------------------------

Installation and configuration instructions for each package are provided:

#. `PostgreSQL Exporter
   <https://access.crunchydata.com/documentation/pgmonitor/latest/exporter>`__
#. `Prometheus
   <https://access.crunchydata.com/documentation/pgmonitor/latest/prometheus>`__
#. `Grafana
   <https://access.crunchydata.com/documentation/pgmonitor/latest/grafana>`__
