Spamassasin
-----------

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
