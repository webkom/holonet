"""
Django settings for holonet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, AUTHENTICATION_BACKENDS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e6c95!2(*@31_)hel5h7-ag**ozwn=s@veoh+n$-y8a-!bn=@$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'omnibus',
    'crispy_forms',
    'djcelery',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',


    'holonet.core',
    'holonet.mappings',
    'holonet.dashboad',
    'holonet.api',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
)

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'holonet.core.context_processors.omnibus',
)

AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
    'django.contrib.auth.backends.ModelBackend',
)

OAUTH2_PROVIDER_APPLICATION_MODEL = 'api.APIApplication'

ROOT_URLCONF = 'holonet.urls'

WSGI_APPLICATION = 'holonet.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'


OMNIBUS_ENDPOINT_SCHEME = 'http'
OMNIBUS_WEBAPP_FACTORY = 'omnibus.factories.sockjs_webapp_factory'
OMNIBUS_CONNECTION_FACTORY = 'omnibus.factories.sockjs_connection_factory'
OMNIBUS_AUTHENTICATOR_FACTORY = 'omnibus.factories.userauthenticator_factory'

WEBSOCKET_CHANNEL = 'holonet'

import djcelery
djcelery.setup_loader()

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_RESULT_BACKEND = 'djcelery.backends.database.DatabaseBackend'
CELERY_TRACK_STARTED = True
CELERY_SEND_EVENTS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'holonet.api.backend.TokenAuthenticationBackend',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}
