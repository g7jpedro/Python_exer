#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(msg):
    v = str(input(msg).strip())
    if v.isalpha() or v == '':
        print('\033[1;31mERRO !!\033[m')
        v = leiaint('Digite um valor inteiro: ')
    return v


v = leiaint('Digite um valor ineteiro: ')
print(f'O  valor {v} é inteiro !')