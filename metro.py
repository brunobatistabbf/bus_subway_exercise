from transporte import Transporte

class Metro(Transporte):
    def __init__(self, capacidade, pagamento, partida, destino):
        super().__init__(capacidade)
        self.pagamento = pagamento
        self.partida = partida
        self.destino = destino
        self.passageiros = 0

    def tarifa(self):
        print(f"Tarifa cobrada: {self.pagamento}")

    def rota(self):
        print(f"Linha: {self.partida} para {self.destino}")

    def capacidade_atual(self):
        print(f"Capacidade: {self.capacidade}")

    def embarcar(self, num_passageiros):
        print(f"Embarque de {num_passageiros} pessoas")
        self.passageiros += num_passageiros
        self.capacidade -= num_passageiros

    def desembarcar(self, num_passageiros):
        print(f"Desembarque de {num_passageiros} pessoas")
        self.passageiros -= num_passageiros
        self.capacidade += num_passageiros

