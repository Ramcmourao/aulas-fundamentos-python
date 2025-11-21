from datetime import datetime
from time import sleep

dados = dict()

print('--- SIMULAÇÃO DE CRÉDITO HABITAÇÃO ---')

dados['Nome'] = input('Digite o seu nome: ')
dados['Ano de nascimento'] = int(input('Digite o seu ano de nascimento: '))
dados['Rendimentos mensais'] = float(input('Digite os rendimentos mensais: '))
dados['Despesas mensais'] = float(input('Digite as despesas mensais: '))
dados['Montante do Crédito'] = float(input('Digite o montante do crédito: '))
dados['Prazo em anos'] = int(input('Digite o prazo em anos: '))

ano_atual = datetime.now().year

dados['Idade'] = ano_atual - dados['Ano de nascimento']
dados['Remanescente'] = dados['Rendimentos mensais'] - dados['Despesas mensais']
dados['Mensalidade'] = dados['Montante do Crédito'] / (dados['Prazo em anos'] * 12)
dados['Situação'] = 'Aprovado' if dados['Remanescente'] > dados['Mensalidade'] else 'Reprovado'

print(f'A analisar a situação do cliente {dados['Nome']}', end='')
for c in range(3):
    print('.', end='')
    sleep(1)
print()

for chave, valor in dados.items():
    if type(valor) == float:
        print(f'{chave} -> {valor:.2f}€')
    else:
        print(f'{chave} -> {valor}')
    sleep(1.5)