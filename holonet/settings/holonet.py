# -*- coding: utf8 -*-

# Postfix exit codes.
EXITCODE_UNKNOWN_RECIPIENT = 67
EXITCODE_UNKNOWN_DOMAIN = 68

# Postfix content-filter actions
REJECT_ACTION = 'REJECT'
ACCEPT_ACTION = 'DUNNO'

# Sendmail backend options
SENDMAIL_EXECUTABLE = '/usr/sbin/sendmail'
SENDMAIL_BATCH_LENGTH = 40

# Domains handled by holonet.
MASTER_DOMAINS = [
    'test.holonet.no',
]
MASTER_DOMAIN = MASTER_DOMAINS[0]

# Email options for system mail
EMAIL_SUBJECT_PREFIX = u'[%s] ' % 'Holonet'
SERVER_EMAIL = 'bounce@holonet.no'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

# Restricted email options
RESTRICTED_PREFIX = 'restricted'
RESTRICTED_TOKEN_PREFIX = 'holonet'

# Unsubscribe link added in every email handled by holonet.
UNSUBSCRIBE_LINK = '<http://holonet.no> - go to your profile and unregister'

# Email backend to process outgoing email
EMAIL_BACKEND = 'holonet.backends.sendmail.EmailBackend'

# Elasticsearch index
INDEX_NAME = 'holonet'

# Celery broker
BROKER_URL = 'amqp://guest:guest@localhost:5672/'

# System aliases (/etc/aliases)
SYSTEM_ALIASES = [
    'root',
    'postmaster'
]

# System admins
# Please don't use emails handled by Holonet. Magic things may happen!
ADMINS = (
    ('Eirik Martiniussen Sylliaas', 'eirik@sylliaas.no'),
)

MANAGERS = ADMINS

# Classes that checks system status
STATUS_CLASSES = (
    'holonet.status.ElasticsearchStatus',
    'holonet.status.CacheStatus',
    'holonet.status.CeleryStatus',
    'holonet.status.PolicyServiceStatus',
    'holonet.status.SASLServiceStatus',
    'holonet.status.PostfixStatus',
)

# Postfix url used by status checks
POSTFIX_URL = 'tcp://127.0.0.1:25'

INCOMING_SOCKET_LOCATION = 'tcp://127.0.0.1:10336'
OUTGOING_SOCKET_LOCATION = 'tcp://127.0.0.1:10337'

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


# Backend to use when storing messages
STORAGE_BACKEND = 'holonet.storage.database'

# Elasticsearch options
ELASTICSEARCH_INDEX_PATTERN = '%W-%Y'
ELASTICSEARCH = {
    'default': {
        'hosts': [
            '127.0.0.1:9200'
        ]
    }
}
