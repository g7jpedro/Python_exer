"""
 Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
lista = []
for i in range(0, 5):
    valores = int(input(f'Digite o {i+1}° valor: '))
    lista.append(valores)

print('Os valores digitados foram: ')
for i in lista:
    print(i, end=' ')