import sys

TESTING = 'test' in sys.argv[:2]

from .base import *  # noqa
from .logging import *  # noqa
from .holonet import *  # noqa

if TESTING:
    from .test import *  # noqa
else:
    try:
        from .local import *  # noqa
    except ImportError:
        print('Unable to load local settings.')

from .celery import app as celery_app  # noqa
