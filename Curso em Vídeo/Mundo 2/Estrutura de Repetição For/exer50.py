a = 0
c = 0
for i in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
       a = a + n
       c = c + 1
print(f'O números de de PARES ecncontrados foi {c}, então a soma é {a}')
