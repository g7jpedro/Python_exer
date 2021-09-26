from datetime import date
cont = 0
cont2 =0
for i in range(1, 4):
    nasc = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    idade = date.today().year - nasc
    if idade > 21 or idade == 21:
        cont = cont + 1
    if idade < 21:
        cont2 = cont2 + 1
print(f'{cont} são da maioridade e {cont2} são menores')