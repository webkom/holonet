from abc import abstractmethod


class StatusCheck:

    NOT_RESPONDING = 0
    READY = 1
    UNKNOWN = 2

    STATUSES = (
        (NOT_RESPONDING, 'Not Responding'),
        (READY, 'Ready'),
        (UNKNOWN, 'Unknown'),
    )

    @property
    @abstractmethod
    def name(self):
        """
        Needs to be valid in a url!
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self):
        raise NotImplementedError
