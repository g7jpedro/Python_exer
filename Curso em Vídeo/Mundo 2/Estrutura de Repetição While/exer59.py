v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opç = 1
while opç == 1 or opç == 2 or opç == 3 or opç == 4:
    print('=='*28)
    opç = int(input('''Escolha a Opção
1 - SOMAR
2 - MulTIPLICAR
3 - MAIOR
4 - NOVOS NÚMEROS
5 - SAIR DO PROGRAMA
DIGITE:  '''))
    if opç == 1:
        print(f'A soma dos dois valores é {v1 + v2}')
    elif opç == 2:
        print(f'A multiplicação dos dois valores é {v1 * v2}')
    elif opç == 3:
        print(f'O maior valor entre os dois é {max(v1, v2)}')
    elif opç == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
if opç == 5:
    print('ACABOU O PROGRAMA')
else:
    print('ERROOOOOOOOOOOOOO')


