
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


