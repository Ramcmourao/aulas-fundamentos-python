'''
Crie um código em Python que teste se o site do IEFP está acessível a partir do seu computador.
'''

from urllib import request

site = 'https://iefp.pt/'
try:
    codigo = request.urlopen(site).getcode()
except:
    print('Erro ao abrir o site')

else:
    print(f'Consegui aceder ao site com o código: {codigo}')