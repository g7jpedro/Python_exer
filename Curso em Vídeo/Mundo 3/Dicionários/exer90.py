# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. N
# o final, mostre o conteúdo da estrutura na tela

aluno = dict()

aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'{aluno["Nome"]}, digite sua média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é {v}')