.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Parameterisation
================

In the next phase of our example, we parameterise the processing and create the
following content in the :file:`params.yaml` file for this purpose:

.. code-block:: yaml

   featurize:
     max_features: 100
     ngrams: 1

To read the parameters, ``-p featurize.max_features,featurize.ngrams`` is added
to the ``dvc stage`` command, in our example:

.. code-block:: console
   :emphasize-lines: 2

   $ uv run dvc stage add \
       -n featurize \
       -p featurize.max_features,featurize.ngrams \
       -d src/dvc_example/featurization.py -d data/prepared \
       -o data/features \
       uv run python src/dvc_example/featurization.py data/prepared data/features

This adds the following to the :file:`dvc.yaml` file:

.. code-block:: yaml

   featurize:
     cmd: uv run python src/dvc_example/featurization.py data/prepared
       data/features
     deps:
     - data/prepared
     - src/dvc_example/featurization.py
     params:
     - featurize.max_features
     - featurize.ngrams
     outs:
     - data/features

To enable this phase to be repeated, the MD5 hash and parameter values are
stored in the :file:`dvc.lock` file:

.. code-block:: yaml

   featurize:
     cmd: uv run python src/dvc_example/featurization.py data/prepared
       data/features
     deps:
     - path: data/prepared
       hash: md5
       md5: 153aad06d376b6595932470e459ef42a.dir
       size: 8437363
       nfiles: 2
     - path: src/dvc_example/featurization.py
       hash: md5
       md5: e22789fc9581cad11ef7a6fa3aa3f17b
       size: 4158
     params:
       params.yaml:
         featurize.max_features: 100
         featurize.ngrams: 1
     outs:
     - path: data/features
       hash: md5
       md5: 820664b8b793837e74ea3a5d334eb85c.dir
       size: 1556292
   nfiles: 2

Finally, :file:`data/.gitignore`, :file:`dvc.lock`, :file:`dvc.yaml`,
:file:`params.yaml` and :file:`src/dvc_example/featurization.py` must be added
to the Git repository:

.. code-block:: console

   $ git add data/.gitignore dvc.lock dvc.yaml src/dvc_example/featurization.py

.. seealso::
   `dvc params <https://dvc.org/doc/command-reference/params>`_
