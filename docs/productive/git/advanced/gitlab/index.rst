.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

GitLab
======

`GitLab <https://about.gitlab.com>`_ is a web application for version management
based on Git. Later, further functions were added such as an issue tracking
system with Kanban board, a system for `Continuous Integration and Continuous
Delivery (CI/CD) <https://about.gitlab.com/solutions/continuous-integration/>`_
as well as a Wiki and Snippets. The GitLab Community Edition (CE) is developed
as open source software under the MIT licence and can be installed on-premises.

The GitLab CI tools enable automated builds and deployments without the need for
external integrations, for example building a Docker container with the Python
version of the project.

If a PaaS solution such as `Kubernetes
<https://en.wikipedia.org/wiki/Kubernetes>`_ is already in use, GitLab-CI/CD can
be used to automatically deploy, test and scale apps. The
:doc:`/productive/security` of your project can also be checked automatically.

GitLab is a completely packaged platform, while GitHub can be extended with apps
from the Marketplace. However, this does not mean that GitLab cannot be
integrated, for example with Asana, Jira, Microsoft Teams, Slack, etc.

.. seealso::
    `Visual Studio Code: GitLab Workflow
    <https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow>`_

.. toctree::
   :hidden:

   roles-permissions
   merge-requests
   ci-cd
   docker
   github-migration
   package-registry
