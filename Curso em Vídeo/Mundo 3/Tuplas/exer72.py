#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze',
        'Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    valor = int(input('Digite um número de 0 a 20: '))
    while valor < 0 or valor > 20:
        valor = int(input('\033[1;31mERRO !\033[m Digite um número de 0 a 20: '))
    print(f'Você digitou o valor \033[1;34m{tupla[valor]}\033[m')
    esc = str(input('Quer continuar ? [S/N]: ')).upper()[0]
    while esc not in'SN':
        esc = str(input('\033[0;31mERRO ! Escolha entre [S/N]:\033[m ')).upper()[0]
    if esc == 'N':
        break
print('\033[1;32mFim do programa ...')

