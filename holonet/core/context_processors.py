# -*- coding: utf8 -*-
from django.conf import settings
from omnibus.authenticators import UserAuthenticator
from omnibus.compat import split_domain_port
from omnibus.settings import SERVER_BASE_URL, SERVER_HOST, SERVER_PORT


def omnibus(request):
    auth_token = ''
    if hasattr(request, 'user') and request.user.is_authenticated():
        auth_token = '{0}:{1}'.format(
            request.user.pk, UserAuthenticator.get_auth_token(request.user.pk))

    server_port = SERVER_PORT
    if split_domain_port(request.get_host())[0] != '127.0.0.1' and \
       split_domain_port(request.get_host())[0] != 'localhost' and \
       settings.OMNIBUS_ENDPOINT_SCHEME == 'https':
        server_port = 443

    return {
        'OMNIBUS_ENDPOINT': u'{0}://{1}:{2}{3}'.format(
            settings.OMNIBUS_ENDPOINT_SCHEME,
            SERVER_HOST or split_domain_port(request.get_host())[0],
            server_port,
            SERVER_BASE_URL
        ),
        'OMNIBUS_AUTH_TOKEN': auth_token
    }
