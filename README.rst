HOLONET |ci|
============

    Mail Delivery System

Documentation_

*NB: The project is under heavy development and are not ready to be used.*


This repository contains the Holonet Mail Delivery System. This project talks to the MTA and
provides a REST API for interacting with the system.

Getting started
---------------

::

    git clone git@github.com:webkom/holonet.git
    cd holonet
    virtualenv venv -p python3
    source venv/bin/activate
    pip install -r requirements/base.txt

Now you need to fix the settings file. Override the settings you want in settings/holonet.py.
Make sure you configure the database, elasticsearch config, celery broker, cache and so on. For
more information about the configuration, please read the documentation.

Read more about how to use Holonet in the Documentation_.

MIT © Abakus Webkom


.. |ci| image:: https://ci.abakus.no/api/badges/webkom/holonet/status.svg
    :target: https://ci.abakus.no/webkom/holonet

.. _Documentation: http://holonet.readthedocs.org/
