.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Testing procedures
==================

Errors occur time and again in data processing (→ :term:`DataOps`) and analysis,
whether in simple queries or in complex data pipelines for machine learning (→
:term:`MLOps`).

In addition to :doc:`data quality <../categories>` issues, there are other
problems that can arise during the various :ref:`phases of a data science
project <ds-phases>`.

Process errors
--------------

The most common causes of errors include:

* poorly documented, inadequately understood and inconsistently recorded input
  data with misleading or obscure field names and values that are difficult to
  interpret
* inadequately specified analysis objectives
* a lack of validation of input and output data
* inadequate verification of the data analysis solution
* inappropriate methods
* a lack of automated testing of the final analysis pipeline
* poorly documented results without a clear understanding of their limitations
  and conditions of validity
* inadequate monitoring of the data pipeline

Our aim is to reduce the frequency and severity of such errors.

Test-driven data analysis
-------------------------

In this context, two types of test-driven data analysis can be distinguished:

:doc:`Range tests <ranges>`
    Sensors are usually calibrated for a clearly defined measurement range only.
    If these sensors then produce results that fall outside this range, they can
    no longer be trusted.
:doc:`regression_tests`
    Errors in the data are automatically detected when they deviate from a
    reference, for example, if the measurement time lies in the future.

Other areas are less readily addressed by software, such as formalisation and
implementation errors. Nevertheless, we will discuss some concepts and explain
approaches to prevent, or at least reduce, their occurrence.

.. _ds-phases:

Phases of a typical data science project
----------------------------------------

+-----------------------+-----------------------+-----------------------+
| Phase                 | Error category        | Explanation           |
+=======================+=======================+=======================+
| 1. Strategy           | Formalisation errors  | Data, subject domain  |
|                       |                       | or methods were not   |
|                       |                       | understood            |
+-----------------------+-----------------------+-----------------------+
| 2. Prototypical       | Implementation errors | Bug                   |
|    data analysis      |                       |                       |
+-----------------------+-----------------------+-----------------------+
| 3. Automated          | Application errors    | No data or incorrect  |
|    data analysis      |                       | data during operation,|
|                       |                       | for example, data     |
|                       |                       | that has not been     |
|                       |                       | fully updated         |
+-----------------------+-----------------------+-----------------------+
| 4. Analysis results   | Analysis errors       | Discrepancy between   |
|                       |                       | the data and          |
|                       |                       | assumptions available |
|                       |                       | during development and|
|                       |                       | those processed during|
|                       |                       | operation             |
+-----------------------+-----------------------+-----------------------+
| 5. Interpretation     | Interpretation errors | Misinterpretation of  |
|                       |                       | the results           |
+-----------------------+-----------------------+-----------------------+

Avoiding errors in analytical processes
---------------------------------------

To minimise the various types of errors mentioned above, different approaches
are required. The most fundamental of these is a constant awareness of how
easily one can be misled in any data analysis. We must constantly bear in mind
that the results produced may be nonsense, made to appear plausible only by
elegant presentations or the appearance of objective infallibility.

Whilst the probability of error can be reduced across all categories, only three
of the error classes can be easily rectified using software:

* Implementation errors (bugs) can be rectified through :doc:`regression testing
  <regression_tests>`
* Application and analysis errors can be reduced if the data is carefully
  checked at all stages of the pipeline
* Interpretation errors, however, can hardly be detected by software.

    ‘There are three kinds of lies: lies, damned lies and statistics.’ [#]_

  Nevertheless, some of the bad practices proposed by Darrell Huff in 1991 [#]_
  should be avoided.

  .. figure:: error_types_2x.png
     :alt: TYPE I ERROR: FALSE POSITIVE
           TYPE II ERROR: FALSE NEGATIVE
           TYPE III ERROR: TRUE POSITIVE FOR INCORRECT REASONS
           TYPE IV ERROR: TRUE NEGATIVE FOR INCORRECT REASONS
           TYPE V ERROR: INCORRECT RESULT WHICH LEADS YOU TO A CORRECT
           CONCLUSION DUE TO UNRELATED ERRORS
           TYPE VI ERROR: CORRECT RESULT WHICH YOU INTERPRET WRONG
           TYPE VII ERROR: INCORRECT RESULT WHICH PRODUCES A COOL GRAPH
           TYPE VIII ERROR: INCORRECT RESULT WHICH SPARKS FURTHER RESEARCH AND
           THE DEVELOPMENT OF NEW TOOLS WHICH REVEAL THE FLAW IN THE ORIGINAL
           RESULT WHILE PRODUCING NOVEL CORRECT RESULTS
           TYPE IX ERROR: THE RISE OF SKYWALKER
     :target: https://xkcd.com/2303/

     Error Types

  The creation and maintenance of good metadata, as well as concepts relating to
  :doc:`reproducibility <../../productive/index>`, are also relevant here.

----

.. [#] In Mark Twain’s autobiography, this quotation is attributed to Benjamin
       Disraeli.
.. [#] “How to Lie with Statistics” by Darrell Huff, 1991

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ranges
    regression_tests
