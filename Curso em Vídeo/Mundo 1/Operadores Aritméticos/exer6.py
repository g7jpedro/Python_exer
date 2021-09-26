#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite o valor:'))
db = n*2
tr = n*3
rz = n**(1/2)
print(f'O dobro de {n} é = {db}')
print(f'O triplo de {n} é = {tr}')
print(f'E a raiz quadrada de {n} é = {rz}')