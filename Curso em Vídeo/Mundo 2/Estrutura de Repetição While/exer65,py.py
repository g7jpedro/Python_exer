c = a = maior = menor = 0
q = 'S'
while q in 'S':
    n = int(input('Digite um número: '))
    q = str(input('Quer continuar ? [S/N]: ')).upper().strip()
    if q not in 'SN':
        print('ERRO. DIgite somente S ou N')
        q = str(input('Quer continuar ? [S/N]: ')).upper().strip()
    c += 1
    a += n
    if c == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if q == 'N':
        print(f'Você digitou {c} números. A média foi de {a/c:.1f}')
        print(f'O maior valor foi {maior}. O menor foi {menor}')