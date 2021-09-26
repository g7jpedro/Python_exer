

def leiaint(v):
    while True:
        try:
            valor = int(input(v))
        except:
            print('ERRO ! Insira um valor inteiro corretamente.')
            continue
        else:
            return valor


