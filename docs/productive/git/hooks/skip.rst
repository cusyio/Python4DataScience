.. SPDX-FileCopyrightText: 2023 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Skip hooks
==========

Most Git :doc:`index` can be bypassed with the ``--no-verify`` option. For
example, you can skip the pre-commit hook with:

.. code-block:: console

   $ git commit --no-verify -m "Quick and dirty"

If you only want to skip certain :doc:`hooks`, you can use the environment
variable ``SKIP`` with a comma-separated list of hook IDs, for example:

.. code-block:: console

   $ SKIP=check-added-large-file,no-commit-to-branch git commit -m "Hotfix"
