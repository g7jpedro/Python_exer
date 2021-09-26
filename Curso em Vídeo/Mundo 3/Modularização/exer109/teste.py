
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
# desafio 108.

import moedas


v = int(input('Digite um valor: '))
print(f'Aumentando 10% é = {moedas.aumentar(v, True)}')
print(f'Diminuindo 13% é = {moedas.diminuir(v, True)}')
print(f'O dobro de {moedas.moeda(v)} é = {moedas.dobro(v, True)}')
print(f'A metade de {moedas.moeda(v)} é = {moedas.metade(v, True)}')