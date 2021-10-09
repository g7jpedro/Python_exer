class Roupa():
    def __init__(self, cor='Branca', tamanho='P', tecido='Poliester'):
        self.cor = cor
        self.tamanho = tamanho
        self.tecido = tecido

    def roupa_descrição(self):
        print('DESCRIÇÃO DA ROUPA ESCOLHIDA:')
        print(f'Cor: {self.cor}\nTamnho: {self.tamanho}\nTecido: {self.tecido}')
        print('='*50)


class Personalização():
    def __init__(self, logo='Nada', frase='Nada'):
        self.logo = logo
        self.frase = frase

    def descrição_personalização(self):
        print(f'A peça terá uma logo de um [ {self.logo} ]\nE a frase/palavra [ {self.frase} ]')

    def fazer_personalização(self, logo, frase):
        self.logo = logo
        self.frase = frase


class Camisa(Roupa):
    def __init__(self, cor='Branco', tamanho='P', tecido='Poliester'):
        super().__init__(cor, tamanho, tecido)
        self.manga = ''
        self.personalização = Personalização()

    def escolher_manga(self, manga='Média'):
        self.manga = manga

    def mostrar_tam_manga(self):
        print(f'Tamnho da Manga é {self.manga}')