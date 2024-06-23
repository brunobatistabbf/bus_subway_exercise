from transport_factory import TransportFactory
from metro import  Metro

class MetroFactory(TransportFactory):
    def criar_transporte(self, capacidade, pagamento, partida, destino):
        return Metro(capacidade, pagamento, partida, destino)