
class Roupa():
    """
    Classe para criação de Roupas
    """
    def __init__(self, tamanho, cor, tecido):
        self.tamanho = tamanho
        self.cor = cor
        self.tecido = tecido

    def info_roupa(self):
        print(f'{self.tamanho}')
        print(f'{self.cor}')
        print(f'{self.tecido}')

    def mudar_tamanho(self, tamanho):
        self.tamanho = tamanho

    def mudar_cor(self, cor):
        self.cor = cor

    def mudar_tecido(self, tecido):
        self.tecido = tecido


class Cueca(Roupa):
    def __init__(self, tamanho, cor, tecido):
        super(Cueca, self).__init__(tamanho, cor, tecido)


class Short(Roupa):
    def __init__(self, tamanho, cor, tecido):
        super(Short, self).__init__(tamanho, cor, tecido)


