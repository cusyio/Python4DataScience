.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Metrics
=======

With DVC, you can easily capture and plot :ref:`metrics <metrics>`,
:ref:`visualise <plots>` performance in charts, and update :doc:`parameters
<params>`. This allows you to run and compare many iterations of your ML
project.

To find the right values for our ML attributes, we add a final evaluation phase to our previous pipeline:

.. code-block:: console

   $ uv run dvc stage add \
       -n evaluate \
       -d src/dvc_example/evaluate.py \
       -d model.pkl \
       -d data/features \
       -o eval \
       uv run python src/dvc_example/evaluate.py model.pkl data/features

This adds a new level to the :file:`dvc.yaml` file:

.. code-block:: yaml
   :lineno-start: 34

   evaluate:
     cmd: uv run python src/dvc_example/evaluate.py model.pkl data/features
     deps:
     - data/features
     - model.pkl
     - src/dvc_example/evaluate.py
     outs:
     - eval

Line 39
    `evaluate.py
    <https://github.com/veit/dvc-example/blob/main/src/dvc_example/evaluate.py>`_
    uses `DVCLive <https://dvc.org/doc/dvclive>`_ to write metrics (for example,
    :abbr:`AUC (Area Under the Curve` and :abbr:`ROC (Receiver Operating
    Characteristic` curve) to the  :file:`eval` directory, which DVC can analyse
    to compare and visualise them across iterations. Typically, DVCLive
    configures metrics and plots in the  :file:`dvc.yaml` file, but in this
    example, we customise them by combining training and test plots.

    .. seealso::
       * `Visualizing Plots
         <https://dvc.org/doc/user-guide/experiment-management/visualizing-plots>`_
       * `DVCLive <https://dvc.org/doc/dvclive>`_

Line 41
    The metrics and plots are stored in the :file:`eval` directory, so these
    files do not affect the Git history. Alternatively, in certain cases, it may
    also be useful to be able to track certain metrics and plots in Git.

Now we can run our evaluations and save the results:

.. code-block:: console

   $ uv run dvc repro
   'data/data.xml.dvc' didn't change, skipping
   Stage 'prepare' didn't change, skipping
   Stage 'featurize' didn't change, skipping
   Stage 'train' didn't change, skipping
   Running stage 'evaluate':
   > uv run python src/dvc_example/evaluate.py model.pkl data/features
   $ git add .gitignore dvc.lock dvc.yaml pyproject.toml src/dvc_example/evaluate.py
   $ git commit -m ':sparkles: Add evaluation step'

.. _metrics:

With `dvc metrics <https://dvc.org/doc/command-reference/metrics>`_, you can
also generate metrics via the command line:

``dvc metrics show``
    displays metrics with optional formatting, for example:

    .. code-block:: console

       $ uv run dvc metrics show
       Path               avg_prec.test    avg_prec.train    roc_auc.test    roc_auc.train
       eval/metrics.json  0.9014           0.95704           0.93196         0.97743

    .. seealso::
       `dvc metrics show <https://dvc.org/doc/command-reference/metrics/show>`_

``dvc metrics diff``
    shows changes in metrics between commits, for example:

    .. code-block:: console

       $ uv run dvc metrics diff
       Path               Metric          HEAD    workspace    Change
       eval/metrics.json  avg_prec.test   -       0.9014       -
       eval/metrics.json  avg_prec.train  -       0.95704      -
       eval/metrics.json  roc_auc.test    -       0.93196      -
       eval/metrics.json  roc_auc.train   -       0.97743      -

    .. seealso::
       `dvc metrics diff <https://dvc.org/doc/command-reference/metrics/diff>`_

.. _plots:

``dvc plots show``
    generates an HTML page with plots:

    .. raw:: html
       :file: plots.html

.. seealso::
   * `dvc plots show <https://dvc.org/doc/command-reference/plots/show>`_
   * `dvc plots diff <https://dvc.org/doc/command-reference/plots/diff>`_

Compare metrics
---------------

If you now change the parameters in the :file:`params.yaml file`, you can
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
