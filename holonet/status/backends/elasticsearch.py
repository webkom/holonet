from holonet.status.base import StatusCheck


class ElasticsearchStatus(StatusCheck):

    name = 'elasticsearch'

    @property
    def status(self):
        return 0
