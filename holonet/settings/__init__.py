# -*- coding: utf8 -*-
import sys

from .base import *
from .holonet import *

TESTING = 'test' in sys.argv

if TESTING:
    from .test import *

try:
    from .local import *
except ImportError as e:
    print('Unable to load local settings.')
