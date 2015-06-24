import sys

TESTING = 'test' in sys.argv

from .base import *  # noqa
from .logging import *  # noqa
from .holonet import *  # noqa

try:
    from .local import *  # noqa
except ImportError:
    print('Unable to load local settings.')

if TESTING:
    from .test import *  # noqa

from .celery import app as celery_app  # noqa
