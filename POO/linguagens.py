
from collections import OrderedDict

linguagens_favoritas = OrderedDict()

linguagens_favoritas['João'] = 'Pyhton'
linguagens_favoritas['Maria'] = 'C'
linguagens_favoritas['Pedro'] = 'Ruby'
linguagens_favoritas['Lari'] = 'Python'

for k, v in linguagens_favoritas.items():
    print(f'Linguagem favortia de {k} = {v}')