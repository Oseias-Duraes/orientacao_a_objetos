import veiculo

class Moto(veiculo.Veiculo):
    def __int__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel,potencia)
        self.qtd_passageiros = qtd_passageiros