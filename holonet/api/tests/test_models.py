# -*- coding: utf8 -*-

import datetime

from django.test import TestCase
from django.utils import timezone

from holonet.api.models import Application, Token
from holonet.api.exceptions import TokenDoesNotExistException


class ModelsTestCase(TestCase):
    fixtures = ['applications.yaml', 'tokens.yaml']

    def test_get_token(self):
        now = timezone.now()

        token = Token.objects.get(token='secret_token')
        self.assertEquals(Token.get_token('secret_token'), token)

        token.valid_from = now + datetime.timedelta(hours=1)
        token.save()
        self.assertRaises(TokenDoesNotExistException, Token.get_token, 'secret_token')

        token.valid_from = now - datetime.timedelta(hours=1)
        token.save()
        self.assertEquals(Token.get_token('secret_token'), token)

        token.valid_from = None
        token.valid_to = now + datetime.timedelta(hours=1)
        token.save()
        self.assertEquals(Token.get_token('secret_token'), token)

        token.valid_from = None
        token.valid_to = now - datetime.timedelta(hours=1)
        token.save()
        self.assertRaises(TokenDoesNotExistException, Token.get_token, 'secret_token')

        token.valid_from = now - datetime.timedelta(hours=1)
        token.valid_to = now + datetime.timedelta(hours=1)
        token.save()
        self.assertEquals(Token.get_token('secret_token'), token)

        token.valid_from = now + datetime.timedelta(hours=1)
        token.valid_to = now - datetime.timedelta(hours=1)
        token.save()
        self.assertRaises(TokenDoesNotExistException, Token.get_token, 'secret_token')

    def test_unknown_token(self):
        self.assertRaises(TokenDoesNotExistException, Token.get_token, 'unknown')

    def test_application_perms(self):
        application = Application.objects.first()
        self.assertTrue(application.has_perm('unknown_perm'))
        self.assertTrue(application.has_perms(['unknown_perm']))
        self.assertTrue(application.is_authenticated())
