
nome = input('Digite seu nome: ').title()

with open('hospede.txt', 'w') as guardar_aquivo:
    guardar_aquivo.write(nome)
