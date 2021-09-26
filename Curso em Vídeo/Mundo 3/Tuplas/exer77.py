#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

p = ('NARUTO','HAIKYUU','KISEIJUU',
     'KARAKAI','SAMURAI','DURARARA')
for i in p:
    print(f'\nNa palavra {i} temos ',end='')
    for p in i:
        if p in 'AEIOU':
            print(p,end='')
print('FIM')