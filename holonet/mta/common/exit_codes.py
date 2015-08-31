from abc import abstractmethod


class ExitCodes:

    @abstractmethod
    def data_error(self):
        pass

    @abstractmethod
    def no_recipient(self):
        pass

    @abstractmethod
    def no_domain(self):
        pass

    @abstractmethod
    def service_unavailable(self):
        pass

    @abstractmethod
    def system_error(self):
        pass
