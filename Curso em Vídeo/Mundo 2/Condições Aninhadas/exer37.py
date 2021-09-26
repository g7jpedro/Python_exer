n = int(input('Digite um valor inteiro: '))
print('''Digite umas das alternativas
[1] - Converter para BINÁRIO
[2] - Converter para OCTAL
[3] - Converter para HEXADECIMAL''')
opção = int(input('Digite a opção: '))
if opção == 1:
    print(f'O valor digitado foi {n}, convertido para BINÁRIO fica: {bin(n)[2:]}')
elif opção == 2:
    print(f'O valor digitado foi {n}, convertido para OCTAL fica: {oct(n)[2:]}')
elif opção == 3:
    print(f'O valor digitado foi {n}, convertido para HEXADECIMAL fica {hex(n)[2:]}')
elif opção != 1 and opção != 2 and opção != 3:
    print('ERRO ! Você só pode escolher as opção de 1 a 3 !')
