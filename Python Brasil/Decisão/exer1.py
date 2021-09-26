"""
 Faça um Programa que peça dois números e imprima o maior deles.
"""

v1 = float(input('Digite o 1° valor: '))
v2 = float(input('Digite o 2° valor: '))

if v1 > v2:
    print(f'O maior é {v1}')
elif v2 > v1:
    print(f'O maior é {v2}')
else:
    print('Os valores são iguais')