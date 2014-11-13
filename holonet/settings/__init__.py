# -*- coding: utf8 -*-
import sys

from holonet.settings.base import *
from holonet.settings.holonet import *

TESTING = 'test' in sys.argv

if TESTING:
    from holonet.settings.test import *

try:
    from holonet.settings.local import *
except ImportError as e:
    raise ImportError("Couldn't load local settings holonet.settings.local")
