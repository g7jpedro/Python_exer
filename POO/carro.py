
class Carro():

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.leitura_odometro = 0

    def nome_descritivo(self):
        nome_completo = f'{str(self.ano)} {self.marca} {self.modelo}'
        return nome_completo

    def ler_odometro(self):
        print(f'Este carro tem {str(self.leitura_odometro)}')

    def atualizar_odometro(self, quilometro):
        if quilometro >= self.leitura_odometro:
            self.leitura_odometro = quilometro
        else:
            print('Você não pode reverter um hodômetro !')

    def incrementando_odometro(self, quilometros):
        self.leitura_odometro += quilometros


meu_carro = Carro('Chevrolet', 'Onix', '2018')
print(meu_carro.nome_descritivo())

meu_carro.atualizar_odometro(23500)
meu_carro.ler_odometro()

meu_carro.incrementando_odometro(100)
meu_carro.ler_odometro()

