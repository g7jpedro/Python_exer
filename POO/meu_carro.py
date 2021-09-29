
from carro import Carro

meu_carro = Carro('Celta', 'A4', '2018')
print(meu_carro.nome_descritivo())

meu_carro.leitura_odometro = 23
meu_carro.ler_odometro()