"""
 Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta,
 nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é
 opcional, com valor default zero e os demais atributos são obrigatórios.
"""


class Conta():
    def __init__(self, num_conta, nome, saldo=0):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar_dinheiro(self, sacar):
        if sacar > self.saldo:
            print('Você não tem tudo isso em conta !')
        else:
            self.saldo -= sacar

    def mostrar_dados(self):
        print(f'Número de conta: {self.num_conta}')
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')


minha_conta = Conta(num_conta= 383832284, nome= 'João Pedro', )
minha_conta.mostrar_dados()