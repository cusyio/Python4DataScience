.. SPDX-FileCopyrightText: 2024 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Tips
====

Project structure
-----------------

If you want to use

* `SQLModel <https://sqlmodel.tiangolo.com/>`_ for Python database interaction
  (ORM)
* `Pydantic <https://docs.pydantic.dev/>`_ for data validation
* `PostgreSQL <https://www.postgresql.org/>`_ for data storage

the data structure could look like this:

.. code-block:: console

    fastapi-example
    ├── LICENSE
    ├── README.rst
    ── alembic.ini
    ── app
       ├── __init__.py
       ├── alembic
       │   ├── README
       │   ├── env.py
       │   ├── script.py.mako
       │   └── versions
       │       └── 3512b954651e_initialize_models.py
       ├── api
       │   ├── __init__.py
       │   ├── deps.py
       │   ├── main.py
       │   └── routes
       │       ├── __init__.py
       │       ├── items.py
       │       └── utils.py
       ├── core
       │   ├── __init__.py
       │   ├── config.py
       │   └── db.py
       ├── crud.py
       ├── main.py
       ├── models.py
       ├── tests
       │    ├── __init__.py
       │    ├── api
       │    │   ├── __init__.py
       │    │   └── routes
       │    │       ├── __init__.py
       │    │       └── test_items.py
       │    ├── conftest.py
       │    └── crud
       │        ├── __init__.py
       │        └── test_items.py
       └── pyproject.toml
