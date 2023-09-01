.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Pipenv and Spack
================

We need Pipenv for our :doc:`Spack environments <../../envs/spack/envs>` to be
able to generate binary-compatible builds with Spack on the one hand and to be
able to easily use Python packages for data collection, visualization,
:abbr:`etc. (et cetera)` on the other.

To do this, first activate the appropriate Python version from the Spack
environment:

   .. code-block:: console

    $  spack env activate python-311
    $ spack env status
    ==> In environment python-311
    $ which python
    /srv/jupyter/spack/var/spack/environments/python-311/.spack-env/view/bin/python

Then you can install the existing Pipenv environment with:

   .. code-block:: console

    $ cd ~/jupyter-tutorial/pipenvs/python-311/
    $ pipenv --python=/Users/veit/jupyter-tutorial/spackenvs/python-311/.spack-env/view/bin/python --site-packages
    $ pipenv install
    Creating a virtualenv for this project…
    Pipfile: /Users/veit/jupyter-tutorial/pipenvs/python-311/Pipfile
    Using /Users/veit/jupyter-tutorial/spackenvs/python-311/.spack-env/view/bin/python3.11 (3.11.4) to create virtualenv…
    …

This uses the environment installed with Spack and installs additional packages.

.. seealso::

    * `Pipenv and Other Python Distributions
      <https://pipenv.pypa.io/en/latest/advanced/#pipenv-and-other-python-distributions>`_
