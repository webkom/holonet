Holonet Handler
---------------

The mail_handler is the main funtion in holonet. Postfix pipes mail into holonet and holonet decides what do do with it and lookup the recipients.

Postfix needs to know where to deliver local mails:

/etc/postfix/main.cf: ::

    local_transport = holonet
    holonet_destination_recipient_limit = 1

/etc/postfix/master.cf: ::

    holonet    unix    -       n       n       -       -       pipe
      user=$LOCALUSER argv=python $PROJECT_DIR/manage.py mail_handler ${sender} ${recipient}

