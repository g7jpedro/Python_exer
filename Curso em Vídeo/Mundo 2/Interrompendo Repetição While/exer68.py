from random import randint
cont = 0
while True:
    print('=*=' * 10)
    n = int(input('Digite um valor: '))
    esc = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()
    sort = randint(1, 10)
    soma = n + sort
    if esc == 'P':
        if soma % 2 == 0:
            print(f'Jogador: {n}\nComputador: {sort}.\nResultado: {soma} > PAR >> JOGADOR GANHOU')
            cont += 1
        else:
            print(f'Jogador: {n}\nComputador: {sort}.\nResultado: {soma} > ÍMPAR >> COMPUTADOR GANHOU')
            break
    if esc == 'I':
        if soma % 2 != 0:
            print(f'Jogador: {n}\nComputador: {sort}.\nResultado: {soma} > ÍMPAR >> JOGADOR GANHOU')
            cont += 1
        else:
            print(f'Jogador: {n}\nComputador: {sort}.\nResultado: {soma} > PAR >> COMPUTADOR GANHOU')
            break

print(f'Você ganhou {cont} vezes !')
