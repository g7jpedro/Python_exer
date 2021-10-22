
try:
    with open('dogs.txt') as ler_arquivo:
        cont = ler_arquivo.read()

    with open('cats.txt') as  ler_arquivo:
        cont2 = ler_arquivo.read()

except FileNotFoundError:
    pass

else:
    print(f'Dogs:\n{cont}')
    print('='*20)
    print(f'Cats:\n{cont2}')