# -*- coding: utf8 -*-

from io import BytesIO


class HolonetEmailMessage(object):

    encoding = None

    def __init__(self, msg, list_recipients, connection=None):
        self.msg = msg
        self.list_recipients = list_recipients
        self.connection = connection
        super(HolonetEmailMessage, self).__init__()

    def __getitem__(self, item):
        return self.msg.get(item)

    def keys(self):
        return self.msg.keys()

    def values(self):
        return self.msg.values()

    def __contains__(self, item):
        return item in self.msg

    def get(self, key, default=None):
        if key in self:
            return self[key]
        else:
            return default

    def recipients(self):
        return self.list_recipients

    def message(self):
        return self

    def get_connection(self, fail_silently=False):
        from django.core.mail import get_connection
        if not self.connection:
            self.connection = get_connection(fail_silently=fail_silently)
        return self.connection

    def send(self, fail_silently=False):
        if not self.recipients():
            return 0
        return self.get_connection(fail_silently).send_messages([self])

    def as_bytes(self, unixfrom=False, policy=None, linesep='\n'):
        from email.generator import BytesGenerator
        policy = self.msg.policy if policy is None else policy
        fp = BytesIO()
        g = BytesGenerator(fp, mangle_from_=False, policy=policy)
        g.flatten(self.msg, unixfrom=unixfrom, linesep=linesep)
        return fp.getvalue()

    def index(self):
        body = {
            'source': self.msg.as_string(),
            'X-List-Recipients': self.recipients()
        }

        for key in self.keys():
            body[key] = self[key]

        return body
