
def leiaDinheiro(msg):
    entrada = str(input(msg).strip().replace(',', '.'))
    while entrada.isalpha() or entrada.strip() == '':
        print('ERRO !')
        entrada = str(input(msg).strip())
    else:
        return float(entrada)






