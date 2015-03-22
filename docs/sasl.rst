Dovecot SASL
------------

Holonet integrates with Dovecot SASL, this can be used to make it possible for remote users to login to the Postfix smtp server.

Install Dovecot: ::

    $ sudo apt-get install dovecot-core

Change the /etc/dovecot/conf.d/10-master.conf: ::

    service auth {
      unix_listener /var/spool/postfix/private/auth {
        mode = 0660
        user = postfix
        group = postfix
      }
    }

Prepeare Postfix for sasl, change /etc/postfic/main.cf: ::

    smtpd_sasl_type = dovecot
    smtpd_sasl_path = private/auth
    queue_directory = /var/spool/postfix
    smtpd_sasl_auth_enable = yes

Enable submission in Postfix master.cf: ::

    submission inet n       -       n       -       -       smtpd
      -o syslog_name=postfix/submission
      -o smtpd_tls_security_level=encrypt
      -o smtpd_sasl_auth_enable=yes
      -o smtpd_sasl_type=dovecot
      -o smtpd_sasl_path=private/auth
      -o smtpd_sasl_local_domain=$myhostname
      -o smtpd_client_restrictions=permit_sasl_authenticated,reject
      -o smtpd_sender_restrictions=reject_sender_login_mismatch
      -o smtpd_relay_restrictions=permit_sasl_authenticated,reject
      -o smtpd_recipient_restrictions=reject_non_fqdn_recipient,reject_unknown_recipient_domain,permit_sasl_authenticated,reject

Change the /etc/dovecot/conf.d/10-auth.conf: ::

    auth_mechanisms = plain login

    passdb {
      driver = dict
      args = /etc/dovecot/dovecot-dict-auth.conf
    }
    userdb {
      driver = prefetch
    }
    userdb {
      driver = dict
      args = /etc/dovecot/dovecot-dict-auth.conf
    }

    #!include auth-system.conf.ext

Configure the Holonet listener, /etc/dovecot/dovecot-dict-auth.conf: ::
