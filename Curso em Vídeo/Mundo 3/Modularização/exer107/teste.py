#  Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e
#  metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moedas


v = int(input('Digite um valor: '))
print(f'Aumentando 10% é = {moedas.aumentar(v)}')
print(f'Diminuindo 13% é = {moedas.diminuir(v)}')
print(f'O dobro de {v} é = {moedas.dobro(v)}')
print(f'A metade de {v} é = {moedas.metade(v)}')