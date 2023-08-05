
===============
ddtrace-graphql
===============


.. image:: https://travis-ci.org/beezz/ddtrace-graphql.svg?branch=master
   :target: https://travis-ci.org/beezz/ddtrace-graphql

.. image:: https://codecov.io/gh/beezz/ddtrace-graphql/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/beezz/ddtrace-graphql

.. image:: https://pyup.io/repos/github/beezz/ddtrace-graphql/shield.svg
   :target: https://pyup.io/repos/github/beezz/ddtrace-graphql/


.. image:: https://badge.fury.io/py/ddtrace-graphql.svg
   :target: https://badge.fury.io/py/ddtrace-graphql


Python library to trace graphql calls with Datadog.

* `graphql-core <https://github.com/graphql-python/graphql-core>`_

* `Datadog APM (Tracing) <https://docs.datadoghq.com/tracing/>`_

* `Datadog Trace Client <http://pypi.datadoghq.com/trace/docs/>`_


Compatibility
-------------

``ddtrace-graphql`` is tested with:

* Python versions: 3.5, 3.6, nightly
* graphql-core: 2.0, 1.1.0, latest
* ddtrace: 0.11.1, 0.10.1, latest

*Screenshots for pyramid app serving GraphQL with tracing enabled:*

.. figure:: screenshots/service.png
   :scale: 80%

   GraphQL service detail.


.. figure:: screenshots/query.png
   :scale: 80%

   GraphQL query detail.



Installation
============

Using pip
---------

.. code-block:: bash

   $ pip install ddtrace-graphql


From source
------------

.. code-block:: bash

   $ git clone https://github.com/beezz/ddtrace-graphql.git
   $ cd ddtrace-graphql && python setup.py install


Usage
=====

To trace all GraphQL requests patch the library. Put this snippet to your
application main entry point.


.. code-block:: python

   __import__('ddtrace_graphql').patch()

   # OR

   from ddtrace_graphql import patch
   patch()


Check out the `datadog trace client <http://pypi.datadoghq.com/trace/docs/>`_
for all supported libraries and frameworks.

.. note:: For the patching to work properly, ``patch`` needs to be called
          before any other imports of the ``graphql`` function.

.. code-block:: python

   # app/__init__.py
   __import__('ddtrace_graphql').patch()

   # from that point all calls to graphql are traced
   from graphql import graphql
   result = graphql(schema, query)


Trace only certain calls with ``traced_graphql`` function

.. code-block:: python

    from ddtrace_graphql import traced_graphql
    traced_graphql(schema, query)


Configuration
=============

Environment variables
=====================

:DDTRACE_GRAPHQL_SERVICE: Define service name under which traces are shown in Datadog. Default value is ``graphql``


.. code-block:: bash

   $ export DDTRACE_GRAPHQL_SERVICE=foobar.graphql


span_kwargs
===========

Default arguments passed to the tracing context manager can be updated using
``span_kwargs`` argument of ``ddtrace_graphql.patch`` or
``ddtrace_graphql.traced_graphql`` functions.

Default values:

:name: Wrapped resource name. Default ``graphql.graphql``.
:span_type: Span type. Default ``graphql``.
:service: Service name. Defaults to ``DDTRACE_GRAPHQL_SERVICE`` environment variable if present, else ``graphql``.
:resource: Processed resource. Defaults to query / mutation signature.

For more information visit `ddtrace.Tracer.trace <http://pypi.datadoghq.com/trace/docs/#ddtrace.Tracer.trace>`_ documentation.


.. code-block:: python

   from ddtrace_graphql import patch
   patch(span_kwargs=dict(service='foo.graphql'))


.. code-block:: python

   from ddtrace_graphql import traced_graphql
   traced_graphql(schema, query, span_kwargs=dict(resource='bar.resource'))



span_callback
=============

In case you want to postprocess trace span you may use ``span_callback``
argument. ``span_callback`` must be function with signature ``def callback(result=result, span=span)``
where ``result`` is graphql execution result or ``None`` in case of fatal error and span is trace span object
(`ddtrace.span.Span <https://github.com/DataDog/dd-trace-py/blob/master/ddtrace/span.py>`_).

What is it good for? Unfortunately one cannot filter/alarm on span metrics resp.
meta information even if those are numeric (why Datadog?) so you can use it to
send metrics based on span, result attributes.

.. code-block:: python

   from datadog import statsd
   from ddtrace_graphql import patch, CLIENT_ERROR, INVALID

   def callback(result, span):
       tags = ['resource:{}'.format(span.resource.replace(' ', '_'))]
       statsd.increment('{}.request'.format(span.service), tags=tags)
       if span.error:
           statsd.increment('{}.error'.format(span.service), tags=tags)
       elif span.get_metric(CLIENT_ERROR):
           statsd.increment('{}.{}'.format(span.service, CLIENT_ERROR), tags=tags)
       if span.get_metric(INVALID):
           statsd.increment('{}.{}'.format(span.service, INVALID), tags=tags)

   patch(span_callback=callback)


ignore_exceptions
=================

Some frameworks use exceptions to handle 404s etc. you may want to ignore some
exceptions resp. not consider them server error. To do this you can supply
`ignore_exceptions` argument as list of exception classes to ignore.
`ignore_exceptions` will be used in python's `isinstance` thus you can ignore
also using base classes.


.. code-block:: python

   from ddtrace_graphql import patch
   patch(ignore_exceptions=(ObjectNotFound, PermissionsDenied))


.. code-block:: python

   from ddtrace_graphql import traced_graphql
   traced_graphql(
       schema, query,
       ignore_exceptions=(ObjectNotFound, PermissionsDenied))


Development
===========

Install from source in development mode
---------------------------------------

.. code-block:: bash

   $ git clone https://github.com/beezz/ddtrace-graphql.git
   $ pip install --editable ddtrace-graphql[test]


Run tests
---------

.. code-block:: bash

   $ cd ddtrace-graphql
   $ tox
