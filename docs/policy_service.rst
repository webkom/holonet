Holonet Policy Service
----------------------

Holonet Policy Service does a lookup in the mailing lists to find if the RCPT TO parameter is handeled by Holonet. This service is not required, the same validation is ran when Postfix pipes the mail into holonet later in the process. The default address and port is tcp://127.0.0.1:10336. The policy service impliments a simple query language defined by Postfix.

**/etc/postfix/main.cf** ::

    smtpd_relay_restrictions =
            permit_mynetworks
            permit_sasl_authenticated
            defer_unauth_destination
            check_policy_service inet:127.0.0.1:10336

            check_policy_service { inet:host:port, timeout=10s, default_action=DUNNO } # NB! Postfix Version >= 3.0


Then start the policy service with the management command: ::

    python $PROJECT_DIR/manage.py policy_service
