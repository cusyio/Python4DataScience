.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Document-oriented database systems
==================================

A document in this context is a structured compilation of certain data. The data
of a document is stored as a :term:`Key/value pair`, whereby the value can also
be a list or an array.

Database systems
----------------
Document-oriented database systems are, for example, MongoDB, CouchDB, Riak,
OrientDB and ArangoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `MongoDB`_                     | `CouchDB`_                     | `Riak`_                        | `OrientDB`_                    | `ArangoDB`_                    |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `mongodb/mongo`_               | `apache/couchdb`_              | `basho/riak`_                  | `orientechnologies/orientdb`_  | `arangodb/arangodb`_           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `www.mongodb.com/docs`_        | `docs.couchdb.org`_            | `docs.riak.com`_               | `orientdb.dev/docs`_           | `docs.arangodb.com/`_          |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Application areas**  | IoT, Mobile apps, CMS,         | Mobile, CRM, CMS, …            | Session storage, Log data,     | Master data management, social | Fraud Detection, IoT,          |
|                        | `simple geospatial data`_, …   |                                | Sensor data, CMS               | networks, `Time Series`_,      | identity management,           |
|                        |                                |                                |                                | `Key Value`_, `Chat`_,         | e-commerce, network, logistics,|
|                        |                                |                                |                                | traffic management             | CMS                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Development          | C++                            | Erlang                         | Erlang                         | Java                           | C++, JavaScript                |
| language**             |                                |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Licenses**           | Server Side Public License     | Apache License 2.0             | Apache License 2.0             | Apache License 2.0             | Apache License 2.0             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Data model**         | Flexible scheme with           | Flexible scheme                | Essentially                    | Multi-Model                    | Multi-model: documents, graphs |
|                        | denormalised model             |                                | :term:`Key/Value pair`         |                                | and :term:`Key/value pair`     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query language**     | jQuery, :term:`MapReduce`      | REST, :term:`MapReduce`        | Key filter, :term:`MapReduce`, | `Gremlin`_                     |`ArangoDB Query Language (AQL)`_|
|                        |                                |                                | link walking, no ad-hoc        |                                |                                |
|                        |                                |                                | queries possible               |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transactions,        | :term:`Two-phase locking (2PL)`|* :term:`Two-phase locking      | :term:`ACID`                   | :term:`ACID`                   | :term:`ACID`,                  |
| concurrency**          |                                |  (2PL)`,                       |                                |                                | :term:`MVCC – Multiversion     |
|                        |                                |* single server:                |                                |                                | Concurrency Control`           |
|                        |                                |  :term:`ACID`,                 |                                |                                |                                |
|                        |                                |* distributed systems:          |                                |                                |                                |
|                        |                                |  :term:`BASE`                  |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replication,         | Master-Slave replication,      | Master-master replication      | Multi-master replication       | Multi-Master-Replication,      | Master-slave replication,      |
| scaling**              | Auto-Sharding                  |                                |                                | Sharding                       | sharding                       |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Remarks**            | `BSON` with a maximum          |                                |                                |                                |                                |
|                        | document size of 16 MB.        |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`MongoDB`: https://www.mongodb.com/
.. _`CouchDB`: https://couchdb.apache.org/
.. _`Riak`: https://riak.com/
.. _`OrientDB`: https://orientdb.dev
.. _`ArangoDB`: https://arangodb.com
.. _`mongodb/mongo`: https://github.com/mongodb/mongo
.. _`apache/couchdb`: https://github.com/apache/couchdb
.. _`basho/riak`: https://github.com/basho/riak
.. _`orientechnologies/orientdb`: https://github.com/orientechnologies/orientdb
.. _`arangodb/arangodb`: https://github.com/arangodb/arangodb
.. _`www.mongodb.com/docs`: https://www.mongodb.com/docs/
.. _`docs.couchdb.org`: https://docs.couchdb.org/en/stable/
.. _`docs.riak.com`: https://docs.riak.com/
.. _`orientdb.dev/docs`: https://orientdb.dev/docs/3.2.x/index.html
.. _`docs.arangodb.com`: https://docs.arangodb.com/stable/
.. _`Time Series`: https://orientdb.dev/docs/3.2.x/gettingstarted/Time-series-use-case.html
.. _`Key Value`: https://orientdb.dev/docs/3.2.x/gettingstarted/Key-Value-use-case.html
.. _`Chat`: https://orientdb.dev/docs/3.2.x/gettingstarted/Chat-use-case.html
.. _`Gremlin`: https://github.com/tinkerpop/gremlin/wiki
.. _`ArangoDB Query Language (AQL)`: https://docs.arangodb.com/3.11/aql/
.. _`simple geospatial data`: https://www.mongodb.com/docs/manual/core/indexes/index-types/geospatial/2d/internals/
.. _`BSON`: http://www.bsonspec.org/
