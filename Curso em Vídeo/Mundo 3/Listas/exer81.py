#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    esc = str(input('Quer continuar ? [S/N]: '))[0].upper()
    while esc not in 'SN':
        print('ERRO !')
        esc = str(input('Quer continuar ? [S/N]: '))[0].upper()
    if esc == 'N':
        break
lista.sort(reverse = True)
print(f'Quantidade de números digidados: {len(lista)}')
print(f'Ordem decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print('O valor 5 não está nalista')