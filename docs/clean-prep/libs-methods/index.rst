.. SPDX-FileCopyrightText: 2026 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Libraries and methods
=====================

For `data cleaning <https://en.wikipedia.org/wiki/Data_cleansing>`_ and
validation in Python, we use not only well-known libraries such as
:doc:`/workspace/numpy/index` and :doc:`/workspace/pandas/index`, but also
several small, specialised libraries such as :doc:`dedupe <deduplicate>`,
:ref:`TheFuzz </clean-prep/libs-methods/text-analysis.ipynb#thefuzz>`,
:doc:`voluptuous <voluptuous>`, :doc:`tdda <tdda>` and :doc:`hypothesis
<hypothesis>`. We prefer these lighter-weight solutions to large,
general-purpose systems such as `Great Expectations
<https://greatexpectations.io/>`_ or `MobyDQ
<https://ubisoft.github.io/mobydq/>`_.

Overview
--------

.. csv-table:: GitHub Insights
    :header: "Name", "Stars", "Contributors", "Commit activity", "Licence"

    "`scikit-learn <https://github.com/scikit-learn/scikit-learn>`_",".. image:: https://raster.shields.io/github/stars/scikit-learn/scikit-learn",".. image:: https://raster.shields.io/github/contributors/scikit-learn/scikit-learn",".. image:: https://raster.shields.io/github/commit-activity/y/scikit-learn/scikit-learn",".. image:: https://raster.shields.io/github/license/scikit-learn/scikit-learn"
    "`fg-data-profiling <https://github.com/Data-Centric-AI-Community/fg-data-profiling>`_",".. image:: https://raster.shields.io/github/stars/Data-Centric-AI-Community/fg-data-profiling",".. image:: https://raster.shields.io/github/contributors/Data-Centric-AI-Community/fg-data-profiling",".. image:: https://raster.shields.io/github/commit-activity/y/Data-Centric-AI-Community/fg-data-profiling",".. image:: https://raster.shields.io/github/license/Data-Centric-AI-Community/fg-data-profiling"
    "`Hypothesis <https://github.com/HypothesisWorks/hypothesis>`_",".. image:: https://raster.shields.io/github/stars/HypothesisWorks/hypothesis",".. image:: https://raster.shields.io/github/contributors/HypothesisWorks/hypothesis",".. image:: https://raster.shields.io/github/commit-activity/y/HypothesisWorks/hypothesis",".. image:: https://raster.shields.io/github/license/HypothesisWorks/hypothesis"
    "`marshmallow <https://github.com/marshmallow-code/marshmallow>`_",".. image:: https://raster.shields.io/github/stars/marshmallow-code/marshmallow",".. image:: https://raster.shields.io/github/contributors/marshmallow-code/marshmallow",".. image:: https://raster.shields.io/github/commit-activity/y/marshmallow-code/marshmallow",".. image:: https://raster.shields.io/github/license/marshmallow-code/marshmallow"
    "`dedupe <https://github.com/dedupeio/dedupe>`_",".. image:: https://raster.shields.io/github/stars/dedupeio/dedupe",".. image:: https://raster.shields.io/github/contributors/dedupeio/dedupe",".. image:: https://raster.shields.io/github/commit-activity/y/dedupeio/dedupe",".. image:: https://raster.shields.io/github/license/dedupeio/dedupe"
    "`pandera <https://github.com/unionai-oss/pandera>`_",".. image:: https://raster.shields.io/github/stars/unionai-oss/pandera",".. image:: https://raster.shields.io/github/contributors/unionai-oss/pandera",".. image:: https://raster.shields.io/github/commit-activity/y/unionai-oss/pandera",".. image:: https://raster.shields.io/github/license/unionai-oss/pandera"
    "`thefuzz <https://github.com/seatgeek/thefuzz>`_",".. image:: https://raster.shields.io/github/stars/seatgeek/thefuzz",".. image:: https://raster.shields.io/github/contributors/seatgeek/thefuzz",".. image:: https://raster.shields.io/github/commit-activity/y/seatgeek/thefuzz",".. image:: https://raster.shields.io/github/license/seatgeek/thefuzz"
    "`cerberus <https://github.com/pyeve/cerberus>`_",".. image:: https://raster.shields.io/github/stars/pyeve/cerberus",".. image:: https://raster.shields.io/github/contributors/pyeve/cerberus",".. image:: https://raster.shields.io/github/commit-activity/y/pyeve/cerberus",".. image:: https://raster.shields.io/github/license/pyeve/cerberus"
    "`Voluptuous <https://github.com/alecthomas/voluptuous>`_",".. image:: https://raster.shields.io/github/stars/alecthomas/voluptuous",".. image:: https://raster.shields.io/github/contributors/alecthomas/voluptuous",".. image:: https://raster.shields.io/github/commit-activity/y/alecthomas/voluptuous",".. image:: https://raster.shields.io/github/license/alecthomas/voluptuous"
    "`DataProfiler <https://github.com/capitalone/DataProfiler>`_",".. image:: https://raster.shields.io/github/stars/capitalone/DataProfiler",".. image:: https://raster.shields.io/github/contributors/capitalone/DataProfiler",".. image:: https://raster.shields.io/github/commit-activity/y/capitalone/DataProfiler",".. image:: https://raster.shields.io/github/license/capitalone/DataProfiler"
    "`datacleaner <https://github.com/rhiever/datacleaner>`_",".. image:: https://raster.shields.io/github/stars/rhiever/datacleaner",".. image:: https://raster.shields.io/github/contributors/rhiever/datacleaner",".. image:: https://raster.shields.io/github/commit-activity/y/rhiever/datacleaner",".. image:: https://raster.shields.io/github/license/rhiever/datacleaner"
    "`popmon <https://github.com/ing-bank/popmon>`_",".. image:: https://raster.shields.io/github/stars/ing-bank/popmon",".. image:: https://raster.shields.io/github/contributors/ing-bank/popmon",".. image:: https://raster.shields.io/github/commit-activity/y/ing-bank/popmon",".. image:: https://raster.shields.io/github/license/ing-bank/popmon"
    "`TDDA <https://github.com/tdda/tdda>`_",".. image:: https://raster.shields.io/github/stars/tdda/tdda",".. image:: https://raster.shields.io/github/contributors/tdda/tdda",".. image:: https://raster.shields.io/github/commit-activity/y/tdda/tdda",".. image:: https://raster.shields.io/github/license/tdda/tdda"
    "`Validr <https://github.com/guyskk/validr>`_",".. image:: https://raster.shields.io/github/stars/guyskk/validr",".. image:: https://raster.shields.io/github/contributors/guyskk/validr",".. image:: https://raster.shields.io/github/commit-activity/y/guyskk/validr",".. image:: https://raster.shields.io/github/license/guyskk/validr"
    "`Probatus <https://github.com/ing-bank/probatus>`_",".. image:: https://raster.shields.io/github/stars/ing-bank/probatus",".. image:: https://raster.shields.io/github/contributors/ing-bank/probatus",".. image:: https://raster.shields.io/github/commit-activity/y/ing-bank/probatus",".. image:: https://raster.shields.io/github/license/ing-bank/probatus"

Dormant projects
----------------

.. csv-table:: GitHub Insights
    :header: "Name", "Stars", "Contributors", "Commit activity", "Licence"

    "`Bulwark <https://github.com/ZaxR/bulwark>`_",".. image:: https://raster.shields.io/github/stars/ZaxR/bulwark",".. image:: https://raster.shields.io/github/contributors/ZaxR/bulwark",".. image:: https://raster.shields.io/github/commit-activity/y/ZaxR/bulwark",".. image:: https://raster.shields.io/github/license/ZaxR/bulwark"
    "`PandasSchema <https://github.com/multimeric/PandasSchema>`_",".. image:: https://raster.shields.io/github/stars/multimeric/PandasSchema",".. image:: https://raster.shields.io/github/contributors/multimeric/PandasSchema",".. image:: https://raster.shields.io/github/commit-activity/y/multimeric/PandasSchema",".. image:: https://raster.shields.io/github/license/multimeric/PandasSchema"
    "`pandas-validation <https://github.com/jmenglund/pandas-validation>`_",".. image:: https://raster.shields.io/github/stars/jmenglund/pandas-validation",".. image:: https://raster.shields.io/github/contributors/jmenglund/pandas-validation",".. image:: https://raster.shields.io/github/commit-activity/y/jmenglund/pandas-validation",".. image:: https://raster.shields.io/github/license/jmenglund/pandas-validation"
    "`Opulent-Pandas <https://github.com/danielvdende/opulent-pandas>`_",".. image:: https://raster.shields.io/github/stars/danielvdende/opulent-pandas",".. image:: https://raster.shields.io/github/contributors/danielvdende/opulent-pandas",".. image:: https://raster.shields.io/github/commit-activity/y/danielvdende/opulent-pandas",".. image:: https://raster.shields.io/github/license/danielvdende/opulent-pandas"
    "`signpost <https://github.com/ilsedippenaar/signpost>`_",".. image:: https://raster.shields.io/github/stars/ilsedippenaar/signpost",".. image:: https://raster.shields.io/github/contributors/ilsedippenaar/signpost",".. image:: https://raster.shields.io/github/commit-activity/y/ilsedippenaar/signpost",".. image:: https://raster.shields.io/github/license/ilsedippenaar/signpost"

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    nulls.ipynb
    outliers.ipynb
    text-analysis.ipynb
    deduplicate.ipynb
    hypothesis.ipynb
    tdda.ipynb
    voluptuous.ipynb
    scikit-learn-reprocessing.ipynb
    dask-pipeline.ipynb
