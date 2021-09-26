#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.


def área(a, b):
    print('='*55)
    print(f'A largura é {a} e comprimeito é {b}, a área é de {a*b}')


l = float(input('Digite a largura: '))
c = float(input('Digite o comprimeto: '))

área(l, c)