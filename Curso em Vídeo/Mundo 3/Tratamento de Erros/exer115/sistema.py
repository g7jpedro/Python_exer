from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivo_encontrado(arq):
    criar_arquivo(arq)

while True:
    opc = menu(['Ver lista de pessoa', 'Cadastrar pessoas', 'Finalizar programa'])
    if opc == 1:
        lerarquivo(arq)
    elif opc == 2:
        cabeçalho('CADASDRO DE PESSOAS')
        nome = str(input('Digite o nome: '))
        idade = leiaint('Digite a idade:')
        cadastrar(arq, nome, idade)
    elif opc == 3:
        print('Saindo do programa')
        break
    else:
        print('ERRO ..........')
