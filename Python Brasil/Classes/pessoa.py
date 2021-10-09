"""
 Crie uma classe que modele uma pessoa:

 Atributos: nome, idade, peso e altura
 Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo
 a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa():
    def __init__(self, nome, idade=0, peso=0, altura=0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelher(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def crescer(self, crescer):
        self.altura += 1

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def descrição_pessoa(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura:.0f}')
        print('='*30)


pessoa = Pessoa('João ', 15, 74, 176)
pessoa.descrição_pessoa()
pessoa.envelher()
pessoa.descrição_pessoa()
pessoa.envelher()
pessoa.descrição_pessoa()
pessoa.engordar()
pessoa.descrição_pessoa()
