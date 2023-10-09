.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-FileContributor: Modified by Kristian Rother
..
.. SPDX-License-Identifier: BSD-3-Clause

Git for binary files
====================

``git diff`` can be configured so that it can also display meaningful diffs for
binary files.

… for Excel files
-----------------

For this we need `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`_
and `pandas <https://pandas.pydata.org>`_:

.. code-block:: console

    $ pipenv install openpyxl pandas

Then we can use :doc:`pandas:reference/api/pandas.DataFrame.to_csv` in
:file:`exceltocsv.py` to convert the Excel files:

.. literalinclude:: exceltocsv.py
    :caption: exceltocsv.py
    :name: exceltocsv.py
    :language: python

Now add the following section to your global Git configuration
:file:`~/.gitconfig`:

.. code-block:: ini

    [diff "excel"]
        textconv=python3 /PATH/TO/exceltocsv.py
        binary=true

Finally, in the global :file:`~/.gitattributes` file, our ``excel`` converter is
linked to :file:`*.xlsx` files:

.. code-block:: ini

    *.xlsx diff=excel

… for PDF files
---------------

For this, ``pdftohtml`` is additionally required. It can be installed with

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install poppler-utils

.. tab:: macOS

   .. code-block:: console

      $ brew install pdftohtml

Add the following section to the global Git configuration :file:`~/.gitconfig`:

.. code-block:: ini

    [diff "pdf"]
        textconv=pdftohtml -stdout

Finally, in the global :file:`~/.gitattributes` file, our ``pdf`` converter is
linked to :file:`*.pdf` files:

.. code-block:: ini

    *.pdf diff=pdf

Now, when ``git diff`` is called, the PDF files are first converted and then a
diff is performed over the outputs of the converter.

… for Word documents
--------------------

Differences in Word documents can also be displayed. For this purpose `Pandoc
<https://pandoc.org/>`_ can be used, which can be easily installed with

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install pandoc

.. tab:: macOS

   .. code-block:: console

      $ brew install pandoc

.. tab:: Windows

   Download and install the :file:`*.msi`. file from `GitHub
   <https://github.com/jgm/pandoc/releases/>`_.

Then add the following section to your global Git configuration
:file:`~/.gitconfig`:

.. code-block:: ini

    [diff "word"]
        textconv=pandoc --to=markdown
        binary=true
        prompt=false

Finally, in the global :file:`~/.gitattributes` file, our ``word`` converter is
linked to :file:`*.docx` files:

.. code-block::

    *.docx diff=word

The same procedure can be used to obtain useful diffs from other binaries, for
example :file:`*.zip`, :file:`*.jar` and other archives with ``unzip`` or for changes in
the meta information of images with ``exiv2``. There are also conversion tools
for converting :file:`*.odt`, :file:`*.doc` and other document formats into plain text.
For binary files for which there is no converter, strings are often sufficient.
