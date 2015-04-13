Spamassasin
-----------

Spamassasin is a easy way to implement spam validation of mail. Holonet understands the spamassassin
format, if spamassasin marks the mail as spam, the mail will stop in Holonet and be indexed in the
Elasticsearch cluster. This service is not required.

Install Spamassasin: ::

    apt-get install spamassassin spamc

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
      user=debian-spamd argv=/usr/bin/spamc -f -e
        /usr/sbin/sendmail -oi -f ${sender} ${recipient}
