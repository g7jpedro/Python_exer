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


class Bateria():
    def __init__(self, bateria_nivel=70):
        self.bateria_nivel = bateria_nivel

    def descri_bateria(self):
        print(f'A bateria do carro elelétrico está em {self.bateria_nivel}%')

    def recarregar(self, bateria):
        if self.bateria_nivel + bateria > 100:
            self.bateria_nivel = 100
        else:
            self.bateria_nivel += bateria

    def distância_percorrida(self):
        if self.bateria_nivel == 70:
            km = 240
        elif self.bateria_nivel == 85:
            km = 270

        menssagem = f'Este carro pode ir aproximadamente em {str(km)}'
        menssagem += f' percorridos completo'
        print(menssagem)

    def atualizar_bateria(self):
        if self.bateria_nivel != 85:
            self.bateria_nivel = 85


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.bateria = Bateria()


my_choque = CarroEletrico('Tesla', 'Modelo S', 2018)
print(my_choque.nome_descritivo())
my_choque.bateria.descri_bateria()
my_choque.bateria.distância_percorrida()
my_choque.bateria.atualizar_bateria()
my_choque.bateria.distância_percorrida()

