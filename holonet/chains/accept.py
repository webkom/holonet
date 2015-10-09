from holonet.interfaces.chain import Chain

SEMISPACE = '; '


class Accept(Chain):
    """
    Messages entrees this chain if it gets approved for posting. This chains task is to send the
    message to the processing pipeline.
    """

    name = 'accept'
    description = 'Accept a message and send it to the processing pipeline'

    def process(self, message_list, message, meta):
        rule_hits = meta.get('rule_hits')
        if rule_hits:
            message['X-Holonet-Rule-Hits'] = SEMISPACE.join(rule_hits)
        rule_misses = meta.get('rule_misses')
        if rule_misses:
            message['X-Holonet-Rule-Misses'] = SEMISPACE.join(rule_misses)

        # Todo: Post message on the pipeline queue.
