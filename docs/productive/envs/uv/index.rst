``uv``
======

:term:`uv` is an extremely fast Python package and project manager.

Both the :ref:`installation of uv  <python-basics:uv>` and the creation of file
structures for :ref:`libraries <python-basics:uv-package-structure>` or
:doc:`python-basics:packs/apps` are already described in our
:doc:`python-basics:index` tutorial.

.. _inline-script-metadata:

Inline script metadata
----------------------

However, ``uv`` is also ideal for individual Python scripts that contain `inline
script metadata
<https://packaging.python.org/en/latest/specifications/inline-script-metadata/>`_,
for example:

.. code-block:: python
   :caption: app.py

    #!/usr/bin/env -S uv run
    # /// script
    # requires-python = ">=3.12"
    # dependencies = [
    #     "rich",
    # ]
    # ///
    import rich

If the permissions for the  :file:`app.py` file are executable, for example with
``chmod 755``, you can run it on any computer with ``uv`` installed:

.. code-block:: console

   ./app.py

A separate isolated environment is automatically created with the correct Python
version and dependencies.

Create packages
---------------

With :ref:`uv build <uv-build>` you can easily create :term:`distribution
packages <Distribution Package>` and :term:`wheels <wheel>`.

Declare, lock and automatically update dependencies
---------------------------------------------------

Updating :ref:`update-uv-lock` describes how you can use ``uv lock --upgrade``
to update all dependencies and :samp:`uv lock --upgrade-package
{PACKAGE}=={VERSION}` to update individual dependencies in a controlled manner.
We describe how you can regularly update the dependencies of your project
automatically in :doc:`dependency-bot`. These measures significantly increase
the security of your project.

.. seealso::
   * :ref:`lock-dependencies`
   * :ref:`automatic-update`

Testing in different Python environments
----------------------------------------

uv simplifies the :ref:`parallel installation of different Python versions,
including PyPy and free-threaded Python 3.13 <various-python-versions>`. With
:ref:`tox_uv` you can then test your project automatically in the different
Python environments.

.. toctree::
   :hidden:

   cicd
   dependency-bot
   docker
