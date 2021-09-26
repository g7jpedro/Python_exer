# Código + difícil que eu consegui fazer.
a = 0
maior = 1
cont = 0
for i in range(1, 5):
    print(f'------ {i}° Pessoa -------')
    n = str(input('Nome: ')).strip()
    id = int(input('Idade: '))
    sex = str(input('Sexo [F/M]: ')).upper()
    a += id
    méd = a / 4
    if sex == 'M':
        if id > maior:
            maior = id
            ch = n
    if sex == 'F':
        if id < 20:
            cont += 1
print(f'A média de idade do grupo é {méd}')
print(f'O homem mais velho tem {maior} anos, é o {ch}.')
print(f'No total tem {cont} mulheres com menos de 20 anos.')



