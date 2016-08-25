Project Plan
============

System Overview
---------------

* Holonet generates transport maps for initial list validation
* Postfix listens on port 25 and SSL enabled ports for incoming email
* Postfix forwards emails to Holonet using LMTP
* Holonet looks up recipients based on the RCPT TO header
* Holonet sends the email to the destination based on a DB lookup. (VERP may be used on 1/10 outgoing emails)

* Postfix support submission and user-validation with SASL
* Dovecot SASL sends a request to Holonet for user validation
* Holonet approves the user and the incoming mail is successfully submitted to the mail system

* LEGO pushes lists to Holonet
* Holonet is operative even if LEGO is down
