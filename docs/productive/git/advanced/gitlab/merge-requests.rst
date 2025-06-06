.. SPDX-FileCopyrightText: 2022 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Merge requests
==============

Merge requests allow you to check source code changes into a branch. When you
open a merge request, you can visualise the code changes before merging and
work on them together. Merge requests contain:

* A description of the request
* Code changes and code reviews
* Information about :doc:`CI/CD-Pipelines <ci-cd/index>`
* discussion posts
* the list of commits

.. tip::
   If you have created a fork, do not issue the merge requests from the ``main``
   branch. This avoids the following difficulties:

   * You can then work on several merge requests instead of just one.
   * If your merge request has been accepted, you can no longer make a ``git
     pull`` because you have conflicting commits.
   * If the ``main`` branch of the target repository is protected, people with
     the maintainer role can no longer edit the merge request. All changes would
     then have to go through you.

.. seealso::
   * `Merge requests <https://docs.gitlab.com/ee/user/project/merge_requests/>`_

Merge request workflows
-----------------------

#. You check out a new branch and submit your changes through a merge request.
#. You gather feedback from your team.
#. You work on the implementation and optimise the code with `code quality
   reports <https://docs.gitlab.com/ee/ci/testing/code_quality.html>`_.
#. You verify your changes with `reports from unit tests
   <https://docs.gitlab.com/ee/ci/testing/unit_test_reports.html>`_ in
   :doc:`GitLab CI/CD <ci-cd/index>`.
#. You avoid using dependencies whose licence is incompatible with your project
   with :ref:`licence compliance reports <reuse-in-gitlab-ci>`.
#. You request `approval
   <https://docs.gitlab.com/ee/user/project/merge_requests/approvals/index.html>`_
   of your changes.
#. When the merge request is approved, :doc:`GitLab CI/CD <ci-cd/index>` will
   deploy the changes to the ``production`` environment.
