from transportation_interface import TransportationFactory
from metro_factory import MetroFactory
from metro import Metro

class MetroTransportationFactory(TransportationFactory):
    def criar_fabrica(self):
        return MetroTransportationFactory()
