"""
 Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

 Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
 tipoCombustivel.
 valorLitro
 quantidadeCombustivel
 Possua no mínimo esses métodos:
 abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
 abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
 alterarValor( ) – altera o valor do litro do combustível.
 alterarCombustivel( ) – altera o tipo do combustível.
 alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
 OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaCombustivel():
    def __init__(self, tipo_combustivel, valor_litro=6.29 , quant_combus=5):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combus

    def abastecerPorvalor(self, valor):
        valor_inicial = valor
        litros = 0
        while valor > 6.25:
            valor -= 6.25
            litros += 1
        self.quant_combustivel += litros
        print(f'Com {valor_inicial} reais. Você abastece {litros} litros.')

    def abastecerPorlitro(self, litros):
        self.quant_combustivel += litros
        valor = litros * 6.29
        print(f'Abastecido com {litros} litros. Valor a ser pago: {valor}')
        print('='*40)

    def mostrar_status(self):
        print(f'Tipo de combustível: {self.tipo_combustivel}')
        print(f'Quantidade de Combustivel: {self.quant_combustivel}')
        print('=' * 40)

    def alterar_valor_litro(self, novo_valor):
        self.valor_litro = novo_valor


carro = BombaCombustivel('Normal')
carro.mostrar_status()
carro.abastecerPorvalor(30)
carro.mostrar_status()
carro.abastecerPorlitro(20)
carro.mostrar_status()




















