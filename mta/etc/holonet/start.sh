#!/bin/bash

echo "Starting Holonet MTA..."

/usr/sbin/postfix -c /etc/postfix start
/usr/sbin/dovecot -c /etc/dovecot/dovecot.conf

/sbin/my_init
