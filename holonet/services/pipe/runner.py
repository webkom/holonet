import sys

from holonet.core.parser import EmailParser
from holonet.core.parser.exceptions import DefectMessageException, ParseEmailException
from holonet.interfaces.runner import Runner
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

        print(message, recipients)

    def close(self):
        pass
