import logging
import os

import djcelery
from django.conf.global_settings import AUTHENTICATION_BACKENDS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'e6c95!2(*@31_)hel5h7-ag**ozwn=s@veoh+n$-y8a-!bn=@$'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cachalot',
    'django_extensions',
    'crispy_forms',
    'djcelery',
    'rest_framework',
    'corsheaders',
    'raven.contrib.django.raven_compat',
    'pipeline',

    'holonet.core',
    'holonet.mappings',
    'holonet.restricted',
    'holonet.dashboard',
    'holonet.api',
    'holonet.status',
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
    'pipeline.middleware.MinifyHTMLMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
)

AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
    'django.contrib.auth.backends.ModelBackend',
)

OAUTH2_PROVIDER_APPLICATION_MODEL = 'api.APIApplication'

ROOT_URLCONF = 'holonet.urls'

WSGI_APPLICATION = 'holonet.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.db'),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_DIRS = (
    ('assets', os.path.join(BASE_DIR, 'assets')),
    ('bower', os.path.join(os.path.dirname(BASE_DIR), 'bower_components')),
)

PIPELINE_COMPILERS = (
    'pipeline.compilers.stylus.StylusCompiler',
)
PIPELINE_STYLUS_BINARY = os.path.join(os.path.dirname(BASE_DIR), 'node_modules/stylus/bin/stylus')
PIPELINE_STYLUS_NIB = os.path.join(os.path.dirname(BASE_DIR), 'node_modules/nib/lib')
PIPELINE_STYLUS_CWD = os.path.join(BASE_DIR, 'assets/styl/')
PIPELINE_STYLUS_ARGUMENTS = '--include %s --include %s --compress' % (PIPELINE_STYLUS_NIB,
                                                                      PIPELINE_STYLUS_CWD)

PIPELINE_YUGLIFY_BINARY = os.path.join(os.path.dirname(BASE_DIR),
                                       'node_modules/yuglify/bin/yuglify')

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_UGLIFYJS_BINARY = os.path.join(os.path.dirname(BASE_DIR),
                                        'node_modules/uglify-js/bin/uglifyjs')

PIPELINE_JS = {
    'components': {
        'source_filenames': (
            'bower/jquery/dist/jquery.js',
            'bower/bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/components.js',
    },
    'holonet': {
        'source_filenames': (
            'asstest/js/holonet.js',
        ),
        'output_filename': 'js/holonet.js',
    },
}

PIPELINE_CSS = {
    'components': {
        'source_filenames': (
            'bower/bootstrap/dist/css/bootstrap.css',
            'bower/font-awsome/css/font-awesome.css',
        ),
        'output_filename': 'css/components.css'
    },
    'holonet': {
        'source_filenames': (
            'assets/styl/style.styl',
        ),
        'output_filename': 'css/holonet.css'
    }
}

djcelery.setup_loader()

SENTRY_CELERY_LOGLEVEL = logging.WARNING
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_RESULT_BACKEND = 'djcelery.backends.database.DatabaseBackend'
CELERY_TRACK_STARTED = True
CELERY_SEND_EVENTS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'holonet.api.backend.TokenAuthenticationBackend',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'holonet.api.backend.StaffRequired',
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO',
        'handlers': ['sentry', 'console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'raven': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
