from transportation_interface import TransportationFactory
from bus_factory import BusFactory

class BusTransportFactory(TransportationFactory):
    def criar_fabrica(self):
        return BusFactory
