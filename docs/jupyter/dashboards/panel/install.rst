Installation
============

Ihr könnt Panel in der virtuellen Umgebung eurer Jupyter-Kernels installieren
mit:

.. code-block:: console

    veit$ pipenv install panel
    Installing panel…
    Collecting panel
    …
    Installing collected packages: param, pyviz-comms, pyct, markdown, bokeh, panel
    Successfully installed bokeh-1.3.4 markdown-3.1.1 panel-0.6.2 param-1.9.1 pyct-0.4.6 pyviz-comms-0.7.2
    …

Für einige der folgenden Beispiele werden zusätzliche Pakete benötigt wie
z.B. `Holoviews <http://holoviews.org/>`_ und `hvPlot
<https://hvplot.pyviz.org/>`_. Sie können installiert werden mit:

.. code-block:: console

    $ pipenv install "holoviews[recommended]"
    Installing holoviews[recommended]…
    …
    Installing collected packages: param, pyviz-comms, kiwisolver, cycler, pyparsing, matplotlib, pyct, markdown, packaging, bokeh, panel, holoviews
    Successfully installed bokeh-1.3.4 cycler-0.10.0 holoviews-1.12.5 kiwisolver-1.1.0 markdown-3.1.1 matplotlib-3.1.1 packaging-19.1 panel-0.6.2 param-1.9.1 pyct-0.4.6 pyparsing-2.4.2 pyviz-comms-0.7.2
    …
    $ pipenv install hvplot
    Installing hvplot…
    Collecting hvplot
    …
    Installing collected packages: hvplot
    Successfully installed hvplot-0.4.0
    …

Beispiele
---------

#. Herunterladen

   .. code-block:: console

    $ pipenv run panel examples
    Copied examples to /Users/veit/jupyter-tutorial/panel-examples

#. Betrachten

   Anschließend könnt ihr euch die Beispiele anschauen, z.B.
   ``Introduction.ipynb`` mit

   .. code-block:: console

    $ pipenv run panel serve panel-examples/getting_started/Introduction.ipynb
    2019-08-18 10:55:44,056 Starting Bokeh server version 1.3.4 (running on Tornado 6.0.3)
    2019-08-18 10:55:44,067 Bokeh app running at: http://localhost:5006/Introduction
    2019-08-18 10:55:44,067 Starting Bokeh server with process id: 86677

