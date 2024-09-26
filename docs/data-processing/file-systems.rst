.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

File systems
============

High-level APIs
---------------

`PyFilesystem <https://www.pyfilesystem.org>`_
    works with files and directories in archives, in storages, in the cloud,
    :abbr:`etc (et cetera)`.

    .. image::
       https://raster.shields.io/github/stars/pyfilesystem/pyfilesystem2
    .. image::
       https://raster.shields.io/github/contributors/pyfilesystem/pyfilesystem2
    .. image::
       https://raster.shields.io/github/commit-activity/y/pyfilesystem/pyfilesystem2
    .. image::
       https://raster.shields.io/github/license/pyfilesystem/pyfilesystem2

    Integrated file systems:

    * `AppFS <https://www.pyfilesystem.org/page/appfs/>`_ for predefined storage
      locations in operating systems where applications can store data
    * `FTPFS <https://www.pyfilesystem.org/page/ftpfs/>`_ for working with FTP
      servers
    * `MemoryFS <https://www.pyfilesystem.org/page/memoryfs/>`_ for caches, temporary data storage, unit tests, :abbr:`etc. (et cetera)` that exist in the
      working memory
    * `MountFS <https://www.pyfilesystem.org/page/mountfs/>`_ for a virtual file
      system that can mount other file systems
    * `MultiFS <https://www.pyfilesystem.org/page/multifs/>`_ for a virtual file
      system that combines other file systems
    * `OSFS <https://www.pyfilesystem.org/page/osfs/>`_ for the OS file system
    * `TarFS <https://www.pyfilesystem.org/page/tarfs/>`_ reads and writes
      compressed tar archives
    * `TempFS <https://www.pyfilesystem.org/page/tempfs/>`_ contains temporary
      data
    * `ZipFS <https://www.pyfilesystem.org/page/zipfs/>`_ reads and writes Zip
      files

    File systems of the PyFilesystem organization on GitHub:

    * `DropBoxFS <https://www.pyfilesystem.org/page/dropboxfs/>`_
    * `S3FS <https://www.pyfilesystem.org/page/s3fs/>`_
    * `WebDavFS <https://www.pyfilesystem.org/page/index-of-filesystems/>`_

    File systems from third-party developers:

    * `fs_basespace <https://github.com/emedgene/fs_basespace>`_ for read access
      to the Illumina Basespace
    * `fs.dropboxfs <https://github.com/rkhwaja/fs.dropboxfs>`_ for Dropbox
    * `fs.imapfs <https://github.com/Maggi-Andrea/fs.imapfs>`_ for Imap
    * `fs.googledrivefs <https://github.com/rkhwaja/fs.googledrivefs>`_ for
      Google Drive
    * `fs.onedrivefs <https://github.com/rkhwaja/fs.onedrivefs>`_ for OneDrive
    * `fs.smbfs <https://github.com/althonos/fs.smbfs>`_ for Samba
    * `fs.sshfs <https://github.com/althonos/fs.sshfs>`_ for  SSH with
      :ref:`paramiko`
    * `mp-fs-wsgidav <https://github.com/mikespub-org/mp-fs-wsgidav>`_ for
      WsgiDAV

.. _fsspec:

`fsspec <https://filesystem-spec.readthedocs.io/en/latest/>`__
    Unified Python interface for many local, remote and embedded file systems
    and byte storages. If you already use :doc:`/workspace/pandas/index`,
    :doc:`/data-processing/intake/index`, :doc:`/performance/dask` or :doc:`DVC
    </productive/dvc/index>` in your project, for example, ``fsspec`` is already
    available.

    .. image::
       https://raster.shields.io/github/stars/fsspec/filesystem_spec
    .. image::
       https://raster.shields.io/github/contributors/fsspec/filesystem_spec
    .. image::
       https://raster.shields.io/github/commit-activity/y/fsspec/filesystem_spec
    .. image::
       https://raster.shields.io/github/license/fsspec/filesystem_spec

    In addition to the `integrated implementations
    <https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations>`_,
    there are also many extensions, for example:

    * `abfs <https://github.com/fsspec/adlfs>`_ for the Azure Blob Service
    * `adl <https://github.com/fsspec/adlfs>`_ for the Azure DataLake storage
    * `alluxiofs <https://github.com/fsspec/alluxiofs>`_ for the Alluxio
      distributed cache
    * `boxfs <https://github.com/IBM/boxfs>`_ for access to Box file storage
    * `dropbox <https://github.com/fsspec/dropboxdrivefs>`_ for access to
      Dropbox shares
    * `dvc <https://github.com/iterative/dvc>`_ for accessing a DVC repository
      as a file system
    * `gcsfs <https://github.com/fsspec/gcsfs>`_ for Google Cloud Storage
    * `gdrive <https://github.com/fsspec/gdrivefs>`_ for access to Google Drive
      and shares
    * `huggingface_hub
      <https://huggingface.co/docs/huggingface_hub/main/en/guides/hf_file_system>`_
      for access to the Hugging Face Hub file system
    * `lakefs <https://github.com/aai-institute/lakefs-spec>`_ for lakeFS
      datalakes
    * `ocifs <https://github.com/oracle/ocifs>`_ for access to the Oracle Cloud
      Object Storage
    * `ossfs <https://github.com/fsspec/ossfs>`_ for the Alibaba Cloud (Aliyun)
      object storage system (OSS)
    * `p9fs <https://github.com/pbchekin/p9fs-py>`_ for :abbr:`9P (Plan 9
      Filesystem Protocol)` servers
    * `s3fs <https://github.com/fsspec/s3fs>`__ for Amazon S3 and other
      compatible storage
    * `wandbfs <https://github.com/jkulhanek/wandbfs>`_ for accessing Wandb data
    * `webdav4 <https://github.com/skshetry/webdav4>`_ for WebDAV

.. seealso::
   `Rclone <https://rclone.org>`_ is a command line programme for managing
   files on cloud storage. It supports more than 70 cloud storages. You can find
   an example of its use with Python in `rclone.py
   <https://github.com/rclone/rclone/blob/master/librclone/python/rclone.py>`_.

Specialised libraries
---------------------

`PyArrow <https://arrow.apache.org/docs/python/>`_
    Apache Arrow Python bindings for the `Hadoop Distributed File System (HDFS)
    <https://arrow.apache.org/docs/python/filesystems.html#hadoop-distributed-file-system-hdfs>`_
    and other :ref:`fsspec`-compatible file systems.

    .. seealso::
       `Using fsspec-compatible filesystems with Arrow
       <https://arrow.apache.org/docs/python/filesystems.html#filesystem-fsspec>`_

    .. image::
       https://raster.shields.io/github/stars/apache/arrow
    .. image::
       https://raster.shields.io/github/contributors/apache/arrow
    .. image::
       https://raster.shields.io/github/commit-activity/y/apache/arrow
    .. image::
       https://raster.shields.io/github/license/apache/arrow

.. _paramiko:

`paramiko <https://www.paramiko.org>`__
    Python implementation of the SSHv2 protocol, which offers both client and
    server functions. It forms the basis for the high-level SSH library  `Fabric
    <https://www.fabfile.org>`_.

    .. image::
       https://raster.shields.io/github/stars/paramiko/paramiko
    .. image::
       https://raster.shields.io/github/contributors/paramiko/paramiko
    .. image::
       https://raster.shields.io/github/commit-activity/y/paramiko/paramiko
    .. image::
       https://raster.shields.io/github/license/paramiko/paramiko

`boto3 <https://aws.amazon.com/de/sdk-for-python/>`_
    AWS SDK for Python facilitates integration with Amazon S3, Amazon EC2,
    Amazon DynamoDB and others.

    .. image::
       https://raster.shields.io/github/stars/boto/boto3
    .. image::
       https://raster.shields.io/github/contributors/boto/boto3
    .. image::
       https://raster.shields.io/github/commit-activity/y/boto/boto3
    .. image::
       https://raster.shields.io/github/license/boto/boto3

`azure-storage-blob <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob>`_
    Azure Storage Blobs client library for Python.

    .. image::
       https://raster.shields.io/github/stars/Azure/azure-sdk-for-python
    .. image::
       https://raster.shields.io/github/contributors/Azure/azure-sdk-for-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/Azure/azure-sdk-for-python
    .. image::
       https://raster.shields.io/github/license/Azure/azure-sdk-for-python

`oss2 <https://pypi.org/project/oss2/>`_
    Python SDK for the Alibaba Cloud Object Storage.

    .. image::
       https://raster.shields.io/github/stars/aliyun/aliyun-oss-python-sdk
    .. image::
       https://raster.shields.io/github/contributors/aliyun/aliyun-oss-python-sdk
    .. image::
       https://raster.shields.io/github/commit-activity/y/aliyun/aliyun-oss-python-sdk
    .. image::
       https://raster.shields.io/github/license/aliyun/aliyun-oss-python-sdk

`minio <https://min.io/docs/minio/linux/developers/python/minio-py.html>`_
    MinIO Python Client SDK for Amazon S3 compatible cloud storage.

    .. image::
       https://raster.shields.io/github/stars/minio/minio-py
    .. image::
       https://raster.shields.io/github/contributors/minio/minio-py
    .. image::
       https://raster.shields.io/github/commit-activity/y/minio/minio-py
    .. image::
       https://raster.shields.io/github/license/minio/minio-py

`PyDrive2 <https://docs.iterative.ai/PyDrive2/>`_
    Python wrapper library of the `google-api-python-client
    <https://github.com/google/google-api-python-client>`_, which simplifies
    many common Google Drive API tasks.

    .. image::
       https://raster.shields.io/github/stars/iterative/PyDrive2
    .. image::
       https://raster.shields.io/github/contributors/iterative/PyDrive2
    .. image::
       https://raster.shields.io/github/commit-activity/y/iterative/PyDrive2
    .. image::
       https://raster.shields.io/github/license/iterative/PyDrive2

`Qcloud COSv5 SDK <https://www.tencentcloud.com/document/product/436/12268>`_
    Python SDK for the Tencent Cloud Object Storage (COS).

    .. image::
       https://raster.shields.io/github/stars/tencentyun/cos-python-sdk-v5
    .. image::
       https://raster.shields.io/github/contributors/tencentyun/cos-python-sdk-v5
    .. image::
       https://raster.shields.io/github/commit-activity/y/tencentyun/cos-python-sdk-v5
    .. image::
       https://raster.shields.io/github/license/tencentyun/cos-python-sdk-v5

`linode_api4 <https://linode-api4.readthedocs.io/en/latest/>`_
    Python bindings for the Linode API v4.

    .. image::
       https://raster.shields.io/github/stars/linode/linode_api4-python
    .. image::
       https://raster.shields.io/github/contributors/linode/linode_api4-python
    .. image::
       https://raster.shields.io/github/commit-activity/y/linode/linode_api4-python
    .. image::
       https://raster.shields.io/github/license/linode/linode_api4-python

`airfs <https://jgoutin.dev/airfs/>`_
    brings standard Python I/O to various storages (such as Alibaba Cloud OSS,
    Amazon Web Services S3, GitHub, Microsoft Azure Blobs Storage and Files
    Storage, OpenStack Swift/Object Store.

    .. image::
       https://raster.shields.io/github/stars/JGoutin/airfs
    .. image::
       https://raster.shields.io/github/contributors/JGoutin/airfs
    .. image::
       https://raster.shields.io/github/commit-activity/y/JGoutin/airfs
    .. image::
       https://raster.shields.io/github/license/JGoutin/airfs

`yandex-s3 <https://pypi.org/project/yandex-s3/>`_
    Asyncio-compatible SDK for Yandex Object Storage.

    .. image::
       https://raster.shields.io/github/stars/mrslow/yandex-s3
    .. image::
       https://raster.shields.io/github/contributors/mrslow/yandex-s3
    .. image::
       https://raster.shields.io/github/commit-activity/y/mrslow/yandex-s3
    .. image::
       https://raster.shields.io/github/license/mrslow/yandex-s3

Dormant projects
----------------

`PyDrive <https://pypi.org/project/PyDrive/>`_
    Python wrapper library of the `google-api-python-client
    <https://github.com/google/google-api-python-client>`_, which simplifies
    many common Google Drive API tasks.

    .. image::
       https://raster.shields.io/github/stars/googlearchive/PyDrive
    .. image::
       https://raster.shields.io/github/contributors/googlearchive/PyDrive
    .. image::
       https://raster.shields.io/github/commit-activity/y/googlearchive/PyDrive
    .. image::
       https://raster.shields.io/github/license/googlearchive/PyDrive

`digital-ocean-spaces <https://pypi.org/project/digital-ocean-spaces/>`_
    Python client for Digital Ocean Spaces with an inbuilt shell.

    .. image::
       https://raster.shields.io/github/stars/ChariotDev/digital-ocean-spaces
    .. image::
       https://raster.shields.io/github/contributors/ChariotDev/digital-ocean-spaces
    .. image::
       https://raster.shields.io/github/commit-activity/y/ChariotDev/digital-ocean-spaces
    .. image::
       https://raster.shields.io/github/license/ChariotDev/digital-ocean-spaces
