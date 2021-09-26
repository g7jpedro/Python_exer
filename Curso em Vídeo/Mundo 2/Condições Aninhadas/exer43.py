peso = float(input('Digite seu PESO KG: '))
altura = float(input('Digite sua ALTURA: '))
f = float = peso / pow(altura,2)
if f < 18.5:
    print(f'Seu IMC foi {f:.1f}, Abaixo do peso.')
elif f >= 18.5 and f <= 24.9:
    print(f'Seu IMC foi {f:.1f}, Peso normal')
elif f >= 25 and f <= 29.9:
    print(f'Seu IMC foi {f:.1f}, Sobrepeso')
elif f >= 30 and f <= 40:
    print(f'Seu IMC foi {f:.1f}, Obesidade')
else:
    print(f'Seu IMC foi {f:.1f}, Obesidade Mórbida')