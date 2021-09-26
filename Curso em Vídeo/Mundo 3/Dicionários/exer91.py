#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python.  No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número
# no dado.

from random import randint
from operator import itemgetter
dici = dict()
ordem = dict()

for i in range(0, 5):
    sorteio = randint(0, 10)
    dici[i] = sorteio

for k, v in dici.items():
    print(f'Jogador {k+1} tirou {v} no dado.')
ordem = sorted(dici.items(), key= itemgetter(1), reverse=True)

print('='*30)
print('== Ranking dos Jogadores ==')
for pos, i in enumerate(ordem):
    print(f'{pos+1}° lugar. Jogador {i[0]} com {i[1]} pontos.')
