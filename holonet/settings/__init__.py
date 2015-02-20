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
    raise ImportError("Couldn't load local settings holonet.settings.local")
