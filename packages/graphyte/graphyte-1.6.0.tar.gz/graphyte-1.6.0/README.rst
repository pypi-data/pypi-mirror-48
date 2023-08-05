graphyte
========

.. image:: https://img.shields.io/pypi/v/graphyte.svg
   :target: https://pypi.python.org/pypi/graphyte
   :alt: graphyte on PyPI (Python Package Index)

.. image:: https://travis-ci.org/Jetsetter/graphyte.svg?branch=master
   :target: https://travis-ci.org/Jetsetter/graphyte
   :alt: Travis CI tests (Linux)

.. image:: https://ci.appveyor.com/api/projects/status/github/Jetsetter/graphyte?branch=master&svg=true
   :target: https://ci.appveyor.com/project/benhoyt/graphyte
   :alt: Appveyor tests (Windows)


graphyte is a small Python library that sends data to a Graphite metrics
server (Carbon). We wrote it because the existing `graphitesend`_ library
didn’t support Python 3, and it also required gevent for asyncronous use.
graphyte is compatible with Python 3.4+ as well as Python 2.7, and uses the
standard library’s ``threading`` module for asynchronous use.

The library is `on the Python Package Index (PyPI)`_, so to install it, fire up
a command prompt, activate your virtualenv if you’re using one, and type:

::

    pip install graphyte

Using graphyte is simple – just call ``init()`` to initialize the default
sender and then ``send()`` to send a message. For example, to send
``system.sync.foo.bar 42 {timestamp}\n`` to graphite.example.com:2003
synchronously:

.. code:: python

    import graphyte
    graphyte.init('graphite.example.com', prefix='system.sync')
    graphyte.send('foo.bar', 42)

If you want to send asynchronously on a background thread (for example, in a
web server context), just specify a send interval. For example, this will
setup a background thread to send every 10 seconds:

.. code:: python

    graphyte.init('graphite.example.com', prefix='system.async', interval=10)
    graphyte.send('foo.bar', 42)

If you want to send tagged metrics, the usage is as follows:

.. code:: python

    graphite.send('foo.bar', 42, tags={'ding': 'dong'})

For more advanced usage, for example if you want to send to multiple servers
or if you want to subclass ``Sender``, you can instantiate instances of
``Sender`` directly. For example, to instantiate two senders sending to
different   servers (one synchronous, one using a background thread with send
interval 10   seconds), use something like the following:

.. code:: python

    sender1 = graphyte.Sender('graphite1.example.com', prefix='system.one')
    sender2 = graphyte.Sender('graphite2.example.com', prefix='system.two', interval=10)
    sender1.send('foo.bar1', 42)
    sender2.send('foo.bar2', 43)

If you want to send via UDP instead of TCP, just add   ``protocol='udp'`` to
the ``init()`` or ``Sender()`` call.

Or, to customize how messages are logged or sent to the socket, subclass
``Sender`` and override ``send_message`` (or even ``send_socket`` if you
want to override logging and exception handling):

.. code:: python

    class CustomSender(graphyte.Sender):
        def send_message(self, message):
            print('Sending bytes in some custom way: {!r}'.format(message))

Socket sending errors are logged using the Python logging system (using
logger name “graphyte”). If the sender is initialized with
``log_sends=True``, all sends are logged at the INFO level.

You can also use graphyte to send metrics directly from the command line:

::

    python -m graphyte foo.bar 42

There are command line arguments to specify the server and port and other
configuration. Type ``python -m graphyte --help`` for help.

Read the code in `graphyte.py`_ for more details – it’s pretty small!

graphyte was written by `Ben Hoyt`_ for `Jetsetter`_ and is licensed with a
permissive MIT license (see `LICENSE.txt`_).


.. _graphitesend: https://github.com/daniellawrence/graphitesend
.. _on the Python Package Index (PyPI): https://pypi.python.org/pypi/graphyte
.. _graphyte.py: https://github.com/Jetsetter/graphyte/blob/master/graphyte.py
.. _Ben Hoyt: http://benhoyt.com/
.. _Jetsetter: http://www.jetsetter.com/
.. _LICENSE.txt: https://github.com/Jetsetter/graphyte/blob/master/LICENSE.txt
