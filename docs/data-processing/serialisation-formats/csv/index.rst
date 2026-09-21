.. SPDX-FileCopyrightText: 2022 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

CSV
===

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| -\-   | CSV is used to store tabular data, but unlike other   |
|                       |       | serialisation formats reviewed here, it’s not suitable|
|                       |       | for (nested) objects.                                 |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | -\-   | CSV is not well standardised: neither the encoding is |
|                       |       | defined nor the separation of the cell contents       |
|                       |       | (comma, semicolon :abbr:`etc. (et cetera)`).          |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | -\-   | No                                                    |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | ++    | The CSV format is well supported by almost every      |
|                       |       | programming language. A `csv`_ module is included in  |
|                       |       | the Python standard library and `pandas`_ can read a  |
|                       |       | CSV file straight into a ``Dataframe``.               |
|                       |       |                                                       |
|                       |       | Even if CSV is the only format described here that is |
|                       |       | well supported by spreadsheet programs like Excel,    |
|                       |       | you should see if you can import more structured      |
|                       |       | Excel files directly, for example  with pandas        |
|                       |       | `read_excel`_.                                        |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | +-    | CSV is readable especially for integer or decimal     |
|                       |       | numbers with the same character length. In all other  |
|                       |       | cases it will be difficult to identify the            |
|                       |       | corresponding columns.                                |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | \+    | CSV is very fast to serialise and deserialise.        |
+-----------------------+-------+-------------------------------------------------------+
| File size             | ++    | Only :doc:`../protobuf` should be more compact.       |
|                       |       |                                                       |
+-----------------------+-------+-------------------------------------------------------+

Example
-------

.. code-block::
   :caption: iris.csv

   5.1,0.222222222,3.5,0.625,1.4,0.06779661,0.2,0.041666667,setosa
   4.9,0.166666667,3,0.416666667,1.4,0.06779661,0.2,0.041666667,setosa
   4.7,0.111111111,3.2,0.5,1.3,0.050847458,0.2,0.041666667,setosa
   4.6,0.083333333,3.1,0.458333333,1.5,0.084745763,0.2,0.041666667,setosa
   5,0.194444444,3.6,0.666666667,1.4,0.06779661,0.2,0.041666667,setosa
   ...

.. seealso::

   * `iris.csv`_
   * :rfc:`4180`
   * `xan <https://github.com/medialab/xan>`_

CSVW
----

`CSVW <https://csvw.org>`_ is a W3C standard *“for describing and clarifying the content
of CSV tables”* on the web and imposes certain restrictions on CSV data. Below are the
first few lines of a sample CSV file, :file:`grit_bins.csv`, from the CSVW website:

.. code-block::
   :caption: grit_bins.csv
   :linenos:

   42, 425584, 439562
   43, 425301, 439519
   44, 425379, 439596
   45, 425024, 439663
   46, 424915, 439697
   48, 425157, 440347
   49, 424784, 439681
   50, 424708, 439759
   51, 424913, 440642
   52, 425342, 440376
   ... ... ...

----

… and here is the corresponding CSVW metadata file, :file:`grit_bins.json`:

.. code-block:: javascript
   :caption: grit_bins.json
   :linenos:

   {
     "@context": ["http://www.w3.org/ns/csvw", {"@language": "en"}],
     "tables": [{
       "url": "http://opendata.leeds.gov.uk/downloads/gritting/grit_bins.csv",
       "tableSchema": {
         "columns": [
         {
           "name": "location",
           "datatype": "integer"
         },
         {
           "name": "easting",
           "datatype": "decimal",
           "propertyUrl": "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/easting"
         },
         {
           "name": "northing",
           "datatype": "decimal",
           "propertyUrl": "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/northing"
         }
         ],
         "aboutUrl": "#{location}"
       }
     }],
     "dialect": {
       "header": false
     }
   }

Line 2
    The ``@context`` element specifies that this is a CSVW specification in English.
Lines 3–24
    CSVW supports multiple tables or CSV files within a single file.
Line 4
    CSVW uses a URL to refer to the data it describes.
Lines 5–23
    CSVW allows the name and data type of each column to be specified.
Lines 14, 19
    The last two columns also have a ``propertyURL``, which serves as a key if the data
    is converted to JSON or RDF. In this case, for example, during such a conversion to
    JSON, the values ``easting`` and ``northing`` would be assigned to the first row of
    the CSV file:

    .. code-block:: javascript

       "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/easting": 425584
       "http://data.ordnancesurvey.co.uk/ontology/spatialrelations/northing": 439562

Line 22
    ``aboutURL`` specifies the location of the information relating to the element
    described in the respective line. In our example, the location is

    .. code-block::

       http://opendata.leeds.gov.uk/downloads/gritting/42

Lines 25–27
    The ``dialect`` field specifies certain format details for the file – in this case,
    the absence of headers. However, in most cases, the encoding and the delimiter should
    also be specified here, for example:

    .. code-block:: javascript

       "dialect": {
         "header": false,
         "encoding": "utf-8",
         "delimiter": ","
       }

    Other aspects, such as quotation marks, escape characters and null indicators, can
    also be specified in this section.

In addition to the elements shown in the example, CSVW also offers the option to set
various types of constraints on the data in a CSV file, including permissible ranges for
columns with minimum and maximum values, formats for numeric data and uniqueness
requirements.

The CSVW website features a `Tools <https://csvw.org/tools.html>`_ section, including
`CSV Lint <https://github.com/Data-Liberation-Front/csvlint.rb>`_, which allows you to
check whether your CSV file is well-formed and to test it against a CSV dialect, a JSON
table schema or a CSVW annotation. With `csvw <https://github.com/cldf/csvw>`_, you can
validate CSV data and convert it to JSON.

.. seealso::
   * `Model for Tabular Data and Metadata on the Web
     <https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/>`_
   * `Metadata Vocabulary for Tabular Data
     <https://www.w3.org/TR/2015/REC-tabular-metadata-20151217/>`_

CSVW and ``tdda.serial``
~~~~~~~~~~~~~~~~~~~~~~~~

The :doc:`tdda </clean-prep/libs-methods/tdda>` library not only provides an API for
reading and writing data and metadata, but also enables the use of metadata files. ``tdda
serial`` can convert between different metadata formats and generate Python code for
reading files, as specified in a metadata file:

:samp:`tdda serial {EXAMPLE_METADATA}.json {EXAMPLE}.serial`
    converts CSVW files to :file:`tdda.serial` files
:samp:`tdda serial --to csvw {EXAMPLE}.serial {EXAMPLE}.json`
    converts :file:`tdda.serial` files in CSVW files
:samp:`tdda serial --to pd.[r|w] {EXAMPLE}.serial {EXAMPLE}.serial`
    converts a :file:`tdda.serial` file using either pandas’ ``read_csv`` or ``to_csv``

.. seealso::
   * `tdda.serial: Metadata and Tools for Flat (“CSV”) Files
     <https://tdda.readthedocs.io/en/latest/serialformat.html>`_
   * `TDDA Serial API <https://tdda.readthedocs.io/en/latest/serial-api.html>`_
   * `Test-Driven Data Analysis
     <https://www.tdda.info/tddaserial-metadata-for-flat-files-csv-files>`_

.. _`csv`: https://docs.python.org/3/library/csv.html
.. _`pandas`: https://pandas.pydata.org/
.. _`read_excel`: https://pandas.pydata.org/docs/user_guide/io.html#io-excel-reader
.. _`iris.csv`: https://sourceforge.net/projects/irisdss/files/latest/download

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    example.ipynb
