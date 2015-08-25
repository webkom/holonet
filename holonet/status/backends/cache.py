from holonet.status.base import StatusCheck


class CacheStatus(StatusCheck):

    name = 'cache'

    @property
    def status(self):
        return 0
