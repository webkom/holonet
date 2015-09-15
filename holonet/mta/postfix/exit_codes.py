import sys

from holonet.interfaces.exit_codes import ExitCodes

DATA_ERROR = 65
NO_USER = 67
NO_HOST = 68
SERVICE_UNAVAILABLE = 69
SOFTWARE_ERROR = 70

REJECT_ACTION = 'REJECT'
ACCEPT_ACTION = 'DUNNO'


class PostfixPipeExit(ExitCodes):

    def data_error(self):
        return sys.exit(DATA_ERROR)

    def no_recipient(self):
        return sys.exit(NO_USER)

    def no_domain(self):
        return sys.exit(NO_HOST)

    def service_unavailable(self):
        return sys.exit(SERVICE_UNAVAILABLE)

    def system_error(self):
        return sys.exit(SOFTWARE_ERROR)


class PostfixPolicyServiceExit(ExitCodes):

    def data_error(self):
        return '{} Message data error'.format(REJECT_ACTION)

    def no_recipient(self):
        return '{} Address does not exist'.format(REJECT_ACTION)

    def no_domain(self):
        return '{} Domain not handled by Holonet'.format(REJECT_ACTION)

    def service_unavailable(self):
        return '{} Service unaviable'.format(REJECT_ACTION)

    def system_error(self):
        return '{} Holonet System Error'.format(REJECT_ACTION)
