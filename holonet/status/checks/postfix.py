from holonet.interfaces.status_check import StatusCheck


class PostfixStatus(StatusCheck):

    name = 'postfix'

    @property
    def status(self):
        return 0
