from holonet.interfaces.chain import Chain


class Discard(Chain):

    name = 'discard'
    description = 'Discard a message and stop processing.'

    def process(self, message_list, message, meta):
        pass
