import logging

from holonet.interfaces.rule import Rule

log = logging.getLogger(__name__)


class Loop(Rule):

    name = 'loop'
    description = 'Rule thats trying to prevent a posting loop.'
    record = True

    def check(self, message_list, message, meta):
        list_posts = set(value.strip().lower() for value in message.get_all('list-post', []))
        return message_list.post_address in list_posts
