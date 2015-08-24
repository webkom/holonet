from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from holonet.lists.helpers import lookup
from holonet.lists.models import MailingList, Recipient
from holonet.lists.serializers import MailingListSerializer, RecipientSerializer


class ReverseLookupTestCase(APITestCase):

    fixtures = ['users.yaml', 'domains.yaml', 'mailing_lists.yaml', 'recipients.yaml']

    def setUp(self):
        self.client.force_authenticate(user=User.objects.get(username='testuser1'))
        self.endpoint = '/lookup/lookup/'

    def test_reverse_lookup(self):
        stored_recipients = MailingList.objects.get(prefix='testlist1').recipients

        data = {
            'email': 'testlist1'
        }

        response = self.client.post(self.endpoint, data=data,  format='json')

        self.assertEqual(len(response.data), len(stored_recipients))

        data = {
            'email': 'testlist1@%s' % settings.MASTER_DOMAIN
        }

        response = self.client.post(self.endpoint, data=data,  format='json')

        self.assertEqual(len(response.data), len(stored_recipients))

        data = {
            'email': 'testlist1@%s@random' % settings.MASTER_DOMAIN
        }

        response = self.client.post(self.endpoint, data=data,  format='json')

        self.assertEquals(len(response.data), len(lookup('testlist1')))

    def test_no_email(self):
        response = self.client.post(self.endpoint, format='json')

        self.assertListEqual(response.data, [])

    def test_unsupported_domain(self):
        data = {
            'email': 'testlist1@test.notsupported.no'
        }

        response = self.client.post(self.endpoint, data=data,  format='json')

        self.assertListEqual(response.data, [])

    def test_system_alias(self):
        data = {
            'email': '%s@%s' % (settings.SYSTEM_ALIASES[0], settings.MASTER_DOMAIN)
        }

        response = self.client.post(self.endpoint, data=data, format='json')

        self.assertEqual(len(response.data), len(settings.ADMINS))

    def test_no_mailinglist(self):
        data = {
            'email': 'unknown@%s' % settings.MASTER_DOMAIN
        }

        response = self.client.post(self.endpoint, data=data, format='json')

        self.assertListEqual(response.data, [])


class RecipientViewSetTestCase(APITestCase):

    fixtures = ['users.yaml', 'recipients.yaml']

    def setUp(self):
        self.client.force_authenticate(user=User.objects.get(username='testuser1'))

    def test_get_recipients(self):
        response = self.client.get('/recipient/', format='json')

        db_data = RecipientSerializer(data=Recipient.objects.all(), many=True)
        db_data.is_valid()

        self.assertListEqual(response.data, db_data.data)

    def test_add_recipient(self):
        data = {'address': 'holonettest@test.holonet.no', 'tag': 'holonettest'}
        response = self.client.post('/recipient/', data=data, format='json')

        self.assertEqual(data, response.data)

    def test_delete_recipient(self):
        self.assertTrue(Recipient.objects.filter(tag='testuser4').exists())
        self.client.delete('/recipient/testuser4/', format='json')
        self.assertRaises(Recipient.DoesNotExist, Recipient.objects.get, tag='testuser4')

    def test_change_recipient(self):
        response = self.client.patch('/recipient/testuser4/', format='json',
                                     data={'address': 'test@holonet.no'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Recipient.objects.get(tag='testuser4').address, 'test@holonet.no')


class MailinglistViewSetTestCase(APITestCase):

    fixtures = ['users.yaml', 'domains.yaml', 'recipients.yaml', 'mailing_lists.yaml']

    def setUp(self):
        self.client.force_authenticate(user=User.objects.get(username='testuser1'))

    def test_get_mailinglists(self):
        response = self.client.get('/mailinglist/', format='json')

        db_data = MailingListSerializer(data=MailingList.objects.all(), many=True)
        db_data.is_valid()

        self.assertListEqual(response.data, db_data.data)
