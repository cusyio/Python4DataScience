.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Code-Smells and design principles
=================================

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

SOLID principles
----------------

`SOLID <https://en.wikipedia.org/wiki/SOLID>`_  an acronym for the first five
principles of object-oriented design (OOD) by Robert C. Martin (also known as
`Uncle Bob <https://en.wikipedia.org/wiki/Robert_C._Martin>`_).

These principles establish practices for developing software with considerations
for maintenance and extensibility as the project grows. Adopting these
principles can also help to avoid code smells, refactor code and develop agile
or adaptive software.

SOLID stands for:

S – :ref:`single-responsibility`
    The methods of a class should be orientated towards a single purpose.
O – :ref:`open-closed`
    Objects should be open for extensions but closed for changes.
L – :ref:`liskov-substitution`
    Subclasses should be substitutable by their superclasses.
I – :ref:`interface-segregation`
    Objects should not depend on methods that they do not use.
D – :ref:`dependency-inversion`
    Abstractions should not depend on details.

.. _single-responsibility:

Single responsibility principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `single responsibility principle
<https://en.wikipedia.org/wiki/Single-responsibility_principle>`_ states that
each class should only fulfil one task:

    A class should have one and only one reason to change, meaning that a class
    should have only one job.

– `SRP: The Single Responsibility Principle
<https://web.archive.org/web/20140407020253/http://www.objectmentor.com/resources/articles/srp.pdf>`_
by Robert C. Martin

For example, consider an application that takes a collection of shapes – circles
and squares – and calculates the sum of the circumferences of all the forms in
the collection.

First create the :class:`Form` classes with the necessary parameters. For
squares this is the edge length and for circles the diameter:

.. literalinclude:: forms.py
   :language: python
   :lines: 4-18, 22-24, 27-29

Now you can create a :class:`SquaresAndCircles` class with the logic to
calculate all the circumferences of squares and circles:

.. literalinclude:: forms.py
   :language: python
   :lines: 1-3, 35-46

The :class:`SquaresAndCircles` class takes over the logic required to calculate
all the circumferences of squares and circles. This fulfils the principle of
individual responsibility.

.. _open-closed:

Open-closed principle
---------------------

The :abbr:`OCP (Open-closed principle)` states:

    Objects or entities should be open for extension but closed for
    modification.

This means that a class should be extendable without changing the class itself.

Let’s take a look at the :class:`SquaresAndCircles` class and focus on the
:func:`circumferences` method. Imagine a scenario where you want to calculate
the sum of additional forms such as triangles, pentagons, hexagons, :abbr:`etc.
(et cetera)` You would have to constantly edit this class and add more  ``if``
blocks. This would violate the open-closed principle. One way to improve this
method is to remove the logic for calculating the circumference of each form
from the :class:`SquaresAndCircles` class and attach it to the special form
classes. Here, the circumference calculations are defined in the :class:`Square`
and :class:`Circle` classes:

.. literalinclude:: forms.py
   :language: python
   :lines: 15-32

The :func:`circumferences` sum method in the :class:`CircumferenceFormInstances`
class can then be rewritten as follows:

.. literalinclude:: forms.py
   :language: python
   :lines: 49-

This fulfils the open-closed principle.

.. tip::
   If your code is not yet open for new requirements, you should first
   refactor the existing code so that it is open for the new function. Only
   then should you add new code.

       Refactoring is the process of changing a software system in such a way
       that it does not alter the external behavior of the code yet improves its
       internal structure.

   – `Refactoring
   <https://www.mitp.de/IT-WEB/Software-Entwicklung/Refactoring.html>`_ by
   Martin Fowler

.. note::
   Safe refactoring relies on :doc:`tests <python-basics:test/index>`. If you
   really refactor the code without changing the behaviour, the existing tests
   should continue to succeed at every step. The tests are a safety net that
   justifies confidence in the new arrangement of the code. If they fail,

   * you have inadvertently broken the code,
   * or the existing tests are flawed.

.. _liskov-substitution:

Liskov substitution principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Liskov substitution principle
<https://en.wikipedia.org/wiki/Liskov_substitution_principle>`_ states that a
programme that uses objects of the base class must also function correctly with
objects of the subclass.

Let’s extend our :class:`Form` class so that derived forms can be moved in the
x and y directions:

.. literalinclude:: forms.py
   :language: python
   :lines: 4-12
   :emphasize-lines: 7-9

You can then move both squares and circles on the x and y axes:

.. code-block:: pycon

   >>> import forms
   >>> s1 = forms.Square()
   >>> c1 = forms.Circle()
   >>> s1.x, s1.y, c1.x, c1.y
   (0, 0, 0, 0)
   >>> s1.move(4, 5)
   >>> c1.move(2, 3)
   >>> s1.x, s1.y, c1.x, c1.y
   (4, 5, 2, 3)

.. note::
   Liskov’s substitution principle also applies to
   :ref:`python-basics:duck-typing`: every object that claims to be a duck must
   fully implement the duck’s API. Duck types should be interchangeable.
   Applying logic across different data types of objects is called `polymorphism
   <https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>`_.

.. _interface-segregation:

Interface segregation principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `interface segregation principle
<https://en.wikipedia.org/wiki/Interface_segregation_principle>`_ applies the
:ref:`single-responsibility` principle to interfaces in order to isolate a
specific behaviour. If a change to a part of your code is required, extracting
an object that plays a role opens up the possibility of supporting the new
behaviour without having to change the existing code. This is preferable to
coded concretisations.

In the previous example, we checked whether our :obj:`Form` object actually
provides a :func:`circumference` method. This is necessary if forms such as
:class:`Point` or :class:`Line` are added later that do not have a
circumference.

.. note::
   In this context, `Demeter’s law
   <https://en.wikipedia.org/wiki/Law_of_Demeter>`_ is also interesting, which
   states that objects should only communicate with objects in their immediate
   vicinity. This effectively restricts the list of other objects to which an
   object can send a message and reduces the coupling between objects: an object
   can only talk to its neighbours, but not to the neighbours of its neighbours;
   objects can only send messages to those directly involved.

.. _dependency-inversion:

Dependency inversion principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Dependency inversion principle
<https://en.wikipedia.org/wiki/Dependency_inversion_principle>`_ can be
defined as

    Abstractions should not depend upon details. Details should depend upon
    abstractions.

– `Robert C. Martin: The Dependency Inversion Principle
<https://www.cs.utexas.edu/users/downing/papers/DIP-1996.pdf>`_

:func:`circumferences` should not already be defined in the :class:`Form` class,
as there are also forms without circumferences.

Typical code smells in Python
-----------------------------

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
    is a Python package that has been around much longer than ``dataclasses``,
    is more comprehensive and can also be used with older versions of Python.

.. seealso::
   * `Effective Python <https://effectivepython.com/>`_
     by Brett Slatkin
   * `When Python Practices Go Wrong
     <https://rhodesmill.org/brandon/slides/2019-11-codedive/>`_
     by Brandon Rhodes
