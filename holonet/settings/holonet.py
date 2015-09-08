# System admins
# Please don't use emails handled by Holonet. Magic things may happen!
ADMINS = (
    ('Holonet Administrator', 'mail-manager@holonet.com'),
)

MANAGERS = ADMINS

# System Information
SYSTEM_NAME = 'Holonet Mail Delivery System'
SYSTEM_OWNER = 'Holonet'
SYSTEM_SUPPORT = 'contact@holonet.no'

# Backend to use when storing messages
STORAGE_BACKEND = 'database'  # database or elasticsearch

# Elasticsearch options
ELASTICSEARCH_INDEX_PATTERN = 'holonet-%Y.%W'
ELASTICSEARCH = {
    'default': {
        'hosts': [
            '127.0.0.1:9200'
        ]
    }
}

# LMTP
LMTP_HOST = 'localhost'
LMTP_PORT = 8024

# Backend for outgoing email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Sendmail backend options
SENDMAIL_EXECUTABLE = '/usr/sbin/sendmail'
SENDMAIL_BATCH_LENGTH = 40

# Email options for system mail
EMAIL_SUBJECT_PREFIX = u'[%s] ' % 'Holonet'
SERVER_EMAIL = 'bounce@holonet.no'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

# Celery broker
BROKER_URL = 'amqp://guest:guest@localhost:5672/'
