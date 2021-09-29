
from carro import Carro
from carro_eletrico import CarroEletrico

meu_carro = Carro('Gol', 'P1', '2021')
print(meu_carro.nome_descritivo())

meu_carro_eletrico = CarroEletrico('Choque', '100Volts', '2021')
print(meu_carro_eletrico.nome_descritivo())
