from email.utils import getaddresses

from holonet.interfaces.rule import Rule


class MaxRecipients(Rule):

    name = 'max_recipients'
    description = 'Catch messages with too many explicit recipients.'
    record = True

    def check(self, message_list, message, meta):
        if message_list.max_num_recipients == 0:
            return False

        recipients = getaddresses(message.get_all('to', []) + message.get_all('cc', []))
        return len(recipients) > message_list.max_num_recipients
