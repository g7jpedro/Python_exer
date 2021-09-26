#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
coplista = []
maior = []
menor = []
while True:
    lista.append(str(input('Dgite seu nome: ')))
    lista.append(float(input('Digite seu peso: ')))
    coplista.append(lista[:])
    lista.clear()
    esc = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    while esc not in 'SN':
        esc = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    if esc == 'N':
        for i in coplista:
            if i[1] >= 100:
                maior.append(i[0])
            elif i[1] <= 70:
                menor.append(i[0])
        break
print(f'{len(coplista)} pessoas cadastradas')
print(f'As pessoas que ultrapassaram de 100kgs foram: {maior}')
print(f'As pessoas que estão com menos de 70kg são: {menor}')







