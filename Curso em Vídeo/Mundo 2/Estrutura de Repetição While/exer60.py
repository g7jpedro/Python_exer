n = int(input('Digite um valor para ver seu FATORIAL: '))
c = n
f = 1
while c > 0:
    print(c, end='')
    f = f * c
    c -= 1
    if c > 0:
        print(' X ', end='')
    else:
        print(' =')
print(f)