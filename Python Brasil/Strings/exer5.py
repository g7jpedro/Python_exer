"""
 Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
"""

nome = str(input('Digite seu nome: '))

for i in range(len(nome)+1, 0, -1):
    print(f'{nome[:i:]}')