import uteis

lista = []

while True:
    op = int(input('Ecolha uma opção:'
                   '\n1 - Ver lista de pessoas'
                   '\n2 - Cadastrar pessoas'
                   '\n3 - Finalizar programa'
                   '\nDigite: '))
    if op == 1:
        print(lista)
    elif op == 2:
        nome = str(input('Digite o nome da pessoa: '))
        uteis.leiastr(nome)
        lista.append(nome)
    elif op == 3:
        break

print('FIM .....')