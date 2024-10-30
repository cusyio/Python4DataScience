.. SPDX-FileCopyrightText: 2019 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Start the IPython shell
=======================

You can easily start IPython in a console:

.. code-block:: console

   uv run ipython
   Python 3.12.7 (main, Oct  1 2024, 02:05:46) [Clang 15.0.0 (clang-1500.1.0.2.5)]
   Type 'copyright', 'credits' or 'license' for more information
   IPython 8.29.0 -- An enhanced Interactive Python. Type '?' for help.

   In [1]:

Alternatively, you can use IPython in a Jupyter notebook. To do this, start the
notebook server first:

.. code-block:: console

   $ uv run --with jupyter jupyter notebook

The standard browser should then be opened with the specified URL. Often this is
``http://localhost:8888``.

Now you can start a Python process in the browser by creating a new notebook.
