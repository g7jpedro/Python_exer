#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.

n =[]
maior = []
menor = []
for i in range(0, 5):
    n.append(int(input('Digite um valor: ')))
print('Valores digitados:',end=' ')
for valores in n:
    print(valores,end=' ')
for pos,valores in enumerate(n):
    if valores == max(n):
        maior.append(pos)
    if valores == min(n):
        menor.append(pos)
print(f'\nO maior valor é {max(n)} e está nas psoições: {maior}')
print(f'O menor valor é {min(n)} nas posições {menor}')



