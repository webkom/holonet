import asyncore
import smtpd

from django.conf import settings

from holonet.core.parser.exceptions import (DefectMessageException, MessageIDNotExistException,
                                            ParseEmailException)
from holonet.interfaces.runner import Runner
from holonet.services.lmtp import channel
from holonet.services.lmtp.paser import LMTPEmailParser

smtpd.__version__ = 'Holonet LMTP'


class LMTPRunner(Runner, smtpd.SMTPServer):
    """
    This runner provides a interface for transporting mail into Holonet using LMTP.
    Command: manage.py lmtp_transport

    Settings:
        LMTP_HOST = 'localhost'
        LMTP_PORT = 8024
    """

    is_queue_runner = False

    name = 'lmtp'
    help = "Start a lmtp server for incoming messages"

    def run(self, *args, **kwargs):
        asyncore.loop()

    def close(self):
        asyncore.socket_map.clear()
        asyncore.close_all()

    def __init__(self):
        localaddr = settings.LMTP_HOST, int(settings.LMTP_PORT)
        self.log.info('LMTP server listening on {}:{}'.format(localaddr[0], localaddr[1]))
        smtpd.SMTPServer.__init__(self, localaddr, remoteaddr=None)
        super(LMTPRunner, self).__init__()

    def handle_accept(self):
        conn, addr = self.accept()
        channel.Channel(self, conn, addr)
        self.log.debug('LMTP accept from %s', addr)

    def process_message(self, peer, mailfrom, recipients, data):
        parser = LMTPEmailParser(data, mailfrom, 'string')

        try:
            message = parser.parse()
        except ParseEmailException:
            self.log.exception('LMTP could not parse the incoming email.')
            return channel.CRLF.join(channel.ERR_451 for to in recipients)
        except MessageIDNotExistException:
            return channel.ERR_550_MID
        except DefectMessageException:
            return channel.ERR_501

        status = []
        for _ in recipients:
            # Send 250 OK for every recipients
            status.append('250 OK')

        print(message, peer, mailfrom, recipients)

        return channel.CRLF.join(status)
