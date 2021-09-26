#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para #pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
a = float(input('Digite  altura:'))
l = float(input('Digite a largura:'))
tin = (a*l)/2
print(f'Serão necessários {tin} litros de tinta para pintar.')