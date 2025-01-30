
Git for binary files
====================

``git diff`` can be configured so that it can also display meaningful diffs for
binary files.

… for Excel files
-----------------

For this we need `openpyxl <https://openpyxl.readthedocs.io/en/stable/>`_
and `pandas <https://pandas.pydata.org>`_:

.. code-block:: console

    $ uv add openpyxl pandas

Then we can use :doc:`pandas:reference/api/pandas.DataFrame.to_csv` in
:file:`exceltocsv.py` to convert the Excel files:

.. literalinclude:: exceltocsv.py
    :caption: exceltocsv.py
    :name: exceltocsv.py
    :language: python

Now add the following section to your global Git configuration
:file:`~/.config/git/config`:

.. code-block:: ini

    [diff "excel"]
        textconv=python3 /PATH/TO/exceltocsv.py
        binary=true

Finally, in the global :file:`~/.config/git/attributes` file, our ``excel``
converter is linked to :file:`*.xlsx` files:

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

Add the following section to the global Git configuration
:file:`~/.config/git/config`:

.. code-block:: ini

    [diff "pdf"]
        textconv=pdftohtml -stdout

Finally, in the global :file:`~/.config/git/attributes` file, our ``pdf``
converter is linked to :file:`*.pdf` files:

.. code-block:: ini

    *.pdf diff=pdf

Now, when ``git diff`` is called, the PDF files are first converted and then a
diff is performed over the outputs of the converter.

.. _pandoc-to-markdown:

… for documents
---------------

Differences in documents can also be displayed. For this purpose `Pandoc
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
:file:`~/.config/git/attributes`:

.. code-block:: ini

   [diff "pandoc-to-markdown"]
       textconv = pandoc --to markdown
       cachetextconv = true

Finally, in the global :file:`~/.config/git/attributes` file, our
``pandoc-to-markdown`` converter is linked to :file:`*.docx`, :file:`*.odt` and
:file:`*.rtf` files:

.. code-block:: ini

   *.docx diff=pandoc-to-markdown
   *.odt diff=pandoc-to-markdown
   *.rtf diff=pandoc-to-markdown

.. tip::
   :doc:`Jupyter Notebooks <jupyter-tutorial:notebook/index>` write to a JSON
   file :ref:`*.ipynb <jupyter-tutorial:whats-an-ipynb-file>`, which is quite
   dense and difficult to read, especially with diffs. The Markdown
   representation of Pandoc simplifies this:

   .. code-block:: ini

      *.ipynb diff=pandoc-to-markdown

The same procedure can be used to obtain useful diffs from other binaries, for
example ``*.zip``, ``*.jar`` and other archives with ``unzip`` or for changes in
the meta information of images with ``exiv2``. There are also conversion tools
for converting ``*.odt``, ``*.doc`` and other document formats into plain text.
For binary files for which there is no converter, strings are often sufficient.

.. _exiftool:

… for media files
-----------------

`ExifTool <https://exiftool.org>`_ can be used to convert the metadata of media
files to text.

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install libimage-exiftool-perl

.. tab:: macOS

   .. code-block:: console

      $ brew install exiftool

.. tab:: Windows

   .. code-block:: ps1

      > choco install exiftool

.. seealso::
   * `Installing ExifTool <https://exiftool.org/install.html>`_

You can then add the following section to the global Git configuration file
:file:`~/.config/git/config`:

.. code-block:: ini

   [diff "exiftool"]
   textconv = exiftool --composite -x 'Exiftool:*'
   cachetextconv = true
   xfuncname = "^-.*$"

Finally, in :file:`~/.config/git/attributes` the ``exiftool`` converter is
linked to file endings of media files:

.. code-block:: ini

   *.avif diff=exiftool
   *.bmp diff=exiftool
   *.gif diff=exiftool
   *.jpeg diff=exiftool
   *.jpg diff=exiftool
   *.png diff=exiftool
   *.webp diff=exiftool

.. seealso::
   ``exiftool`` can process many more media files. You can find a complete list
   in `Supported File Types <https://exiftool.org/#supported>`_.
