from transportation_interface import TransportationFactory
from metro import Metro

class MetroTransportationFactory(TransportationFactory):
    def criar_fabrica(self):
        print("Criar Fábrica de Metro")
    def criar_transporte(self, capacidade, pagamento, origem, destino):
        return  Metro(capacidade, pagamento, origem, destino)
