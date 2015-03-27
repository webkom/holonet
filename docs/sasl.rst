Dovecot SASL
------------

Holonet integrates with Dovecot SASL, this can be used to make it possible for remote users to
login to the Postfix smtp server.
All active users in the user database gets a token. The user can login on the web interface to see
the generated token.

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
    smtpd_helo_restrictions = reject_unknown_helo_hostname

Enable submission in Postfix master.cf: ::

    submission inet n       -       n       -       -       smtpd
      -o syslog_name=postfix/submission
      -o smtpd_tls_security_level=encrypt
      -o smtpd_sasl_auth_enable=yes
      -o smtpd_sasl_type=dovecot
      -o smtpd_sasl_path=private/auth
      -o smtpd_sasl_local_domain=
      -o smtpd_client_restrictions=permit_sasl_authenticated,reject
      -o smtpd_sender_restrictions=reject_unknown_sender_domain
      -o smtpd_relay_restrictions=permit_sasl_authenticated,reject
      -o smtpd_recipient_restrictions=reject_non_fqdn_recipient,permit_sasl_authenticated,reject

Change the /etc/dovecot/conf.d/10-auth.conf: ::

    auth_mechanisms = plain login

    passdb {
      driver = dict
      args = /etc/dovecot/dovecot-dict-auth.conf
    }
    userdb {
      driver = prefetch
    }

    #!include auth-system.conf.ext

Configure the Holonet listener, /etc/dovecot/dovecot-dict-auth.conf: ::

    uri = proxy:/home/holonet/holonet/sasl_socket:holonet

    password_key = passdb/%u/%w
    user_key = userdb/%u/%w
    iterate_disable = yes
    default_pass_scheme = plain
