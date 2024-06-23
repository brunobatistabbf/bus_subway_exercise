from transportation_interface import TransportationFactory
from bus_factory import BusFactory
from onibus import  Onibus

class BusTransportFactory(TransportationFactory):
    def criar_fabrica(self):
        return BusFactory

