Getting Started
---------------

::

    git clone git@github.com:webkom/holonet.git
    cd holonet
    pip install -Ur requirements/prod.txt
    npm install && bower install
    make frontend
    make venv
    python manage.py migrate
    python manage.py collectstatic

Now you need to fix the settings file. Override the settings you want in settings/holonet.py. Make sure you configure the database, elasticsearch config, celery broker, cache and so on.

The django project is now probably ready to run. You can now run it with gunicorn or uwsgi. Now you need to setup postfix to pipe mail into holonet, start the policy service, start the sasl service and start the celery worker.

It is recommended to run the scripts with supervisor.
