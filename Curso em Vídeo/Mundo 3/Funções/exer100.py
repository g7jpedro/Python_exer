#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
# os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
números = []


def sorteio():
    for i in range(1, 6):
        sort = randint(0, 10)
        números.append(sort)
    print('Sorteando 5 valores: ', end='')
    for i in números:
        sleep(1)
        print(i, end=' ')


def somarPar():
    soma = 0
    print('\nSomando valores pares:',end=' ')
    for i in números:
        if i % 2 == 0:
            soma += i
    print(soma)


sorteio()
somarPar()
