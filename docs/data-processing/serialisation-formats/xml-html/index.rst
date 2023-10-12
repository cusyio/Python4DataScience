.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

XML/HTML
========

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| ++    | XML is very flexible as each element can have         |
|                       |       | attributes and arbitrary child elements.              |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | ++    | XML is well standardised, the specification can be    |
|                       |       | found at https://www.w3.org/TR/xml/. XML supports     |
|                       |       | both DOM style and streaming SAX style parsers.       |
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | ++    | `XML schema`_, `RELAX NG`_                            |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | \+    | Supported in all major languages, usually with        |
|                       |       | built-in libraries.                                   |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | +-    | XML is a human-readable serialisation protocol. One   |
|                       |       | disadvantage of XML is it’s verbosity, in particular  |
|                       |       | it’s descriptive end tags.                            |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | \+    | XML is quite fast, although typically slower to parse |
|                       |       | than JSON.                                            |
+-----------------------+-------+-------------------------------------------------------+
| File size             | -\-   | XML has the largest file size in comparison.          |
|                       |       |                                                       |
+-----------------------+-------+-------------------------------------------------------+

Example
-------

.. literalinclude:: books.xml
   :caption: books.xml
   :name: books.xml
   :language: xml

.. seealso::

    * `Home <https://www.w3.org/XML/>`_
    * `Specification <https://www.w3.org/TR/REC-xml/>`_
    * `Validator <http://validator.w3.org/>`_
    * `The XML FAQ <http://xml.silmaril.ie/>`_

.. _`XML schema`: https://www.w3.org/TR/xmlschema-0/
.. _`RELAX NG`: https://relaxng.org/

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    xml-html-examples.ipynb
    beautifulsoup.ipynb
