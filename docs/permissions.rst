User and Application permissions
================================

User permissions
----------------

It is three (3) levels of permissions:

* active
* staff
* superuser

An active user can login on the webpage and get its sasl token. A active user has the right to
logon the smtp server using Holonet SASL.

Staff user has can access the dashboard and search in bounce, spam and blacklisted email. The staff
user has read-only access to the api.

Superuser can change mappings, access the admin page and create mailing lists.

A user has always lower rights too.

Application permissions
-----------------------

An application has read-write access to the api if it has a valid token. Extensions like
django-holonet uses this kind of permission.
