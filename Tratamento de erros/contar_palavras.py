
def cont_palavras(nome_arquivo):
    """

    :param nome_arquivo: Nome do arquivo para ser aberto
    :return: Irá retornar o número de palavras que tem no arquivo
    """
    try:
        with open(nome_arquivo) as ler_objeto:
            cont = ler_objeto.read()
    except FileNotFoundError:
        nome = 'sem_arquivos.txt'
        with open(nome, 'a') as ler_arquivo:
            ler_arquivo.write(f'{nome_arquivo.rstrip()}\n')

    else:
        palavras = cont.split()
        num_frases = len(palavras)
        print(f'O arquivo {nome_arquivo} tem cerca de {num_frases} palavras')


nome_arquivos = ['alice.txt', 'siddhartha.txt', 'little_women.txt','teste.txt', 'naruto.txt']

for nome_arquivo in nome_arquivos:
    cont_palavras(nome_arquivo)