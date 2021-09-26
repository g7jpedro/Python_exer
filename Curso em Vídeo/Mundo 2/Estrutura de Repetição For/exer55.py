#Não consegui
maior = 0
menor = 0
for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print(f'O maior é {maior} e o menor {menor}')