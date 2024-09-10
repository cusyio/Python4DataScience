.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Key-value database systems
==========================

Key-value databases, also known as key value stores, store :term:`key/value
pairs <Key/value pair>`.

Database systems
----------------

Key/value database systems are e.g. Riak, Cassandra, Redis and MongoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Riak`_                        | `Cassandra`_                   | `Redis`_                       | `MongoDB`_                     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `basho/riak`_                  | `apache/cassandra`_            | `redis/redis`_                 | `mongodb/mongo`_               |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `docs.riak.com`_               | `cassandra.apache.org/doc/`_   | `redis.io/docs`_               | `www.mongodb.com/docs`_        |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Application areas**  | Session storage, Log data,     | Georedundancy, high writing    | Session Cache, Full Page       | IoT, Mobile apps, CMS,         |
|                        | Sensor data, CMS               | speed, democratic peer-to-peer | Cache (FPC), Queues, Pub/Sub   | `2d Index Internals`_, …       |
|                        |                                | (P2P) architecture, data with  |                                |                                |
|                        |                                | a defined lifetime             |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Development          | Erlang                         | Java                           | ANSI C                         | C++                            |
| language**             |                                |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Licenses**           | Apache License 2.0             | Apache License 2.0             | Redis Source Available License | Server Side Public License     |
|                        |                                |                                | v2, Server-Side Public License |                                |
|                        |                                |                                | v1                             |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Data model**         | Essentially                    | :term:`Column Family`          | Keys are stored as strings,    | Flexible scheme with           |
|                        | :term:`Key/value pair`         | correspond to tables, keyspaces| values as strings, hashes,     | denormalised model             |
|                        |                                | to databases; no logical       | lists, sets and sorted sets    |                                |
|                        |                                | structure, no scheme           |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query langauge**     | Keyfilter, :term:`MapReduce`,  | `Cassandra Query Language      |                                | jQuery, :term:`MapReduce`      |
|                        | Link walking, no ad hoc queries| (CQL)`_                        |                                |                                |
|                        | possible                       |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transactions,        | :term:`ACID`                   | :term:`Eventual Consistency`   | in-memory, asynchronous on disc| :term:`Two-phase locking (2PL)`|
| concurrency**          |                                |                                | with *Append Only File Mode*   |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replication,         | Multi-master replication       | SimpleStrategy,                |Master-N-Slaves replication,    | Master-Slave replication,      |
| skaling**              |                                | NetworkTopologyStrategy and    |Sharding using                  | Auto-Sharding                  |
|                        |                                | OldNetworkTopologyStrategy     |:term:`Consistent hash function`|                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Remarks**            |                                | See also `Scylla`_, a          | See also:                      | `BSON` with a maximum          |
|                        |                                | Cassandra-compatible           |                                | document size of 16 MB.        |
|                        |                                | reimplementation in C.         | `KeyDB`_                       |                                |
|                        |                                |                                |     a fork with multithreading |                                |
|                        |                                |                                | `Redict`_                      |                                |
|                        |                                |                                |     a fork, licenced under     |                                |
|                        |                                |                                |     LGPL-3.0                   |                                |
|                        |                                |                                | `Valkey`_                      |                                |
|                        |                                |                                |     a fork by the Linux        |                                |
|                        |                                |                                |     Foundation                 |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

.. _`Riak`: https://riak.com/
.. _`Cassandra`: https://cassandra.apache.org/_/index.html
.. _`Redis`: https://redis.io/
.. _`MongoDB`: https://www.mongodb.com/
.. _`basho/riak`: https://github.com/basho/riak
.. _`apache/cassandra`: https://github.com/apache/cassandra
.. _`redis/redis`: https://github.com/redis/redis
.. _`mongodb/mongo`: https://github.com/mongodb/mongo
.. _`docs.riak.com`: https://docs.riak.com/
.. _`cassandra.apache.org/doc/`: https://cassandra.apache.org/doc/latest/
.. _`redis.io/docs`: https://redis.io/docs/latest/
.. _`www.mongodb.com/docs`: https://www.mongodb.com/docs/
.. _`2d Index Internals`: https://www.mongodb.com/docs/manual/core/indexes/index-types/geospatial/2d/internals/
.. _`Cassandra Query Language (CQL)`: https://cassandra.apache.org/doc/stable/cassandra/cql/
.. _`Scylla`: https://www.scylladb.com/
.. _`KeyDB`: https://github.com/Snapchat/KeyDB
.. _`Redict`: https://redict.io/
.. _`Valkey`: https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community
.. _`BSON`: http://www.bsonspec.org/
