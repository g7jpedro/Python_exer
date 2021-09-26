#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = []
listcop = []

print('='*30)
print('      \033[34mJOGUE NA MEGA SENA\033[m')
print('='*30)

esc = int(input('Digite a quantidade de vezes que quer jogar: '))
print('='*6,f'\033[34mSORTEANDO {esc} JOGOS\033[m','='*6)
for i in range(0, esc):
    for a in range(0, 6):
        sorteio = randint(1, 60)
        while sorteio in lista:
            sorteio = randint(1, 60)
        lista.append(sorteio)
    listcop.append(lista[:])
    lista.clear()
for pos, i in enumerate(listcop):
    sleep(1)
    print(f'Jogo {pos+1}: {sorted(i)} ')
