
from carro import Carro

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

