#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado !')
    esc = str(input('Quer continuar ? [S/N]: '))[0].upper().strip()
    while esc not in 'SN':
        print('ERRO! Digite S ou N')
        esc = str(input('Quer continuar ? [S/N]: '))[0].upper().strip()
    if esc == 'N':
        break
print(lista)
print(f'Valores digitados na ordem crescente:\n{sorted(lista)}')
