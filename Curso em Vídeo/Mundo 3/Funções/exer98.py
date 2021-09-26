#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(i, f, p):
    if i < f and i == 1 and f == 10 and p == 1:
        print('Contagem de 1 até 10:')
        for i in range(i, f+1, p):
            sleep(0.5)
            print(i, end=' ')
    elif i > f and i == 10 and f == 0 and p == 2:
        print('\nContagem de 10 até 1 de 2 em 2:')
        for i in range(i, f-1, -p):
            sleep(0.5)
            print(i, end=' ')
    else:
        if i < f:
            if p == 0:
                for i in range(i, f, 1):
                    sleep(0.5)
                    print(i, end=' ')
            else:
                for i in range(i, f, p):
                    sleep(0.5)
                    print(i, end=' ')
        elif i > f:
            if p > 0:
                for i in range(i, f, -p):
                    sleep(0.5)
                    print(i, end=' ')
            elif p == 0:
                for i in range(i, f, -1):
                    sleep(0.5)
                    print(i, end=' ')
            else:
                for i in range(i, f, p):
                    sleep(0.5)
                    print(i, end=' ')


contador(1, 10, 1)
contador(10, 0, 2)

print('\nAgora personalize sua contagem:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)