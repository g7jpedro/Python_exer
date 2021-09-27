

class User():

    def __init__(self, primeiro_nome, segundo_nome=''):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.tentativas_login = 0

    def descri_user(self):
        print(f'Nome do user é {self.primeiro_nome} {self.segundo_nome}')

    def saudar(self):
        print(f'Olá, {self.primeiro_nome} !')

    def incrementar_tentativas_login(self):
        self.tentativas_login += 1

    def quant_tentativas_login(self):
        print(f'{self.tentativas_login} tentativas de login')

    def resetar_tentativas_login(self):
        self.tentativas_login = 0


pessoa = User('João')
pessoa.descri_user()
pessoa.saudar()

pessoa.incrementar_tentativas_login()
pessoa.incrementar_tentativas_login()
pessoa.incrementar_tentativas_login()
pessoa.incrementar_tentativas_login()
pessoa.resetar_tentativas_login()
pessoa.quant_tentativas_login()









