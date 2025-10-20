.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Manage data
===========

Add data and directories
------------------------

With DVC, you can store and version files, ML models, directories, and
intermediate results with Git without having to check in the file contents to
Git:

.. code-block:: console

    $ uv run dvc get https://github.com/iterative/dataset-registry \
        get-started/data.xml -o data/data.xml
    $ uv run dvc add data/data.xml

This adds the file :file:`data/data.xml` to :file:`data/.gitignore` and writes
the meta information to :file:`data/data.xml.dvc`.

.. seealso::
   `.dvc Files <https://dvc.org/doc/user-guide/project-structure/dvc-files>`_

To manage different versions of your project data with Git, simply add :file:`data/.gitignore` and :file:`data/data.xml.dvc`:

.. code-block:: console

    $ git add data/.gitignore data/data.xml.dvc
    $ git commit -m ":monocle_face: Add data to dvc"

.. seealso::
   `External Dependencies and Outputs
   <https://dvc.org/doc/user-guide/pipelines/external-dependencies-and-outputs>`_

Saving and retrieving data
--------------------------

The data can be copied from the working directory of your Git repository to the
remote storage location with

.. code-block:: console

    $ uv run dvc push

If you want to retrieve more recent data, you can do so with

.. code-block:: console

    $ uv run dvc pull

Importing and updating data
---------------------------

As an alternative to ``dvc get``, you can also import data and models from
another project using ``dvc import``, for example:

.. code-block:: console

   $ uv run dvc import https://github.com/iterative/dataset-registry  get-started/data.xml -o data/data.xml
   Importing 'get-started/data.xml (https://github.com/iterative/dataset-registry)' -> 'data/data.xml'

This loads the file from the `dataset-registry
<https://github.com/iterative/dataset-registry>`_ into our :file:`data`
directory, adds it to :file:`.gitignore`, and creates :file:`data.xml.dvc`.

You can use ``dvc update`` to update these data sources before reproducing a
pipeline that depends on them, for example:

.. code-block:: console

   $ uv run dvc update data/data.xml.dvc
   'data/data.xml.dvc' didn't change, skipping

.. seealso::
   * `Discovering and accessing data
     <https://dvc.org/doc/user-guide/data-management/discovering-and-accessing-data>`_
   * `External Data
     <https://dvc.org/doc/user-guide/data-management/importing-external-data>`_

Deleting data
-------------

If you want to remove files or directories from DVC management, you can do so
with `dvc remove <https://dvc.org/doc/command-reference/remove>`_:

.. code-block::

   $ uv run dvc remove data/data.xml.dvc

You can then use dvc ``gc -w`` to delete all files and their previous versions
from the cache.
