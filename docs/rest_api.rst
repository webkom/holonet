Holonet REST API
================

Information
-----------

.. http:get:: /api/information/

    Information about the running configuration of the system.

    **Example request**:

    .. sourcecode:: http

        GET /api/information/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, HEAD, OPTIONS
        Vary: Accept

        {
            "System Owner": "Abakus Linjeforening / Webkom",
            "Server Email": "bounce@holonet.no",
            "Master Domains": [
                "test.holonet.no"
            ],
            "Admins": [
                [
                    "Eirik Martiniussen Sylliaas",
                    "eirik@sylliaas.no"
                ]
            ],
            "System Aliases": [
                "root",
                "postmaster"
            ],
            "Restricted Email": "restricted@test.holonet.no"
        }

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error

Sender Blacklist
----------------

.. http:get:: /api/sender-blacklist/

    List blacklisted senders.

    **Example request**:

    .. sourcecode:: http

        GET /api/sender-blacklist/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, POST, HEAD, OPTIONS
        Vary: Accept

        [
            {
                "id": 1,
                "sender": "spam@spamsender.com"
            }
        ]

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error

.. http:post:: /api/sender-blacklist/

    Add blacklisted sender.

    **Example request**:

    .. sourcecode:: http

        POST /api/sender-blacklist/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

        {
            "sender": "test@spam.com"
        }

    **Example response**:

    .. sourcecode:: http

        HTTP 201 CREATED
        Content-Type: application/json
        Allow: GET, POST, HEAD, OPTIONS
        Vary: Accept

        {
            "id": 2,
            "sender": "test@spam.com"
        }

    :reqheader Authorization: Session auth or token

    :statuscode 201: Created

.. http:get:: /api/sender-blacklist/(int:sender_id)

    Get blacklisted sender.

    **Example request**:

    .. sourcecode:: http

        GET /api/sender-blacklist/1 HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, DELETE, HEAD, OPTIONS
        Vary: Accept

        {
            "id": 1,
            "sender": "spam@spamsender.com"
        }

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error
    :statuscode 404: Sender not found

.. http:delete:: /api/sender-blacklist/(int:sender_id)

    Delete blacklisted sender.

    **Example request**:

    .. sourcecode:: http

        DELETE /api/sender-blacklist/1/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 204 NO CONTENT
        Content-Type: application/json
        Allow: GET, DELETE, HEAD, OPTIONS
        Vary: Accept


    :reqheader Authorization: Session auth or token

    :statuscode 204: No content
    :statuscode 404: Sender not found

Domain Blacklist
----------------

.. http:get:: /api/domain-blacklist/

    List blacklisted domains.

    **Example request**:

    .. sourcecode:: http

        GET /api/domain-blacklist/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, POST, HEAD, OPTIONS
        Vary: Accept

        [
            {
                "id": 1,
                "domain": "spamsender.com"
            }
        ]

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error

.. http:post:: /api/domain-blacklist/

    Add blacklisted domain.

    **Example request**:

    .. sourcecode:: http

        POST /api/domain-blacklist/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

        {
            "domain": "spam.com"
        }

    **Example response**:

    .. sourcecode:: http

        HTTP 201 CREATED
        Content-Type: application/json
        Allow: GET, POST, HEAD, OPTIONS
        Vary: Accept

        {
            "id": 2,
            "domain": "spam.com"
        }

    :reqheader Authorization: Session auth or token

    :statuscode 201: Created

.. http:get:: /api/domain-blacklist/(int:domain_id)

    Get blacklisted domain.

    **Example request**:

    .. sourcecode:: http

        GET /api/domain-blacklist/1 HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, DELETE, HEAD, OPTIONS
        Vary: Accept

        {
            "id": 1,
            "domian": "spamsender.com"
        }

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error
    :statuscode 404: Sender not found

.. http:delete:: /api/domain-blacklist/(int:domain_id)

    Delete blacklisted domain.

    **Example request**:

    .. sourcecode:: http

        DELETE /api/domain-blacklist/1/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 204 NO CONTENT
        Content-Type: application/json
        Allow: GET, DELETE, HEAD, OPTIONS
        Vary: Accept


    :reqheader Authorization: Session auth or token

    :statuscode 204: No content
    :statuscode 404: Sender not found

Status
------

.. http:get:: /api/status/

    Get the current status for system services.

    **Example request**:

    .. sourcecode:: http

        GET /api/status/ HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, HEAD, OPTIONS
        Vary: Accept

        [
            {
                "name": "elasticsearch",
                "status": 0
            },
            {
                "name": "cache",
                "status": 1
            },
            {
                "name": "celery",
                "status": 0
            },
            {
                "name": "websockets",
                "status": 0
            },
            {
                "name": "policyservice",
                "status": 0
            },
            {
                "name": "postfix",
                "status": 1
            }
        ]

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error

.. http:get:: /api/status/types

    Get available status codes.

    **Example request**:

    .. sourcecode:: http

        GET /api/status/types HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, HEAD, OPTIONS
        Vary: Accept

        [
            [
                0,
                "Not Responding"
            ],
            [
                1,
                "Ready"
            ],
            [
                2,
                "Unknown"
            ]
        ]

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error

.. http:get:: /api/status/(str:service_name)

    Get service status for a specific service.

    **Example request**:

    .. sourcecode:: http

        GET /api/status/elasticsearch HTTP/1.1
        Host: holonet.abakus.no
        Accept: application/json, text/javascript

    **Example response**:

    .. sourcecode:: http

        HTTP 200 OK
        Content-Type: application/json
        Allow: GET, HEAD, OPTIONS
        Vary: Accept

        {
            "name": "elasticsearch",
            "status": 0
        }

    :reqheader Authorization: Session auth or token

    :statuscode 200: No error


