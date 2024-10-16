.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Mypy
====

With `Mypy <https://mypy-lang.org>`_ you can do a static type check.

.. seealso::
    * `Home <https://mypy-lang.org>`_
    * `GitHub <https://github.com/python/mypy>`_
    * `Docs <https://mypy.readthedocs.io/en/stable/>`_
    * `PyPI <https://pypi.org/project/mypy/>`_
    * `Using Mypy in production at Spring
      <https://notes.crmarsh.com/using-mypy-in-production-at-spring>`_

Installation
------------

Mypy requires Python≥3.5. Then it can be installed, for example with:

.. code-block:: console

    $ uv add mypy

Check
-----

Then you can check it, for example with:

.. code-block:: console

    $ uv run mypy myprogram.py

.. note::
    Although Mypy needs to be installed with Python3, it can also parse Python2
    code, for example with:

    .. code-block:: console

        $ uv run mypy --py2 myprogram.py
