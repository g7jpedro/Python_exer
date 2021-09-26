#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n = float(input('Digite seu salário: '))
n2 = float(input('Digite a % de aumento: '))
aume = (n*n2)/100
print(f'Seu salário atual é {n} reais, com o aumento de {n2}% será = {n+aume} ')