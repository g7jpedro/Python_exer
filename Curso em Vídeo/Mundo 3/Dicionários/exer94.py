

dados_pessoas = dict()
pessoas = list()
lista_mulheres = list()
soma_idades = 0
while True:
    dados_pessoas['Nome'] = str(input('Digite seu nome: ').title())
    dados_pessoas['Sexo'] = str(input('Digite seu sexo [M/F]: ').upper())

    while dados_pessoas['Sexo'] not in 'MF':
        dados_pessoas['Sexo'] = str(input('Digite seu sexo [M/F]: ').upper())
    dados_pessoas['Idade'] = int(input('Digite sua idade: '))
    pessoas.append(dados_pessoas.copy())
    soma_idades += dados_pessoas['Idade']
    if dados_pessoas['Sexo'] == 'F':
        lista_mulheres.append(dados_pessoas['Nome'])
    esc = str(input('Quer continuar ? [S/N]: ')).upper()[0]
    while esc not in 'SN':
        esc = str(input('Quer continuar ? [S/N]: ')).upper()[0]
    if esc == 'N':
        break

print(pessoas)
print(f'== {len(pessoas)} pessoas foram cadastradas')
print(f'== A média de pessoas cadastradas é de {soma_idades / len(pessoas):.2f}')
print('== Mulheres cadastradas:', end=' ')
for i in lista_mulheres:
    print(i, end=' ')

print('\n== As pessoas que estão acima da média de idade são: ')
for i in pessoas:
    if i['Idade'] > soma_idades / len(pessoas):
        print(f'Nome: {i["Nome"]} Sexo: {i["Sexo"]} Idade: {i["Idade"]} ')

print('FIm ..............')