Buffer
------

The buffer is a place where Holonet stores a message before it gets processed by the queue.
Holonet comes with multiple buffer backends. Django cache framework and redis can be used. Redis
is probably the best, therefore Redis is default.

Redis
=====

The Redis backend is probably the best. Redis is a fast in-memory database. If you use this
backend make sure the server has enough memory.

.. code:: python

    MESSAGE_BUFFER = 'holonet.storage.buffer.backends.redis.RedisBuffer'

Django Cache Framework
======================

The Django cache buffer uses the Django cache as a backend. If you use this backend, make sure
you are using Memcached or Redis as a backend in Django. Other backends does not work. Memcached
may work, but problems with payload size and non persistent data may occur.

.. code:: python

    MESSAGE_BUFFER = 'holonet.storage.buffer.backends.django_cache.DjangoCacheBuffer'

