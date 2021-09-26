"""
 Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def exer3(v1, v2, v3):
    soma = v1 + v2 + v3
    return soma


v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
v3 = int(input('Digite o 3° valor: '))
soma = exer3(v1, v2, v3)
print(f'A soma dos valores foi {soma} ')
