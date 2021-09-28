"""
 Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a
 quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função
 “altera” o valor de custo para incluir o imposto sobre vendas.
"""


def somaImposto(taxa_imposto, custo):
    imposto = (taxa_imposto * custo)/100
    return imposto + custo


imposto = int(input('Digite o imposto que eur colocar: '))
custo_item = float(input('Digite o valor do item: '))
total = somaImposto(imposto, custo_item)
print(f'Valor do Item: {custo_item}$ e com imposto é {total}$ ')
