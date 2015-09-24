import sys

from holonet.interfaces.exit_codes import ExitCodes


class PostfixPipeExit(ExitCodes):

    DATA_ERROR = 65
    NO_USER = 67
    NO_HOST = 68
    SERVICE_UNAVAILABLE = 69
    SOFTWARE_ERROR = 70

    def data_error(self):
        return sys.exit(self.DATA_ERROR)

    def no_recipient(self):
        return sys.exit(self.NO_USER)

    def no_domain(self):
        return sys.exit(self.NO_HOST)

    def service_unavailable(self):
        return sys.exit(self.SERVICE_UNAVAILABLE)

    def system_error(self):
        return sys.exit(self.SOFTWARE_ERROR)


class PostfixPolicyServiceExit(ExitCodes):

    REJECT_ACTION = 'REJECT'
    ACCEPT_ACTION = 'DUNNO'

    def data_error(self):
        return '{} Message data error'.format(self.REJECT_ACTION)

    def no_recipient(self):
        return '{} Address does not exist'.format(self.REJECT_ACTION)

    def no_domain(self):
        return '{} Domain not handled by Holonet'.format(self.REJECT_ACTION)

    def service_unavailable(self):
        return '{} Service unaviable'.format(self.REJECT_ACTION)

    def system_error(self):
        return '{} Holonet System Error'.format(self.REJECT_ACTION)
