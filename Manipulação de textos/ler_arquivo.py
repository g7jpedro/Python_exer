
nomearquivo = 'digitação.txt'

with open(nomearquivo) as ler_arquivo:
    linhas = ler_arquivo.readlines()

for linha in linhas:
    print(linha.rstrip())
