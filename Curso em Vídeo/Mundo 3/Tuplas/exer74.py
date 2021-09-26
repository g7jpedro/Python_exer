#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
# listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
sorteio = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
print('Valores sorteados:',end=' ')
for i in sorteio:
    print(f'\033[34m{i}\033[m',end=' ')
print(f'\nO maior valor da tupla é {max(sorteio)}')
print(f'O menor valor da tupla é {min(sorteio)}')