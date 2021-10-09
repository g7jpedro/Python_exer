
nome_txt = 'aprendendo_python.txt'
print('='*40)
print('Lendo arquivo inteiro')
print('='*40)
with open(nome_txt) as ler_arquivo:
    cont = ler_arquivo.read()
    print(cont)
print('='*40)

print('Lendo arquivo em um laço')
print('='*40)

with open(nome_txt) as ler_arquivo:
    for linhas in ler_arquivo:
        print(linhas.rstrip())
print('='*40)

print('Botando texto em uma lista')
print('='*40)

with open(nome_txt) as ler_arquivo:
    linhas = ler_arquivo.readlines()

ler_lista = ''
for linha in linhas:
    ler_lista += linha.rstrip()

print(ler_lista)
