# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
# números como um valor monetário formatado.

import moedas


v = int(input('Digite um valor: '))
print(f'Aumentando 10% é = {moedas.aumentar(v)}')
print(f'Diminuindo 13% é = {moedas.diminuir(v)}')
print(f'O dobro de {moedas.moeda(v)} é = {moedas.moeda(moedas.dobro(v))}')
print(f'A metade de {moedas.moeda(v)} é = {moedas.moeda(moedas.metade(v))}')