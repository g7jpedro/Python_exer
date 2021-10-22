
while True:
    n1 = input('Digite o primeiro valor: ')
    if n1 == 'q':
        break
    n2 = input('Digite o segundo valor: ')
    if n1 == 'q':
        break
    try:
        somar = float(n1) + float(n2)
    except ValueError:
        print('ERRO ! Informe um tipo certo de dado.')
    else:
        print(f'A soma de {n1} + {n2} = {somar}')