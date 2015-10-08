from holonet.interfaces.rule import Rule


class Truth(Rule):

    name = 'truth'
    description = 'A rule that always matches'
    record = False

    def check(self, message_list, message, meta):
        return True
