.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Object database systems
=======================

Many programming languages suggest object-oriented programming, so storing these
objects seems natural. It therefore makes sense to design the entire process
from implementation to storage uniformly and simply. In detail, the advantages
are:

Natural modeling and representation of problems
    Problems can be modeled in ways that are very close to the human way of
    thinking.
Clearer, more readable and more understandable
    The data and the functions operating on them are combined into one unit,
    making the programs clearer, more readable and easier to understand.
Modular and reusable
    Program parts can be easily and flexibly reused.
Expandable
    Programs can be easily expanded and adapted to changed requirements.

Object-relational impedance mismatch
------------------------------------

Object-oriented programming and relational data storage are problematic for
various reasons. Inheritance is an important concept in OOP for implementing
complex models. In the relational paradigm, however, there is nothing like it.
Object-relational mappers, ORM, such as :doc:`../postgresql/sqlalchemy`, were
developed to convert corresponding class hierarchies into a relational model. In
principle there are two different approaches for an ORM, whereby in both cases a
table is created for a class:

Vertical partitioning
    The table only contains the attributes of the corresponding class and a
    foreign key for the table of the superclass. An entry is then created for
    each object in the table belonging to the class and in the tables of all
    superclasses. When accessing the tables, joins must be used, which can
    lead to significant performance losses in complex models.
Horizontal partitioning
    Each table contains the attributes of the associated class and all
    superclasses. If the superclass is changed, however, the tables of all
    derived classes must also be updated.

Basically, when combining OOP and relational data management, two data models
must always be created. This makes this architecture significantly more complex,
more error-prone and more time-consuming to maintain.

Database systems
----------------

Examples of object database systems are ZODB.

+------------------------+----------------------------------------+
| **Home**               | `ZODB`_                                |
+------------------------+----------------------------------------+
| **GitHub**             | `zopefoundation/ZODB`_                 |
+------------------------+----------------------------------------+
| **Docs**               | `zodb.org/en/latest/tutorial.html`_    |
+------------------------+----------------------------------------+
| **Application areas**  | Plone, Pyramid, BTrees, volatile data  |
|                        |                                        |
+------------------------+----------------------------------------+
| **Development          | Python                                 |
| language**             |                                        |
+------------------------+----------------------------------------+
| **Licenses**           | Zope Public License (ZPL) 2.1          |
+------------------------+----------------------------------------+
| **Data model**         | PersistentList, PersistentMapping,     |
|                        | BTree                                  |
+------------------------+----------------------------------------+
| **Query language**     |                                        |
+------------------------+----------------------------------------+
| **Transactions,        | :term:`ACID`                           |
| concurrency**          |                                        |
+------------------------+----------------------------------------+
| **Replication,         | `ZODB Replication Services (ZRS)`_     |
| skaling**              |                                        |
+------------------------+----------------------------------------+
| **Remarks**            |                                        |
+------------------------+----------------------------------------+

.. _`ZODB`: https://zodb.org/en/latest/
.. _`Objectivity/DB`: https://www.objectivity.com/products/objectivitydb/
.. _`zopefoundation/ZODB`: https://github.com/zopefoundation/ZODB
.. _`zodb.org/en/latest/tutorial.html`: https://zodb.org/en/latest/tutorial.html
.. _`ZODB Replication Services (ZRS)`: https://pypi.org/project/zc.zrs/
