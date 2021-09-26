#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição
#ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('------------- ANALISANDO --------------')
print('A letra A pararece na frase:', frase.count('A'), 'vezes')
print('A letra A aparece pela primeira vez na posição:',frase.find('A')+1)
print('A letra A aparece pela última vez na posição:',frase.rfind('A')+1)

