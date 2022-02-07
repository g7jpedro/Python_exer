"""
 Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista = []

for i in range(0, 4):
    valores = int(input(f'Digite o {i}° valor: '))
    lista.append(valores)

print(lista[::-1])