==========
 Examples
==========

While developing Zag the team has worked *hard* to make sure the various
concepts are explained by *relevant* examples. Here are a few selected examples
to get started (ordered by *perceived* complexity):

To explore more of these examples please check out the `examples`_ directory
in the Zag `source tree`_.

.. note::

    If the examples provided are not satisfactory (or up to your
    standards) contributions are welcome and very much appreciated to help
    improve them. The higher the quality and the clearer the examples are the
    better and more useful they are for everyone.

.. _examples: http://git.openstack.org/cgit/openstack/zag/tree/zag/examples
.. _source tree: http://git.openstack.org/cgit/openstack/zag/

Hello world
===========

.. note::

    Full source located at :example:`hello_world`.

.. literalinclude:: ../../../zag/examples/hello_world.py
    :language: python
    :linenos:
    :lines: 16-

Passing values from and to tasks
================================

.. note::

    Full source located at :example:`simple_linear_pass`.

.. literalinclude:: ../../../zag/examples/simple_linear_pass.py
    :language: python
    :linenos:
    :lines: 16-

Using listeners
===============

.. note::

    Full source located at :example:`echo_listener`.

.. literalinclude:: ../../../zag/examples/echo_listener.py
    :language: python
    :linenos:
    :lines: 16-

Using listeners (to watch a phone call)
=======================================

.. note::

    Full source located at :example:`simple_linear_listening`.

.. literalinclude:: ../../../zag/examples/simple_linear_listening.py
    :language: python
    :linenos:
    :lines: 16-

Dumping a in-memory backend
===========================

.. note::

    Full source located at :example:`dump_memory_backend`.

.. literalinclude:: ../../../zag/examples/dump_memory_backend.py
    :language: python
    :linenos:
    :lines: 16-

Making phone calls
==================

.. note::

    Full source located at :example:`simple_linear`.

.. literalinclude:: ../../../zag/examples/simple_linear.py
    :language: python
    :linenos:
    :lines: 16-

Making phone calls (automatically reverting)
============================================

.. note::

    Full source located at :example:`reverting_linear`.

.. literalinclude:: ../../../zag/examples/reverting_linear.py
    :language: python
    :linenos:
    :lines: 16-

Building a car
==============

.. note::

    Full source located at :example:`build_a_car`.

.. literalinclude:: ../../../zag/examples/build_a_car.py
    :language: python
    :linenos:
    :lines: 16-

Iterating over the alphabet (using processes)
=============================================

.. note::

    Full source located at :example:`alphabet_soup`.

.. literalinclude:: ../../../zag/examples/alphabet_soup.py
    :language: python
    :linenos:
    :lines: 16-

Watching execution timing
=========================

.. note::

    Full source located at :example:`timing_listener`.

.. literalinclude:: ../../../zag/examples/timing_listener.py
    :language: python
    :linenos:
    :lines: 16-

Distance calculator
===================

.. note::

    Full source located at :example:`distance_calculator`

.. literalinclude:: ../../../zag/examples/distance_calculator.py
    :language: python
    :linenos:
    :lines: 16-

Table multiplier (in parallel)
==============================

.. note::

    Full source located at :example:`parallel_table_multiply`

.. literalinclude:: ../../../zag/examples/parallel_table_multiply.py
    :language: python
    :linenos:
    :lines: 16-

Linear equation solver (explicit dependencies)
==============================================

.. note::

    Full source located at :example:`calculate_linear`.

.. literalinclude:: ../../../zag/examples/calculate_linear.py
    :language: python
    :linenos:
    :lines: 16-

Linear equation solver (inferred dependencies)
==============================================

``Source:`` :example:`graph_flow.py`

.. literalinclude:: ../../../zag/examples/graph_flow.py
    :language: python
    :linenos:
    :lines: 16-

Linear equation solver (in parallel)
====================================

.. note::

    Full source located at :example:`calculate_in_parallel`

.. literalinclude:: ../../../zag/examples/calculate_in_parallel.py
    :language: python
    :linenos:
    :lines: 16-

Creating a volume (in parallel)
===============================

.. note::

    Full source located at :example:`create_parallel_volume`

.. literalinclude:: ../../../zag/examples/create_parallel_volume.py
    :language: python
    :linenos:
    :lines: 16-

Summation mapper(s) and reducer (in parallel)
=============================================

.. note::

    Full source located at :example:`simple_map_reduce`

.. literalinclude:: ../../../zag/examples/simple_map_reduce.py
    :language: python
    :linenos:
    :lines: 16-

Sharing a thread pool executor (in parallel)
============================================

.. note::

    Full source located at :example:`share_engine_thread`

.. literalinclude:: ../../../zag/examples/share_engine_thread.py
    :language: python
    :linenos:
    :lines: 16-

Storing & emitting a bill
=========================

.. note::

    Full source located at :example:`fake_billing`

.. literalinclude:: ../../../zag/examples/fake_billing.py
    :language: python
    :linenos:
    :lines: 16-

Suspending a workflow & resuming
================================

.. note::

    Full source located at :example:`resume_from_backend`

.. literalinclude:: ../../../zag/examples/resume_from_backend.py
    :language: python
    :linenos:
    :lines: 16-

Creating a virtual machine (resumable)
======================================

.. note::

    Full source located at :example:`resume_vm_boot`

.. literalinclude:: ../../../zag/examples/resume_vm_boot.py
    :language: python
    :linenos:
    :lines: 16-

Creating a volume (resumable)
=============================

.. note::

    Full source located at :example:`resume_volume_create`

.. literalinclude:: ../../../zag/examples/resume_volume_create.py
    :language: python
    :linenos:
    :lines: 16-

Running engines via iteration
=============================

.. note::

    Full source located at :example:`run_by_iter`

.. literalinclude:: ../../../zag/examples/run_by_iter.py
    :language: python
    :linenos:
    :lines: 16-

Controlling retries using a retry controller
============================================

.. note::

    Full source located at :example:`retry_flow`

.. literalinclude:: ../../../zag/examples/retry_flow.py
    :language: python
    :linenos:
    :lines: 16-

Distributed execution (simple)
==============================

.. note::

    Full source located at :example:`wbe_simple_linear`

.. literalinclude:: ../../../zag/examples/wbe_simple_linear.py
    :language: python
    :linenos:
    :lines: 16-

Distributed notification (simple)
=================================

.. note::

    Full source located at :example:`wbe_event_sender`

.. literalinclude:: ../../../zag/examples/wbe_event_sender.py
    :language: python
    :linenos:
    :lines: 16-

Distributed mandelbrot (complex)
================================

.. note::

    Full source located at :example:`wbe_mandelbrot`

Output
------

.. image:: img/mandelbrot.png
   :height: 128px
   :align: right
   :alt: Generated mandelbrot fractal

Code
----

.. literalinclude:: ../../../zag/examples/wbe_mandelbrot.py
    :language: python
    :linenos:
    :lines: 16-

Jobboard producer/consumer (simple)
===================================

.. note::

    Full source located at :example:`jobboard_produce_consume_colors`

.. literalinclude:: ../../../zag/examples/jobboard_produce_consume_colors.py
    :language: python
    :linenos:
    :lines: 16-

Conductor simulating a CI pipeline
==================================

.. note::

    Full source located at :example:`tox_conductor`

.. literalinclude:: ../../../zag/examples/tox_conductor.py
    :language: python
    :linenos:
    :lines: 16-


Conductor running 99 bottles of beer song requests
==================================================

.. note::

    Full source located at :example:`99_bottles`

.. literalinclude:: ../../../zag/examples/99_bottles.py
    :language: python
    :linenos:
    :lines: 16-
