#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
# manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep

c = {'Sem': '\033[m',
     'Branco': '\033[1;30m',
     'Vermelho': '\033[1;31m',
     'Amarelo': '\033[1;33m',
     'Azul': '\033[1;34m'}


def ajuda(msg, cor=c['Sem']):
    print(c[cor])
    help(msg)
    print(f'\033[m')


def texto_personalizado(msg, cor=c['Sem']):
    print('='*len(msg), end='')
    print(f'{c[cor]}')
    print(msg)
    print(c['Sem'],end='')
    print('=' * len(msg))


while True:
    texto_personalizado('Sistema de Ajuda Pyhton', cor='Vermelho')
    escolha = str(input('Digite a Função ou Biblioteca: ')).strip().lower()
    if escolha.upper() == 'FIM':
        sleep(3)
        break
    texto_personalizado('Acessando o Manual ......', cor='Azul')
    sleep(3)

    ajuda(escolha, cor='Azul')


texto_personalizado('FIM ........', 'Vermelho')