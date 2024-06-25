from abc import ABC, abstractmethod

class TransportFactory(ABC):
    @abstractmethod
    def criar_transporte(self, *args):
        pass

    @abstractmethod
    def criar_transporte(self, capacidade, pagamento, origem, destino):
        pass