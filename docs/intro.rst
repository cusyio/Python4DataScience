Introduction
============

Target groups
-------------
The target groups are diverse, from data scientists to data engineers and
analysts to systems engineers. Their skills and workflows are very different.
However, one of the great strengths of Python for Data Science is that it
allows these different experts to work closely together in cross-functional
teams.

Data scientists
    explore data with different parameters and summarise the results.
Data engineers
    check the quality of the code and make it more robust, efficient and
    scalable.
Data analysts
    use the code provided by data engineers to systematically analyse the data.
System engineers
    provide the research platform based on the :doc:`jupyter-tutorial:hub/index`
    on which the other roles can perform their work.

In this tutorial we address system engineers who want to build and run a
platform based on Jupyter notebooks. We then explain how this platform can be
used effectively by data scientists, data engineers and analysts.

Structure of the Python for Data Science tutorial
-------------------------------------------------

From Chapter 2, the tutorial follows the prototype of a research project:

2.  :doc:`workspace/index` with the installation and configuration of
    :doc:`workspace/ipython/index`, :doc:`Jupyter notebooks
    <jupyter-tutorial:index>` with :doc:`jupyter-tutorial:nbextensions/index`
    and :doc:`jupyter-tutorial:ipywidgets/index`.
#.  :doc:`data-processing/index` either through a :doc:`REST API
    <data-processing/requests/index>` or directly from an :doc:`HTML page
    <data-processing/serialisation-formats/xml-html/beautifulsoup>`.
#.  :doc:`clean-prep/index` is a recurring task that involves removing or
    changing redundant, inconsistent or incorrectly formatted data.
#.  :doc:`viz/index` has been moved to a separate tutorial with the many
    different possibilities.
#.  :doc:`performance/index` introduces ways to make your code run faster.
#.  :doc:`productive/index` shows what is necessary to achieve reproducible
    results: not only :doc:`reproducible environments <productive/envs/index>`
    are needed, but also versioning of the :doc:`source code
    <productive/git/index>` and :doc:`data <productive/dvc/index>`. The source
    code should be :doc:`packed into programme libraries <productive/packaging>`
    with :doc:`documentation <productive/documenting>`, :doc:`licence(s)
    <productive/licensing>`, :doc:`tests <productive/testing>` and
    :doc:`logging <productive/logging/index>`. Finally, the chapter includes
    advice on :doc:`improving code quality <productive/qa/index>` and
    :doc:`secure operation <productive/security>`.
#.  :doc:`web/index` can either generate dashboards from Jupyter notebooks or
    require more comprehensive application logic, such as demonstrated in
    :doc:`pyviz:bokeh/embedding-export/flask`, or provide data via a `RESTful
    API <https://en.wikipedia.org/wiki/Representational_state_transfer>`_.

.. include:: ../README.rst
   :start-after: badges
   :end-before: first-steps

.. include:: ../README.rst
   :start-after: follow-us
