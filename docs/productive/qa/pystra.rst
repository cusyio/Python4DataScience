.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Pystra
======

:abbr:`Pystra (Python Structural Reliability Analysis)` analyses the structural
reliability of Python code and summarises it in a report.

.. seealso::
   * `Docs <http://pystra.github.io/pystra/>`_
   * `GitHub <https://github.com/pystra/pystra>`_

Installation
------------

.. code-block:: console

    $ uv add pystra

Reliability analysis
--------------------

A FORM (first-order reliability method) analysis can lead to the following
result, for example:

.. code-block:: console

    ==================================================

     RESULTS FROM RUNNING FORM RELIABILITY ANALYSIS

     Number of iterations:      17
     Reliability index beta:    1.75397614074
     Failure probability:       0.039717297753
     Number of calls to the limit-state function: 164

    ==================================================
