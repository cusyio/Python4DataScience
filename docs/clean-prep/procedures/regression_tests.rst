.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Regression testing
==================

Regression testing is intended to ensure that, should the analysis process be
modified, the results obtained to date remain valid. However, it may also happen
that the results change even if the source code remains unchanged.

#. Recording sample input data and the expected reference results
#. Tests to verify whether the recorded input data leads to the expected
   reference results; these can be created, for example, using `tdda gentest
   <https://tdda.readthedocs.io/en/latest/gentest.html>`_. Alternatively, the
   :doc:`../libs-methods/tdda` library provides tools, most notably `tdda diff
   <https://tdda.readthedocs.io/en/latest/tddadiff.html>`_, for writing your own
   tests.
#. Fully automated data analysis process

.. seealso::
   * :doc:`../../productive/index`
   * :doc:`python-basics:test/tdd`
