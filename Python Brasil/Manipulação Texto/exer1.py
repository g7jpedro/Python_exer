
with open('ips.txt', 'w') as objeto:
    cont = objeto.write('Endereços válidos: 200.135.80.9\n192.168.1.1'
                        '\n8.35.67.74\n1.2.3.4')
    cont = objeto.write('\nEndereços inválidos: 257.32.4.5\n85.345.1.2'
                        '\n9.8.234.5\n192.168.0.256')
