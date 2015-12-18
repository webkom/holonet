from holonet.interfaces.rule import Rule


class Emergency(Rule):

    name = 'emergency'
    description = 'Hold a message if the list is in emergency mode.'
    record = True

    def check(self, message_list, message, meta):
        return message_list.emergency
