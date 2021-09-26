
dici = dict()
gols = list()
soma_gols = 0
dici['Nome'] = str(input('Digite seu nome: '))
dici['Jogos'] = int(input('Quantas partidas você jogou ?: '))
dici['Gols'] = ''

for i in range(0, dici['Jogos']):
    núm_gols = (int(input(f'Digite quantos gols no {i + 1} jogo: ')))
    gols.append(núm_gols)
    soma_gols += núm_gols

dici['Gols'] = gols
dici['Total'] = soma_gols

print(dici)
print('='*30)
for k, v in dici.items():
    print(f'O campo {k} tem o valor {v}.')
print('='*30)

for pos,i in enumerate(gols):
    print(f'Na {pos+1}° partida fez {i} gols.')
print(f'No total fez um total de {soma_gols} gols.')