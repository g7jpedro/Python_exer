# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except(TypeError, ValueError):
            print('ERRO ! Tipo ou valor errado.')
            continue
        else:
            return valor


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO ! Tipo ou valor errado.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferio não botar nenhum valor.')
            return 0
        else:
            return valor


v = leiaint('Digite um valor inteiro: ')
v2 = leiafloat('Digite um valor float: ')
print(f'O valor inteiro digitado foi {v} e o float foi {v2}')


