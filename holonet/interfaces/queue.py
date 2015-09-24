from abc import abstractmethod


class Queue:

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def enqueue(self, message):
        raise NotImplementedError
