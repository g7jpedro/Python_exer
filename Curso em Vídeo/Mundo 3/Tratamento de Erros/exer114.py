# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from urllib import request
from time import sleep

print('Verificando se o site está disponível .....')
sleep(5)
try:
    acesso = request.urlopen('http://www.pudim.com.br')
except:
    print('O site Pudim não está disponível.')
else:
    print('O site Pudim está disponível.')
