Abakus Mail Delivery System
===========================
## Holonet 

[![Build status] (https://ci.frigg.io/badges/webkom/holonet/)](https://ci.frigg.io/webkom/holonet/last/)

Holonet has many features, but it is designed to handle mail as long as the management command mail_handler can connect to the database. Services like rabbitmq, elasticsearch, celery, omnibus and policy_services are not required to handle valid mail, but the bounce, spam and blacklist services may not work properly. Postfix may require services like spamassasin and the policy_service to work properly. This depends on your postfix config. If spamassasin is down postfix will send a bounce message to the sender. Postfix may work without the policy_service if a default value exist in the postfix config, if not send a bounce. The sender will get a bounce if something goes wrong under the mail_handler, mail_handler raises different exit codes based on the result.

### Supported Features
* Index spam and blacklisted mail in Elasticsearch
* Policy Service
* Handle mail using pipe

### Planned Features
* Create a mailinglist api (Create / Edit / Delete mappings using a json REST API.)
* Store statistics in Elasticsearch
* Stats frontend
* Make it possible to resend blacklisted/spam/bounce mail
* Restricted mail support

## Pipeline
1. Postfix (Recipient validation uses Holonet Policy Service)
2. Spamassasin
3. Postfix Pipe (Holonet Mail Handling)
4. Holonet does a mailinglist lookup and uses sendmail to process mail to it's recipients

## Holonet Policy Service
Holonet Policy Service does a lookup in the mailing lists to find if the RCPT TO parameter is handeled by Holonet.

/etc/postfix/main.cf:
```
smtpd_relay_restrictions =
        permit_mynetworks
        permit_sasl_authenticated
        defer_unauth_destination
        check_policy_service inet:127.0.0.1:13000
```
Then start the policy service with the management command:
```
$PROJECT_DIR/venv/bin/python $PROJECT_DIR/manage.py policy_service
```
## Postfix Setup
Postfix needs to accept all recipients:

/etc/postfix/main.cf:
```
luser_relay = $LOCALUSER
local_recipient_maps =
```
Postfix needs to know the destination domains:

```
mydestination = holonet.abakus.no, localhost.abakus.no, localhost, abakus.no
```

## Holonet Mail Handler
Postfix needs to know where to deliver local mails:

/etc/postfix/main.cf
```
local_transport = holonet
holonet_destination_recipient_limit = 1
```
/etc/postfix/master.cf
```
holonet    unix    -       n       n       -       -       pipe
  user=$LOCALUSER argv=$PROJECT_DIR/venv/bin/python $PROJECT_DIR/manage.py mail_handler ${sender} ${recipient}
```

## Spamassasin Support
Install Spamassasin
```
apt-get install spamassassin spamc
groupadd spamd
useradd -g spamd -s /bin/false -d /var/log/spamassassin spamd
mkdir /var/log/spamassassin
chown spamd:spamd /var/log/spamassassin
```
Set up Spamassasin

Change /etc/default/spamassassin (Just change the listed parameters)
```
ENABLED=1
CRON=1
OPTIONS="--create-prefs --max-children 5 --helper-home-dir --ipv4only"
```
Change /etc/spamassassin/local.cf (Just change the listed parameters)
```
rewrite_header Subject ***** SPAM _SCORE_ :: Holonet Mail Service *****
report_safe 0
required_score 3.0
use_bayes 1
bayes_auto_learn 1
add_header ham HAM-Report _REPORT_
```
