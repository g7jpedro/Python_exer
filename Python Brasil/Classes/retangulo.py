"""
 Classe Retangulo: Crie uma classe que modele um retangulo:

 Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
 Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
 Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
 Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""

 #Não terminei
class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self, ladoa, ladob):
        self.base = ladoa
        self.altura= ladob

    def mostrar_valor_lado(self):
        print(f'O valor dos lado é de {self.base}x{self.altura}')

    def calcular_perimetro(self):
        perimetro = (2*self.base) + (2*self.altura)
        return perimetro


retangulo = Retangulo(6, 4)
retangulo.mostrar_valor_lado()

