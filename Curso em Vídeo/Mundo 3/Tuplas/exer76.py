#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Caderno',2.50,
            'Lápis',1.50,
            'Bolsa',10,
            'Caneta',1.80,
            'Corretivo',1,
            'Apontador',1.30,
            'Régua',2.30)

print('\033[34m=====LISTAGEM DE PREÇOS======\033[m')
for i in range(0,len(produtos)):
    if i % 2 == 0:
        print(produtos[i],end='-------------- R$ ')
    else:
        print(f'{produtos[i]:.2f}')
print('\033[34m='*30)