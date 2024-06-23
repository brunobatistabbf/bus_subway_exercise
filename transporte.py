from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, capacidade):
        self.capacidade = capacidade

    @abstractmethod
    def tarifa(self):
        pass

    @abstractmethod
    def rota(self):
        pass

    def capacidade_atual(self):
        print(f"Capacidade Atual: {self.capacidade}")

    def embarcar(self, passageiros):
        if passageiros <= self.capacidade:
            self.capacidade -= passageiros
            print(f"{passageiros} passageiros embarcaram")
        else:
            print("\nCapacidade Insuficiente")


    def desembarcar(self, passageiros):
        self.capacidade += passageiros
        print(f"{passageiros} passageiros desembarcaram")