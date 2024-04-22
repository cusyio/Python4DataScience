.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Check and improve code quality and complexity
=============================================

If the quality of software is neglected, this quickly leads to superfluous code,
also known as cruft. This then slows down the further development of functions.
This also happens to great teams who are not allowed to spend time maintaining
high code quality. High code quality reduces cruft to a minimum and allows the
team to add features with less effort, time and cost. Although there are some
indicators that can be used to measure internal quality, these can only provide
an initial indication of further productivity. However, a recent `study
<https://arxiv.org/abs/2203.04374>`_ indicates that low quality code took more
than twice as long to fix as high quality code, and that low quality code had a
15 times higher defect density.

In the following, I will show you some :doc:`code-smells` and then some tools
with which you can perform automated static analyses and reformat the code. You
can integrate some of these tools into your editor as well as via the
:doc:`../git/advanced/hooks/pre-commit`. Finally, I’ll introduce you to
:doc:`rope`, a tool that supports you with refactorings.

.. seealso::
   * `PyCQA Meta Documentation <https://meta.pycqa.org/>`_
   * `github.com/PyCQA <https://github.com/PyCQA>`_

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   code-smells

Checker
-------

:doc:`flake8`
    is a wrapper around `PyFlakes <https://pypi.org/project/pyflakes/>`_,
    `pycodestyle <https://pypi.org/project/pycodestyle/>`_ and `McCabe
    <https://pypi.org/project/mccabe/>`_. However, automatic formatting, for
    example with :doc:`black`, is even more convenient.
:doc:`mypy`
    is a static type checker.
:doc:`pytype`
    is a static analysis tool that derives types from your Python code without
    the need for type annotations.
:doc:`wily`
    is a command line tool for checking the complexity of Python code in tests
    and applications.
:doc:`pystra`
    analyses the structural reliability of Python code and summarises it in a
    report.
:doc:`pysa`
    performs `taint <https://en.wikipedia.org/wiki/Taint_checking>`_ analysis to
    identify potential security problems. Pysa traces data streams from their
    origin to their endpoint and identifies vulnerable code.
:doc:`manifest`
    is a tool with which you can quickly check whether the file
    :ref:`python-basics:manifest-in` for Python packages is complete.

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   flake8
   mypy
   pytype
   wily
   pystra
   pysa
   manifest

Formatter
---------

:doc:`black`
    formats your code in a nice and deterministic format.
:doc:`isort`
    formats your ``import`` statements in separate and sorted blocks.
:doc:`prettier`
    offers automatic formatters for other file types.

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   black
   isort
   prettier

Refactoring
-----------

:doc:`rope`
    is a Python refactoring library.

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   rope.ipynb

.. seealso::
   * `Martin Fowler: Refactoring
     <https://www.mitp.de/IT-WEB/Software-Entwicklung/Refactoring.html>`_
