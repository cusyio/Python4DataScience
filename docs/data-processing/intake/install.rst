.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Install Intake
==============

Requirements
------------

Current versions of Bokeh≥2.0 and Panel must be available in order to use
`intake.gui`.

Installation
------------

Intake can be easily installed for your Jupyter kernel with:

.. code-block:: console

    $ pipenv install intake

Create a catalog with sample data
---------------------------------

For the following examples we need some data sets that we create with:

.. code-block:: console

    $ pipenv run intake example
    Creating example catalog...
      Writing us_states.yml
      Writing states_1.csv
      Writing states_2.csv

    To load the catalog:
        >>> import intake
        >>> cat = intake.open_catalog('us_states.yml')
