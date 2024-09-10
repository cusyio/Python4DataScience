.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Graph database systems
======================

Graph databases specialise in networked information and the simplest and most
efficient possible :term:`Graph traversal`.

Graph model
-----------

A graph consists of a number of nodes and edges. Graphs are used to represent a
variety of problems through nodes, edges and their relationships, for example
in navigation systems in which the paths are stored in the form of graphs.

Graph traversal
---------------

Graph traversal is mostly used to find nodes. There are different algorithms for
such search queries in a graph, which can be roughly divided into

* Breadth-first search, BFS and depth-first search, DFS

  The breadth-first search begins with all neighboring nodes of the start node.
  In the next step, the neighbors of the neighbors are then searched. The path
  length increases with each iteration.

  The depth-first search follows a path until a node with no outgoing edges is
  found. The path is then traced back to a node that has further outgoing edges.
  The search will then continue there.

* Algorithmic traversal

  Examples of algorithmic traversal are

  * Hamiltonian path (traveling salesman)
  * Eulerian path
  * Dijkstra’s algorithm

* Randomised traversal

  The graph is not run through according to a certain scheme, but the next node
  is selected at random. This allows a search result to be presented much
  faster, especially with large graphs, but this is not always the best.

Database systems
----------------

Typical graph databases are Neo4j, OrientDB and ArangoDB.

+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Home**               | `Neo4j`_                       | `OrientDB`_                    | `ArangoDB`_                    |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **GitHub**             | `neo4j/neo4j`_                 | `orientechnologies/orientdb`_  | `arangodb/arangodb`_           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Docs**               | `neo4j.com/docs/`_             | `orientdb.dev/docs/`_          | `docs.arangodb.com`_           |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Application areas**  | CMS, social networks,          | Master data management, social | Fraud Detection, IoT,          |
|                        | GIS systems, ERP, …            | networks, `time series`_,      | identity management,,          |
|                        |                                | `key value`_,                  | e-commerce, network, logistics,|
|                        |                                | traffic management             | CMS                            |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Development          | Java                           | Java                           | C++, JavaScript                |
| language**             |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Licenses**           | AGPL and commercially          | Apache License 2.0             | Apache License 2.0             |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Data model**         | :term:`Property graph model`   | Multi-Model                    | Multi-model: documents, graphs |
|                        |                                |                                | and :term:`Key/value pair`     |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Query language**     | REST, `Cypher`_, `Gremlin`_    | `Extended SQL`_, `Gremlin`_    | ArangoDB Query Language (AQL)`_|
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Transactions,        |* :term:`Two-phase locking      | :term:`ACID`                   | :term:`ACID`,                  |
| concurrency**          |  (2PL)`                        |                                | :term:`MVCC – Multiversion     |
|                        |* single Server:                |                                | Concurrency Control`           |
|                        |  :term:`ACID`                  |                                |                                |
|                        |* distributed systems:          |                                |                                |
|                        |  :term:`BASE`                  |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Replication,         | Master-slave with master       | Multi-master replication,      | Master-slave replication,      |
| skaling**              | failover                       | Sharding                       | sharding                       |
|                        |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+
| **Remarks**            |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
|                        |                                |                                |                                |
+------------------------+--------------------------------+--------------------------------+--------------------------------+

.. seealso::
   * `Apache TinkerPop Home <https://tinkerpop.apache.org/>`_
   * `TinkerPop Documentation <https://tinkerpop.apache.org/docs/current/>`_
   * `github.com/apache/tinkerpop <https://github.com/apache/tinkerpop>`_
   * `Practical Gremlin – An Apache TinkerPop Tutorial
     <https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html>`_
   * `gremlinpython <https://pypi.org/project/gremlinpython/>`_

.. _`Neo4j`: https://neo4j.com
.. _`OrientDB`: https://orientdb.dev
.. _`neo4j/neo4j`: https://github.com/neo4j/neo4j
.. _`ArangoDB`: https://arangodb.com
.. _`orientechnologies/orientdb`: https://github.com/orientechnologies/orientdb
.. _`arangodb/arangodb`: https://github.com/arangodb/arangodb
.. _`time series`: https://orientdb.dev/docs/3.2.x/gettingstarted/Time-series-use-case.html
.. _`key value`: https://orientdb.dev/docs/3.2.x/gettingstarted/Key-Value-use-case.html
.. _`neo4j.com/docs/`: https://neo4j.com/docs/
.. _`orientdb.dev/docs/`: https://orientdb.dev/docs/3.2.x/index.html
.. _`docs.arangodb.com`: https://docs.arangodb.com/
.. _`Extended SQL`: https://orientdb.dev/docs/3.2.x/sql/index.html
.. _`Cypher`: https://neo4j.com/docs/1.4/cypher-query-lang.html
.. _`Gremlin`: https://github.com/tinkerpop/gremlin/wiki
.. _`ArangoDB Query Language (AQL)`: https://www.arangodb.com/docs/stable/aql/
