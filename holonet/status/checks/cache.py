from holonet.interfaces.status_check import StatusCheck


class CacheStatus(StatusCheck):

    name = 'cache'

    @property
    def status(self):
        return 0
