
class User():

    def __init__(self, primeiro_nome, segundo_nome=''):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome

    def descri_user(self):
        print(f'Nome do user é {self.primeiro_nome} {self.segundo_nome}')

    def saudar(self):
        print(f'Olá, {self.primeiro_nome} !')


pessoa = User('João')
pessoa2 = User('Natália', 'Figueiredo')
pessoa3 = User('Victor', 'Gabriel')

pessoa.descri_user()
pessoa.saudar()
pessoa2.descri_user()
pessoa2.saudar()
pessoa3.descri_user()
pessoa3.saudar()