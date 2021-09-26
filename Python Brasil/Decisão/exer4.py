"""
 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = str(input('Digite um letra: ')).upper()[0]
if letra in 'AEIOU':
    print('Vogal')
else:
    print('Consoante')