sex = str(input('Olá, digite seu sexo [M/F]: ')).strip().upper()
while sex not in 'MF':
    sex = str(input('ERRO. Digite [M/F]: ')).strip().upper()
print(f'ACABOU O PROGRAMA, foi digidado {sex}')
