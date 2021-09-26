from random import randint
print('=='*9)
print('JOGO DA ADVINHAÇÃO')
print('=='*9)
sort = randint(0,10)
esc = 0
cont = 0
while esc != sort:
    esc = int(input('Tente advinha em qual valor pensei, entre 0 e 10. DIGITE: '))
    cont += 1
    if esc > sort:
        print('É menos ...')
    elif esc < sort:
        print('É mais ...')
print('=='*19)
print('ACERTOU')
print(f'Precisou de {cont} tentativas para acertar.')
print('=='*19)