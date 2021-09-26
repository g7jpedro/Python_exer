from time import sleep
nome = str(input('Olá, Qual o seu nome ?? ')).strip()
n = int(input(f'Olá, {nome}! Qual foi a velocidade corrida ?\n '))
multa = (n-80)*7
print('................ANALISANDO SE TEM ALGUMA IRREGULARIDADE--------------')
sleep(4)
if n > 80:
    print('IRREGULARIDADE DETECTADA!')
    print('CALCULANDO MULTA .......')
    sleep(5)
    print(f'Você foi multado !\nVocê irá pagar {multa} reais !')
else:
    print('Você não não fez nenhuma infração.......')