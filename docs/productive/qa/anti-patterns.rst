.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Code-Smells and Anti-Patterns
=============================

Code smells are coding patterns that indicate that something is wrong with the
design of a programme. For example, the overuse of isinstance checks against
concrete classes is a code smell, as it makes the programme more difficult to
extend to deal with new types in the future.

Recognising code smells
-----------------------

One way to better recognise code smells is to describe the characteristics of
code. Make a note of the things you recognise; add any patterns you see, like or
don’t understand. The following questions may prompt you to think further:

* Are there methods that have the same form?
* Are there methods that have an argument with the same name?
* Do arguments with the same name always mean the same thing?
* If you want to add a private method to a class, where would it go?
* If you were to split the class into two parts, where would the dividing line
  be?
* Do the tests in the conditions have anything in common?
* How many branches do the conditions have?
* Do the methods contain any code other than the condition?
* Does each method depend more on the argument passed or on the class as a
  whole?

Typical code smells in Python
-----------------------------

.. seealso::
   * `Effective Python <https://effectivepython.com/>`_
     by Brett Slatkin
   * `When Python Practices Go Wrong
     <https://rhodesmill.org/brandon/slides/2019-11-codedive/>`_
     by Brandon Rhodes

Functions that should be objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to object-oriented programming, Python also supports procedural
programming using functions and inheritable classes. Both paradigms should,
however, be applied to the appropriate problems.

Typical symptoms of functional code that should be converted to classes are

* similar arguments across functions
* high number of distinct Halstead operands
* mix of mutable and immutable functions

For example, three functions with ambiguous usage can be reorganised so, that
``load_image()`` is replaced by ``.__init__()``, ``crop()`` becomes a class
method, and ``get_thumbnail()`` a property:

.. code-block:: python

    class Image(object):
        thumbnail_resolution = 128

        def __init__(self, path):
            ...

        def crop(self, width, height):
            ...

        @property
        def thumbnail(self):
            ...
            return thumb

Objects that should be functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, however, object-oriented code should also be better broken down into
functions, for example if a class contains only one other method apart from
``.__init__()`` or only static methods.

.. note::
   You do not have to search for such classes manually, but there is a pylint
   rule for it:

   .. code-block:: console

    $ pipenv run pylint --disable=all --enable=R0903 requests
    ************* Module requests.auth
    requests/auth.py:72:0: R0903: Too few public methods (1/2) (too-few-public-methods)
    requests/auth.py:100:0: R0903: Too few public methods (1/2) (too-few-public-methods)
    ************* Module requests.models
    requests/models.py:60:0: R0903: Too few public methods (1/2) (too-few-public-methods)

    -----------------------------------
    Your code has been rated at 9.99/10

   This shows us that two classes with only one public method have been defined in
   ``auth.py``, in lines 72ff. and 100ff. Also in ``models.py`` there is a class
   with only one public method from line 60.

Nested code
~~~~~~~~~~~

    *«Flat is better than nested.»*

– Tim Peters, `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`_

Nested code makes it difficult to read and understand. You need to understand
and remember the conditions as you go through the nestings. Objectively, the
cyclomatic complexity increases as the number of code branches increases.

You can reduce nested methods with multiple nested ``if`` statements by
replacing levels with methods that return ``False`` if necessary. Then you can
use ``.count()`` to check if the number of errors is ``> 0``.

Another possibility is to use list comprehensions. This way the code

.. code-block:: python

    results = []
    for item in iterable:
        if item == match:
            results.append(item)

can be replaced by

.. code-block:: python

    results = [item for item in iterable if item == match]

.. note::
   The `itertools <https://docs.python.org/3/library/itertools.html>`_ of the
   Python standard library are often also good for reducing the nesting depth by
   creating functions to create iterators from data structures.

.. note::
   You can also filter with itertools, for example with `filterfalse
   <https://docs.python.org/3/library/itertools.html#itertools.filterfalse>`_:

   .. code-block::

      >>> from itertools import filterfalse
      >>> from math import isnan
      >>> from statistics import median
      >>> data = [20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4]
      >>> sorted(data)
      [20.7, nan, 14.4, 18.3, 19.2, nan]
      >>> median(data)
      16.35
      >>> sum(map(isnan, data))
      2
      >>> clean = list(filterfalse(isnan, data))
      >>> clean
      [20.7, 19.2, 18.3, 14.4]
      >>> sorted(clean)
      [14.4, 18.3, 19.2, 20.7]
      >>> median(clean)
      18.75

Query tools for complex dicts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`JMESPath <https://jmespath.org/>`_, `glom <https://github.com/mahmoud/glom>`_,
`asq <https://asq.readthedocs.io/en/latest/>`_ and `flupy
<https://flupy.readthedocs.io/en/latest/>`_ can significantly simplify the query
of dicts in Python.

Reduce code with ``dataclasses`` and ``attrs``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`python-basics:dataclasses`
    are intended to simplify the definition of classes that are mainly created to store
    values and can then be accessed via attribute search. Some examples are
    :func:`collections.namedtuple`, :py:class:`typing.NamedTuple`, recipes for `records
    <https://web.archive.org/web/20170904185553/http://code.activestate.com/recipes/576555-records/>`_
    and `nested dicts
    <https://web.archive.org/web/20100604034714/http://code.activestate.com/recipes/576586-dot-style-nested-lookups-over-dictionary-based-dat>`_.
    Data classes save you from having to write and manage these methods.

    .. seealso::
       * :pep:`557` – Data Classes

`attrs <https://www.attrs.org/en/stable/>`_
    is a Python package that has been around much longer than ``dataclasses``, is more
    comprehensive and can also be used with older versions of Python.
