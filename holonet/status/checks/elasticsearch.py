from holonet.interfaces.status_check import StatusCheck


class ElasticsearchStatus(StatusCheck):

    name = 'elasticsearch'

    @property
    def status(self):
        return 0
