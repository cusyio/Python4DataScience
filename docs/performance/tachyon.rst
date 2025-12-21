Tachyon
=======

Tachyon is a new statistical sampling profiler that was added to Python 3.15 as
:mod:`profiling.sampling`. This profiler enables powerful analysis of running
Python processes with low overhead, without requiring code changes or a process
restart.

Unlike deterministic profilers such as :mod:`profiling.tracing`, which
instrument every function call, :mod:`profiling.sampling` regularly collects
stack traces from running processes.

Key features include:

Profiling without overhead
    :mod:`profiling.sampling` integrates into any running Python process without
    affecting its performance. This is ideal for debugging in production
    environments where your application cannot be restarted or slowed down.
No code changes required
    Existing applications can be profiled without restarting. Simply point the
    profiler at a running process using its PID and start collecting data.
Profiles running processes or modules
    :samp:`attach`
        profiles running processes using their PID.
    :samp:`run -m {MODULE}`
        runs modules and profiles them.
Multiple profiling modes
    You can choose what to measure:

    ``--mode wall``
        Default value that measures the actual elapsed time, including I/O,
        network latency, and blocking operations. This is ideal for
        understanding where your programme is spending time, including waiting
        for external resources.
    ``--mode cpu``
        measures only active CPU execution time, excluding I/O wait times and
        blocking. Use this option to identify CPU-bound bottlenecks and optimise
        computing power.
    ``--mode gil``
        measures the time spent on Python’s :abbr:`GIL (Global Interpreter
        Lock)`. Use this option to determine which threads are being slowed down
        by the GIL.
    ``--mode exception``
        only collects samples from threads with an active exception. Use this
        option to analyse the overhead of exception handling.
    ``-a``
        profiles all threads or only the main thread, increasing understanding
        of the behaviour of multithreaded applications.

Multiple output formats
    Choose the visualisation that best suits your workflow:

    ``--pstats``
        provides detailed tabular statistics, compatible with :mod:`pstats`. It
        displays timing at the function level with direct and cumulative samples
        and is best suited for detailed analysis and integration with existing
        Python profiling tools.
    ``--collapsed``
        generates summarised stack traces. This format is specifically designed
        for creating `flame graphs
        <https://www.brendangregg.com/flamegraphs.html>`_ with external tools
        such as `Brendan Gregg’s FlameGraph scripts
        <https://github.com/brendangregg/FlameGraph>`_ or `Speedscope
        <https://jamie-wong.com/post/speedscope/>`_.
    ``--flamegraph``
        generates a standalone interactive HTML flame graph using `D3.js
        <https://d3js.org/>`_, which opens directly in your browser for
        immediate visual analysis.
    ``--gecko``
        generates a Gecko profiler format that is compatible with `Firefox
        Profiler <https://profiler.firefox.com>`_. The output can be uploaded to
        Firefox Profiler to perform advanced timeline-based analysis with
        features such as bar charts, markers, and network activity.
    ``--heatmap``
        rgGenerates an interactive HTML heatmap visualisation and creates one
        heatmap per file, showing exactly where time is spent at the source code
        level.

``--live``
    `top <https://man7.org/linux/man-pages/man1/top.1.html>`_-like interface,
    allowing you to monitor your application’s performance during execution with
    interactive sorting and filtering.
``--async-aware``
    Profiles :doc:`async/await code <asyncio-example>`, showing you which
    coroutines are consuming time. Additional options show you only running
    tasks or all tasks, including those that are waiting.
``--opcodes``
    collects bytecode opcode information for instruction-level profiling and
    shows which bytecode instructions are being executed, including
    specialisations from the adaptive interpreter.

.. seealso::
   :mod:`profiling.sampling`
