.. SPDX-FileCopyrightText: 2023 cusy GmbH
..
.. SPDX-License-Identifier: BSD-3-Clause

Security
========

As of July 2026, :term:`PyPI` hosts over 750,000 packages, and this number is
growing daily. An average Python project includes dozens of additional
dependencies – packages that you have never explicitly chosen, but on which you
nevertheless rely because your dependencies require them. When you install
pandas in your application, you get more than just pandas. The complete
dependency tree looks like this:

.. code-block:: console

   $ uv add pandas
   $ uv pip tree
   myapp v0.1.0
   └── pandas v3.0.5
       ├── numpy v2.5.1
       └── python-dateutil v2.9.0.post0
           └── six v1.17.0

Although you only wanted to add one package (``pandas``), you ended up with four
without being asked. Even if just one of these transitive packages – which you
never explicitly installed – were to contain a security vulnerability, your
entire application would be at risk. This greatly increases the attack surface
compared to what you yourself specified in ``dependencies``.

Here are just a few recent attacks on the software supply chain:

LiteLLM/Telnyx
    In March this year, following the disclosure of an API token due to an
    `exploited trivy dependency
    <https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/>`_,
    versions of the `litellm <https://pypi.org/project/litellm/>`_ and `telnyx
    <https://pypi.org/project/telnyx/>`_ packages were published on :term:`PyPI`
    that contained malware designed to steal login credentials. The malware was
    executed upon installation, collected sensitive login credentials and files,
    and forwarded them to a remote API.

    .. seealso::
       `Incident Report: LiteLLM/Telnyx supply-chain attacks, with guidance
       <https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/>`_

Email phishing attack targeting PyPI users
    In April 2026, the wave of phishing attacks – which exploit domain name
    confusion and involve the sending of emails that appear legitimate –
    continues. This is the same attack that occurred in June 2025 and targets
    many other open-source repositories, albeit with a different domain name.

    .. seealso::
       `PyPI Users Email Phishing Attack
       <https://blog.pypi.org/posts/2025-07-28-pypi-phishing-attack/>`_

Shai-Hulud
    In November 2025, an attack on the `npm <https://www.npmjs.com/>`_ ecosystem
    escalated, exploiting compromised accounts to publish malicious packages.
    This campaign, known as Shai-Hulud, targeted a large number of JavaScript
    packages and stole credentials to spread further. Although :term:`PyPI`
    itself was not exploited, some PyPI login credentials were exposed in
    compromised repositories.

    .. seealso::
       `PyPI and Shai-Hulud: Staying Secure Amid Emerging Threats
       <https://blog.pypi.org/posts/2025-11-26-pypi-and-shai-hulud/>`_

.. _token_exfiltration:

Token Exfiltration
    In September 2025, code was injected into GitHub Actions workflows in over
    570 repositories, resulting in the theft of more than 3,300 secrets,
    including :term:`PyPI` and npm tokens as well as AWS access keys. PyPI
    blocked all the stolen tokens and urged all users to switch to
    :ref:`trusted_publishers`.

    .. seealso::
       `Token Exfiltration Campaign via GitHub Actions Workflows
       <https://blog.pypi.org/posts/2025-09-16-github-actions-token-exfiltration/>`_

ZIP parser confusion attacks
    In August 2025, :term:`PyPI` introduced restrictions designed to prevent
    confusion arising from different implementations of the ZIP parser in
    installation and verification programmes for Python packages. :term:`uv`
    exhibited different extraction behaviour to many Python-based installation
    programmes that use :mod:`zipfile`.

    .. seealso::
       `uv security advisory: ZIP payload obfuscation
       <https://astral.sh/blog/uv-security-advisory-cve-2025-54368>`_

.. _ultralytics:

Ultralytics
    In December 2024, `ultralytics <https://pypi.org/project/ultralytics/>`_
    fell victim to a supply-chain attack in which the project’s GitHub Actions
    workflows were first compromised, followed by its PyPI API tokens. No
    vulnerability in :term:`PyPI` was exploited to carry out this attack.

    .. seealso::
       `Supply-chain attack analysis: Ultralytics
       <https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/>`_

These are not theoretical attacks. They have occurred in real-world projects
with millions of users. If you discover a malicious package on PyPI, you can
report it via `PyPI’s security reporting system <https://pypi.org/security/>`_.

In June 2026, Seth Larson, a member of the `Python Security Response Team
<https://devguide.python.org/security/psrt/>`_, published a chart showing the
annual trend in security vulnerabilities published by Python, which indicates
that the number is expected to triple in 2026:

.. figure:: python-cve-per-year.png
   :alt: Number of CVEs published annually by Python. It is expected that around
         65 CVEs will be published in 2026.

   Source: https://mastodon.social/@sethmlarson/116680832573268456

However, this merely reflects the results and does not provide an overview of
the reports received. Many of these are closed and treated instead as
non-security-related error reports; others are closed as neither security nor
error reports. Here is the number of reports created since July 2024 relating to
GitHub security advisories:

.. figure:: ghsas-by-month.webp
   :alt: Chart showing new security reports. From 2024, single-digit numbers or
         zero per month, rising to around 40 in 2026.

   Source: Hugo van Kemenade: `Security: line goes up
   <https://hugovk.dev/blog/2026/security-line-goes-up/>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    own-code
    dependencies
    environments
    sbom
