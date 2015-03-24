Postfix
-------

Holonet uses Postfix as its mail server. The mail server handles the smtp conections. The server recieves list mail and forward it to the recipients.

Postfix needs to accept all recipients, holonet handles address validation:

/etc/postfix/main.cf: ::

    luser_relay = $LOCALUSER
    local_recipient_maps =

Postfix needs to know the destination domains, this is the same as MASTER_DOMAINS setting in the django project: ::

    mydestination = holonet.abakus.no, localhost.abakus.no, localhost, abakus.no
