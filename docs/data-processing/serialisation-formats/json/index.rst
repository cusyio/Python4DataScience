.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

JSON
====

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| +-    | JSON supports array and map or object structures and  |
|                       |       | many different data types including strings, numbers, |
|                       |       | boolean, null etc., but no date formats.              |
|                       |       |                                                       |
|                       |       | However, JSON does not support all data types of      |
|                       |       | JavaScript: ``NaN`` and ``Infinity`` become ``null``. |
|                       |       |                                                       |
|                       |       | Note that the JSON syntax also don’t support comments |
|                       |       | and you have to work around for example with a        |
|                       |       | ``__comment__`` key/value pair.                       |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | \+    | JSON has a formal strongly typed `standard`_ (see     |
|                       |       | also :rfc:`8259`).                                    |
|                       |       | However, JSON data also contains some pitfalls due to |
|                       |       | the ambiguity of the JSON specifications:             |
|                       |       |                                                       |
|                       |       | *A JSON parser MUST accept all texts that conform to  |
|                       |       | the JSON grammar* (:rfc:`7159`)                       |
|                       |       |                                                       |
|                       |       | and                                                   |
|                       |       |                                                       |
|                       |       | *An implementation may set limits on the size of texts|
|                       |       | that it accepts. An implementation may set limits on  |
|                       |       | the maximum depth of nesting. An implementation may   |
|                       |       | set limits on the range and precision of numbers. An  |
|                       |       | implementation may set limits on the length and       |
|                       |       | character contents of strings*                        |
|                       |       | (:rfc:`7158#section-9`).                              |
|                       |       |                                                       |
|                       |       | Unfortunately there is neither a reference            |
|                       |       | implementation nor an official test suite that would  |
|                       |       | show the expected behaviour – at least `JSON_Checker`_|
|                       |       | gives some hints.                                     |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | +-    | Partly with `JSON Schema Proposal`_, `JSON Encoding   |
|                       |       | Rules (JER)`_, `Kwalify`_, `Rx`_, `JSON-LD`_ or       |
|                       |       | `JMESPath`_.                                          |
|                       |       |                                                       |
|                       |       | After all, there are many different `validators`_     |
|                       |       | available.                                            |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | ++    | The JSON format is very well supported by almost every|
|                       |       | programming language.                                 |
|                       |       |                                                       |
|                       |       | The data structure of JSON closely represent objects  |
|                       |       | in many languages for example a Python ``dict`` can   |
|                       |       | be represented as JSON ``object``, and a Python       |
|                       |       | ``list`` by a JSON ``array``.                         |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | +-    | JSON is a human-readable serialisation format but it  |
|                       |       | does not support comments.                            |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | ++    | JSON is one of the fastest human-readable formats to  |
|                       |       | serialise and deserialise.                            |
+-----------------------+-------+-------------------------------------------------------+
| File size             | +-    | JSON is in the medium range similar to                |
|                       |       | :doc:`../yaml/index` and :doc:`../toml/index`.        |
+-----------------------+-------+-------------------------------------------------------+

Example
-------

Response of the :ref:`OSM-Nominatim-API
</data-processing/httpx/install-example.ipynb#example-osm-nominatim-api>`

.. code-block:: javascript

    [
        {
            'place_id': 234847916,
            'licence': 'Data Â© OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'relation',
            'osm_id': 131761,
            'boundingbox': ['52.5200695', '52.5232601', '13.4103097', '13.4160798'],
            'lat': '52.521670650000004',
            'lon': '13.413278026558228',
            'display_name': 'Alexanderplatz, Mitte, Berlin, 10178, Deutschland',
            'class': 'highway',
            'type': 'pedestrian',
            'importance': 0.6914982526373583
        },
        {
            'place_id': 53256307,
            'licence': 'Data Â© OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'node',
            'osm_id': 4389211800,
            'boundingbox': ['52.5231653', '52.5232653', '13.414475', '13.414575'],
            'lat': '52.5232153',
            'lon': '13.414525',
            'display_name': 'Alexanderplatz, AlexanderstraÃŸe, Mitte, Berlin, 10178, Deutschland',
            'class': 'highway',
            'type': 'bus_stop',
            'importance': 0.22100000000000003,
            'icon': 'https://nominatim.openstreetmap.org/images/mapicons/transport_bus_stop2.p.20.png'
        },
        {
            'place_id': 90037579,
            'licence': 'Data Â© OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'way',
            'osm_id': 23853138,
            'boundingbox': ['52.5214702', '52.5217276', '13.4037885', '13.4045026'],
            'lat': '52.5215991',
            'lon': '13.404112295159964',
            'display_name': 'Alexander Plaza, 1, RosenstraÃŸe, Mitte, Berlin, 10178, Deutschland',
            'class': 'tourism',
            'type': 'hotel',
            'importance': 0.11100000000000002,
            'icon': 'https://nominatim.openstreetmap.org/images/mapicons/accommodation_hotel2.p.20.png'
        }
    ]

JSON tools
----------

`fx <https://github.com/antonmedv/fx>`_
    makes JSON searchable. This makes it easier to explore APIs that return
    large JSON blocks but are poorly documented.

    .. image:: https://raster.shields.io/github/stars/antonmedv/fx
       :alt: Stars
       :target: https://github.com/antonmedv/fx

    .. image:: https://raster.shields.io/github/contributors/antonmedv/fx
       :alt: Contributors
       :target: https://github.com/antonmedv/fx/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/antonmedv/fx
       :alt: Commit activity
       :target: https://github.com/antonmedv/fx/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/antonmedv/fx
       :alt: Licence

`gron <https://github.com/tomnomnom/gron>`_
    Terminal JSON viewer & processor

    .. image:: https://raster.shields.io/github/stars/tomnomnom/gron
       :alt: Stars
       :target: https://github.com/tomnomnom/gron

    .. image:: https://raster.shields.io/github/contributors/tomnomnom/gron
       :alt: Contributors
       :target: https://github.com/tomnomnom/gron/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/tomnomnom/gron
       :alt: Commit activity
       :target: https://github.com/tomnomnom/gron/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/tomnomnom/gron
       :alt: Licence

`JC – JSON Convert <https://github.com/kellyjonbrazil/jc>`_
    is a CLI tool and Python library that converts the output of common command
    line tools, file types and strings to JSON, :doc:`../yaml/index` or
    :doc:`python-basics:types/dicts`; this allows the output to be passed to
    tools such as `jq <https://jqlang.org>`_ and simplifies automation scripts.

    .. image:: https://raster.shields.io/github/stars/kellyjonbrazil/jc
       :alt: Stars
       :target: https://github.com/kellyjonbrazil/jc

    .. image:: https://raster.shields.io/github/contributors/kellyjonbrazil/jc
       :alt: Contributors
       :target: https://github.com/kellyjonbrazil/jc/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/kellyjonbrazil/jc
       :alt: Commit activity
       :target: https://github.com/kellyjonbrazil/jc/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/kellyjonbrazil/jc
       :alt: Licence

`UltraJSON <https://github.com/ultrajson/ultrajson>`_
    is a fast JSON encoder and decoder written in pure C and providing bindings
    for Python≥3.9.

    .. image:: https://raster.shields.io/github/stars/ultrajson/ultrajson
       :alt: Stars
       :target: https://github.com/ultrajson/ultrajson

    .. image:: https://raster.shields.io/github/contributors/ultrajson/ultrajson
       :alt: Contributors
       :target: https://github.com/ultrajson/ultrajson/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/ultrajson/ultrajson
       :alt: Commit activity
       :target: https://github.com/ultrajson/ultrajson/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/ultrajson/ultrajson
       :alt: Licence

`simplejson <https://github.com/simplejson/simplejson>`_
    is a simple, fast and extensible JSON encoder/decoder for Python.

    .. image:: https://raster.shields.io/github/stars/simplejson/simplejson
       :alt: Stars
       :target: https://github.com/simplejson/simplejson

    .. image:: https://raster.shields.io/github/contributors/simplejson/simplejson
       :alt: Contributors
       :target: https://github.com/simplejson/simplejson/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/simplejson/simplejson
       :alt: Commit activity
       :target: https://github.com/simplejson/simplejson/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/simplejson/simplejson
       :alt: Licence

`python-json-patch <https://github.com/stefankoegl/python-json-patch>`_
    is a Python library for JSON patches according to :rfc:`6902`.

    .. image:: https://raster.shields.io/github/stars/stefankoegl/python-json-patch
       :alt: Stars
       :target: https://github.com/stefankoegl/python-json-patch

    .. image:: https://raster.shields.io/github/contributors/stefankoegl/python-json-patch
       :alt: Contributors
       :target: https://github.com/stefankoegl/python-json-patch/graphs/contributors

    .. image:: https://raster.shields.io/github/commit-activity/y/stefankoegl/python-json-patch
       :alt: Commit activity
       :target: https://github.com/stefankoegl/python-json-patch/graphs/commit-activity

    .. image:: https://raster.shields.io/github/license/stefankoegl/python-json-patch
       :alt: Licence

.. _`standard`: https://www.json.org/json-en.html
.. _`JSON_Checker`: http://www.json.org/JSON_checker/
.. _`JSON Schema Proposal`: https://json-schema.org
.. _`JSON Encoding Rules (JER)`: https://www.itu.int/rec/T-REC-X.697-201710-I/
.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: https://rx.codesimply.com
.. _`JSON-LD`: https://json-ld.org#
.. _`JMESPath`: https://jmespath.org/
.. _`validators`: https://json-schema.org/tools?query=&sortBy=name&sortOrder=ascending&groupBy=toolingTypes&licenses=&languages=&drafts=&toolingTypes=#validator

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    example.ipynb
