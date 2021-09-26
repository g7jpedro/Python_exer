distância = float(input('Qual a distância da viagem ? '))
p1 = distância*0.50
p2 = distância*0.45
if distância <= 200:
    print(f'O valor da passagem é {p1:.2f}')
else:
    print(f'O valor da passagem é {p2:.2f}')
