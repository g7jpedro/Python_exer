"""
 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações.
"""

senha = input('Digite uma senha: ')
nick = input('Digite um usuário: ')
while senha.upper() == nick.upper():
    print('ERRO ! Senha e usuários não podem ser iguais.')
    senha = input('Digite uma senha: ')
    nick = input('Digite um usuário: ')

print('Conta Criada.. fim....')