menor = c = a = a2 = 0
barato = ''
while True:
    produto = str(input('Produto: ')).strip().upper()
    valor= float(input('Valor: '))
    esc = str(input('Quer continuar ?[S/N]: ')).strip().upper()
    c += 1
    a += valor
    while esc not in 'SN':
        esc = str(input('Quer continuar ?[S/N]: ')).strip().upper()
    print('=' * 25)
    if valor > 1000:
        a2 += 1
    if c == 1 or valor < menor:
        menor = valor
        barato = produto
    if esc == 'N':
        break
print(f'O valor total é = {a:10.2f}$')
print(f'Mais de {a2} produtos são mais de 1000$')
print(f'O valor mais barato foi o(a) {barato} = {menor:.2f}$')

