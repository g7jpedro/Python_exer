n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
n3 = int(input('Valor 3: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('Os valores podem formar um TRIANGULO !')
    if n1 == n2 == n3:
        print('É EQUILÁTERO.')
    elif n1 != n2 != n3 != n1:
        print('É ESCALENO.')
    else:
        print('É ISÓSCELES.')
else:
    print('Os valores não podem formar um TRIANGULO !')