primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
a = primeiro
for i in range(1, 11):
    print(a,' > ', end='')
    a += razão
print('ACABOU')