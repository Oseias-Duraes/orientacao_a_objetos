import carro, moto

uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)  # isso é um objeto, é a declaração do que é o carro#
# help(carro.Carro)
uno_vermelho.ligar()  # chamando o método ligar da classe uno para o carro uno vermelho que contem as propriedades acima
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)

moto_vermelha = moto.Moto("vermelho","Flex",1.0,4)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
print(moto_vermelha.is_ligado)
