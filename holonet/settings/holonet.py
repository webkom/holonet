# -*- coding: utf8 -*-

SHELL_PLUS = 'ipython'

EXITCODE_UNKNOWN_RECIPIENT = 67
EXITCODE_UNKNOWN_DOMAIN = 68

REJECT_ACTION = 'REJECT'
ACCEPT_ACTION = 'DUNNO'

SENDMAIL_EXECUTABLE = '/usr/sbin/sendmail'
SENDMAIL_BATCH_LENGTH = 40

MASTER_DOMAINS = [
    'test.holonet.no'
]
MASTER_DOMAIN = MASTER_DOMAINS[0]


EMAIL_SUBJECT_PREFIX = u'[%s] ' % 'Holonet'
SERVER_EMAIL = 'bounce@holonet.no'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

RESTRICTED_PREFIX = 'restricted'

UNSUBSCRIBE_LINK = '<http://holonet.no> - go to your profile and unregister'

EMAIL_BACKEND = 'holonet.backends.sendmail.EmailBackend'

ELASTICSEARCH = [
    {'host': '127.0.0.1', 'port': 9200, 'use_ssl': False},
]

INDEX_NAME = 'holonet'

BROKER_URL = 'amqp://guest:guest@localhost:5672/'

SYSTEM_ALIASES = [
    'root',
    'postmaster'
]

# Please don't use emails handled by Holonet. Magic things may happen!
ADMINS = (
    ('Eirik Martiniussen Sylliaas', 'eirik@sylliaas.no'),
)

MANAGERS = ADMINS

STATUS_CLASSES = (
    'holonet.status.ElasticsearchStatus',
    'holonet.status.CacheStatus',
    'holonet.status.CeleryStatus',
    'holonet.status.WebSocketsStatus',
    'holonet.status.PolicyServiceStatus',
    'holonet.status.PostfixStatus',
)

POSTFIX_URL = 'tcp://127.0.0.1:25'

POLICYSERVICE_URL = 'tcp://127.0.0.1:10336'

SYSTEM_OWNER = 'Abakus Linjeforening / Webkom'
