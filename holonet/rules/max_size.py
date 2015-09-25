from holonet.interfaces.rule import Rule


class MaxSizeRule(Rule):
    """
    Check message size if the list requires it.
    """

    name = 'max-size'
    description = 'Validate message size'
    record = True

    def check(self, message_list, message, meta):
        if message_list.max_message_size == 0:
            return False
        assert hasattr(message, 'original_size'), 'Message was not sized on initial parsing.'

        return message.original_size / 1024.0 > message_list.max_message_size
