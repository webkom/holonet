from abc import abstractmethod

from django.utils import timezone


class StorageBackend:

    MESSAGE_TYPES = (
        ('spam', 'spam'),
        ('blacklisted', 'blacklisted'),
        ('bounce', 'bounce'),
        ('archive', 'archive'),
    )
    MESSAGE_TYPES_LIST = list(element[0] for element in MESSAGE_TYPES)

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def index_message(self, message):
        pass

    @abstractmethod
    def retrieve_history(self, from_time, to_time, filter=None, search_query=None):
        pass


class StoredEmail:

    def __init__(self, from_email, to, copy, blind_copy, recipients, subject,
                 raw, message_type, timestamp=None,
                 *args, **kwargs):
        self.from_email = from_email
        self.to = to
        self.copy = copy
        self.blind_copy = blind_copy
        self.recipients = recipients
        self.subject = subject
        self.raw = raw
        self.message_type = message_type

        if timestamp is None:
            timestamp = timezone.now()

        self.timestamp = timestamp

    def as_dict(self):
        return {
            'from_email': self.from_email,
            'to': self.to,
            'copy': self.copy,
            'blind_copy': self.blind_copy,
            'recipients': self.recipients,
            'subject': self.subject,
            'raw': self.raw,
            'message_type': self.message_type,
            'timestamp': self.timestamp
        }
