Abakus Mail Delivery System
===========================
## Holonet [![Build status](https://ci.frigg.io/badges/webkom/holonet/)](https://ci.frigg.io/webkom/holonet/last/)
### Supported Features
* Index spam in Elasticsearch
* Policy Service
* Handle mail using pipe

### Planned Features
* Create a mailinglist api (Create / Edit / Delete mappings using a json REST API.)
* Store statistics in Elasticsearch
* Stats frontend
* Send resend messages marked bounce and spam
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
