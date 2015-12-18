import os

import environ

from holonet.settings import BASE_DIR

root = environ.Path(__file__) - 3
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db()
}

CACHES = {
    'default': env.cache(),
}

SECRET_KEY = env('SECRET_KEY')

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats-prod.json')
    }
}
