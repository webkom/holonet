import asyncore
import logging
import smtpd

from django.conf import settings
from django.utils import timezone

from holonet.apps.incoming.lmtp import channel
from holonet.apps.incoming.lmtp.paser import LMTPEmailParser
from holonet.apps.utils.base_service import Service
from holonet.apps.utils.parsers.email_parser import ParserMessageType
from holonet.apps.utils.parsers.exceptions import (DefectMessageException,
                                                   MessageIDNotExistException, ParseEmailException)
from holonet.apps.utils.utils import split_address

smtpd.__version__ = 'Holonet LMTP'
log = logging.getLogger(__name__)


class LMTPService(Service, smtpd.SMTPServer):
    """
    This runner provides a interface for transporting mail into Holonet using LMTP.
    Command: manage.py lmtp_transport

    Settings:
        LMTP_HOST = 'localhost'
        LMTP_PORT = 8024
    """

    name = 'lmtp'
    help = 'Start a lmtp server for incoming messages'
    channel_class = channel.Channel
    log = log

    def run(self, *args, **kwargs):
        asyncore.loop(use_poll=True)

    def close(self):
        asyncore.socket_map.clear()
        asyncore.close_all()

    def __init__(self):
        localaddr = settings.LMTP_HOST, int(settings.LMTP_PORT)
        self.log.info('Starting LMTP server on {0}:{1}'.format(*localaddr))
        smtpd.SMTPServer.__init__(self, localaddr, remoteaddr=None)
        super().__init__()

    def handle_accept(self):
        conn, addr = self.accept()
        channel.Channel(self, conn, addr)
        self.log.debug('LMTP accept from %s', addr)

    def process_message(self, peer, mailfrom, recipients, data):
        parser = LMTPEmailParser(data, mailfrom, ParserMessageType.STRING)

        try:
            message = parser.parse()
        except ParseEmailException:
            self.log.exception('LMTP could not parse the incoming email')
            return channel.CRLF.join(channel.ERR_451 for _ in recipients)
        except MessageIDNotExistException:
            self.log.exception('LMTP received message with no Message-ID')
            return channel.CRLF.join(channel.ERR_550_MID for _ in recipients)
        except DefectMessageException:
            self.log.exception('LMTP received a message with defects')
            return channel.CRLF.join(channel.ERR_501 for _ in recipients)

        status = []
        for recipient in recipients:
            try:
                local, domain = split_address(recipient)
                message_data = {
                    'original_size': message.original_size,
                    'received_time': timezone.now()
                }

                print(local, domain, message_data)

                # TODO: Handle system messages like bounce and VERP messages
                """
                message_list = List.lookup_list(local, domain)
                if message_list:
                    message_data['to_list'] = True
                    queues.get('in').dispose(message_list, message, message_data)
                """

                status.append(channel.OK_250)

            except Exception:
                from raven.contrib.django.raven_compat.models import client
                client.captureException()
                self.log.error('Failed to lookup message recipient')
                status.append(channel.ERR_550)

        return channel.CRLF.join(status)
