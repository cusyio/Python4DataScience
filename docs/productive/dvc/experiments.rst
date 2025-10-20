.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Experiments
===========

If you now change the parameters in the :file:`params.yaml` file, you can
compare your current working directory with the last commit (``HEAD``):

.. code-block:: console

   $ uv run dvc params diff
   Path         Param                   HEAD    workspace
   params.yaml  featurize.max_features  100     200
   params.yaml  featurize.ngrams        1       2

.. code-block:: console

   $ uv run dvc metrics diff
   Path               Metric          HEAD     workspace    Change
   eval/metrics.json  avg_prec.test   0.9014   0.925        0.0236
   eval/metrics.json  avg_prec.train  0.95704  0.97437      0.01733
   eval/metrics.json  roc_auc.test    0.93196  0.94602      0.01406
   eval/metrics.json  roc_auc.train   0.97743  0.98667      0.00924

.. code-block:: console

   $ uv run dvc plots diff
   file:///Users/veit/dvc-example/dvc_plots/index.html

.. raw:: html
   :file: plots-diff.html

``dvc exp``
-----------

With `dvc exp <https://dvc.org/doc/command-reference/exp>`_, you can also set
the parameters in the command line, for example:

.. code-block:: console

   $ uv run dvc exp run \
       --set-param 'featurize.max_features=200'

You can also change multiple parameters with a single call:

.. code-block:: console

   $ uv run dvc exp run \
       -S 'featurize.max_features=200' \
       -S 'featurize.ngrams=2'

With ``--queue``, you can also specify multiple values for a parameter:

.. code-block:: console

   $ uv run dvc exp run --queue \
       -S 'featurize.max_features=200,300,400' \
       -S 'featurize.ngrams=2,3,4'
   Queueing with overrides '{'params.yaml': ['featurize.max_features=200', 'featurize.ngrams=2']}'.
   Queued experiment 'sober-name' for future execution.
   Queueing with overrides '{'params.yaml': ['featurize.max_features=200', 'featurize.ngrams=3']}'.
   Queued experiment 'erect-loir' for future execution.
   Queueing with overrides '{'params.yaml': ['featurize.max_features=200', 'featurize.ngrams=4']}'.
   Queued experiment 'tonic-hood' for future execution.
   Queueing with overrides '{'params.yaml': ['featurize.max_features=300', 'featurize.ngrams=2']}'.
    ...

To better identify the experiments, you can also specify ``--name``:

.. code-block:: console

   $ uv run dvc exp run --name 'feature-matrix' --queue \
       -S 'featurize.max_features=200,300,400' \
       -S 'featurize.ngrams=2,3,4'
   Queueing with overrides '{'params.yaml': ['featurize.max_features=200', 'featurize.ngrams=2']}'.
   Queued experiment 'feature-matrix-1' for future execution.
   Queueing with overrides '{'params.yaml': ['featurize.max_features=200', 'featurize.ngrams=3']}'.
   Queued experiment 'feature-matrix-2' for future execution.
   ...

Once you have placed some experiments in the queue, you can run them all with
the following command:

.. code-block:: console

   $ uv run dvc exp run --run-all

With the ``job`` flag of ``dvc queue start``, you can also use multiple workers
for the experiments:

.. code-block:: console

   $ uv run dvc queue start --job 8
   Started '8' new experiments task queue workers.

.. seealso::
   * `Get Started: Experimenting Using Pipelines
     <https://dvc.org/doc/start/experiments/experiment-pipelines>`_
   * `Running Experiments
     <https://dvc.org/doc/user-guide/experiment-management/running-experiments#the-experiments-queue>`_
   * `dvc queue <https://dvc.org/doc/command-reference/queue>`_
