import logging

from holonet.interfaces.rule import Rule

log = logging.getLogger(__name__)


class Loop(Rule):

    name = 'loop'
    description = 'Rule thats trying to prevent a posting loop.'
    record = True

    def check(self, message_list, message, meta):
        list_posts = set(value.strip().lower() for value in message.get_all('list-post', []))
        log.error('Could not check the message for a loop. Postings: {}'.format(
            ', '.join(list_posts)))
        # TODO: Create a posting_address on the message_list object and see if it exists in the
        # list_posts list
        return False
