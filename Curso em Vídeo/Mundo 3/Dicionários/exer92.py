from datetime import datetime


dici = dict()
aposentadoria = ''
idade = ''
anos_trabalhados = ''
anos_faltando = ''

dici['Nome'] = str(input('Digite seu nome: '))
dici['Idade'] = int(input('Digite o ano de seu nascimento: '))
dici['Carteira'] = int(input('Digite sua carteira de trabalho [0: Caso não tenha]: '))
idade = datetime.now().year - dici['Idade']
dici['Idade'] = idade
if dici['Carteira'] != 0:
    dici['AnoContra'] = int(input('Digite o ano de contratação: '))
    dici['Salário'] = float(input('Digite o salário: '))

    anos_trabalhados = datetime.now().year - dici['AnoContra']
    aposentadoria_prevista = 35 - anos_trabalhados
    aposentadoria = idade + aposentadoria_prevista
    dici['Aposentadoria'] = aposentadoria

    for k, v in dici.items():
        print(f'{k} tem {v}')

else:
    print(dici)