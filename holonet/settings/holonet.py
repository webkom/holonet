SITE = {
    'name': 'Holonet Mail Delivery System',
}

# System admins
# Please don't use emails handled by Holonet. Magic things may happen!
ADMINS = (
    ('Holonet Administrator', 'mail-manager@holonet.com'),
)

MANAGERS = ADMINS

# Postfix
POSTFIX_POSTMAP_COMMAND = 'postmap'
POSTFIX_TRANSPORT_MAPS_LOCATION = None

# LMTP
LMTP_HOST = '127.0.0.1'
LMTP_PORT = 8024

# Transport Maps
TRANSPORT_MAP_LMTP_HOST = LMTP_HOST
TRANSPORT_MAP_LMTP_PORT = LMTP_PORT

# Backend for outgoing email
EMAIL_BACKEND = 'django.utils.mail.backends.smtp.EmailBackend'

# Email options for system mail
EMAIL_SUBJECT_PREFIX = u'[%s] ' % 'Holonet'
SERVER_EMAIL = 'bounce@holonet.no'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

# VERP settings
VERP_ENABLED = True
VERP_DELIMITER = '+='
