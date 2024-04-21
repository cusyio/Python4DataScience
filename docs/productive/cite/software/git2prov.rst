.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git2PROV
========

`Git2PROV <https://github.com/IDLabResearch/Git2PROV>`_ generates PROV data from
the information in a Git repository.

On the command line, the conversion can be easily executed with:

.. code-block:: console

    $ git2prov git_url [serialization]

For example:

.. code-block:: console

    $ git2prov git@github.com:veit/python4datascience.git PROV-JSON

In total, the following serialisation formats are available:

* ``PROV-N``
* ``PROV-JSON``
* ``PROV-O``
* ``PROV-XML``

Alternatively, Git2PROV also provides a web server with:

.. code-block:: console

    $ git2prov-server [port]

.. seealso::
   * `Git2PROV: Exposing Version Control System Content as W3C PROV
     <http://ceur-ws.org/Vol-1035/iswc2013_demo_32.pdf>`_
   * `GitHub-Repository <https://github.com/IDLabResearch/Git2PROV>`_
