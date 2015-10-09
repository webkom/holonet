# HOLONET [![Build status] (https://ci.frigg.io/badges/webkom/holonet/)](https://ci.frigg.io/webkom/holonet/last/) [![Coverage status](http://ci.frigg.io/badges/coverage/webkom/holonet/)](https://ci.frigg.io/webkom/holonet/last/) [![Documentation Status](https://readthedocs.org/projects/holonet/badge/?version=latest)](http://holonet.readthedocs.org) [![Requirements Status](https://requires.io/github/webkom/holonet/requirements.svg?branch=master)](https://requires.io/github/webkom/holonet/requirements/?branch=master)
> Mail Delivery System

[Documentation](http://holonet.readthedocs.org/)

*NB: The project is under heavy development and are not ready to be used.*

This repository contains the Holonet Mail Delivery System. This project talks to the MTA and 
provides a REST API for interacting with the system.

## Getting started
```
git clone git@github.com:webkom/holonet.git
cd holonet
make venv
source venv/bin/activate
make dev
```

Now you need to fix the settings file. Override the settings you want in settings/holonet.py.
Make sure you configure the database, elasticsearch config, celery broker, cache and so on. For 
more information about the configuration, please read the documentation.

Read more about how to use Holonet in the [documentation](http://holonet.readthedocs.org/).

---

### MIT © Abakus Webkom
