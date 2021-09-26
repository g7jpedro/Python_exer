a = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        a = a + i
        cont = cont + 1
print(f'A soma dos números ímpares multiplos de 3 é {a}, e o números de multplos por 3 foram {cont}')