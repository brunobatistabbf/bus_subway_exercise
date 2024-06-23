from abc import ABC, abstractmethod

class TransportFactory(ABC):
    @abstractmethod
    def criar_transporte(self, *args):
        pass