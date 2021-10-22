"""
 Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e
Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma
combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""


class Tamagushi():
    def __init__(self, nome, fome, saúde, idade):
        self.nome = nome
        self.fome = fome
        self.saúde = saúde
        self.idade = idade

    def status_tamagushi(self):
        print(f'Nome: {self.nome}')
        print(f'Fome: {self.fome}/10')
        print(f'Sáude: {self.saúde}/10')
        print(f'Idade: {self.idade}')
        print(f'Humor: {self.mostrar_humor()}')

    def mostrar_humor(self):
        if self.fome <=5 or self.saúde <= 5:
            return 'Irritado'
        elif 5 < self.saúde <= 8 or 5 < self.fome <= 8:
            return 'Normal'
        else:
            return 'Muito bem'


bichinho = Tamagushi('Pedoca', 9, 9, 5)
bichinho.status_tamagushi()