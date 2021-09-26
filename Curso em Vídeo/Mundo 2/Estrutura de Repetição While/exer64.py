a = 0
c = 0
n = 0
n = int(input('Digite um valor [999 PARA PARAR]: ')) #n entendi a parada do flag
while n != 999:
    a += n
    c += 1
    n = int(input('Digite um valor [999 PARA PARAR]: '))
print(f'Você digitou {c} números e ao soma entre eles deu {a}')