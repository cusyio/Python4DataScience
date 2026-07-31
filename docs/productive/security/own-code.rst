.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Your own code
=============

Attacks on the supply chain do not only stem from :doc:`dependencies
<dependencies>`; your own code can also provide points of entry. A PyPI token
hard-coded into the source code, once uploaded to a public repository, provides
everything needed to launch an attack, compromise your account and publish
malicious packages under your name. Apart from secrets, common security flaws
are often hidden in everyday coding patterns that may initially appear harmless
during a code review and can be overlooked by humans. Detecting these using a
linter is the first line of defence.

The eternal secret
------------------

Leaked credentials are the starting point for many security breaches in the
supply chain. An exposed :term:`PyPI` token makes it possible to publish
versions of your packages containing backdoors. An exposed database URL makes it
possible to steal data. And yet, this pattern is all too common. It is better to
use environment variables:

.. code-block:: python

   import os

   DATABASE_KEY = os.environ["DB_KEY"]
   DATABASE_URL = os.environ["DB_URL"]

.. warning::
   Git never forgets: once you’ve managed a secret via Git, it remains in your
   repository’s history forever. Simply deleting it in a later commit doesn’t
   really help. Anyone with access to the repository can extract these
   credentials. In attacks, the Git history is often scoured for secrets first,
   and a PyPI token or cloud credentials that have been exposed are often the
   first step in a supply chain compromise.

Cryptographic vulnerabilities
-----------------------------

Other common security vulnerabilities include cryptographic weaknesses such as
`MD5 <https://en.wikipedia.org/wiki/MD5>`_ and `SHA-1
<https://en.wikipedia.org/wiki/SHA-1>`_. MD5 collisions were first demonstrated
in 2004 and SHA-1 collisions in 2017. This means that collisions can be
generated using different inputs that produce the same hash value. This enables
the forgery of certificates, the manipulation of downloads or the circumvention
of integrity checks. Therefore, do not use either of these algorithms for
security purposes; instead, use `SHA-256 <https://en.wikipedia.org/wiki/SHA-2>`_
or better:

.. code-block:: python

   import hashlib

   digest = hashlib.sha256(payload).hexdigest()

Stalled connections
-------------------

This may be subtle, but it is nonetheless dangerous, as a slow server can bring
your process to a standstill indefinitely. An attack via such a server, with
which your application communicates, can bring every request to a standstill,
exhaust your thread pool and trigger a denial-of-service attack. Your entire
application will then grind to a halt because you forgot to specify a parameter.
You should therefore always specify a timeout:

.. code-block:: pycon

   >>> import httpx
   >>> r = httpx.get("https://httpbin.org/get", timeout=30)
   httpx.ReadTimeout: The read operation timed out

.. _bandit:

Detect security vulnerabilities with Ruff
-----------------------------------------

:doc:`../qa/ruff` is a fast Python linter that includes comprehensive security
rules from :ref:`Bandit <bandit>`:

.. code-block:: console

   $ uvx ruff check --select S .

.. seealso::
   Further information can be found in the `Ruff security rules documentation
   <https://docs.astral.sh/ruff/rules/#flake8-bandit-s>`_.

For future checks, you can configure ``ruff`` in the :file:`pyproject.toml`
file:

.. code-block:: toml

   [tool.ruff]
   lint.select = ["S"]

The ``["S"]`` security rules, which use Bandit checks, detect hard-coded
secrets, weak encryption and insecure deserialisation. Ruff runs in less than a
second, so you can run it whilst typing in your IDE and before every commit. All
three vulnerabilities mentioned above are detected, along with many more,
including:

+--------+-----------------------------------------------------------------------+
| Rule   | Description                                                           |
+--------+-----------------------------------------------------------------------+
| `S105`_| Hard-coded secrets                                                    |
+--------+-----------------------------------------------------------------------+
| `S301`_| :doc:`/data-processing/serialisation-formats/pickle/index` and other  |
|        | insecure deserialisation                                              |
+--------+-----------------------------------------------------------------------+
| `S307`_| Use of :func:`eval` with untrusted input                              |
+--------+-----------------------------------------------------------------------+
| `S113`_| Missing timeouts                                                      |
+--------+-----------------------------------------------------------------------+
| `S324`_| Weak cryptography, such as MD5 collisions                             |
+--------+-----------------------------------------------------------------------+
| `S608`_| SQL injection via string formatting                                   |
+--------+-----------------------------------------------------------------------+

.. seealso::
   * `flake8-bandit (S) <https://docs.astral.sh/ruff/rules/#flake8-bandit-s>`_
   * `lint.flake8-bandit
     <https://docs.astral.sh/ruff/settings/#lintflake8-bandit>`_

You can also integrate Bandit into Jupyter Notebooks, :abbr:`IDEs (Integrated
Development Wnvironments)` and :doc:`../git/advanced/hooks/prek`.

You can also use :doc:`../qa/pysa` for `taint analysis
<https://en.wikipedia.org/wiki/Taint_checking>`_.

For GitHub repositories, you can alternatively use `CodeQL
<https://codeql.github.com>`_; see also `codeql-action
<https://github.com/github/codeql-action/blob/main/README.md#usage>`_.

Trusted publishing
------------------

In an earlier section, we’ve already provided some guidance on how to secure the
publication of Python packages on :term:`PyPI`:

.. seealso::
   * :ref:`secure-release-workflow`
   * :ref:`add_2fa`

.. seealso::
   * `Publishing package distribution releases using GitHub Actions CI/CD
     workflows
     <https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`_

.. _S105: https://docs.astral.sh/ruff/rules/hardcoded-password-string/
.. _S301: https://docs.astral.sh/ruff/rules/suspicious-pickle-usage/
.. _S307: https://docs.astral.sh/ruff/rules/suspicious-eval-usage/
.. _S113: https://docs.astral.sh/ruff/rules/request-without-timeout/
.. _S324: https://docs.astral.sh/ruff/rules/hashlib-insecure-hash-function/
.. _S608: https://docs.astral.sh/ruff/rules/hardcoded-sql-expression/
.. _S608: https://docs.astral.sh/ruff/rules/hardcoded-sql-expression/
