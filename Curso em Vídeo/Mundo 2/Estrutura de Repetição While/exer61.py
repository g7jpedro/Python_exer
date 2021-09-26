primeirotermo = int(input('Primeiro TERMO: '))
razão = int(input('Digite a RAZÃO: '))
x = primeirotermo
c = 1
while c < 11:
    print(x, end=' > ')
    x += razão
    c += 1
print('FIM')