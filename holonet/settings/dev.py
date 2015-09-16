from .base import INSTALLED_APPS

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = '0&e=or16z)nrsl6u(h=8((763+1pckt@o@7xrgje4ht((_61j='

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
