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

Enable submission in Postfix master.cf: ::

    submission inet n       -       n       -       -       smtpd
      -o syslog_name=postfix/submission
      -o smtpd_tls_security_level=encrypt
      -o smtpd_sasl_auth_enable=yes
      -o smtpd_sasl_type=dovecot
      -o smtpd_sasl_path=private/auth
      -o smtpd_sasl_local_domain=
      -o smtpd_client_restrictions=permit_sasl_authenticated,reject
      -o smtpd_relay_restrictions=permit_sasl_authenticated,reject
      -o smtpd_recipient_restrictions=reject_non_fqdn_recipient,permit_sasl_authenticated,reject

If you want to validate submission mail you could use the outgoing policy service. The outgoing
policy service validates the sasl username and does a lookup to find the lists this user has a
connection to. Append the following setting to the previous file: ::

    -o smtpd_sender_restrictions=
        reject_unknown_sender_domain
        check_policy_service inet:127.0.0.1:10337
        reject

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
