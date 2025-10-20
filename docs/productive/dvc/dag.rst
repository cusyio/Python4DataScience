.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Display pipelines
=================

DVC represents a pipeline internally as directed acyclic graphs (DAGs).

.. seealso::
   `DVC DAG <https://dvc.org/doc/user-guide/pipelines/running-pipelines#dag>`_

You can use ``dvc dag`` to visualise or export pipelines:

.. code-block:: console

    $ uv run dvc dag

        +-------------------+
        | data/data.xml.dvc |
        +-------------------+
                  *
                  *
                  *
              +-------+
              | split |
              +-------+
                  *
                  *
                  *
            +-----------+
            | featurize |
            +-----------+
             **        **
           **            *
          *               **
    +-------+               *
    | train |             **
    +-------+            *
             **        **
               **    **
                 *  *
            +----------+
            | evaluate |
            +----------+

* With ``dvc dag --dot``, a :file:`.dot` file for `Graphviz
  <https://www.graphviz.org>`_ can also be generated:

.. graphviz::

    strict digraph  {
        "data/data.xml.dvc";
        "split";
        "train";
        "featurize";
        "evaluate";
        "data/data.xml.dvc" -> "split";
        "split" -> "featurize";
        "featurize" -> "train";
        "featurize" -> "evaluate";
        "train" -> "evaluate";
    }

With ``dvc status``, you can see whether the levels or local and remote storage
have been changed:

.. code-block:: console

   $ uv run dvc status
   evaluate:
       changed deps:
           modified:           src/dvc_example/evaluate.py
       changed outs:
           modified:           eval

.. seealso::
   `dvc status <https://man.dvc.org/status>`_

In :doc:`CI jobs <../git/advanced/gitlab/ci-cd/index>`, it is usually necessary
to check whether the pipeline is up to date without retrieving or executing
anything. With ``dvc repro --dry``, you can find out which pipeline stages would
need to be executed. However, if data is missing, the command will fail. If
missing data should be ignored, you can use ``dvc repro --dry --allow-missing``.

.. code-block:: console

   $ uv run dvc repro --allow-missing --dry
   'data/data.xml.dvc' didn't change, skipping
   Stage 'prepare' didn't change, skipping
   Stage 'featurize' didn't change, skipping
   Stage 'train' didn't change, skipping
   Stage 'evaluate' is cached - skipping run, checking out outputs
   Running stage 'evaluate':
   > uv run python src/dvc_example/evaluate.py model.pkl data/features
   Use `dvc push` to send your updates to remote storage.
