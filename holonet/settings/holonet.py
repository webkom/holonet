# -*- coding: utf8 -*-

SHELL_PLUS = 'ipython'

EXITCODE_UNKNOWN_RECIPIENT = 67
EXITCODE_UNKNOWN_DOMAIN = 68

REJECT_ACTION = 'REJECT'
ACCEPT_ACTION = 'DUNNO'

SENDMAIL_EXECUTABLE = '/usr/sbin/sendmail'
SENDMAIL_BATCH_LENGTH = 40

MASTER_DOMAINS = [
    'test.holonet.no',
]
MASTER_DOMAIN = MASTER_DOMAINS[0]


EMAIL_SUBJECT_PREFIX = u'[%s] ' % 'Holonet'
SERVER_EMAIL = 'bounce@holonet.no'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

RESTRICTED_PREFIX = 'restricted'
RESTRICTED_TOKEN_PREFIX = 'holonet'

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
    'holonet.status.PolicyServiceStatus',
    'holonet.status.SASLServiceStatus',
    'holonet.status.PostfixStatus',
)

POSTFIX_URL = 'tcp://127.0.0.1:25'

INCOMING_SOCKET_LOCATION = 'incoming_policy'
OUTGOING_SOCKET_LOCATION = 'outgoing_policy'

SYSTEM_NAME = 'Holonet Mail Delivery System'
SYSTEM_OWNER = 'Holonet'
SYSTEM_SUPPORT = 'contact@holonet.no'

SMTP_SERVER = 'smtp.holonet.no'
SMTP_PORT = 587
SMTP_ENCRYPTION_METHOD = 'STARTTLS'
SMTP_AUTHENTICATION_METHOD = 'plain or login'

SENDER_WHITELIST_ENABLED = False
DOMAIN_WHITELIST_ENABLED = SENDER_WHITELIST_ENABLED

SASL_SOCKET_LOCATION = 'sasl_authentication'
SASL_LUSER_HOME = '/home/holonet'
SASL_LUSER_UID = '1001'
SASL_LUSER_GID = '1001'
