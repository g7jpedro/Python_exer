#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a expressão: '))
c = c2 = 0
for i in exp:
    if i == '(':
        c+=1
    elif i == ')':
        c2+=1
if c == c2:
    print('Expressão válida')
else:
    print('Expressão inválida')

