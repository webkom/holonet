from abc import abstractmethod


class Rule:

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def record(self):
        raise NotImplementedError

    @abstractmethod
    def check(self, message_list, message, meta):
        """
        :param message_list: The mailing list object.
        :param message: The message object.
        :param meta: The message metadata.
        :returns: a boolean specifying whether the rule matched or not.
        """

        raise NotImplementedError
