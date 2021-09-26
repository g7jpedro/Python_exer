from random import randint
import time
p = randint(0,5)
print('===='*20)
print('Vou pensar em um valor entre 0 e 5 ! O Você tente advinhar ...')
print('===='*20)

jogador = int(input('Qual número eu pensei ??: '))
print('PROCESSANDO ......')
time.sleep(4)
if jogador == p:
    print('===='*20)
    print(F'PERDI ! MEU PARABÉNS ! VOCÊ ACERTOU.\nO VALOR QUE ESCOLHI FOI EXATAMENTE {jogador}')
    print('===='*20)
else:
    print('====' * 20)
    print(f'GANHEI ! VOCÊ ERROU, O NÚMERO QUE EU ESCOLHI FOI {p} E NÃO {jogador} HAHAH')
