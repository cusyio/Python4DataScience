.. SPDX-FileCopyrightText: 2019 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Start the IPython shell
=======================

You can easily start IPython in a console:

.. code-block:: console

   $ uv run ipython
   Python 3.11.10 (main, Sep  7 2024, 01:03:31) [Clang 16.0.0 (clang-1600.0.26.3)]
   Type 'copyright', 'credits' or 'license' for more information
   IPython 8.21.0 -- An enhanced Interactive Python. Type '?' for help.

   In [1]:

Alternatively, you can use IPython in a Jupyter notebook. To do this, start the
notebook server first:

.. code-block:: console

    $ uv run --with jupyter jupyter notebook
    [I 17:35:02.419 NotebookApp] Serving notebooks from local directory: /Users/veit/cusy/trn/Python4DataScience
    [I 17:35:02.419 NotebookApp] The Jupyter Notebook is running at:
    [I 17:35:02.427 NotebookApp] http://localhost:8888/?token=72209334c2e325a68115902a63bd064db436c0c84aeced7f
    [I 17:35:02.428 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 17:35:02.497 NotebookApp]

The standard browser should then be opened with the specified URL. Often this is
``http://localhost:8888``.

Now you can start a Python process in the browser by creating a new notebook.
