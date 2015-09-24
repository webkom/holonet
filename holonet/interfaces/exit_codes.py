from abc import abstractmethod


class ExitCodes:

    @abstractmethod
    def data_error(self):
        raise NotImplementedError

    @abstractmethod
    def no_recipient(self):
        raise NotImplementedError

    @abstractmethod
    def no_domain(self):
        raise NotImplementedError

    @abstractmethod
    def service_unavailable(self):
        raise NotImplementedError

    @abstractmethod
    def system_error(self):
        raise NotImplementedError
