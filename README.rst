Cycles: A data processing framework
===================================

.. image:: https://travis-ci.org/pcarolan/cycles.svg?branch=master
    :target: https://travis-ci.org/pcarolan/cycles



Spin it up.

Features
--------

* Queue
* Logging

Using cycles
------------

Getting started:

.. code-block:: bash

    $ pip install cycles

.. code-block:: python

    from cycles import Hub

    hub = Hub()

    hub.log('Cycle complete.')
