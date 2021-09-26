n = float(input('Digite seu salário R$ '))
p1 = n*10/100+n
p2 = n*15/100+n
if n > 1250:
    print(f'Terão um aumento de 10%, então ficará {p1:.2f} reais')
else:
    print(f'Terão um aumento de 15%, então ficará {p2:.2f} reais')