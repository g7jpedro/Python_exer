soma = c = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'A soma dos {c} números que você digitou foi = {soma}')