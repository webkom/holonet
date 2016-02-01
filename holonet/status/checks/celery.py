from holonet.interfaces.status_check import StatusCheck


class CeleryStatus(StatusCheck):

    name = 'celery'

    @property
    def status(self):
        return 0
