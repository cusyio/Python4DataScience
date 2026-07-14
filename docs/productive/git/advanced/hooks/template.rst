.. SPDX-FileCopyrightText: 2020 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Template for Git repositories
=============================

``prek init-templatedir`` can be used to set up a template for Git’s
`init.templateDir <https://git-scm.com/docs/git-init#_template_directory>`_
option, whereby any newly cloned repository will automatically receive the
pre-commit checks without having to run ``prek install`` , for example:

.. code-block:: console

    $ git config --global init.templateDir ~/.config/git/template
    $ prek init-templatedir ~/.config/git/template
    prek installed at /Users/veit/.config/git/template/hooks/pre-commit
