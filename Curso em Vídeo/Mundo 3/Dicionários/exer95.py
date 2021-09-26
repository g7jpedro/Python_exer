
dici = dict()
lista_jogadores = list()
gols = list()
soma_gols = 0

while True:
    dici['Nome'] = str(input('Digite seu nome: ')).title()
    dici['Jogos'] = int(input('Quantas partidas você jogou ?: '))

    for i in range(0, dici['Jogos']):
        gols.append((int(input(f'Gols feitos na {i+1}° partida: '))))

    dici['Gols'] = gols[:]
    dici['Total_gols'] = sum(gols)
    gols.clear()
    lista_jogadores.append(dici.copy())
    esc = str(input('Que continuar ? [S/N]: ')).upper()[0]
    while esc not in 'SN':
        esc = str(input('Que continuar ? [S/N]: ')).upper()[0]
    if esc == 'N':
        break

print('Cód nomes       gols       total')
for k, v in enumerate(lista_jogadores):
    print(f'{k}  {v["Nome"]}           {v["Gols"]}           {v["Total_gols"]}')

while True:
    esc = int(input('Quer dado de qual jogador ?: [999] para parar: '))
    if esc == 999:
        break
    while esc < 0 or esc > len(lista_jogadores):
        esc = int(input('Quer dado de qual jogador ?: [999] para parar: '))
    print('=='*20)
    print(f'Levantamentos do jogador: {lista_jogadores[esc]["Nome"]}')
    for pos, v in enumerate(lista_jogadores[esc]["Gols"]):
        print(f'Na {pos+1}° partida fez {v} gols..')

print('Fim .......')