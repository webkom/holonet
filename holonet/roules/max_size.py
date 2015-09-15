from holonet.interfaces.rule import Rule


class MaxSizeRule(Rule):

    name = 'max-size'
    description = ''

    def check(self, message_list, message, meta):
        return False
