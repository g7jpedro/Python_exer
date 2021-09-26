#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

lista = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    esc = str(input('Quer continuar ? [S/N]: ')).upper()[0]
    while esc not in 'SN':
        print('.......ERRO.......')
        esc = str(input('Quer continuar ? [S/N]: ')).upper()[0]
    if esc in 'N':
        break
print(f'Lista completa: {lista}')
print(f'Lista com ímpares: {impar}')
print(f'Lista com pares: {par}')

