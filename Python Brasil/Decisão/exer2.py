"""
 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

v = float(input('Digite um valor: '))
if v > 0:
    print('Positivo')
elif v < 0:
    print('Negativo')
else:
    print('Neutro')