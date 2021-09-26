#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
coplista = []
for i in range(1, 8):
    coplista = int(input(f'Digite o {i}° valor: '))
    if coplista % 2 == 0:
        lista[0].append(coplista)
    else:
        lista[1].append(coplista)

print(f'Valores pares digitados: \033[34m{lista[0]}\033[m')
print(f'Valores ímpares digitados: \033[34m{lista[1]}\033[m')
