# -*- coding: utf8 -*-

from django.test import TestCase

from holonet.restricted.models import RestrictedMapping


class RestrictedModelTestCase(TestCase):

    fixtures = ['recipients.yaml', 'restricted_mappings.yaml']

    def test_token_get(self):
        token = '6375717d-9296-4db8-a0ec-40855cb94d79'
        mapping = RestrictedMapping.objects.get(token=token)
        get_token = RestrictedMapping.get_token(token)

        self.assertEqual(get_token, mapping)

        mapping.mark_sent()
        self.assertRaises(RestrictedMapping.DoesNotExist, RestrictedMapping.get_token, token)

    def test_token_generator(self):
        token = '6375717d-9296-4db8-a0ec-40855cb94d79'
        mapping = RestrictedMapping.objects.get(token=token)

        mapping.regenerate_token()
        self.assertNotEqual(token, mapping.token)

    def test_recipients(self):
        token = '6375717d-9296-4db8-a0ec-40855cb94d79'
        mapping = RestrictedMapping.objects.get(token=token)

        self.assertEquals(len(mapping.recipients), mapping.recipient_list.count())

    def test_save_without_token(self):
        mapping = RestrictedMapping(from_address='test@holonet.no')
        mapping.save()

        self.assertIsNotNone(mapping.token)

    def test_duplicate_tags(self):
        mapping1 = RestrictedMapping.objects.get(pk=1)
        mapping2 = RestrictedMapping.objects.get(pk=2)

        mapping1.tag = '1'
        mapping2.tag = '1'

        mapping1.save()

        self.assertRaises(ValueError, mapping2.save)

        mapping2.tag = ''
        self.assertIsNone(mapping2.save())

        mapping1.tag = ''
        self.assertIsNone(mapping1.save())
