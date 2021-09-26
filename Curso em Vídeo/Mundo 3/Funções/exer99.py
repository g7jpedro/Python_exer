# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior.

from time import  sleep

def li():
    print('='*35)


def maior(*valores):
    print('Análisando os valores passados: ')
    for i in valores:
        print(i, end=' ',)
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores.')
    print(f'O maior valor informado foi {max(valores)}')
    li()




maior(3, 4, 5, 7, 8)
maior(2, 3, 4, 5)
maior(1, 2, 3)

