"""
 Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
 Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""

n1 = str(input('Digite uma palavra: ')).strip().title()
n2 = str(input('Digite uam palavra de novo: ')).strip().title()

print(f'Primeira coisa digitada: {n1} I Tam: {len(n1)}')
print(f'Segunda coisa digitada: {n2} I Tam: {len(n2)}')
if len(n1) == len(n2):
    print('Mesmo comprimento !')
else:
    print('Comprimento diferentes !')

if n1.upper() == n2.upper():
    print('Mesmo conteúdo')
else:
    print('Conteúdo diferente')





















