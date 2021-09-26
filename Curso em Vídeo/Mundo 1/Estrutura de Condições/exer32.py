import datetime
data = int(input("Digite o ano para verficarmos se é bissexto: "))
print('PROCESSANDO RESPOSTA ..........')
if data == 0:
    
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print('O ano é Bissexto !', )
else:
    print('O ano não é bissexto !')