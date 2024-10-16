.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Python environments
===================

The Python Basics tutorial already describes how you can create a Python
environment with :ref:`python-basics:venv`. However, creating this reproducibly
and securely is much more complex. With the Python package manager :term:`pip`,
it could look like this, for example:

.. code-block:: console

    $ python -m pip install --no-deps --require-hashes ----only-binary=:all:

Dedicated environments (for example with :term:`uv` or :doc:`Spack
<spack/index>` simplify this if you save the files with the specifications, for
example with :file:`uv.lock` or or :file:`spack.lock`. This way you and others
can reproduce your environments.

.. toctree::
    :hidden:

    uv/index
    spack/index
