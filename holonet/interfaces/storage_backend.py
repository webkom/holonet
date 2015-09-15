from abc import abstractmethod


class StorageBackend:

    SPAM = 'spam'
    BLACKLISTED = 'blacklisted'
    BOUNCE = 'bounce'
    ARCHIVE = 'archive'

    MESSAGE_TYPES = (
        (SPAM, 'spam'),
        (BLACKLISTED, 'blacklisted'),
        (BOUNCE, 'bounce'),
        (ARCHIVE, 'archive'),
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
