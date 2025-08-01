.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Geodata
=======

File formats
------------

.. _pmtiles:

PMTiles
~~~~~~~

`PMTiles <https://docs.protomaps.com>`_ is a general format for tile data
addressed by Z/X/Y coordinates. This can be cartographic vector tiles,
:ref:`remote sensing data <remote-sensing>`, JPEG images or similar.

`HTTP Range Requests
<https://developer.mozilla.org/en-US/docs/Web/HTTP/Range_requests>`_ are used
for reading in order to retrieve only the relevant tiles or metadata within a
PMTiles archive. The arrangement of tiles and directories is designed to
minimise the number of requests when moving and zooming.

However, PMTiles is a read-only format: it is not possible to update part of the
archive without rewriting the entire file. If you need transactional updates,
you should use a database such as SQLite or :doc:`postgresql/postgis/index` and
`ST_asMVT <https://postgis.net/docs/ST_AsMVT.html>`_.

.. seealso::
   * `GitHub Repository <https://github.com/protomaps/PMTiles>`_
   * `PMTiles Version 3 Specification
     <https://github.com/protomaps/PMTiles/blob/main/spec/v3/spec.md>`_
   * `pmtiles Python package
     <https://github.com/protomaps/PMTiles/tree/main/python/pmtiles>`_

Mapbox Vector Tiles (MVT)
~~~~~~~~~~~~~~~~~~~~~~~~~

The `Mapbox Vector Tiles
<https://docs.mapbox.com/data/tilesets/guides/vector-tiles-standards/>`_ file
format stores each tile in a directory tree like :file:`/Z/X/Y.mvt`. This works
well for small tile sets, but updating an entire global pyramid of ~300 million
tiles is very inefficient. :ref:`pmtiles`, on the other hand, is a single file
with tiles de-duplicated, reducing the size of global vector basemaps by ~70%.

For writing, the :ref:`gdal` library with `SQLite <https://www.sqlite.org>`_ and
`GEOS <https://libgeos.org>`_ support must be installed. The :ref:`mbtiles` are
stored in SQLite like mbtiles and can be processed with the MBTiles driver.

.. seealso::
   * `Mapbox Vector Tile specification
     <https://github.com/mapbox/vector-tile-spec>`_
   * `MVT: Mapbox Vector Tiles
     <https://gdal.org/en/stable/drivers/vector/mvt.html>`_

.. _mbtiles:

MBTiles
~~~~~~~

`MBTiles <https://docs.mapbox.com/help/glossary/mbtiles/>`_ is a container
format for tile data based on SQLite. It is optimised for local access, not for
access via HTTP like :ref:`pmtiles`.

.. seealso::
   * `MBTiles specification <https://github.com/mapbox/mbtiles-spec>`_

.. _geodata-repositories:

Cloud Optimized GeoTIFF (COG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Cloud Optimized GeoTIFF <https://cogeo.org>`_ is a raster TIFF file that, like
:ref:`pmtiles`, is optimised for reading from a cloud storage. :ref:`pmtiles`
can also deliver other tile data, for example vector tiles. However, COG is
backwards compatible with most GIS programmes that work with GeoTIFF.

.. seealso::
   * `OGC Cloud Optimized GeoTIFF Standard
     <https://docs.ogc.org/is/21-026/21-026.html>`_

.. _geoparquet:

GeoParquet
~~~~~~~~~~

`Parquet <https://parquet.apache.org>`_ is an open-source, column-orientated
data file format that was developed for the efficient storage and retrieval of
data. It offers efficient data compression and encoding methods with optimised
processing of large, complex data. `GeoParquet <https://geoparquet.org>`_
extends Parquet with interoperable geodata types (point, line, polygon).


* :doc:`pyviz:matplotlib/geopandas/index` supports the `reading
  <https://geopandas.org/en/stable/docs/reference/api/geopandas.read_parquet.html>`_
  and `writing
  <https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_parquet.html>`_
  of GeoParquet.
* `GeoParquet Downloader Plugin
  <https://plugins.qgis.org/plugins/qgis_plugin_gpq_downloader/>`_ for `QGIS
  <https://qgis.org>`_ enables streaming downloads of large GeoParquet datasets.
* `DuckDB <https://duckdb.org>`_ allows the reading and writing of GeoParquet
  files with the `Spatial Extension
  <https://duckdb.org/docs/stable/extensions/spatial/overview.html>`_.

.. seealso::
   * `GeoParquet specification <https://github.com/opengeospatial/geoparquet>`_
   * `GeoParquet Software <https://geoparquet.org/#implementations>`_
   * `validate_geoparquet.py
     <https://github.com/OSGeo/gdal/blob/master/swig/python/gdal-utils/osgeo_utils/samples/validate_geoparquet.py>`_

.. _geodata-repositories:

Data repositories
-----------------

`Norwegian Polar Data Centre: Datasets <https://data.npolar.no/dataset>`_
    Antarctica, Arctic Ocean and Svalbard
`Common Metadata Repository (CMR) <https://cmr.earthdata.nasa.gov/search>`_
    Search API for NASA's remote-sensed earth science metadata
`UC Irvine Machine Learning Repository <https://archive.ics.uci.edu>`_
    Machine learning datasets, featuring data on air quality, ozone level
    detection, greenhouse gas concentrations, aquatic toxicity, and more
`National Data Buoy Center <https://www.ndbc.noaa.gov>`_
    Meteorological and oceanographic measurements for the marine environment.

.. seealso::
   `List of GIS data sources
   <https://en.wikipedia.org/wiki/List_of_GIS_data_sources>`_

Software
--------

Reading and writing
~~~~~~~~~~~~~~~~~~~

.. _gdal:

`Geospatial Data Abstraction Library (GDAL) <https://gdal.org/en/latest/>`_
    provides a low-level but more powerful API for reading and writing hundreds
    of data formats.

    .. image::
       https://raster.shields.io/github/stars/OSGeo/gdal
    .. image::
       https://raster.shields.io/github/contributors/OSGeo/gdal
    .. image::
       https://raster.shields.io/github/commit-activity/y/OSGeo/gdal
    .. image::
       https://raster.shields.io/github/license/OSGeo/gdal

`pyogrio <https://pyogrio.readthedocs.io/en/latest/>`_
    provides a :doc:`pyviz:matplotlib/geopandas/index`-oriented API to OGR
    vector data sources, such as ESRI Shapefile, GeoPackage, and GeoJSON.

    .. image::
       https://raster.shields.io/github/stars/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/contributors/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/commit-activity/y/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/license/geopandas/geopandas

`Rasterio <https://rasterio.readthedocs.io/en/latest/>`_
    reads and writes GeoTIFF and other forms of raster datasets.

    .. image::
       https://raster.shields.io/github/stars/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/contributors/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/commit-activity/y/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/license/rasterio/rasterio

`Zarr-Python <https://zarr.readthedocs.io/en/stable/>`_
    `Zarr <https://zarr.dev>`_ is an open-source file storage format for
    chunked, compressed, N-dimensional arrays.

    .. image::
       https://raster.shields.io/github/stars/zarr-developers/zarr-python
    .. image::
       https://raster.shields.io/github/contributors/zarr-developers/zarr-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/zarr-developers/zarr-python
    .. image::
       https://raster.shields.io/github/license/zarr-developers/zarr-python

`Fiona <https://fiona.readthedocs.io/en/latest/>`_
    reads and writes :file:`*.shp`- and :file:`*.json` data and many other
    formats.

    .. image::
       https://raster.shields.io/github/stars/Toblerity/Fiona
    .. image::
       https://raster.shields.io/github/contributors/Toblerity/Fiona
    .. image::
       https://raster.shields.io/github/commit-activity/y/Toblerity/Fiona
    .. image::
       https://raster.shields.io/github/license/Toblerity/Fiona

`netCDF4 <https://unidata.github.io/netcdf4-python/>`_
    is a Python interface to the `netCDF
    <https://www.unidata.ucar.edu/software/netcdf/>`_ C library.

    .. image::
       https://raster.shields.io/github/stars/Unidata/netcdf4-python
    .. image::
       https://raster.shields.io/github/contributors/Unidata/netcdf4-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/Unidata/netcdf4-python
    .. image::
       https://raster.shields.io/github/license/Unidata/netcdf4-python

`pyModis <http://www.pymodis.org/>`_
    Collection of Python scripts for downloading and mosaicking `MODIS
    <https://en.wikipedia.org/wiki/Moderate_Resolution_Imaging_Spectroradiometer>`__
    data.

    .. image::
       https://raster.shields.io/github/stars/lucadelu/pyModis
    .. image::
       https://raster.shields.io/github/contributors/lucadelu/pyModis
    .. image::
       https://raster.shields.io/github/commit-activity/y/lucadelu/pyModis
    .. image::
       https://raster.shields.io/github/license/lucadelu/pyModis

`xmitgcm <https://xmitgcm.readthedocs.io/en/latest/>`_
    reads `MITgcm <https://mitgcm.org>`_ binary MDS files into xarray data
    structures.

    .. image::
       https://raster.shields.io/github/stars/MITgcm/xmitgcm
    .. image::
       https://raster.shields.io/github/contributors/MITgcm/xmitgcm
    .. image::
       https://raster.shields.io/github/commit-activity/y/MITgcm/xmitgcm
    .. image::
       https://raster.shields.io/github/license/MITgcm/xmitgcm

.. seealso::
   :ref:`geo-wrappers`

.. _remote-sensing:

Remote sensing
~~~~~~~~~~~~~~

`Satpy <https://satpy.readthedocs.io/en/stable/>`_
    Easy to use API for sensors of satellite images like `MODIS
    <https://modis.gsfc.nasa.gov/data/>`_, `Sentinel-2
    <https://sentiwiki.copernicus.eu/web/s2-mission>`_ :abbr:`etc (et cetera)`.

    .. image::
       https://raster.shields.io/github/stars/pytroll/satpy
    .. image::
       https://raster.shields.io/github/contributors/pytroll/satpy
    .. image::
       https://raster.shields.io/github/commit-activity/y/pytroll/satpy
    .. image::
       https://raster.shields.io/github/license/pytroll/satpy

`sentinelsat <https://github.com/sentinelsat/sentinelsat>`_
    Find and download Copernicus Sentinel satellite imagery using command line
    or Python.

    .. image::
       https://raster.shields.io/github/stars/sentinelsat/sentinelsat
    .. image::
       https://raster.shields.io/github/contributors/sentinelsat/sentinelsat
    .. image::
       https://raster.shields.io/github/commit-activity/y/sentinelsat/sentinelsat
    .. image::
       https://raster.shields.io/github/license/sentinelsat/sentinelsat

`Open Data Cube <https://www.opendatacube.org>`_
    Open Source Geospatial Data Management and Analysis Software.

    .. image::
       https://raster.shields.io/github/stars/opendatacube/datacube-core
    .. image::
       https://raster.shields.io/github/contributors/opendatacube/datacube-core
    .. image::
       https://raster.shields.io/github/commit-activity/y/opendatacube/datacube-core
    .. image::
       https://raster.shields.io/github/license/opendatacube/datacube-core

`RSGISLib <http://rsgislib.org/>`_
    or *The Remote Sensing and GIS Software Library* is a set of remote sensing
    tools for raster processing and analysis.

    .. image::
       https://raster.shields.io/github/stars/remotesensinginfo/rsgislib
    .. image::
       https://raster.shields.io/github/contributors/remotesensinginfo/rsgislib
    .. image::
       https://raster.shields.io/github/commit-activity/y/remotesensinginfo/rsgislib
    .. image::
       https://raster.shields.io/github/license/remotesensinginfo/rsgislib

.. seealso::
   :doc:`/clean-prep/dask-pipeline`

General purposes
~~~~~~~~~~~~~~~~

`pyproj <https://github.com/pyproj4/pyproj>`_
    Python interface to `PROJ <https://proj.org/>`_, a library for cartographic
    projections and coordinate transformations.

    .. image::
       https://raster.shields.io/github/stars/pyproj4/pyproj
    .. image::
       https://raster.shields.io/github/contributors/pyproj4/pyproj
    .. image::
       https://raster.shields.io/github/commit-activity/y/pyproj4/pyproj
    .. image::
       https://raster.shields.io/github/license/pyproj4/pyproj

.. _geopython:

`geopython <https://geopython.github.io/>`_
    is a GitHub organization that covers Python projects related to geodata.

    `pygeoapi <https://github.com/geopython/pygeoapi>`_
        is a Python server implementation of the `OGC-API
        <https://ogcapi.ogc.org>`_ standard suite.

        .. image::
           https://raster.shields.io/github/stars/geopython/pygeoapi
        .. image::
           https://raster.shields.io/github/contributors/geopython/pygeoapi
        .. image::
           https://raster.shields.io/github/commit-activity/y/geopython/pygeoapi
        .. image::
           https://raster.shields.io/github/license/geopython/pygeoapi

    `OWSLib <https://github.com/geopython/OWSLib>`_
        is a Python package for client programming using the `Open Geospatial
        Consortium (OGC) Web Service <https://www.ogc.org/standards/owc/>`_
        interface standards and associated content models.

        .. image::
           https://raster.shields.io/github/stars/geopython/OWSLib
        .. image::
           https://raster.shields.io/github/contributors/geopython/OWSLib
        .. image::
           https://raster.shields.io/github/commit-activity/y/geopython/OWSLib
        .. image::
           https://raster.shields.io/github/license/geopython/OWSLib

    `pycsw <https://github.com/geopython/pycsw>`_
        is an `OGC CSW <https://www.ogc.org/standards/cat/>`_ server
        implementation written in Python that fully implements the `OpenGIS
        Catalogue Service <https://www.ogc.org/standards/cat/>`_.

        .. image::
           https://raster.shields.io/github/stars/geopython/pygeoapi
        .. image::
           https://raster.shields.io/github/contributors/geopython/pygeoapi
        .. image::
           https://raster.shields.io/github/commit-activity/y/geopython/pygeoapi
        .. image::
           https://raster.shields.io/github/license/geopython/pygeoapi

    `pygeometa <https://github.com/geopython/pygeometa>`_
        can be used to generate metadata for spatial data sets.

        .. image::
           https://raster.shields.io/github/stars/geopython/pygeometa
        .. image::
           https://raster.shields.io/github/contributors/geopython/pygeometa
        .. image::
           https://raster.shields.io/github/commit-activity/y/geopython/pygeometa
        .. image::
           https://raster.shields.io/github/license/geopython/pygeometa

`pgeocode <https://pypi.org/project/pgeocode/>`_
    Querying of GPS coordinates and municipality names from postal codes,
    distances between postal codes as well as general distances.

    .. image::
       https://raster.shields.io/github/stars/symerio/pgeocode
    .. image::
       https://raster.shields.io/github/contributors/symerio/pgeocode
    .. image::
       https://raster.shields.io/github/commit-activity/y/symerio/pgeocode
    .. image::
       https://raster.shields.io/github/license/symerio/pgeocode

`Arcpy <https://pro.arcgis.com/de/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm>`_
    is used by `Esri ArcGIS <https://en.wikipedia.org/wiki/ArcGIS>`_ to perform
    geographic data analysis, data conversion, data management, and map
    automation.

GIS
~~~

`QGIS <https://qgis.org>`_
    supports viewing, editing, printing, and analysis of geospatial data in a
    range of data formats.

    .. image::
       https://raster.shields.io/github/stars/qgis/QGIS
    .. image::
       https://raster.shields.io/github/contributors/qgis/QGIS
    .. image::
       https://raster.shields.io/github/commit-activity/y/qgis/QGIS
    .. image::
       https://raster.shields.io/github/license/qgis/QGIS

`GeoPandas <https://geopandas.org/en/stable/>`_
    extends the datatypes used by pandas to allow spatial operations on
    geometric types.

    .. image::
       https://raster.shields.io/github/stars/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/contributors/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/commit-activity/y/geopandas/geopandas
    .. image::
       https://raster.shields.io/github/license/geopandas/geopandas

`regionmask <https://regionmask.readthedocs.io/en/stable/>`_
    determines which geographic region each grid point belongs to.

    .. image::
       https://raster.shields.io/github/stars/regionmask/regionmask
    .. image::
       https://raster.shields.io/github/contributors/regionmask/regionmask
    .. image::
       https://raster.shields.io/github/commit-activity/y/regionmask/regionmask
    .. image::
       https://raster.shields.io/github/license/regionmask/regionmask

`Salem <https://salem.readthedocs.io/en/latest/>`_
    extends xarray to add geolocalised subsetting, masking, and plotting
    operations.

    .. image::
       https://raster.shields.io/github/stars/fmaussion/salem
    .. image::
       https://raster.shields.io/github/contributors/fmaussion/salem
    .. image::
       https://raster.shields.io/github/commit-activity/y/fmaussion/salem
    .. image::
       https://raster.shields.io/github/license/fmaussion/salem

Spatiotemporal statistics
~~~~~~~~~~~~~~~~~~~~~~~~~

`rasterstats <https://pythonhosted.org/rasterstats/>`_
    Summarizing geospatial raster datasets based on vector geometries.

    .. image::
       https://raster.shields.io/github/stars/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/contributors/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/commit-activity/y/rasterio/rasterio
    .. image::
       https://raster.shields.io/github/license/rasterio/rasterio

`eofs <https://ajdawson.github.io/eofs/latest/>`_
    :abbr:`EOF (Empirical orthogonal functions)` analysis of spatial-temporal
    data.

    .. image::
       https://raster.shields.io/github/stars/ajdawson/eofs
    .. image::
       https://raster.shields.io/github/contributors/ajdawson/eofs
    .. image::
       https://raster.shields.io/github/commit-activity/y/ajdawson/eofs
    .. image::
       https://raster.shields.io/github/license/ajdawson/eofs

Re-gridding
~~~~~~~~~~~

`Pyresample <https://pyresample.readthedocs.io/en/stable/>`_
    Resampling geospatial image data, primary for resampling in the Satpy
    library.

    .. image::
       https://raster.shields.io/github/stars/pytroll/pyresample
    .. image::
       https://raster.shields.io/github/contributors/pytroll/pyresample
    .. image::
       https://raster.shields.io/github/commit-activity/y/pytroll/pyresample
    .. image::
       https://raster.shields.io/github/license/pytroll/pyresample

`xESMF <https://xesmf.readthedocs.io/en/latest/>`_
    Universal Regridder for Geospatial Data.

    .. image::
       https://raster.shields.io/github/stars/pangeo-data/xESMF
    .. image::
       https://raster.shields.io/github/contributors/pangeo-data/xESMF
    .. image::
       https://raster.shields.io/github/commit-activity/y/pangeo-data/xESMF
    .. image::
       https://raster.shields.io/github/license/pangeo-data/xESMF

Simulation
~~~~~~~~~~

`xarray-simlab <https://xarray-simlab.readthedocs.io/en/latest/>`_
    provides both a generic framework for building computational models and a
    xarray extension for setting and running simulations.

    .. image::
       https://raster.shields.io/github/stars/xarray-contrib/xarray-simlab
    .. image::
       https://raster.shields.io/github/contributors/xarray-contrib/xarray-simlab
    .. image::
       https://raster.shields.io/github/commit-activity/y/xarray-contrib/xarray-simlab
    .. image::
       https://raster.shields.io/github/license/xarray-contrib/xarray-simlab

`Fastscape <https://fastscape.readthedocs.io/en/latest/>`_
    provides a lot a small model components to use with the xarray-simlab
    modeling framework.

    .. image::
       https://raster.shields.io/github/stars/fastscape-lem/fastscape
    .. image::
       https://raster.shields.io/github/contributors/fastscape-lem/fastscape
    .. image::
       https://raster.shields.io/github/commit-activity/y/fastscape-lem/fastscape
    .. image::
       https://raster.shields.io/github/license/fastscape-lem/fastscape

`EarthSim <https://earthsim.holoviz.org>`_
    Tools for environmental simulation.

    .. image::
       https://raster.shields.io/github/stars/holoviz-topics/EarthSim
    .. image::
       https://raster.shields.io/github/contributors/holoviz-topics/EarthSim
    .. image::
       https://raster.shields.io/github/commit-activity/y/holoviz-topics/EarthSim
    .. image::
       https://raster.shields.io/github/license/holoviz-topics/EarthSim

Visualisation
~~~~~~~~~~~~~

:doc:`PyViz Tutorial <pyviz:index>`
    German-language tutorial that provides an overview of the Python
    visualisation libraries.

    :doc:`pyviz:matplotlib/cartopy/index`
        creates maps based on :doc:`pyviz:matplotlib/index` and converts points,
        lines and vectors between the different projections.
    :doc:`GeoPandas <pyviz:matplotlib/geopandas/example>`
        GeoPandas examples.
    :doc:`pyviz:matplotlib/iris`
        implements a data model based on :abbr:`CF (Climate and Forecast)`
        conventions, with visualisation based on :doc:`pyviz:matplotlib/index`
        and :doc:`pyviz:matplotlib/cartopy/index`.
    :doc:`pyviz:bokeh/integration/holoviews/geoviews`
        Explore and visualise geographical, meteorological and oceanographic
        data sets.
    :doc:`pyviz:js/ipyleaflet`
        is a Jupyter widget for `Leaflet.js <https://leafletjs.com>`_.
    :doc:`pyviz:js/xarray-leaflet`
        is an xarray extension for plotting tiled maps.

Meteorology
~~~~~~~~~~~

`MetPy <https://unidata.github.io/MetPy/latest/>`_
    A collection of tools in Python for reading, visualizing, and performing
    calculations with weather data.

    .. image::
       https://raster.shields.io/github/stars/Unidata/MetPy
    .. image::
       https://raster.shields.io/github/contributors/Unidata/MetPy
    .. image::
       https://raster.shields.io/github/commit-activity/y/Unidata/MetPy
    .. image::
       https://raster.shields.io/github/license/Unidata/MetPy

`wrf-python <https://wrf-python.readthedocs.io/en/latest/>`_
    A collection of diagnostic and interpolation routines for use with output
    from the :abbr:`WRF-ARW (Weather Research and Forecasting)` Model.

    .. image::
       https://raster.shields.io/github/stars/NCAR/wrf-python
    .. image::
       https://raster.shields.io/github/contributors/NCAR/wrf-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/NCAR/wrf-python
    .. image::
       https://raster.shields.io/github/license/NCAR/wrf-python

`windspharm <https://ajdawson.github.io/windspharm/latest/>`_
    Computations on global wind fields in spherical geometry.

    .. image::
       https://raster.shields.io/github/stars/ajdawson/windspharm
    .. image::
       https://raster.shields.io/github/contributors/ajdawson/windspharm
    .. image::
       https://raster.shields.io/github/commit-activity/y/ajdawson/windspharm
    .. image::
       https://raster.shields.io/github/license/ajdawson/windspharm

Oceanography
~~~~~~~~~~~~

`GSW-Python <https://github.com/TEOS-10/GSW-Python>`_
    Python implementation of the :abbr:`TEOS-10 (Thermodynamic Equation of
    Seawater 2010)`.

    .. image::
       https://raster.shields.io/github/stars/TEOS-10/GSW-Python
    .. image::
       https://raster.shields.io/github/contributors/TEOS-10/GSW-Python
    .. image::
       https://raster.shields.io/github/commit-activity/y/TEOS-10/GSW-Python
    .. image::
       https://raster.shields.io/github/license/TEOS-10/GSW-Python

`PyCO2SYS <https://pyco2sys.readthedocs.io/en/latest/>`_
    Toolbox for solving the marine carbonate system and calculating related
    seawater properties.

    .. image::
       https://raster.shields.io/github/stars/mvdh7/PyCO2SYS
    .. image::
       https://raster.shields.io/github/contributors/mvdh7/PyCO2SYS
    .. image::
       https://raster.shields.io/github/commit-activity/y/mvdh7/PyCO2SYS
    .. image::
       https://raster.shields.io/github/license/mvdh7/PyCO2SYS

`pyoos <https://pypi.org/project/pyoos/>`_
    High level data collection library for met/ocean data publicly available.

    .. image::
       https://raster.shields.io/github/stars/ioos/pyoos
    .. image::
       https://raster.shields.io/github/contributors/ioos/pyoos
    .. image::
       https://raster.shields.io/github/commit-activity/y/ioos/pyoos
    .. image::
       https://raster.shields.io/github/license/ioos/pyoos

`UMWM <https://github.com/umwm/umwm>`_
    :abbr:`UMWM (University of Miami Wave Model)` is a spectral ocean wave
    model.

    .. image::
       https://raster.shields.io/github/stars/umwm/umwm
    .. image::
       https://raster.shields.io/github/contributors/umwm/umwm
    .. image::
       https://raster.shields.io/github/commit-activity/y/umwm/umwm
    .. image::
       https://raster.shields.io/github/license/umwm/umwm

Climate
~~~~~~~

`PyOWM <https://github.com/csparpa/pyowm>`_
    A Python wrapper around OpenWeatherMap web APIs.

    .. image::
       https://raster.shields.io/github/stars/csparpa/pyowm
    .. image::
       https://raster.shields.io/github/contributors/csparpa/pyowm
    .. image::
       https://raster.shields.io/github/commit-activity/y/csparpa/pyowm
    .. image::
       https://raster.shields.io/github/license/csparpa/pyowm

`climpred <https://climpred.readthedocs.io/en/stable/>`_
    Verification of weather and climate forecasts.

    .. image::
       https://raster.shields.io/github/stars/pangeo-data/climpred
    .. image::
       https://raster.shields.io/github/contributors/pangeo-data/climpred
    .. image::
       https://raster.shields.io/github/commit-activity/y/pangeo-data/climpred
    .. image::
       https://raster.shields.io/github/license/pangeo-data/climpred

`xgcm <https://xgcm.readthedocs.io/en/latest/>`_
    `General Circulation Model
    <https://en.wikipedia.org/wiki/General_circulation_model>`_ Postprocessing
    with xarray.

    .. image::
       https://raster.shields.io/github/stars/xgcm/xgcm
    .. image::
       https://raster.shields.io/github/contributors/xgcm/xgcm
    .. image::
       https://raster.shields.io/github/commit-activity/y/xgcm/xgcm
    .. image::
       https://raster.shields.io/github/license/xgcm/xgcm

`climlab <https://climlab.readthedocs.io/en/latest/>`_
    Process-oriented climate modeling.

    .. image::
       https://raster.shields.io/github/stars/climlab/climlab
    .. image::
       https://raster.shields.io/github/contributors/climlab/climlab
    .. image::
       https://raster.shields.io/github/commit-activity/y/climlab/climlab
    .. image::
       https://raster.shields.io/github/license/climlab/climlab

`aospy <https://aospy.readthedocs.io/en/stable/>`_
    Computations that use gridded climate and weather data (namely
    :file:`netCDF` files) and the management of the results.

    .. image::
       https://raster.shields.io/github/stars/spencerahill/aospy
    .. image::
       https://raster.shields.io/github/contributors/spencerahill/aospy
    .. image::
       https://raster.shields.io/github/commit-activity/y/spencerahill/aospy
    .. image::
       https://raster.shields.io/github/license/spencerahill/aospy

`OpenClimateGIS <https://ocgis.readthedocs.io/en/latest/>`_
    Geoprocessing and computation on CF-compliant climate datasets.

    .. image::
       https://raster.shields.io/github/stars/NCPP/ocgis
    .. image::
       https://raster.shields.io/github/contributors/NCPP/ocgis
    .. image::
       https://raster.shields.io/github/commit-activity/y/NCPP/ocgis
    .. image::
       https://raster.shields.io/github/license/NCPP/ocgis

`oocgcm <https://oocgcm.readthedocs.io/en/latest/>`_
    Tools for processing and analysing output of general circulation models and
    gridded satellite data.

    .. image::
       https://raster.shields.io/github/stars/lesommer/oocgcm
    .. image::
       https://raster.shields.io/github/contributors/lesommer/oocgcm
    .. image::
       https://raster.shields.io/github/commit-activity/y/lesommer/oocgcm
    .. image::
       https://raster.shields.io/github/license/lesommer/oocgcm

`pangaea <https://pangaea.readthedocs.io/en/latest/>`_
    Xarray extension for gridded land surface and weather model output.

    .. image::
       https://raster.shields.io/github/stars/erdc/pangaea
    .. image::
       https://raster.shields.io/github/contributors/erdc/pangaea
    .. image::
       https://raster.shields.io/github/commit-activity/y/erdc/pangaea
    .. image::
       https://raster.shields.io/github/license/erdc/pangaea

Glaciology
~~~~~~~~~~

`OGGM <https://oggm.org>`_
    Open source modelling framework for glaciers.

    .. image::
       https://raster.shields.io/github/stars/OGGM/oggm
    .. image::
       https://raster.shields.io/github/contributors/OGGM/oggm
    .. image::
       https://raster.shields.io/github/commit-activity/y/OGGM/oggm
    .. image::
       https://raster.shields.io/github/license/OGGM/oggm
