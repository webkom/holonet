Holonet Handler
---------------

Postfix needs to know where to deliver local mails:

/etc/postfix/main.cf: ::

    local_transport = holonet
    holonet_destination_recipient_limit = 1

/etc/postfix/master.cf: ::

    holonet    unix    -       n       n       -       -       pipe
      user=$LOCALUSER argv=$PROJECT_DIR/venv/bin/python $PROJECT_DIR/manage.py mail_handler ${sender} ${recipient}
