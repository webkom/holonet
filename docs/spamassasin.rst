Spamassasin
-----------

Spamassasin is a easy way to implement spam validation of mail. Holonet understands the spamassain format, if spamassasin markes the mail as spam, the mail will stop in holonet and be indexed in the Elasticsearch cluster. This servce is not required.

Install Spamassasin: ::

    apt-get install spamassassin spamc
    groupadd spamd
    useradd -g spamd -s /bin/false -d /var/log/spamassassin spamd
    mkdir /var/log/spamassassin
    chown spamd:spamd /var/log/spamassassin

Set up Spamassasin

Change /etc/default/spamassassin (Just change the listed parameters): ::

    ENABLED=1
    CRON=1
    OPTIONS="--create-prefs --max-children 5 --helper-home-dir --ipv4only"

Change /etc/spamassassin/local.cf (Just change the listed parameters): ::

    rewrite_header Subject ***** SPAM _SCORE_ :: Holonet Mail Service *****
    report_safe 0
    required_score 3.0
    use_bayes 1
    bayes_auto_learn 1
    add_header ham HAM-Report _REPORT_

Postfix needs do be aware of spamassasin, change /etc/postfix/master.cf: ::

    smtp      inet  n       -       -       -       -       smtpd -o content_filter=spamassassin

    spamassassin unix -     n       n       -       -       pipe
      user=spamd argv=/usr/bin/spamc -f -e
        /usr/sbin/sendmail -oi -f ${sender} ${recipient}
