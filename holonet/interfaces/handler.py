from abc import abstractmethod


class Handler:

    @classmethod
    @abstractmethod
    def process(cls, message_list, message, meta):
        """

        :param message_list: The message list object for this message
        :param message: email.Email object containing the message
        :param meta: Metadata attached to this message
        :return:
        """
        pass
