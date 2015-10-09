from abc import abstractmethod


class Chain:

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self):
        raise NotImplementedError

    @abstractmethod
    def process(self, message_list, message, meta):
        pass
