"""
 Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do
 canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro
 de faixas válidas.
"""


class Televisão():
    def __init__(self, canal=5, volume=2):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self):
        if self.volume <= 100:
            self.volume += 1
        else:
            self.volume = 100

    def diminuir_volume(self):
        if self.volume >= 0:
            self.volume -= 1
        else:
            self.volume = 0

    def mostrar_volume(self):
        print(f'Volume da tv está em {self.volume}')

    def mudar_canal(self, canal):
        self.canal = canal

    def mostrar_canal(self):
        print(f'O canal está no {self.canal} ')


televisor = Televisão()
televisor.aumentar_volume()
televisor.mostrar_canal()
televisor.mudar_canal(4)
televisor.mostrar_canal()


