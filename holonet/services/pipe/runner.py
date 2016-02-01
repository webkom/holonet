import sys

from django.utils import timezone

from holonet import queues
from holonet.core.parser import EmailParser
from holonet.core.parser.exceptions import DefectMessageException, ParseEmailException
from holonet.core.utils import split_address
from holonet.interfaces.runner import Runner
from holonet.lists.models import List
from holonet.mta.postfix.exit_codes import PostfixPipeExit


class PipeRunner(Runner):
    """
    This runner provides a interface for transporting mail into Holonet using pipe, STDIN.
    Command: manage.py pipe_transport
    """

    name = 'pipe'
    help = 'Command for delivering of messages using pipe'

    exit_handler = PostfixPipeExit()

    def add_arguments(self, parser):
        parser.add_argument('sender', type=str)
        parser.add_argument('recipients', nargs='+', type=str)

    def run(self, *args, **kwargs):
        self.log.info('Parsing message received using pipe')

        sender = kwargs.get('sender')
        recipients = kwargs.get('recipients', [])
        if sender is None:
            return self.exit_handler.data_error()

        parser = EmailParser(sys.stdin.buffer, sender, 'binary_file')

        try:
            message = parser.parse()
        except ParseEmailException:
            return self.exit_handler.data_error()
        except DefectMessageException:
            return self.exit_handler.data_error()

        status = []
        for recipient in recipients:

            local, domain = split_address(recipient)
            message_data = {
                'original_size': message.original_size,
                'received_time': timezone.now()
            }

            # TODO: Handle system messages like bounce and VERP messages

            # If list exists - enqueue mail
            message_list = List.lookup_list(local, domain)
            if message_list:
                message_data['to_list'] = True
                queues.get('in').dispose(message_list, message, message_data)

            status.append(recipient)

        if len(status) == 0:
            return self.exit_handler.no_recipient()

    def close(self):
        pass
