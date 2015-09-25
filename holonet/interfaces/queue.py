from abc import abstractmethod


class Queue:

    @abstractmethod
    def dispose(self, message_list, message, meta):
        raise NotImplementedError
