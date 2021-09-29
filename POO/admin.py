from usuario import User

class Privilegios():
    def __init__(self):
        self.privilegiados = 'Mario', 'luigi'

    def mostrar_privilegiados(self):
        print('Privilegiados: ')
        for i in self.privilegiados:
            print(i)


class Admin(User):
    def __init__(self, primeiro_nome, segundo_nome):
        super(Admin, self).__init__((primeiro_nome, segundo_nome))
        self.privilegiados = Privilegios()