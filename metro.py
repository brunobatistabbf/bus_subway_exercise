from transporte import Transporte

class Metro(Transporte):
    def __init__(self, capacidade, pagamento, partida, destino):
        super().__init__(capacidade)
        self.pagamento = pagamento
        self.partida = partida
        self.destino = destino

    def tarifa(self):
        print(f"Tarifa cobrada: {self.pagamento}")

    def rota(self):
        print(f"Linha: {self.partida} para {self.destino}")