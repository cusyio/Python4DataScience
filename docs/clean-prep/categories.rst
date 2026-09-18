.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Categories of data quality
==========================

There are various ways to categorise data quality issues – by the cause of the
problem, by its likely or potential impact, by the type of data element, or by
the level of a data hierarchy at which the error or inconsistency becomes
apparent, to name but a few. In this tutorial, categorisation is generally
implicit, and we focus on the methods for detecting problems and the tools
suitable for this purpose. However, it is useful to at least briefly touch upon
other ways of categorising data problems before we turn our attention to
detection.

Impossible data
    such as temperatures below absolute zero (0 Kelvin or −273.15 °C) or
    nonsensical date and time values – whilst these cannot occur in the
    :class:`datetime` data type in Python, they can occur in
    :doc:`../data-processing/serialisation-formats/json/index` and :doc:`SQLite
    <python-basics:save-data/sqlite/index>`, where text fields are usually used
    to store date information.
Special values
    The `IEEE-754 <https://en.wikipedia.org/wiki/IEEE_754>`_ standard for
    representing floating-point numbers also includes special values for
    positive and negative infinity (+∞, −∞) as well as *Not a Number* (``NaN``)
    values.
Unspecified Values
    Values that conform to a specific format may nevertheless be invalid, such
    as email addresses.
Inconsistencies
    Groups of related field values for each record may be mutually exclusive. To
    avoid such inconsistencies, the :abbr:`DRY (Don’t Repeat Yourself)`
    principle recommends disregarding calculable values. Checksums, however, are
    the exact opposite of this.

    *‘Single Source of Truth’* is an example of database normalisation and
    simplifies updates; with denormalised data stores, on the other hand, joins
    and calculations can be avoided during data analysis.

Anomalies and data drift
    The checks carried out to date have made it possible to declare data
    invalid. However, anomalies and data drift do not necessarily support this
    conclusion and therefore rarely allow for automated data cleansing.
Malware
    Not all input or output data should be processed in analysis systems.

    .. figure:: exploits_of_a_mom_2x.png
       :alt: Hi, this is your son’s school. We’re having some  computer trouble.
             Oh, dear - did he break something? In a way –
             Did you really name your son Robert'); DROP TABLE Students; -- ?
             Oh, yes. Little bobby tables, we call him.
             Well, weve lost this year’s student records. I hope you’re happy.
             And I hope, youe’ve learned to sanitize your database inpots.
       :target: https://xkcd.com/327/

       Exploits of a Mom

    Ein offensichtliches Beispiel für versehentlich offengelegte Ausgabedaten
    sind :abbr:`z. B. (zum Beispiel)` aus fortlaufenden Personenkennziffern
    generierte URLs mit personenbezogenen Daten.
