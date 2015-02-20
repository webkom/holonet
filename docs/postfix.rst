Postfix
-------

Postfix needs to accept all recipients:

/etc/postfix/main.cf: ::

    luser_relay = $LOCALUSER
    local_recipient_maps =

Postfix needs to know the destination domains: ::

    mydestination = holonet.abakus.no, localhost.abakus.no, localhost, abakus.no
