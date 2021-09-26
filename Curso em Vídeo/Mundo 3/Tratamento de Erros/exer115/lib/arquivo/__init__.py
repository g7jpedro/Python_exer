from lib.interface import *

def arquivo_encontrado(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro !')
    else:
        print('Arquivo criado com sucesso !')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro !')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro')
        else:
            print(f'{nome} casdastrado com sucesso !')
            a.close()