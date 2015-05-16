# HOLONET [![Build status] (https://ci.frigg.io/badges/webkom/holonet/)](https://ci.frigg.io/webkom/holonet/last/) [![Coverage status](http://ci.frigg.io/badges/coverage/webkom/holonet/)](https://ci.frigg.io/webkom/holonet/last/) [![Documentation Status](https://readthedocs.org/projects/holonet/badge/?version=latest)](http://holonet.readthedocs.org) [![Requirements Status](https://requires.io/github/webkom/holonet/requirements.svg?branch=master)](https://requires.io/github/webkom/holonet/requirements/?branch=master)
> Mail Delivery System

[Documentation](http://holonet.readthedocs.org/)

![web](http://i.imgur.com/tz76uZv.png)

## Getting started
```
git clone git@github.com:webkom/holonet.git
cd holonet
make venv
source venv/bin/activate
make dev
```

Now you need to fix the settings file. Override the settings you want in settings/holonet.py.
Make sure you configure the database, elasticsearch config, celery broker, cache and so on.

```
make static
```

The django project is now probably ready to run. You can now run it with gunicorn or uwsgi. 
Now you need to setup postfix to pipe mail into holonet, start the policy service and start the celery worker. It is recomended to run the scripts with supervisor.

Read more about how to use Holonet in the [documentation](http://holonet.readthedocs.org/).

---

### MIT © Abakus Webkom
