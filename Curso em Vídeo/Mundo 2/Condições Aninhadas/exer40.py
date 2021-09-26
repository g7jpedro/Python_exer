n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Você foi REPROVADO ! Seria necessário sua média der mais do que 5, e sua nota foi {media}')
elif media >= 5 and media < 6.9:
    print(f'Você está de RECUPERAÇÃO ! sua média foi {media:.1f}')
else:
    print(f'Parabéns, você foi APROVADO! Sua média foi {media:.1f}')