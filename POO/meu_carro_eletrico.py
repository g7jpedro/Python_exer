
from carro import CarroEletrico

meu_carro_ele = CarroEletrico('Gol', 'P1', '2021')
print(meu_carro_ele.nome_descritivo())
meu_carro_ele.bateria.descri_bateria()
meu_carro_ele.bateria.distância_percorrida()