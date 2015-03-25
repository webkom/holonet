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

Now you need to fix the settings file. Override the settings you want in settings/holonet.py. Make
sure you configure the database, elasticsearch config, celery broker, cache and so on.

The Holonet project is ready to be set up. It will work with gunicorn, uwsgi or another wsgi
app-server. In order to get Holonet working it is necessary to configure postfix to pipe emails to
Holonet and start the policy-service, the sasl-service and the celery-worker.

It is recommended to run the scripts with supervisor.
