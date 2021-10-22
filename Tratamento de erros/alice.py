
nome_arquivo = 'alice.txt'

try:
    with open(nome_arquivo) as ler_objeto:
        cont = ler_objeto.read()
except FileNotFoundError:
    msg = 'Desculpe, mas não achamos esse arquivo.'
    print(msg)
else:
    palavras = cont.split()
    num_frases = len(palavras)
    print(f'O arquivo tem cerca de {num_frases} palavras')