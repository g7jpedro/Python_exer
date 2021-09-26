"""
 Faça um Programa que leia três números e mostre o maior deles.
"""

v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
v3 = int(input('Digite o 3° valor: '))

if v1 > v2 and v1 > v3:
    print(f'{v1} é o maior valor')
elif v2 > v1 and v2 > v3:
    print(f'{v2} é o maior')
else:
    print(f'{v3} é o maior')