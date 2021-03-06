import socket

from holonet.settings import TESTING


def skip_if_testing(*args, **kwargs):
    return not TESTING

hostname = socket.gethostname()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG',
        'handlers': ['sentry', 'console', 'syslog'],
    },
    'filters': {
        'skip_if_testing': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_if_testing,
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s [%(name)s] %(message)s'
        },
        'syslog': {
            'format': '{hostname} holonet[%(process)d]: [%(name)s] %(message)s'.format(
                hostname=hostname)
        }
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'filters': ['skip_if_testing'],
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['skip_if_testing'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'syslog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local7',
            'formatter': 'syslog',
        }
    },
    'loggers': {
        'celery': {
            'level': 'DEBUG',
            'propagate': True,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'level': 'DEBUG',
            'propagate': True,
            'filters': ['require_debug_true'],
        },
        'django.requests': {
            'level': 'DEBUG',
            'propagate': True,
            'filters': ['require_debug_true'],
        },
        'invoke': {
            'level': 'WARNING',
            'propagate': True
        }
    },
}
