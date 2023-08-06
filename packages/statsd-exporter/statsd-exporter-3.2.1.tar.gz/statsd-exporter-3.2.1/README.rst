===========================================================
A Python statsd client with prom/statsd-exporter compatible tag support
===========================================================

_This is a fork of `statsd-telegraf` which is a fork of `pystatsd` package._

statsd_ is a friendly front-end to Graphite_. This is a Python client
for the statsd daemon. More specifically, this is a fork of jsocol's
pystatsd client, with the addition of support for DogTag-compatible
tags.

:Code:          https://github.com/openmotics/statsd-exporter
:License:       MIT; see LICENSE file
:Issues:        https://github.com/openmotics/statsd-exporter/issues

Quickly, to use:

.. code-block:: python

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125)
    >>> c.incr('foo')  # Increment the 'foo' counter.
    >>> c.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'.

You can also add a prefix to all your stats:

.. code-block:: python

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125, prefix='foo')
    >>> c.incr('bar')  # Will be 'foo.bar' in statsd/graphite.

Datadog-compatible tags are supported, as well:

.. code-block:: python

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125)
    >>> c.incr('baz', tags={'type': 'response'}) 
    >>> # baz,type=response:1|c


Installing
==========

The easiest way to install statsd is with pip!

You can install from PyPI::

    $ pip install statsd-exporter

Or GitHub::

    $ pip install -e git+https://github.com/openmotics/statsd-exporter#egg=statsd-exporter

Or from source::

    $ git clone https://github.com/openmotics/statsd-exporter
    $ cd statsd-exporter
    $ python setup.py install
