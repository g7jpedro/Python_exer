from random import randint
print('==-=='*8)
print('''VAMOS JOGAR !!
Escolha uma das opções:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
jog = ('PEDRA', 'PAPEL', 'TESOURA')
sort = randint(0,2)
op = int(input('Digite a opção: '))
if op > 3:
    print('ERRO !! ESCOLHA AS OPÇÕES ENTRE 0 e 2')
else:
    print('==-=='*6)
    print(f'O JOGADOR ESCOLHEU {jog[op]}\nO COMPUTADOR ESCOLHEU {jog[sort]}')
    print('==-=='*6)
if op == 0:
    if sort == 0:
        print('EMPATE**')
    elif sort == 1:
        print('O COMPUTADOR GANHOU**')
    elif sort == 2:
        print('O JOGADOR GANHOU**')
if op == 1:
    if sort == 1:
        print('EMPATE**')
    elif sort == 0:
        print('O JOGADOR GANHOU**')
    elif sort == 2:
        print('O COMPUTADOR GANHOU**')
if op == 2:
    if sort == 2:
        print('EMPATE**')
    elif sort == 0:
        print('O COMPUTADOR GANHOU**')
    elif sort == 1:
        print('O JOGADOR GANHOU**')



