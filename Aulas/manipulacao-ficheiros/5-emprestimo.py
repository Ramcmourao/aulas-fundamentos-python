from pathlib import Path
from datetime import datetime

def cabecalho(txt: str) -> None:
    print(f'--- {txt.upper()} ---')


def busca_informacao() -> dict:
    dados = dict()
    caminho = Path(r'ficheiros/dados.txt')
    with caminho.open('r', encoding='utf-8', errors='ignore') as file:
        for linha in file:
            linha_dividida = linha.split(': ')
            dados[linha_dividida[0]] = linha_dividida[1].replace('\n', '')

    return dados


def calcula_informacao(dados: dict) -> dict:
    dados['Montante do Crédito'] = float(input('Digite o montante do crédito: '))
    dados['Prazo em anos'] = int(input('Digite o prazo em anos: '))

    ano_atual = datetime.now().year

    dados['Idade'] = ano_atual - int(dados['Ano de Nascimento'])
    dados['Remanescente'] = float(dados['Rendimentos Mensais']) - float(dados['Despesas Mensais'])
    dados['Mensalidade'] = dados['Montante do Crédito'] / (dados['Prazo em anos'] * 12)
    dados['Situação'] = 'Aprovado' if dados['Remanescente'] > dados['Mensalidade'] else 'Reprovado'

    return dados


def guarda(dados: dict) -> str:
    caminho = Path(rf'ficheiros/{dados["Nome"]}_resultado.txt')
    with caminho.open('w', encoding='utf-8', errors='ignore') as file:
        for key, value in dados.items():
            file.write(f'{key}: {value}\n')

    return f'Resultado de {dados["Nome"]} guardado com sucesso.'

###############################################################################

pessoa = calcula_informacao(busca_informacao())

print(guarda(pessoa))