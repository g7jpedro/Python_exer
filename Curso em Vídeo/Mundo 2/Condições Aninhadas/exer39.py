from datetime import date
sexo = int(input('''Qual o seu SEXO ?
[1] - MASCULINO
[2] - FEMININO
Digite de acordo com seu SEXO: '''))
if sexo == 1:
    nasc = int(input('Digite o ano do seu NASCIMENTO:'))
    idade = date.today().year - nasc
    if idade < 18:
        print(f'Você tem {idade} anos, faltam {18 - idade} anos para se ALISTAR.')
    elif idade == 18:
        print(f'Você tem {idade} anos, está na hora de se ALISTAR.')
    elif idade > 18:
        print(f'Você tem {idade} anos, já se passaram {idade - 18} anos do seu ALISTAMENTO.')
else:
    print('Não é preciso se ALISTAR.')