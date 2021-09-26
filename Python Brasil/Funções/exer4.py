"""
 Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu
 argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def exer4(v):
    if v > 0:
        return 'P'
    else:
        return 'N'


v = exer4(int(input('Digite um valor: ')))
print(v)
