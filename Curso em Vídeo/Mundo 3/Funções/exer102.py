#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(fato, opção=True):
    '''
    >> Cáculo para Fatorial
    :param fato: receberá o valor para o cálculo do fatorial
    :param opção: Opção se mostrará o passo a passo ou só o resultado final do fatorial
    :return:
    '''

    fatorial = 1
    for i in range(fato, 0, -1):
        fatorial *= i
        if opção:
            print(fatorial)

    return fatorial


print(fatorial(5))
help(fatorial)