"""
 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
 aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
média = (nota1 + nota2) / 2

print(f'Sua média foi {média}')
if média >= 7 and média != 10:
    print('Aprovado !')
elif média < 7:
    print('Reprovado !')
else:
    print('Aprovado com Distinção')
