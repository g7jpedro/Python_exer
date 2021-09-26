#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Flamengo.

tabela = ('Internacional','Flamengo','Atlético-MG','São Paulo',
          'Fluminense','Palmeiras','Grêmio','Athlético-PR',
          'Ceará SC','Corinthians','Santos','Athlético-GO',
          'Bragantino','Vasco da Gama','Bahia','Sport','Fortaleza',
          'Goiás','Coritiba','Botafogo')

print(f'\033[34mTABELA NO DIA 02/02/2021\033[m')
print('\033[1;42;30mPRIMEIROS COLOCADOS\033[m')
for times in range(0,5):
    print(f'\033[34m{times+1}° {tabela[times]}\033[m')
print('='*20)

print('\033[1;41;30mÚLTIMOS COLOCADOS\033[m')
for times in tabela[16:]:
    print(f'\033[31m{tabela.index(times)+1}° {times}\033[m')

print('='*20)
print('\033[45;30mORDEM ALFABÉTICA\033[m')
for times in sorted(tabela):
    print(times)
print('='*20)

print('\033[44;30mTABELA COMPLETA 02/02/2021\033[m')
for pos,times in enumerate(tabela):
    if pos < 5:
        print(f'\033[34m{pos+1}° {times}\033[m')
    elif pos > 15:
        print(f'\033[31m{pos+1}° {times}\033[m')
    else:
        print(f'{pos}° {times}')
        
print(f'O time do FLAMENGO está na posição',tabela.index('Flamengo')+1)
