from abc import ABC, abstractmethod

class TransportationFactory(ABC):
    @abstractmethod
    def criar_fabrica(self):
        pass