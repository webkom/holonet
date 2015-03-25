Holonet |frigg| |coverage| |deps|
=================================

Holonet has many features, but it is designed to handle mail as long as the management command
mail_handler can connect to the database. Services like rabbitmq/redis, elasticsearch, celery,
sasl_authentication and policy_services are not required to handle valid mail, but the bounce, spam
and blacklist services may not work properly. Postfix may require services like spamassasin and the
policy_service to work properly. This depends on your postfix configuration. If spamassasin is down
postfix will send a bounce message to the sender. Postfix may work without the policy_service if a
default value exist in the postfix configuration, if not send a bounce. The sender will get a
bounce if something goes wrong under the mail_handler, it raises different exit codes based on the
result.

Goals and the issue we try to solve
-----------------------------------
In Abakus linjeforening we don't want to maintain a lagre smtp/imap server with many mailing lists.
Our mail system is closely integrated with our webpage. The users recieve mail on their private
addresses. Holonet is like a key-value store. We lookup abakus mail and send it to its recipients.
We could use a stack like Postfix - Dovecot - Spamassasin - Mailman but we want it to integrate it
more closely to our existing systems. Holonet exposes a tiny rest api, this makes it easy for our
services to talk to it. We also want to get a better overview over the mail that we handles.
Previously we did not have a clue about how many mails we processed in a day. With Holonet we
stores a tiny log message about every mail. We can now see stats about how many mails we process
and its recipients. The system is easy to understand and maintain, we want mail to be more fun not
a black box!

.. image:: /_static/web.png

Features
--------
* Index spam, blacklisted and bounce mail in Elasticsearch
* Policy Service
* SASL Support
* Handle mail using pipe
* Mapping API (Create / Edit / Delete mappings using a json REST API.)
* Store statistics in Elasticsearch
* Stats frontend
* Restricted mail

Pipeline
--------
1. Postfix (Recipient validation uses Holonet Policy Service)
2. Spamassasin
3. Postfix Pipe (Holonet Mail Handling)
4. Holonet does a mailinglist lookup and uses sendmail to process mail to it's recipients


.. include:: getting_started.rst


Contents
--------

.. toctree::
   :maxdepth: 2

    Holonet Worker <worker>
    Postfix <postfix>
    Holonet Policy Service <policy_service>
    Holonet Handler <handler>
    Spamassasin <spamassasin>
    Dovecot SASL <sasl>
    Permissions <permissions>
    REST API <rest_api>

Indices and tables
------------------

* :ref:`search`


.. |frigg| image:: https://ci.frigg.io/badges/webkom/holonet/
    :target: https://ci.frigg.io/webkom/holonet/last/

.. |coverage| image:: https://ci.frigg.io/badges/coverage/webkom/holonet/
    :target: https://ci.frigg.io/webkom/holonet/last/

.. |deps| image:: https://requires.io/github/webkom/holonet/requirements.svg?branch=master
     :target: https://requires.io/github/webkom/holonet/requirements/?branch=master
     :alt: Requirements Status
