# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n = float(input('Digite quantos reais você tem R$:'))
dólar = n*0.23
iene = n*25.42
euro = n*0.21
venez = n*16785.48
print(f'O valor em dólar é = {dólar:.2f} R$')
print(f'O valor em Iene é = {iene:.2f} R$')
print(f'O valor em Euro é = {euro:.2f} R$')
print(f'O valor em Petro é = {venez:.2f} R$')