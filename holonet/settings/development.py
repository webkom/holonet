from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE_CLASSES, REST_FRAMEWORK

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = 'secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'holonet',
        'USER': 'holonet',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0',
    }
}

EMAIL_BACKEND = 'django.utils.mail.backends.console.EmailBackend'

BROKER_URL = 'redis://127.0.0.1'

ELASTICSEARCH = {
    'default': {
        'hosts': [
            '127.0.0.1:9200'
        ]
    }
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ['rest_framework.renderers.BrowsableAPIRenderer']

INSTALLED_APPS += ('debug_toolbar', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
INTERNAL_IPS = ('127.0.0.1', )

POSTFIX_TRANSPORT_MAPS_LOCATION = '{0}/../mta/shared/'.format(BASE_DIR)
