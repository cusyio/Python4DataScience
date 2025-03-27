.. SPDX-FileCopyrightText: 2025 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

GitLab Pages
============

With GitLab Pages, static websites can be published directly from a repository
in GitLab.

These websites are automatically deployed with :doc:`index` pipelines and
support static website generators such as
:doc:`python-basics:document/sphinx/index` `Hugo <https://gohugo.io>`_, `Jekyll
<https://jekyllrb.com>`_ or `Gatsby <https://www.gatsbyjs.com>`_. They can be
connected to custom domains and SSL/TLS certificates.

First steps
-----------

#. First create a :file:`.gitlab-ci.yml` file, for
   :doc:`python-basics:document/sphinx/index` for example with the following
   content:

   .. code-block:: yaml
      :caption: gitlab-ci.yml
      :linenos:
      :emphasize-lines: 6, 15, 18

      image: python:latest

      stages:
        - deploy

      pages:
        stage: deploy
        rules:
          - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
        before_script:
          - python -m pip install furo sphinxext-opengraph sphinx-copybutton sphinx_inline_tabs
        script:
          - cd docs && make html
        after_script:
          - mv docs/_build/html/ ./public/
        artifacts:
          paths:
            - public

   Line 6
       GitLab recognises from the job name ``pages`` that you want to provide a
       GitLab Pages website.
   Lines 15, 18
       GitLab always makes your website available from a specific folder called
       :file:`public` in your repository.

#. GitLab Pages provides default domain names based on your account or group
   name and project. Predictable URLs are generated from these. For the cusy
   GitLab instance, this is ``pages.cusy.io``. If your project is accessible at
   :samp:`https://ce.cusy.io/{GROUPNAME}/{PROJECTNAME}`, then the associated
   GitLab Pages are accessible at
   :samp:`https://{GROUPNAME}.pages.cusy.io/{PROJECTNAME}`.

   .. seealso::
      GitLab Pages also supports custom domains. You can find more information
      at `GitLab Pages custom domains
      <https://docs.gitlab.com/user/project/pages/custom_domains_ssl_tls_certification/>`_.
