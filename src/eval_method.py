from abc import ABCMeta, abstractmethod

class IEvalMethod(metaclass=ABCMeta):
    @abstractmethod
    def evaluate(self):
        raise NotImplementedError("Please specify evaluation method")
