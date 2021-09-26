"""
 Fazendo 3 instâncias restaurantes
"""
class Restaurante():

    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome = nome_restaurante
        self.tipo = tipo_cozinha

    def descrição_restaurante(self):
        print(f'O nome do restaurante é {self.nome} e é feito {self.tipo}')

    def aberto(self):
        print(f'O restaurante {self.nome} está aberto')


restaurante = Restaurante('Casa do João', 'Salgados')
restaurante2 = Restaurante('Casa da Maria', 'Pastel')
restaurante3 = Restaurante('Casa do Pedro', 'Peixe')

restaurante.descrição_restaurante()
restaurante2.descrição_restaurante()
restaurante3.descrição_restaurante()