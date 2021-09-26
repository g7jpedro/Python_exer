# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(id):
    idade = 2021 -id
    if idade < 16:
        return f'Com {idade}. NEGADO !'
    elif idade >= 16 and idade <= 60:
        return f'Com {idade}. OBRIGATÓRIO !'
    else:
        return f'Com {idade}. OPCIONAL !'


ano_nascimento = voto(int(input('Digite o seu ano de NAscimento: ')))
print(ano_nascimento)