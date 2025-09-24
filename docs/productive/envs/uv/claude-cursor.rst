Configuring Claude Code or Cursor for uv
========================================

How do we configure `Claude Code <https://claude.com/product/claude-code>`_ or
`Cursor <https://cursor.com>`_ to automatically use uv instead of pip for Python
package management?

.. tab:: Claude Code

   Claude Code uses :file:`CLAUDE.md` files to configure your project’s storage
   and context, ensuring a consistent tooling environment for your entire
   development workflow.

   Assuming Claude Code and uv are already installed on your system and you have
   already created a uv-based Python project, for example  with :ref:`uv init
   <uv-package-structure>`.

   .. tip::
      You can use the ``/init`` command in Claude Code to automatically create a
      :file:`CLAUDE.md` file and then add uv-specific instructions to it.

   .. code-block:: md
      :caption: CLAUDE.md

      # Python environment with uv
      Use uv exclusively for the Python environment in this project.

      ## Environment commands
      - Use uv to install, sync, and lock Python dependencies
      - Never use pip, pip-tools, poetry, or conda for dependency management

      Use these commands:
      - Install dependencies: `uv add <package>`
      - Remove dependencies: `uv remove <package>`
      - Sync dependencies: `uv sync`

      ## Running Python Code
      - Run a Python script with `uv run <script-name>.py`
      - Run Python tools like pytest with `uv run pytest`

   .. tip::
      Remember to manage your project-specific :file:`CLAUDE.md` file with
      :doc:`Git </productive/git/index>` so that everyone on the team working
      with Claude Code automatically receives the same configuration.

   .. seealso::
      * `Claude Docs <https://docs.claude.com/en/home>`_
      * `Manage Claude's memory
        <https://docs.claude.com/en/docs/claude-code/memory>`_

.. tab:: Cursor

   `Cursor Rules <https://cursor.com/docs/context/rules>`_ can be used to use uv
   instead of pip.

   This assumes that Cursor and uv are already installed on your system and you
   have already created a uv-based Python project, for example, with :ref:`uv
   init <uv-package-structure>`.

   Then you can create a *Cursor Markdown Context* file :file:`uv.mdc` in
   :samp:`{PROJECT}/.cursor/rules/` for your Cursor Rules in
   :menuselection:`View Menu --> Command Palette --> New Cursor Rule` with

   * Name: ``uv``
   * Rule Type: *Agent Requested*
   * Description: *Exclusively use uv for the Python environment in this project.*

   Afterwards, you can add the following rules:

   .. code-block:: md
      :caption: .cursor/rules/uv.mdc

      # Python environment with uv
      Exclusively use uv for the Python environment in this project.

      ## Environment commands
      - Use uv to install, sync, and lock Python dependencies
      - Never use pip, pip-tools, poetry, or conda for dependency management

      Use these commands:
      - Install dependencies: `uv add <package>`
      - Remove dependencies: `uv remove <package>`
      - Sync dependencies: `uv sync`

      ## Running Python Code
      - Run a Python script with `uv run <script-name>.py`
      - Run Python tools like pytest with `uv run pytest`
