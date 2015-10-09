from holonet.interfaces.rule import Rule


class Truth(Rule):
    """
    This rule always returns True. This rule is usually used in the end of a chain.
    """

    name = 'truth'
    description = 'A rule that always matches'
    record = False

    def check(self, message_list, message, meta):
        return True
