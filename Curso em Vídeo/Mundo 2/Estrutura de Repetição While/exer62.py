# Que código mais lindo
n1 = int(input('Primeiro termo: '))
n2= int(input('Razão: '))
c = 0
a = n1
t = 10
while c < t:
    print(a, ' > ', end='')
    a += n2
    c += 1
    if c == t:
        print('PAUSE')
        novos = int(input('Quantos termos mais ?: '))
        if novos != 0:
            t += novos
        else:
            print('ACABOU')
            print(f'A progressão acabou com {t} termos mostrados.')

















