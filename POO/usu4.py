

class User():

    def __init__(self, primeiro_nome, segundo_nome=''):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome

    def descri_user(self):
        print(f'Nome do user é {self.primeiro_nome} {self.segundo_nome}')

    def saudar(self):
        print(f'Olá, {self.primeiro_nome} !')


class Privilegios():
    def __init__(self):
        self.privilegiados = 'Mario', 'luigi'

    def mostrar_privilegiados(self):
        print('Privilegiados: ')
        for i in self.privilegiados:
            print(i)


class Admin(User):
    def __init__(self, primeiro_nome, segundo_nome):
        super(Admin, self).__init__((primeiro_nome, segundo_nome))
        self.privilegiados = Privilegios()


pessoa = Admin('João', 'Pedro')
pessoa.privilegiados.mostrar_privilegiados()

