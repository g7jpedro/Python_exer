from time import sleep
casa = float(input('Digite o valor da Casa: R$ '))
salário = float(input('Digite o valor do seu Salário: R$ '))
anos = float(input('Digite em quantos anos deseja pagar: '))
print('AGUARDE, PROCESSANDO .................')
sleep(5)
n = salário * 30 / 100
x = casa / (anos*12)
if x < n:
    print(f'Olá ! Emprestimo AUTORIZADO ! Você terá que pagar R${x:.2f} todo mês!')
else:
    print(f'Olá! Empréstimo NEGADO, seria necessário R${x:.2f} e você só tem R${salário:.2f}, que ultrapassa 30% do sa : (')