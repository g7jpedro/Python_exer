"""
 Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

lista = []

for i in range(0, 4):
    notas = int(input('Digite sua nota: '))
    lista.append(notas)

média = sum(lista) / 4
print(f'As notas foram {lista[::-1]}')
print(f'A média foi de {média}')