p = int(input('Digite o primeiro valor: '))
s = int(input('Digite o segundo valor: '))
t = int(input('Digite o terceiro valor: '))
maior = p
menor = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')