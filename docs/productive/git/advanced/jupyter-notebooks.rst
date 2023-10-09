.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-FileContributor: Modified by Kristian Rother
..
.. SPDX-License-Identifier: BSD-3-Clause

Jupyter Notebooks with Git
==========================

Problems with version control of Jupyter Notebooks
--------------------------------------------------

There are several issues to manage Jupyter Notebooks with Git:

* Jupyter Notebooks cell metadata changes even when no content changes have been
  made to the cells. This makes Git diffs unnecessarily complicated.
* The lines that Git writes to the :file:`*.ipynb` files in case of :ref:`merge
  conflicts <merge-conflicts>` cause the notebooks to no longer be valid JSON
  and therefore cannot be opened by Jupyter: you will then get the *Error
  loading notebook* message when opening them.

  Conflicts are especially common in notebooks because Jupyter changes the
  following each time a notebook is run:

  * Each cell contains a number that indicates the order in which it was
    executed. If team members execute the cells in different order, every single
    cell has a conflict! To fix this manually would take a very long time.
  * For each image, such as a plot, Jupyter records not only the image itself in
    the notebook, but also a simple text description containing the ID of the
    object, for example :samp:`{<matplotlib.axes._subplots.AxesSubplot at
    0x7fbc113dbe90>}`. This will change every time you run a notebook, and
    therefore will conflict every time two people run that cell.
  * Some output can be non-deterministic, such as a notebook that uses random
    numbers or interacts with a service that provides different output over
    time.
  * Jupyter adds metadata to the notebook that describes the environment in
    which it was last run, such as the name of the kernel. This often varies
    between different installations, and so two people saving a notebook (even
    without other changes) will often have a conflict in the metadata.

``nbdev2``
----------

`nbdev2 <https://nbdev.fast.ai>`_ has a set of git hooks that provide clean git
diffs that automatically resolve most git conflicts and ensure that any
remaining conflicts can be fully resolved within the standard Jupyter notebook
environment:

* A new ``git merge`` driver provides notebook-native conflict markers that
  result in notebooks opening directly in Jupyter, even if there are Git
  conflicts. Local and remote changes are each shown as separate cells in the
  notebook, so you can simply delete the version you don’t want to keep or
  combine the two cells as needed.

  .. seealso::
     `nbdev.merge docs <https://nbdev.fast.ai/api/merge.html>`_

* Resolving git merges locally is extremely helpful, but we also need to resolve
  them remotely. For example, if a :doc:`merge request <gitlab/merge-requests>`
  is submitted and then someone else submits the same notebook before the merge
  request is merged, it could cause a conflict:

  .. code-block:: javascript

        "outputs": [
         {
     <<<<<< HEAD
          "execution_count": 8,
     ======
          "execution_count": 5,
     >>>>>> 83e94d58314ea43ccd136e6d53b8989ccf9aab1b
          "metadata": {},

  The *save hook* of nbdev2 automatically removes all unnecessary metadata
  (including :samp:`execution_count`) and non-deterministic cell output; this
  means that there are no pointless conflicts like the one above, since this
  information is not stored in the commits in the first place.

To get started, follow the instructions in `Git-Friendly Jupyter
<https://nbdev.fast.ai/tutorials/git_friendly_jupyter.html>`_.


``jq``
------

The results of the calculations can also be saved in the notebook file format
:ref:`nbformat <whats-an-ipynb-file>`. These can also be Base-64-coded blobs
for images and other binary data that should not normally be included in a
version management. These can be removed manually with :menuselection:`Cell -->
All Output --> Clear`, but you have to carry out these steps before every ``git
add``, and it also does not solve a second cause of the noise in ``git diff``,
namely some in the `metadata
<https://nbformat.readthedocs.io/en/latest/format_description.html#metadata>`_.

In order to get systematically comparable versions of notebooks in the version
management, we can use `jq <https://stedolan.github.io/jq/>`_, a lightweight
JSON processor. It takes some time to set up ``jq`` because it has its own
query/filter language, but the default settings are usually well chosen.

Installation
~~~~~~~~~~~~

``jq`` can be installed with:

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install jq

.. tab:: macOS

   .. code-block:: console

      $ brew install jq

Example
~~~~~~~

A typical call is:

.. code-block:: console

    jq --indent 1  \
      '(.cells [] | select (has ("output")) | .outputs) = []
      | (.cells [] | select (has ("execution_count")) | .execution_count) = null
      | .metadata = {"language_info": {"name": "python", "pygments_lexer": "ipython3"}}
      | .Cells []. metadata = {}
      '  example.ipynb

Each line within the single quotation marks defines a filter – the first selects
all entries from the cells list and deletes the output. The next entry resets all
outputs. The third step deletes the notebook’s metadata and replaces it with a
minimum of necessary information so that the notebook can still be run without
complaints. The fourth filter line ``.cells []. metadata = {}``, deletes all meta
information. If you want to keep certain meta information, you can indicate this
here.

Set up
~~~~~~

#. To make your work easier, you can create an alias in the ``~/.bashrc`` file:

   .. code-block:: bash

    alias nbstrip_jq="jq --indent 1 \
        '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
        | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
        | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
        | .cells[].metadata = {} \
        '"

#. Then you can conveniently enter the following in the terminal:

   .. code-block:: console

    $ nbstrip_jq example.ipynb > stripped.ipynb

#. If you start with an existing notebook, you should first add a ``filter``
   commit by simply reading in the newly filtered version of your notebook
   without the unwanted metadata. After you have added the notebook with ``git
   add``, you can see whether the filter has really worked with ``git diff
   --cached``  before you do ``git commit -m 'filter'``.

#. If you want to use this filter for all Git repositories, you can also
   configure your Git globally:

   #. First you add the following to your ``~/.gitconfig`` file:

      .. code-block:: ini

        [core]
        attributesfile = ~/.gitattributes

        [filter "nbstrip_jq"]
        clean = "jq --indent 1 \
                '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
                | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
                | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
                | .cells[].metadata = {} \
                '"
        smudge = cat
        required = true

      ``clean``
          is applied when adding changes to the stage area.
      ``smudge``
          is used when resetting the workspace by changes from the stage area.

   #. Then you have to specify the following in the ``~/.gitattributes`` file:

      .. code-block:: ini

         *.ipynb filter=nbstrip_jq

#. If you then use ``git add`` to add your notebok to the stage area, the
   ``nbstrip_jq`` filter will be applied.

   .. note::
      However, ``git diff`` will not show you any changes between the working
      and stage areas. Only with ``git diff --staged`` you can see that only the
      filtered changes have been applied.

   .. warning::
      ``clean`` and ``smudge`` filters often do not play well with ``git
      rebase`` across such filtered commits. Then you should disable these
      filters before rebasing.

#. And there is another problem: If such a notebook is run again, ``git diff``
   will not show any changes, but ``git status`` will. Therefore, the following
   should be entered in the ``~/.bashrc`` file to be able to quickly clean the
   respective working directory:

   .. code-block:: bash

      function nbstrip_all_cwd {
          for nbfile in *.ipynb; do
              echo "$( nbstrip_jq $nbfile )" > $nbfile
          done
          unset nbfile
      }


ReviewNB
--------

`ReviewNB <https://www.reviewnb.com>`_ solves the problem of doing
:doc:`gitlab/merge-requests` with notebooks. GitLab’s code review GUI only works
with line-based file formats, such as Python scripts. Most of the time, however,
I prefer to check the source code notebooks because:

* I want to check the documentation and the tests, not just the implementation
* I want to see the changes to the cell output, like charts and tables, not just
  the code.

For this purpose ReviewNB is perfect.

``nbdime``
----------

`nbdime <https://nbdime.readthedocs.io/>`_ is a GUI for `nbformat
<https://nbformat.readthedocs.io/>`_ diffs and replaces `nbdiff
<https://github.com/tarmstrong/nbdiff>`_. It attempts content-aware diffing
locally as well as merging notebooks, is not limited to displaying diffs, but
also prevents unnecessary changes from being checked in. However, it is not
compatible with ``nbdev2``.

.. _nbstripout_label:

``nbstripout``
--------------

`nbstripout <https://github.com/kynan/nbstripout>`_ automates *Clear all
outputs*. It uses `nbformat <https://nbformat.readthedocs.io/>`_ and a few auto
magic to set up ``.git config``. In my opinion, however, it has two drawbacks:

* it is limited to the problematic metadata section
* it is slow.
