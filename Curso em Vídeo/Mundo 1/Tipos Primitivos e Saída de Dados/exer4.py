#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
n = input('Digite algo: ')
print(f'É númerico ?:',n.isnumeric())
print(f'É de que tipo ?:',type(n))
print(f'É alfabético ?: ',n.isalpha())
print(f'É maiúsculo ?:',n.isupper())
print(f'É minúsculo ?:',n.islower())
print(f'É capitalizado ?:',n.istitle())