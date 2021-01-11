jupyter-flex
============

Jupyter extension that turns notebooks into dashboards:

* uses Markdown headers and Jupyter notebook cell tags to define the layout and
  components of the dashboard
* flexible and easy way to define row- and column-oriented layouts
* uses :doc:`/workspace/jupyter/nbconvert` for static reports
* uses :doc:`../voila/index` for dynamic applications with a Jupyter
  :doc:`/workspace/jupyter/kernels/index`
* :doc:`/workspace/jupyter/ipywidgets/index` support

.. seealso::
   * `Docs <https://jupyter-flex.extrapolations.dev/>`_
   * `GitHub <https://github.com/danielfrg/jupyter-flex>`_

Examples
--------

.. figure:: movie-explorer.png
   :alt: Movie explorer
   :target: https://mybinder.org/v2/gh/danielfrg/jupyter-flex/0.6.4?urlpath=%2Fvoila%2Frender%2Fexamples%2Fmovie-explorer.ipynb

.. figure:: data-scoring.png
   :alt: NBA scoring
   :target: https://jupyter-flex.extrapolations.dev/examples/nba-scoring.html

.. figure:: altair.png
   :alt: Altair plots
   :target: https://jupyter-flex.extrapolations.dev/examples/altair.html

Installation
------------

.. code-block:: console

    $ pipenv install jupyter-flex
