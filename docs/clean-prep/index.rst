.. SPDX-FileCopyrightText: 2021 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Cleaning and validating data
============================

*‘Garbage in, garbage out’* is a stark reminder that it is almost impossible to
draw meaningful insights from poor-quality data. Whilst there are highly
regulated, safety-critical sectors in which data is routinely checked at every
stage, the general standard of data validation in most analytical projects tends
to be rather low.

However, if we write code to analyse data without first checking it, some
results will be misleading, incorrect or invalid. The same applies if we fail to
validate our output. In doing so, we end up contributing to the very *‘bad
data’* that we all rail against. *Postel’s Law* – the principle of robustness
proposed in the TCP standard – is helpful here:

    *“be conservative in what you do, be liberal in what you accept from
    others.”* [#]_

This stands in stark contrast to one of Python’s principles:

    *“Errors should never pass silently.”* [#]_

The :doc:`XML <../data-processing/serialisation-formats/xml-html/index>`
specification also requires that malformed XML documents be rejected:

    “„Validating and non-validating processors alike MUST report violations of
    this specification's well-formedness constraints … that they read.”* [#]_

The sections on :doc:`procedures/index`, :doc:`procedures/ranges` and
:doc:`procedures/regression_tests` do not require any prior knowledge of Python
and are therefore generally suitable for professionals in the fields of data
management, business management and quality assurance.

We will then provide you with a practical overview of various :doc:`libraries
and methods <libs-methods/index>` for `data cleaning
<https://en.wikipedia.org/wiki/Data_cleansing>`_ and validation using Python.

.. tip::
   `cusy seminar: Cleanse and validate data with Python
   <https://cusy.io/en/our-training-courses/cleanse-and-validate-data-with-python.html>`_

----

.. [#] Jon Postel: `Transmission Control Protocol
       <https://www.rfc-editor.org/info/rfc761/#section-2.10>`_, 1980
.. [#] Tim Peters: :pep:`The Zen of Python <20>`, 1999
.. [#] `XML Specification 1.0, Section 5.1
       <https://www.w3.org/TR/2008/REC-xml-20081126/#proc-types>`_, 1998

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    categories
    procedures/index
    libs-methods/index
