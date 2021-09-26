#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(0,9):
    valores = int(input('Digite o valor: '))
    if i == 0:
        lista.append(valores)
        print('\033[34mAdicionado ao final..\033[m')
    elif valores > max(lista):
        lista.append(valores)
        print('\033[34mAdicionado ao final..\033[m')
    elif valores < min(lista):
        lista.insert(0,valores)
        print('\033[34mAdicionado no começo..\033[m')
    else:
        for pos,i in enumerate(lista):
            if valores <= lista[pos]:
                lista.insert(pos,valores)
                print(f'Adicionado na posição \033[34m{pos}..\033[m')
                break
print(f'lista em ordem:\n\033[34m{lista}\033[m')

