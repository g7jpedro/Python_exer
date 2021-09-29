"""
 Classe Bola: Crie uma classe que modele uma bola:

 Atributos: Cor, circunferência, material
 Métodos: trocaCor e mostraCor
"""


class Bola():
    def __init__(self, cor='Branca', circuferencia='20', material='Couro'):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocar_cor(self, cor):
        self.cor = cor

    def mostrar_cor(self):
        print(f'A cor da bola é {self.cor}')

    def descri_bola(self):
        print(f'{self.cor} - {self.circuferencia} - {self.material}')


bola = Bola()
bola.descri_bola()
bola.mostrar_cor()
bola.trocar_cor('Preta')
bola.mostrar_cor()
