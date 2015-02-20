Getting Started
---------------

::

    git clone git@github.com:webkom/holonet.git
    cd holonet
    npm install && bower install
    make frontend
    make venv
    source venv/bin/activate
    pip install -r requirements/prod.txt

Now you need to fix the settings file. Override the settings you want in settings/holonet.py. Make sure you configure the database, elasticsearch config, celery broker, cache and so on.

::

    python manage.py collectstatic

The django project is now probably ready to run. You can now run it with gunicorn or uwsgi. Now you need to setup postfix to pipe mail into holonet, start the policy service and start the celery worker. This process is described later in this document.

It is recommended to run the scripts with supervisor.
