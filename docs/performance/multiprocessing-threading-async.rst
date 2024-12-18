.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Introduction to multithreading, multiprocessing and async
=========================================================

Martelli’s model of scalability
-------------------------------

+------------------+----------------------------------------+
| Number of cores  | Description                            |
+==================+========================================+
| 1                | Single thread and single process       |
+------------------+----------------------------------------+
| 2–8              | Multiple threads and multiple processes|
+------------------+----------------------------------------+
| >8               | Distributed processing                 |
+------------------+----------------------------------------+

Martelli’s observation was that over time the second category becomes less and
less important as individual cores become more powerful and large data sets
become larger.

Global Interpreter Lock (GIL)
-----------------------------

CPython has a lock on its internally shared global state. As a result, no more
than one thread can run at the same time.

The GIL is not a big problem for I/O-heavy applications; however, using
threading will slow down CPU-heavy applications. Accordingly, multi-processing
is exciting for us to get more CPU cycles.

`Literate programming <http://www.literateprogramming.com/>`_ and *Martelli's
model of scalability* determined the design decisions on Python’s performance
for a long time. Little has changed in this assessment to this day: Contrary to
intuitive expectations, more CPUs and threads in Python initially lead to less
efficient applications. However, the `Gilectomy
<https://pythoncapi.readthedocs.io/gilectomy.html>`_ project, which was supposed
to replace the GIL, also encountered another problem: the Python C API exposes
too many implementation details. With this, however, performance improvements
would quickly lead to incompatible changes, which then seem unacceptable,
especially in a language as popular as Python.

Overview
--------

+------------------+------------------+------------------+--------------------------------+
| Criterion        | Multithreading   | Multiprocessing  | asyncio                        |
+==================+==================+==================+================================+
| Separation       | Threads share one| The processes are| With                           |
|                  | state.           | independent of   | ``run_coroutine_threadsafe()``,|
|                  |                  | each other.      | ``asyncio`` objects can also   |
|                  | However, sharing |                  | be used by other threads.      |
|                  | a state can lead | If they are to   |                                |
|                  | to race          | communicate with | Almost all ``asyncio`` objects |
|                  | conditions, i.e. | each other,      | are not thread-safe.           |
|                  | the result of an | `interprocess    |                                |
|                  | operation can    | communication    |                                |
|                  | depend on the    | (IPC)`_, `object |                                |
|                  | timing of certain| pickling`_  and  |                                |
|                  | individual       | other overhead   |                                |
|                  | operations.      | is necessary.    |                                |
+------------------+------------------+------------------+--------------------------------+
| Switch           | Threads change   | As soon as you   | ``asyncio`` switches           |
|                  | `preemptively`_, | get a process    | `cooperatively`_, i.e. `yield`_|
|                  | i.e. no explicit | assigned,        | or `await`_ must be explicitly |
|                  | code needs to be | significant      | specified to cause a switch.   |
|                  | added to cause   | progress should  | You can therefore keep the     |
|                  | a change of      | be made. So you  | effort to these changes very   |
|                  | tasks.           | should not make  | low.                           |
|                  |                  | too many         |                                |
|                  | However, such a  | roundtrips back  |                                |
|                  | change is        | and forth.       |                                |
|                  | possible at any  |                  |                                |
|                  | time;            |                  |                                |
|                  | accordingly,     |                  |                                |
|                  | critical areas   |                  |                                |
|                  | must be protected|                  |                                |
|                  | with ``lock``.   |                  |                                |
+------------------+------------------+------------------+--------------------------------+
| Tooling          | Threads require  | Simple tooling   | At least for complex systems,  |
|                  | very little      | with `map`_ and  | ``asyncio`` leads to the goal  |
|                  | tooling: `Lock`_ | `imap_unordered`_| more easy than multithreading  |
|                  | and `Queue`_.    | among others, to | locks.                         |
|                  |                  | test individual  |                                |
|                  | Locks are        | processes in a   | However ``asyncio`` requires a |
|                  | difficult to     | single thread    | large set of tools:            |
|                  | understand in    | before switching | `futures`_, `Event Loops`_ and |
|                  | non-trivial      | to               | non-blocking versions of almost|
|                  | examples. For    | multiprocessing. | everything.                    |
|                  | complex          |                  |                                |
|                  | applications, it | If IPC or        |                                |
|                  | is therefore     | object pickling  |                                |
|                  | better to use    | is used, the     |                                |
|                  | atomic message   | tooling becomes  |                                |
|                  | queues or        | more complex.    |                                |
|                  | ``asyncio``.     |                  |                                |
+------------------+------------------+------------------+--------------------------------+
| Performance      | Multithreading   | The processes can| Calling a poor Python function |
|                  | produces the best| be distributed   | takes more overhead than       |
|                  | results for      | to several CPUs  | requesting a ``generator`` or  |
|                  | IO-heavy tasks.  | and should       | ``awaitable`` – i.e.,          |
|                  |                  | therefore be     | ``asyncio`` can utilise the CPU|
|                  | The performance  | used for         | efficiently.                   |
|                  | limit for threads| CPU-heavy tasks. |                                |
|                  | is one CPU minus |                  | For CPU-intensive tasks,       |
|                  | task switches and| However,         | however, multiprocessing is    |
|                  | synchronisation  | additional effort| more suitable.                 |
|                  | overheads.       | may be required  |                                |
|                  |                  | and              |                                |
|                  |                  | synchronisation  |                                |
|                  |                  | of the processes.|                                |
+------------------+------------------+------------------+--------------------------------+

Summary
-------

There is no one ideal implementation of concurrency – each of the approaches
presented next has specific advantages and disadvantages. So before you decide
which approach to follow, you should analyse the performance problems carefully
and then choose the most suitable solution. In our projects, we often use
several approaches, depending on the part for which the performance is to be
optimised.

.. _`interprocess Communication (IPC)`: https://docs.python.org/3/library/ipc.html
.. _`object pickling`: https://docs.python.org/3/library/pickle.html
.. _`preemptively`: https://en.wikipedia.org/wiki/Computer_multitasking#Preemptive_multitasking
.. _`Lock`: https://docs.python.org/3/library/threading.html#threading.Lock
.. _`Queue`: https://docs.python.org/3/library/queue.html
.. _`cooperatively`: https://en.wikipedia.org/wiki/Computer_multitasking#Cooperative_multitasking
.. _`yield`: https://docs.python.org/3/reference/simple_stmts.html#yield
.. _`await`: https://docs.python.org/3/reference/expressions.html#await
.. _`map`: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map
.. _`imap_unordered`: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap_unordered
.. _`futures`: https://docs.python.org/3/library/asyncio-task.html#awaitables
.. _`Event Loops`: https://docs.python.org/3/library/asyncio-eventloop.html
