from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
print('------------PROCESSANDO------------')
sleep(4)
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('Os valores podem formar um TRIANGULO !')
else:
    print("Os valores não podem formar um triangulo !")