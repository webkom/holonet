from holonet.interfaces.chain import Chain


class Reject(Chain):

    name = 'reject'
    description = 'Reject/bounce a message and stop processing.'

    def process(self, message_list, message, meta):
        pass
