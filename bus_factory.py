from transport_factory import TransportFactory
from onibus import  Onibus

class BusFactory(TransportFactory):
    def criar_transporte(self, capacidade, pagamento, partida, destino):
        return Onibus(capacidade, pagamento, partida, destino)

