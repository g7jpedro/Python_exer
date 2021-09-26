def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except(TypeError, ValueError):
            print('ERRO ! Tipo ou valor errado.')
            continue
        else:
            return valor


def linha(tam=40):
    return '='*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opç = leiaint('Escolha: ')
    return opç
