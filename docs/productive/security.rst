.. SPDX-FileCopyrightText: 2023 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Security
========

In the previous chapters we have already given some hints that enable a safer
operation. Here we want to summarise and expand the individual elements. In
doing so, we will be guided by the `OpenSSF
Scorecard <https://securityscorecards.dev/>`_. Alternatively, you can also
follow :ref:`open_chain`.

.. _check-vulnerabilities:

Check vulnerabilities
---------------------

Risk: High

This check determines whether the project has open, unfixed vulnerabilities in
its own code base or in its dependencies. An open vulnerability can be easily
exploited and should be closed as soon as possible.

For such a check, you can use for example `uv-secure
<https://pypi.org/project/uv-secure/>`_. Alternatively, you can use `osv
<https://pypi.org/project/osv/>`_ or `pip-audit
<https://pypi.org/project/pip-audit/>`_, which uses the `Open Source
Vulnerability Database <https://osv.dev>`_.

If a vulnerability is found in a dependency, you should update to a
non-vulnerable version; if no update is available, you should consider removing
the dependency.

If you believe that the vulnerability does not affect your project, an
:file:`osv-scanner.toml` file can be created for ``osv``, including the ID to
ignore and a reason, for example:

.. code-block:: toml

   [[IgnoredVulns]]
   id = "GO-2022-1059"
   # ignoreUntil = 2022-11-09 # Optional exception expiry date
   reason = "No external http servers are written in Go lang."

Maintenance
-----------

.. _automatic-update:

Are the dependencies updated automatically?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: High

Outdated dependencies make a project vulnerable to attacks on known
vulnerabilities. Therefore, the process of updating dependencies should be
automated by checking for outdated or insecure requirements and updating them if
necessary. You can use `dependabot <https://github.com/dependabot>`_ or `Safety
CLI <https://safetycli.com>`_ for this purpose.

You can also update your :doc:`/productive/envs/uv/index` environments
automatically.

.. seealso::
   * :ref:`Update uv.lock <python-basics:update-uv-lock>`

Are the dependencies still maintained?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: High

This indicates possible unpatched security vulnerabilities. Therefore, it should
be checked regularly whether a project has been archived. Conversely, the OSSF
scorecard assumes that with at least one commit a week for 90 days, the project
is very actively maintained. However, a lack of active maintenance is not
necessarily always a problem: smaller utilities in particular usually do not
need to be maintained, or only very rarely. So a lack of active maintenance only
tells you that you should investigate the situation more closely.

You can also display the activities of a project with badges, for example:

.. image:: https://img.shields.io/github/commit-activity/y/veit/python4datascience
   :alt: Annual commit activity
.. image:: https://img.shields.io/github/commit-activity/m/veit/python4datascience
   :alt: Monthly commit activity
.. image:: https://img.shields.io/github/commit-activity/w/veit/python4datascience
   :alt: Weekly commit activity

Is there a safety concept for the project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: Medium

Ideally, a :file:`SECURITY.md` or similar file should have been published with
the project. This file should contain information

* how a security vulnerability can be reported without it becoming publicly
  visible,
* on the procedure and schedule for disclosing the vulnerability,
* to links, for example  URLs and emails, where support can be requested.

.. seealso::
   * `Guide to implementing a coordinated vulnerability disclosure process for
     open source projects
     <https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md>`_
   * `Adding a security policy to your repository
     <https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository>`_
   * `Runbook
     <https://github.com/ossf/oss-vulnerability-guide/blob/main/runbook.md>`_

Does the project contain a usable licence?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: Low

A :doc:`license </productive/licensing>` indicates how the source code may or
may not be used. The absence of a licence complicates any kind of security
review or audit and poses a legal risk for potential use.

OSSF-Scorecard uses the `GitHub License API
<https://docs.github.com/en/rest/licenses/licenses?apiVersion=2022-11-28#get-the-license-for-a-repository>`_
for projects hosted on GitHub, otherwise it uses its own heuristics to detect a
published license file. Files in a :file:`LICENSES` directory should be named
with their :ref:`SPDX <standard_format_licensing>` licence identifier followed
by an appropriate file extension as described in the :ref:`REUSE <reuse>`
specification.

Are the best practices of the :abbr:`OpenSSF (Open Source Security Foundation)` being followed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: Low

The `Open Source Security Foundation (OpenSSF) Best Practices Program
<https://github.com/ossf/wg-best-practices-os-developers/>`_ includes a set of
security-oriented best practices for open source software development:

* the vulnerability reporting procedure is published on the project page
* a working build system automatically rebuilds the software from source code
* a general policy that tests are added to an automated test suite when
  important new features are added
* various cryptography criteria are met, if applicable
* at least one static code analysis tool applied to each planned major
  production release

You can also get a corresponding badge with the `OpenSSF Best Practices Badge Program <https://www.bestpractices.dev/en>`_.

Continuous testing
------------------

Are CI tests carried out in the project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: Low

Before code is merged into pull or merge requests, tests should be performed to
help detect errors early and reduce the number of vulnerabilities in a project.

Does the project use fuzzing tools?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

risk: Medium

Fuzzing or fuzz testing passes unexpected or random data to your programme to
detect bugs. Regular fuzzing is important to detect vulnerabilities that can be
exploited by others, especially since fuzzing can also be used in an attack to
find the same vulnerabilities.

* Does your project use `fuzzing <https://owasp.org/www-community/Fuzzing>`_?
* Is the name of the repository included in the `OSS fuzz
  <https://github.com/google/oss-fuzz>`_ project list?
* Is `ClusterFuzzLite <https://google.github.io/clusterfuzzlite/>`_ used in the
  repository?
* Are custom language-specific fuzzing features present in the repository, for
  example with `atheris <https://pypi.org/project/atheris/>`_ or `OneFuzz
  <https://github.com/microsoft/onefuzz>`_?

Does your project use static code analysis tools?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: Medium

`Static code analysis <https://en.wikipedia.org/wiki/Static_program_analysis>`_
tests the source code before the application is executed. This can prevent known
bug classes from being accidentally introduced into the code base.

To check for vulnerabilities, you can use `bandit
<https://github.com/PyCQA/bandit>`_, which you can also integrate into your
:file:`.pre-commit-hooks.yaml`:

.. code-block:: yaml

    repos:
    - repo: https://github.com/PyCQA/bandit
      rev: '1.7.5'
      hooks:
      - id: bandit

You can also use :doc:`/productive/qa/pysa` for `taint
<https://en.wikipedia.org/wiki/Taint_checking>`_ analyses.

For GitHub repositories you can also use `CodeQL <https://codeql.github.com>`_;
see `codeql-action <https://github.com/github/codeql-action/blob/main/README.md#usage>`_.

Risk assessment of the source code
----------------------------------

Is the project free of checked-in binaries?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: High

Generated executables in the source code repository (for example  Java
:file:`.class` files, Python :file:`.pyc` files) increase risk because they are
difficult to verify, so they may be out of date or maliciously tampered with.
These problems can be countered with verified, reproducible builds, but their
executables should not end up back in the source code repository.

Is the development process vulnerable to the introduction of malicious code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: High

With :ref:`protected Git branches <protected_branches>`, rules can be defined
for the adoption of changes in standard and release branches, for example
automated `static code analyses
<https://en.wikipedia.org/wiki/Static_program_analysis>`_ with :doc:`qa/flake8`,
:doc:`qa/pysa`, :doc:`qa/wily` and :ref:`code reviews <code_reviews>` via
:doc:`merge requests <git/advanced/gitlab/merge-requests>`.

.. seealso::
   * `Reproducible Builds <https://reproducible-builds.org>`_
   * `Python 3.12.0 from a supply chain security perspective
     <https://sethmlarson.dev/security-developer-in-residence-weekly-report-13>`_
   * `Defending against the PyTorch supply chain attack PoC
     <https://sethmlarson.dev/security-developer-in-residence-weekly-report-25>`_

.. _code_reviews:

Are code reviews performed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: High

Code reviews can detect unintentional vulnerabilities or possible introduction
of malicious code. Possible attacks can be detected in which the account of a
team member has been infiltrated.

Does the project involve people from several organisations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: Low

This is taken as an indication of a lower number of trustworthy code reviewers.
For this purpose, you can search for different entries in the * Company* field
in the profiles. At least three different companies in the last 30 commits are
desirable, whereby each of these team members should have made at least five
commits.

Risk assessment of the builds
-----------------------------

.. _lock-dependencies:

Are dependencies declared and fixed in the project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Risk: Medium

In your project, dependencies used during the build and release process should
be pinned. A pinned dependency should be explicitly set to a specific hash and
not just to a mutable version or version range.

:doc:`envs/spack/index` writes these hashes for the respective environment in
:ref:`spack_lock`, :doc:`envs/uv/index` in :ref:`uv_lock`.

.. tip::
   Üblicherweise verwalte ich diese Dateien jedoch nur bei
   :doc:`python-basics:packs/apps` in :doc:`git/index`. Bei
   :doc:`python-basics:libs/index` schränke ich üblicherweise lediglich den
   Versionsbereich der Abhängigkeiten in der :file:`pyproject.toml`-Datei ein.

:doc:`envs/spack/index` writes these hashes for the respective environment in
:ref:`spack_lock`, :doc:`envs/uv/index` in :ref:`uv_lock`. These files should
therefore also be checked in with the source code.

This can reduce the following security risks for
:doc:`python-basics:packs/apps`:

* Testing and deployment are done with the same software, which reduces
  deployment risks, simplifies debugging and enables reproducibility.
* Compromised dependencies do not undermine the security of the project.
* Substitution attacks, :abbr:`i.e. (id est)` attacks that aim to confuse
  dependencies, can thus be countered.

However, fixing dependencies should not prevent software updates. You can
reduce this risk by

* automated tools that notify you when dependencies in your project are out of
  date
* update applications that lock dependencies quickly.
