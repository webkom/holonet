# -*- coding: utf8 -*-
import sys

TESTING = 'test' in sys.argv

from .base import *
from .logging import *
from .holonet import *

try:
    from .local import *
except ImportError as e:
    print('Unable to load local settings.')

if TESTING:
    from .test import *

from .celery import app as celery_app
