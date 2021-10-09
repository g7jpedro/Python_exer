
with open('aprendendo_python.txt') as ler_arquivo:
    for linha in ler_arquivo:
        print(linha.rstrip().replace('python', 'PHP'))

