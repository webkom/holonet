from holonet.interfaces.rule import Rule


class Any(Rule):
    """
    Return True if any previous rules have matched.
    """

    name = 'any'
    description = 'Return True if a previous rule have matched.'
    record = False

    def check(self, message_list, message, meta):
        return len(meta.get('rule_hits', [])) > 0
