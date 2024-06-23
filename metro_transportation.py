from transportation_interface import TransportationFactory
from metro_factory import MetroFactory

class MetroTransportationFactory(TransportationFactory):
    def criar_fabrica(self):
        return MetroFactory()