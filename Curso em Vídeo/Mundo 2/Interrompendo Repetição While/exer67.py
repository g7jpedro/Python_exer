while True:
    n = int(input('Digite o VALOR em que quer ver a TABUADA: '))
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    if n < 0:
        break
print('ACABOU')