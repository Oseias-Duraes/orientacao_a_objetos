import carro

uno_vermelho = carro.Carro("vermelho", 4, "Flex", 1.0) #isso é um objeto, é a declaração do que é o carro#
#help(carro.Carro)
uno_vermelho.ligar() #chamando o método ligar da classe uno para o carro uno vermelho que contem as propriedades acima
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)

#qtd_abastecida = uno_vermelho.abastecer(input(f"Quantos litros gostaria de abastecer"))
print(f"A quantidade de combustível do carro é: {uno_vermelho.qtd_combustivel}")

uno_preto = carro.Carro("preto", 2, "Flex", 1.4)
uno_preto.desligar()
print(f"A quantidade de combustível do carro é: {uno_preto.qtd_combustivel}")
uno_preto.ligar()
uno_preto.acelerar()
print(uno_preto.velocidade)