.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Protocol Buffers (Protobuf)
===========================

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| \+    | Protobuf allows you to define data structures in      |
|                       |       | ``*.proto`` files. Protobuf supports many primitive   |
|                       |       | types, which can be combined into nested classes.     |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | +-    | Protobuf is a strongly typed flexible standard.       |
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | ++    | Built-in IDL compiler                                 |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | ++    | The protobuf format is well supported by many         |
|                       |       | programming languages.                                |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | -\-   | Protobuf is not designed to be human readable.        |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | ++    | Protobuf is very fast, especially in C++.             |
+-----------------------+-------+-------------------------------------------------------+
| File size             | ++    | Protobuf is the most compact format.                  |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    * `Home <https://protobuf.dev>`__
    * `GitHub <https://github.com/protocolbuffers/protobuf>`__
    * `Language Guide (proto3)
      <https://protobuf.dev/programming-guides/proto3/>`_
    * Buf

      * `Home <https://buf.build/>`__
      * `Docs <https://buf.build/docs/introduction>`_
      * `GitHub <https://github.com/bufbuild/buf>`__

    * :doc:`../apis/grpc/index`
