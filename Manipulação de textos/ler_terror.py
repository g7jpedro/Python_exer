
with open('terror.txt') as ler_arquivo:
    cont = ler_arquivo.read()

ler = cont.lower().count('the')
print(f'Foram encontradas: {ler} "the" no texto.')
