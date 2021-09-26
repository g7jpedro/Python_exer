print('========= LOJA DO PEDOCA ==========')
total = float(input('Valor total das COMPRAS: '))
opções = int(input('''=== FORMAS DE PAGAMENTO ===
[1] - Pagamento à VISTA/ CHEQUE
[2] - Pagamento à VISTA/ CARTÃO
[3] - 2x no CARTÃO
[4] - 3x ou mais no CARTÃO
Escolha a OPÇÃO: '''))
if opções == 1:
    avistaDinheiro = total * 10 / 100
    print(f'Você ganhará 10% de desconto, de {total}, você pagará {total - avistaDinheiro}')
elif opções == 2:
    avistaCartao = total * 5 / 100
    print(f'Você ganhará 5% de desconto, de {total}, você irá pagar {total - avistaCartao}')
elif opções == 3:
    print(f'Para 2x no cartão não tem DESCONTO, o total será {total}')
elif opções == 4:
    parcelas = int(input('Digite em quantas PARCELAS vocêquer pagar: '))
    p = total * 20 / 100
    print(f'Você terá juros de 20%, de {total}, você irá pagar {p + total}. Serão {(p + total) / parcelas} rais por mês.')

else:
    print('ERRRROOOOOO, escolha a opção entre 1 e 4')

