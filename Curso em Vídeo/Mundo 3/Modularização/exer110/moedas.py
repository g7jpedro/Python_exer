
def aumentar(v, forma=False):
    aumen = v + ((v * 10) / 100)
    if forma == True:
        return moeda(aumen)
    else:
        return aumen


def diminuir(v, forma=False):
    dimin = v - ((v * 13) / 100)
    if forma == True:
        return moeda(dimin)
    else:
        return dimin


def dobro(v, forma=False):
    dob = v * 2
    if forma == True:
        return moeda(dob)
    else:
        return dob


def metade(v, forma=False):
    met = v / 2
    if forma == True:
        return moeda(met)
    else:
        return met


def moeda(v):
    return f'${v:.2f}'


def resumo(v):
    print('='*8,'RESUMO' ,'='*8)
    print(f'Aumentando 10% é = :{aumentar(v, True)}')
    print(f'Diminuindo 13% é = {diminuir(v, True)}')
    print(f'O dobro de {moeda(v)} é = {dobro(v, True)}')
    print(f'A metade de {moeda(v)} é = {metade(v, True)}')

