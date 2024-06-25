from transportation_interface import TransportationFactory
from onibus import  Onibus

class BusTransportFactory(TransportationFactory):
    def criar_fabrica(self):
        print("Criar Fabrica de Onibus")

    def criar_transporte(self, capacidade, pagamento, origem, destino):
        return  Onibus(capacidade, pagamento, origem, destino)
