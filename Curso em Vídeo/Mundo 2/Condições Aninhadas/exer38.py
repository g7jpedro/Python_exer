n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print(f'Valores digitados: {n1} e {n2}. O maior é {n1} e o menor {n2}')
elif n2 > n1:
    print(f'Valores digitados: {n1} e {n2}. O maior é {n2} e o menor é {n1}')
else:
    print(f'Valores digitados: {n1} e {n2}. Os valores são iguais!')
    