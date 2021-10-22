
print('Me de dois valores e vou dividr eles.')
print("Aperte 'q' para sair. " )

while True:
    n1 = input('\nPrimeiro valor: ')
    if n1 == 'q':
        break
    n2 = input('Segundo valor: ')
    if n2 == 'q':
        break
    try:
        div = int(n1) / int(n2)
    except ZeroDivisionError:
        print('Você não pode dividir um valor por zero.')
    else:
        print(f'{div:.1f}')