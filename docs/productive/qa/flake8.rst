.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

``flake8``
==========

`flake8 <https://pypi.org/project/flake8/>`_ is a wrapper around `PyFlakes
<https://pypi.org/project/pyflakes/>`_, `pycodestyle
<https://pypi.org/project/pycodestyle/>`_ and `McCabe
<https://pypi.org/project/mccabe/>`_. However, automatic formatting, for example
with :doc:`black`, is even more convenient.

Installation
------------

.. code-block:: console

    $ spack env activate python-311
    $ spack install py-flake8

Check
-----

:samp:`$ flake8 {PATH/TO/YOUR/CODE}`

Configuration
-------------

``flake8`` can be configured for :doc:`python-basics:test/tox` in the
``tox.ini`` file of a package, for example:

.. code-block:: ini

    [tox]
    envlist = py38, py311, flake8, docs

    [testenv:flake8]
    basepython = python
    deps =
        flake8
        flake8-isort
    commands =
        flake8 src tests setup.py conftest.py docs/conf.py

.. seealso::
    * `Configuring flake8
      <https://flake8.pycqa.org/en/latest/user/configuration.html>`_
    * `flake8 error/violation codes
      <https://flake8.pycqa.org/en/latest/user/error-codes.html>`_
    * `pycodestyle error codes
      <https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes>`_
