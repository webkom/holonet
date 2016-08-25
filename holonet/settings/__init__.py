import sys
import os

TESTING = 'test' in sys.argv[:2]

from .base import *  # noqa
from .logging import *  # noqa
from .holonet import *  # noqa

if TESTING:
    from .test import *  # noqa
else:
    if os.environ.get('ENV_CONFIG'):
        from .environment import *  # noqa
    else:
        try:
            from .local import *  # noqa
        except ImportError:
            print('Unable to load local settings.')
