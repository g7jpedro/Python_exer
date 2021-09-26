#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = [[], [], []]
par = coluna3 = 0

for i in range(1, 10):
    v = int(input(f'Digite o {i}° valor: '))
    if v % 2 == 0:
        par+=v
    if i < 4:
        lista[0].append(v)
    elif i > 3 and i < 7:
        lista[1].append(v)
    else:
        lista[2].append(v)
for i in lista:
    print(i)
print(f'A soma dos pares é {par}')
for i in lista:
    coluna3+=i[2]
print(f'A soma da 3° coluna é {coluna3}')
print(f'O maior valor da 2° linha é {max(lista[1])}')