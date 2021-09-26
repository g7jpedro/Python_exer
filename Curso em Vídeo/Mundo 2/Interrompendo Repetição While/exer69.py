print('===== CADASTRE UMA PESSOA =====')
c = 0
c2 = 0
c3 = 0
while True:
    id = int(input('Idade: '))
    sex = str(input('Sexo[H/M]: ')).strip().upper()
    while sex not in 'HM':
        sex = str(input('Sexo[H/M]: ')).strip().upper()
    esc = str(input('Quer CONTINUAR ?[S/N]')).strip().upper()
    while esc not in 'SN':
        esc = str(input('Quer CONTINUAR ?[S/N]')).strip().upper()
    print('='*22)
    if id > 18:
        c += 1
    if sex == 'H':
        c2 += 1
    if sex == 'M' and id < 20:
        c3 += 1
    if esc == 'N':
        break
print(f'Tem {c} pessoas com + de 18 annos.')
print(f'Tem {c2} homens cadastrados.')
print(f'Tem {c3} mulheres com menos de 20 anos.')


