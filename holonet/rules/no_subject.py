from holonet.interfaces.rule import Rule


class NoSubject(Rule):
    """
    Return True if the message don't have a header.
    """

    name = 'no-subject'
    description = 'Catch messages with empty subject.'
    record = True

    def check(self, message_list, message, meta):
        subject = message.get('subject', '').strip()
        return subject == ''
