.. SPDX-FileCopyrightText: 2020 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Git log
=======

:samp:`$ git log [-n {COUNT}]`
    list the commit history of the current branch.

    ``-n``
        limits the number of commits to the specified number.

:samp:`$ git log [--after="{YYYY-MM-DD}"] [--before="{YYYY-MM-DD}"]`
    Commit history filtered by date.

    Relative information such as ``1 week ago`` or ``yesterday`` is also
    permitted.

:samp:`$ git log --author="{NAME}"`
    filters the commit history by authors.

    You can also search for several authors at the same time, for example

    :samp:`$ git log --author="{VEIT}\|{VSC}"`

:samp:`$ git log --grep = "{TERM}"`
    filters the commit history for regular expressions in the commit message.

    .. seealso::

        * :doc:`python-basics:appendix/regex`

:samp:`$ git log -S"{FOO}"`
    filters commits according to certain lines in the source code.

:samp:`$ git log -G"{BA*}"`
    filters commits based on regular expressions in the source code.

:samp:`$ git log -- {PATH/TO/FOO.PY}`
    filters the commit history for specific files.

:samp:`$ git log {MAIN} ..{FEATURE}`
    filters for different commits in different branches, in our case between the
    branches ``main`` and ``feature``.

    However, this is not the same as :samp:`$ git log {FEATURE}..{MAIN}`. Let’s
    take the following example.

    .. code-block::

       A - B main
        \
         C - D feature

    :samp:`$ git log {MAIN}..{FEATURE}`
        shows changes in :samp:`{FEATURE}` that are not contained in
        :samp:`{MAIN}`, that are the commits ``C`` and ``D``.
    :samp:`$ git log {FEATURE}..{MAIN}`
        shows changes in :samp:`{MAIN}` that are not contained in
        :samp:`{FEATURE}`, that is the commit ``B``.
    :samp:`$ git log {MAIN}...{FEATURE}`
        shows the changes on both sides, the commits ``B``, ``C`` and ``D``.

:samp:`$ git log --oneline --graph --decorate`
    Show the history diagram with references, one commit per line.

:samp:`$ git log {REF}..`
    List commits that exist in the current branch and are not merged into
    ``ref``. ``ref`` can be the name of a branch or a tag.

:samp:`$ git log ..{REF}`
    List commits that exist in ``ref`` and are not merged with the current
    branch.
:samp:`$ git reflog`
    List operations (for example ``switch``, ``commit``) that have been
    performed in the local repository.
