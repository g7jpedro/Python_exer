
class Dog():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(f'{self.nome} agora está sentado !')

    def rolando(self):
        print(f'{self.nome} está rolando !')


meu_dog = Dog('willie', 6)
seu_dog = Dog('Lucy', 3)

print("Meus dog se chama " + meu_dog.nome.title() + ".")
print("A idade do meu dog é " + str(meu_dog.idade) + " anos.")
meu_dog.sentar()
print("\nO nome do seu dog é " + seu_dog.nome.title() + ".")
print("A idade do seu dog é" + str(seu_dog.idade) + " anos.")
seu_dog.rolando()

