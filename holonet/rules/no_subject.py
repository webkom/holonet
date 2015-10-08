from holonet.interfaces.rule import Rule


class NoSubject(Rule):

    name = 'no-subject'
    description = 'Catch messages with empty subject.'
    record = True

    def check(self, message_list, message, meta):
        subject = message.get('subject', '').strip()
        return subject == ''
