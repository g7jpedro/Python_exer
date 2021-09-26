"""
 Faça um programa que leia e valide as seguintes informações:
 Nome: maior que 3 caracteres;
 Idade: entre 0 e 150;
 Salário: maior que zero;
 Sexo: 'f' ou 'm';
 Estado Civil: 's', 'c', 'v', 'd';
"""


nome = str(input('Digite seu nome: '))
while len(nome) <= 3:
    print('ERRO ! O nome precisa ter mais de 3 caracteres')
    nome = str(input('Digite seu nome: '))

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    print('ERRO ! Idade deve ser entre 0 e 150')
    idade = int(input('Digite sua idade: '))

salário = float(input('Digite seu salário: '))
while salário < 0:
    print('ERRO ! O salário deve ser maior que 0')
    salário = float(input('Digite seu salário: '))

sexo = str(input('Digite seu sexo [F/M]: ')).upper()[0]
while sexo not  in 'FM':
    print('ERRO ! Digite sexo válido')
    sexo = str(input('Digite seu sexo [F/M]: ')).upper()[0]

estado_civil = str(input('Digite seu estado civil[S, C, V, D]: ')).upper()[0]
while estado_civil not in 'SCVD':
    print('ERRO ! Digite um estado civil válido')
    estado_civil = str(input('Digite seu estado civil[S, C, V, D]: ')).upper()[0]

