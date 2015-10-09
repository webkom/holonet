from holonet.interfaces.chain import Chain


class BuiltIn(Chain):

    name = 'builtin'
    description = 'The built-in moderation chain. Run rules and act on results.'

    def process(self, message_list, message, meta):
        pass
