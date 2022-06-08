class Veiculo(): #classe é um carro por exemplo
    """Essa é a classe carro. Esta classe é utilizada para instanciar novos carros em nosso programa"""
    def __init__(self, cor, tipo_combustivel, potencia):# atributos são as caracteristicas
        self.__cor = cor #dois underlines colocam os atributos como privados e só podem ser alterados com a função
        self.__combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.is_ligado = False
        self.__velocidade = 0
        self._libras = 0

    def __del__(self):
        print("O objeto foi removido da memória.")

    def abastecer (self, qtd_combustivel): #def sempre cria função. Nesse caso estamos criando um método, método abastecer
        """O método abastecer, recebe como parâmetro a quantidade de combustivel e coloca no atributo qtd_combustivel o objeto carro"""
        self._qtd_combustivel += qtd_combustivel
    def ligar (self):
        if self.is_ligado == True:
           print("O veículo já está ligado")
        else:
            self.is_ligado = True
            print("O veículo foi ligado")
    def desligar (self):
        if self.is_ligado == False:
            print("O veículo já está desligado")
        else:
            self.is_ligado = False
    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.__velocidade += velocidade
        else:
            print("O carro precisa estar ligado para ser acelerado")

