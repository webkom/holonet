import smtpd
import asyncore

from django.conf import settings

from holonet.services.runner import Runner
from holonet.services.lmtp import channel
from holonet.core.parser import EmailParser
from holonet.core.parser.exceptions import ParseEmailException, MessageIDNotExistException, \
    DefectMessageException

smtpd.__version__ = 'Holonet LMTP'


class LMTPRunner(Runner, smtpd.SMTPServer):

    is_queue_runner = False
    name = 'lmtp'

    def run(self):
        asyncore.loop()

    def close(self):
        asyncore.socket_map.clear()
        asyncore.close_all()

    def __init__(self):
        localaddr = settings.LMTP_HOST, int(settings.LMTP_PORT)
        self.log.debug('LMTP server listening on {}:{}'.format(localaddr[0], localaddr[1]))
        smtpd.SMTPServer.__init__(self, localaddr, remoteaddr=None)
        super(LMTPRunner, self).__init__()

    def handle_accept(self):
        conn, addr = self.accept()
        channel.Channel(self, conn, addr)
        self.log.debug('LMTP accept from %s', addr)

    def process_message(self, peer, mailfrom, rcpttos, data):
        parser = EmailParser(data, mailfrom, 'string')

        try:
            message = parser.parse()
        except ParseEmailException:
            self.log.exception('LMTP could not parse the incoming email.')
            return channel.CRLF.join(channel.ERR_451 for to in rcpttos)
        except MessageIDNotExistException:
            return channel.ERR_550_MID
        except DefectMessageException:
            return channel.ERR_501

        status = []
        for to in rcpttos:
            status.append('250 Ok')

        return channel.CRLF.join(status)
