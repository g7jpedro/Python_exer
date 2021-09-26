from math import sqrt, pow
cateto = float(input('Digite o valor do Cateto Oposto: '))
adjacente = float(input('Digit o valor da adjacente: '))
hipotenusa = sqrt(pow(cateto,2) + pow(adjacente,2))
print(f'O valor da Hipotenusa é {hipotenusa:.2f}')