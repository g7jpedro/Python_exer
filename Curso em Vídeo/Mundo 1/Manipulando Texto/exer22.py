#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print('.............................Analisando seu nome.............................')
print('Seu nome em maiúsculo é: ',nome.upper())
print(f'Seu nome em minúsculo é: ',nome.lower())
print('O seu nome tem',len(nome) - nome.count(' '),'letras ao todo')
print(f'Seu primeiro nome tem', nome.find(' '),'letras')
