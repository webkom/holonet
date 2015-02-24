Holonet Worker
==============

The Holonet worker stores documents in Elasticsearch.
Holonet worker executes tasks asynchronous. Holonet may work without it, but it is recommended to run it.

::

    PROJECT_DIR/venv/bin/python $PROJECT_DIR/manage.py celery worker

