
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):
    dob = n * 2
    return dob


def triplo(n):
    tri = n * 3
    return tri


num = int(input('Digite um valor para fatorial: '))
fat = fatorial(num)
print(fat)
