#Não consegui esse, exercício do Palídremo
n = str(input('Digite uma frase: ')).strip().upper()
sep = n.split()
junt = ''.join(sep)
tam = len(junt)
inv = ''
for i in range(tam-1, -1, -1):
        inv += junt[i]
print(junt, inv)
if inv == junt:
    print('É Palíndromo')
else:
    print('Não é Palídromo')