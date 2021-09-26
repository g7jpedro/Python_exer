from datetime import date
nasc = int(input('Digite o ano do seu NASCIMENTO: '))
data = date.today()
id = data.year - nasc
if id <= 9:
    print(f'Você tem {id} anos. Sua categoria é MIRIM !')
elif id > 9 and id <= 14:
    print(f'Você tem {id} anos. Sua categoria é INFANTIL !')
elif id > 14 and id <= 19:
    print(f'Você tem {id} anos. Sua categoria é JUNIOR !')
elif id > 19 and id <= 20:
    print(f'Você tem {id} anos. Sua categoria é SÊNIOR !')
elif id > 20:
    print(f'Você tem {id} anos. Sua categoria é MASTER !')
