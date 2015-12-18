from email.utils import getaddresses

from holonet.interfaces.rule import Rule


class ImplicitDestination(Rule):

    name = 'implicit_destination'
    description = 'Catch messages with implicit destination.'
    record = True

    def check(self, message_list, message, meta):
        if not message_list.require_explicit_destination:
            return False

        aliases = set()
        aliases.add(message_list.posting_address)

        # Todo: Alias support is not implemented. To do this, add aliases to the aliases set.

        for header in ['to', 'cc', 'resent-to', 'resent-cc']:
            for real_name, email in getaddresses(message.get_all(header, [])):
                if isinstance(email, bytes):
                    email = email.decode('ascii')
                email = email.lower()
                if email in aliases:
                    return False
        return True
