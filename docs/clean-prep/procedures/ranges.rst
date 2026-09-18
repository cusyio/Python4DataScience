.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Value ranges
============

Checking the value range of data is nothing new; almost any form of data
validation can be regarded as such a check. What is new, at best, is the
automated definition of these value ranges. As with machine learning, we start
with training data that has the same structure as the data we intend to work
with later. Ideally, the training data has already been checked and represents
correct data.

Value ranges can be determined from training data using the function
:func:`tdda.discover_df`, see also
:ref:`/clean-prep/libs-methods/tdda.ipynb#3.-creating-a-constraints-object`. For
numeric fields, the minimum and maximum values from the training data are used
as value ranges. For text fields, the function attempts to identify
:doc:`regular expressions <python-basics:types/strings/built-in-modules/regex>`
– that is, consistent patterns – such as those found in telephone numbers,
dates and times, BICs and IBANs.

Some of these generators can be instructed that the data may contain outliers
that deviate from most of the training data. Other generators can recognise
relationships between fields, such as the fact that the start date must always
precede the end date.

Typically, we review and refine the generated value ranges. As with machine
learning, it can also be useful here to split the training data into two or more
groups, with one group used for training and the others for validation. This is
particularly useful when there is a large amount of training data available.
