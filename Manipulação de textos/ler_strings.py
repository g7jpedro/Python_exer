
nomearquivo = 'digitação.txt'

with open(nomearquivo) as ler_arquivo:
    linhas = ler_arquivo.readlines()


ler_strings = ''
for linha in linhas:
    ler_strings += linha.strip()

aninversário = input('Sua da está no arquivo ?: ')
if aninversário.upper() in ler_strings.upper():
    print('Sim, ele está')
else:
    print('Não, ele não está')
