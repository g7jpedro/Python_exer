"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

from ajuda import ler_valores


def exer2(n):
    for i in range(1, n + 1):
        for a in range(1, i+1):
            print(a, end=' ')
        print()


v = ler_valores.leiaint('Digite um valor inteiro: ')
exer2(v)
