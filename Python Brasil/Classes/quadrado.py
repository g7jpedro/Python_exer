"""
 Classe Quadrado: Crie uma classe que modele um quadrado:

 Atributos: Tamanho do lado
 Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado():
    def __init__(self, tamanho_lado= 40):
        self.tamanho_lado = tamanho_lado

    def calcular_area(self):
        cálculo = self.tamanho_lado * 4
        return cálculo

    def descri_quadrado(self):
        print(f'O valor do lado é {self.tamanho_lado}\nA Àrea é de {self.calcular_area()} ')

    def mudar_valor_lado(self, valor_lado):
        self.tamanho_lado = valor_lado


quadrado = Quadrado()
quadrado.descri_quadrado()

quadrado.mudar_valor_lado(10)
quadrado.descri_quadrado()


