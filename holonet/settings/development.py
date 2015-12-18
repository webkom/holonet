import os

from .base import BASE_DIR, INSTALLED_APPS

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = 'secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'holonet',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'holonet',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (
    'debug_toolbar',
)

BROKER_URL = 'redis://127.0.0.1'

REDIS = {
    'host': '127.0.0.1',
}

ELASTICSEARCH = {
    'default': {
        'hosts': [
            '127.0.0.1:9200'
        ]
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats.json')
    }
}
