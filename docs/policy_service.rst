Holonet Policy Service
----------------------

Holonet has two policy services, one for incoming and one for outgoing mail. Incoming mail is mail
received with normal smtp without user authentication. The outgoing policy service validates sasl
username and the MAIL_FROM header. This prevents users from sending mail as a other user. The
incoming policy service does a lookup in the mailing lists to find if the RCPT TO parameter is
handeled by Holonet. The services is not required, the same validation runs when Postfix pipes
the mail into Holonet later in the process. The policy services listens on a tcp socket.
The policy services implements a simple query language defined by Postfix.


Incoming policy service, **/etc/postfix/main.cf** ::

    smtpd_relay_restrictions =
            permit_mynetworks
            permit_sasl_authenticated
            defer_unauth_destination
            check_policy_service inet:127.0.0.1:10336
            reject

            # NB! Postfix Version >= 3.0
            check_policy_service { inet:host:port, timeout=10s, default_action=DUNNO }


Then start the policy service with the management command: ::

    python $PROJECT_DIR/manage.py incoming_policy

Usage of the outgoing policy is described in the document about SASL.
