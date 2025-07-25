.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Create a product
================

With Jupyter Notebooks you can quickly build prototypes for data analysis. You
can also use them to document and present your results. However, they are not
well suited for reproducing your results with :menuselection:`Kernel ‣ Restart
and Run All` in a few days or years. For example, the notebooks contain very
little information about the environment, the :doc:`kernel
<jupyter-tutorial:kernels/index>`, with which they have been able to run
successfully in the past. Although you can use ``pd.show_versions()`` to display
:ref:`/workspace/ipython/examples.ipynb#Information-about-the-host-operating-system-and-the-versions-of-installed-Python-packages`,
this is unfortunately not sufficient to reproduce such an environment.

    «Non-reproducible single occurrences are of no significance to science.»[#]_

.. [#] Karl Popper in *The Logic of Scientific Discovery*, 1959

.. figure:: replication_crisis_2x.png
   :alt: XKCD #3117: Replication Crisis

In order for others to be able to use your code, it should meet some conditions:

* You should not silently rely on specific resources and environments
* Required software packages and hardware should be specified in the
  requirements
* Path information will only work in a different context within your package or
  in previously generated directories and files
* Do not share secrets like login details or internal IP numbers in your
  published product

There are various tools that support you in creating shareable products. These
can be tools on the one hand for the :doc:`versioning of the source code
<git/index>` and the :doc:`training data <dvc/index>` as well as for the
reproducibility of the :doc:`execution environments <envs/index>`, on the other
hand for :doc:`testing`, :doc:`python-basics:logging/index`, :doc:`documenting
<documenting>` and :doc:`creating packages <python-basics:libs/index>`.

.. seealso::

   * `Dustin Boswell, Trevor Foucher: The Art of Readable Code
     <https://www.oreilly.com/library/view/the-art-of/9781449318482/>`_
   * TIB workshop «FAIR Data and Software»

     * `GitHub Page
       <https://tibhannover.github.io/2018-07-09-FAIR-Data-and-Software/>`_
     * `GitHub Repository
       <https://github.com/TIBHannover/2018-07-09-FAIR-Data-and-Software>`_
     * `Slides <https://zenodo.org/records/3707745>`_
   * `Dryad: Best practices for creating reusable data publications
     <https://datadryad.org/stash/best_practices>`_
   * Project templates:

     * `GIN-Tonic: Research folder structure standard
       <https://gin-tonic.netlify.app/standard/>`_
     * `The Turing Way: Reproducible project template
       <https://github.com/the-turing-way/reproducible-project-template>`_
     * `TIER Protocol 4.0
       <https://www.projecttier.org/tier-protocol/protocol-4-0/>`_
     * `Materials Data Science and Informatics:
       <https://github.com/Materials-Data-Science-and-Informatics/fair-python-cookiecutter>`_
     * `YODA: Best practices for data analyses in a dataset
       <https://handbook.datalad.org/en/latest/basics/101-127-yoda.html>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    git/index
    dvc/index
    envs/index
    packaging
    documenting
    licensing
    cite/index
    testing
    logging
    qa/index
    security
