.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Managing data with DVC
======================

For data analysis, and especially for machine learning, it is extremely valuable
to be able to reproduce different versions of analyses that were performed with
different data sets and parameters. However, in order to obtain reproducible
analyses, both the data and the model (including algorithms, parameters,
:abbr:`etc. (et cetera)`) must be versioned. Due to the size of the data,
versioning data for reproducible analyses is a bigger problem than versioning
models. Tools such as `DVC <https://dvc.org/>`_ help with data management by
allowing users to transfer data to a remote data storage location using a
:doc:`Git <../git/index>`-like workflow. This simplifies the retrieval of
specific versions of data to reproduce an analysis.

DVC was developed to enable the sharing and traceable management of :abbr:`ML
(Machine Learning)` models and data sets. It uses its own system for storing
files with support for :abbr:`SSH (Secure Shell)` and :abbr:`HDFS (Hadoop
Distributed File System)`, among others.

.. tip::
   `cusy seminar: Storing code and data in a versioned and reproducible manner
   <https://cusy.io/en/our-training-courses/versioned-and-reproducible-storage-of-code-and-data.html>`_

.. seealso::
   * `Get Started with DVC <https://dvc.org/doc/start>`_
   * `Documentation <https://dvc.org/doc>`_
   * `Git Repository <https://github.com/iterative/dvc>`_

Comparison with related technologies
------------------------------------

git-annex
~~~~~~~~~

`git-annex <https://git-annex.branchable.com/>`_ focuses more on discovering and
using datasets, which are then easily managed with Git. DVC, on the other hand,
stores the data generated at each step of the pipeline in :file:`.dvc` files,
which can then be managed by Git. DVC also provides handy tools for manipulating
and visualising data pipelines, see for example :doc:`dvc status <dag>`.
Finally, :ref:`dvc remote <dvc-remote>` can also be used to specify external
dependencies.

Workflow management systems such as Airflow and Luigi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DVC focuses on data science workflows and modelling; therefore, DVC pipelines
are much lighter, easier to create and modify than with `Airflow
<https://airflow.incubator.apache.org>`_ and `Luigi
<https://luigi.readthedocs.io/en/stable/>`_. However, DVC lacks advanced
features such as execution monitoring, optimisation and fault tolerance. DVC is
also a pure command line tool with no graphical user interface, and it does not
run daemons or servers. `CML <https://cml.dev>`_ attempts to fill some of these
gaps in a lightweight manner with GitHub, GitLab, or Bitbucket. However, DVC and
CML are well suited for iterative machine learning processes; and once a good
model has been found with the two, you are still free to integrate the pipeline
into Luigi or Airflow.

Installation
------------

DVC can be installed with  :term:`uv`. Please note, however, that you must
explicitly specify the extras. These can be ``[ssh]``, ``[s3]``, ``[gs]``,
``[azure]``, and ``[oss]`` or ``[all]``. For ``ssh``, the command looks like
this:

.. code-block:: console

    $ uv add dvc[ssh]

Alternatively, DVC can also be installed via other package managers:

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list
      $ sudo apt update
      $ sudo apt install dvc

.. tab:: macOS

   .. code-block:: console

      $ brew install iterative/homebrew-dvc/dvc

.. toctree::
   :hidden:

   init
   data
   pipeline
   params
   metrics
   experiments
   dag
   reproduce
   integration
   fds
