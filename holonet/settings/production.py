import os

from holonet.settings import BASE_DIR

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, '../webpack-stats-prod.json')
    }
}
