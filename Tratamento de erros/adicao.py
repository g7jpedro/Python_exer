

n1 = input('Digite o primeiro valor: ')
n2 = input('Digite o segundo valor: ')

try:
    somar = float(n1) + float(n2)
except ValueError:
    print('ERRO ! Informe um tipo certo de dado.')
else:
    print(f'A soma de {n1} + {n2} = {somar}')