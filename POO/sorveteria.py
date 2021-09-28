class Restaurante():

    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome = nome_restaurante
        self.tipo = tipo_cozinha
        self.numeros_servidos = 0

    def descrição_restaurante(self):
        print(f'O nome do restaurante é {self.nome} e é feito {self.tipo}')

    def aberto(self):
        print(f'O restaurante {self.nome} está aberto')

    def ler_numeros_sevidos(self):
        print(f'{self.numeros_servidos} pessoas foram servidas')

    def atualizar_numeros_atendidos(self, numero_servidos):
        if numero_servidos >= self.numeros_servidos:
            self.numeros_servidos = numero_servidos
        else:
            print('Você não pode botar menos clientes que já tem')

    def incrementar_pessoas_atendidas(self, incrementar_pessoas):
        self.numeros_servidos += incrementar_pessoas


class Sorveteria(Restaurante):
    def __init__(self, nome_restaurante, tipo_cozinha):
        super(Sorveteria, self).__init__(nome_restaurante, tipo_cozinha)
        self.sabores = 'Chocolate', 'Morango'

    def sabor(self):
        print('Sabores disponíveis: ')
        for i in self.sabores:
            print(i)


minha_sorveteria = Sorveteria('Sorveteria do João', 'Sorvete')
minha_sorveteria.sabor()


