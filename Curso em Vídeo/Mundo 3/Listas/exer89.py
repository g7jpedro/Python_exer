# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
coplista = []
méd = 0
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
    n1 = float(input('Digite a 1° Nota: '))
    n2 = float(input('Digite a 2° Nota: '))
    méd = (n1 + n2) / 2
    lista.append([nome, [n1, n2], méd])

    esc = str(input('Que continuar ? [S/N]: ')).upper().strip()[0]
    while esc not in 'SN':
        esc = str(input('Que continuar ? [S/N]: ')).upper().strip()[0]
    if esc == 'N':
        print('N° Nome     Média')
        print('=' * 30)
        for pos, i in enumerate(lista):
            print(f'{pos} {i[0]:<10} {i[2]:<10.1f}')
        while True:
            esc = int(input(f'Digite o aluno que quer ver a nota: [999] Finaliza o programa: '))
            if esc != 999:
                print(f'As notas de {lista[esc][0]} foram: {lista[esc][1]}')
            else:
                break
        break
print('FIM ............')
