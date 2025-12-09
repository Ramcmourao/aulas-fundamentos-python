from pathlib import Path
from src.utils import cabecalho

FICHEIRO = Path(r'bloco-notas/notas.txt')

def adicionar_notas():
    cabecalho('ADICIONAR NOTA')
    with FICHEIRO.open('a', encoding='utf-8', errors='ignore') as file:
        nota = input('--> ')
        file.write(f'{nota}\n')

    print('Nota guardada com sucesso.')


def mostrar_notas():
    cabecalho('MOSTRAR NOTAS')
    with FICHEIRO.open('r', encoding='utf-8', errors='ignore') as file:
        contador = 1
        for linha in file:
            print(f'{contador} - {linha}', end='')
            contador += 1

    print('--- FIM NOTAS ---')


def apagar_notas():
    cabecalho('APAGAR NOTAS')
    confirmacao = int(input('Confirma que quer apagar TODAS as notas?\n[ 1 ] Sim\n[ 2 ] Não\n-->'))
    if confirmacao == 1:
        with FICHEIRO.open('w', encoding='utf-8', errors='ignore') as file:
            file.write('')

            print('Notas apagadas com sucesso.')


def pesquisar_notas():
    cabecalho('PESQUISAR NOTAS')
    termo = input('Digite o termo a pesquisar: ').strip()
    encontrados = 0
    with FICHEIRO.open('r', encoding='utf-8', errors='ignore') as file:
        for linha in file:
            if termo.lower() in linha.lower():
                print(f'{encontrados + 1} - {linha}', end='')
                encontrados += 1

    if encontrados == 0:
        print(f'Não há notas com o termo \"{termo}\"')