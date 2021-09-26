#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# – Quantidade de notas
#  – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def nota(*valores, sit='True'):
    '''

    :param valores: Receberá vários valores para guardar no dicionário
    :param sit: Verá se mostrará a  "Situação" do aluno ou não
    :return: Retornará os valores contidos no dicionário
    '''
    notas = {'Nota': valores}
    notas['Quantidade_notas'] = len(notas['Nota'])
    notas['Menor_nota'] = min(notas['Nota'])
    notas['Média_turma'] = sum(notas['Nota']) / len(notas['Nota'])
    if sit:
        if notas['Média_turma'] < 7:
            notas['Situação'] = 'Reprovado'
        elif notas['Média_turma'] > 7:
            notas['Situação'] = 'Aprovado'

    return notas


print(nota(5.5, 9.5, 0, 6.5, sit=False))

help(nota)