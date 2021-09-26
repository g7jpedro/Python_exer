#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

t = (int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))
print(t)
print(f'O valor \033[34m9\033[m apareceu \033[34m{t.count(9)}\033[m vezes.')
if 3 in t:
    print(f'O primeiro valor \033[34m3\033[m foi digitado na posição \033[34m{t.index(3)}\033[m')
else:
    print(f'O \033[34m3\033[m não está na lista')
c = 0
print('Pares digitados:\033[34m ',end='')
for i in t:
    if i % 2 == 0:
        print(i,end=' ')
