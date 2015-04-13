Holonet Handler
---------------

Local Transport Handler
=======================

The mail_handler is the main function in Holonet. Postfix pipes mail into Holonet and Holonet
decides what do do with it and lookup the recipients.

Postfix needs to know where to deliver local mails:

/etc/postfix/main.cf: ::

    local_transport = holonet
    holonet_destination_recipient_limit = 1

/etc/postfix/master.cf: ::

    holonet    unix    -       n       n       -       -       pipe
      user=$LOCALUSER argv=python $PROJECT_DIR/manage.py mail_handler ${sender} ${recipient}


Submission Handler
==================

This handler in only for statistics and spam detection in submission mails.

Add content_filter on the submission service, /etc/postfix/main.cf: ::

    submission inet n       -       n       -       -       smtpd
        -o content_filter=holonet_submission


And add the service in the bottom of the file, /etc/postfix/main.cf: ::

    holonet-submission unix -     n       n       -       -       pipe
        user=debian-spamd argv=/usr/bin/spamc -f -e
            /home/holonet/holonet/venv/bin/python /home/holonet/holonet/manage.py submission ${sender} ${recipient}
