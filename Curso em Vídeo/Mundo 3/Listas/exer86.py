#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

lista = [[], [], []]
for i in range(1, 10):
    v = int(input(f'Digite o {i}° valor: '))
    if i < 4:
        lista[0].append(v)
    elif i > 3 and i < 7:
        lista[1].append(v)
    else:
        lista[2].append(v)
for i in lista:
    print(i)