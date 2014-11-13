# -*- coding: utf8 -*-

from django.core.mail.backends.base import BaseEmailBackend


class EmailBackend(BaseEmailBackend):

    def __init__(self, **kwargs):
        super(EmailBackend, self).__init__(**kwargs)

    def open(self):
        pass

    def close(self):
        pass

    def send_messages(self, email_messages):
        raise NotImplementedError(
            'subclasses of BaseEmailBackend must override send_messages() method'
        )
