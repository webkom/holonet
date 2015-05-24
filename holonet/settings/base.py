import os

from django.conf.global_settings import AUTHENTICATION_BACKENDS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
    'django.contrib.auth.backends.ModelBackend',
)

OAUTH2_PROVIDER_APPLICATION_MODEL = 'api.APIApplication'

ROOT_URLCONF = 'holonet.urls'

WSGI_APPLICATION = 'holonet.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

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
            'assets/js/holonet.js',
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
