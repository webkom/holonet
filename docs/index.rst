Holonet |frigg| |coverage|
==========================

Holonet has many features, but it is designed to handle mail as long as the management command mail_handler can connect to the database. Services like rabbitmq/redis, elasticsearch, celery, omnibus and policy_services are not required to handle valid mail, but the bounce, spam and blacklist services may not work properly. Postfix may require services like spamassasin and the policy_service to work properly. This depends on your postfix config. If spamassasin is down postfix will send a bounce message to the sender. Postfix may work without the policy_service if a default value exist in the postfix config, if not send a bounce. The sender will get a bounce if something goes wrong under the mail_handler, mail_handler raises different exit codes based on the result.

Features
--------
* Index spam, blacklisted and bounce mail in Elasticsearch
* Policy Service
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
    Holonet Policy Service <policy_service>
    Postfix <postfix>
    Holonet Handler <handler>
    Spamassasin <spamassasin>
    API reference </apidocs/modules>

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |frigg| image:: https://ci.frigg.io/badges/webkom/holonet/
    :target: https://ci.frigg.io/webkom/holonet/last/

.. |coverage| image:: https://ci.frigg.io/badges/coverage/webkom/holonet/
    :target: https://ci.frigg.io/webkom/holonet/last/
