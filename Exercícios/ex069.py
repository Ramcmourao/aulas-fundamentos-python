import os
from random import randint

nomes = ['Ricardo', 'Luanna', 'Pedro', 'Victor', 'Inês', 'Nádia']

jogadores = list()

for c in range(len(nomes)):
    jogador = dict()

    jogador['Nome'] = nomes[c]
    jogador['Quantidade de Golos'] = randint(1, 20)
    jogador['Quantidade de Jogos'] = randint(1, 10)
    jogador['Média de Golos'] = jogador['Quantidade de Golos'] / jogador['Quantidade de Jogos']

    jogadores.append(jogador.copy())

print(jogadores)

while True:
    print('--- SISTEMA DE CONSULTA DE JOGADORES ---')
    print('[ 1 ] - Lista de jogadores')
    print('[ 2 ] - Melhor marcador')
    print('[ 3 ] - Pesquisar pelo nome')
    print('[ 4 ] - Ranking')
    print('[ 5 ] - Registar novo jogador')
    print('[ 6 ] - Sair')
    opcao = int(input('---> '))

    if opcao == 1:
        print('--- LISTA DE JOGADORES ---')
        contador = 1
        for jogador in jogadores:
            print(f'{contador} - {jogador['Nome']}')
            contador += 1
        os.system('Pause')

    elif opcao == 2:
        print('--- MELHOR MARCADOR ---')
        nome = ''
        golos = 0

        for jogador in jogadores:
            if jogador['Quantidade de Golos'] > golos:
                golos = jogador['Quantidade de Golos']
                nome = jogador['Nome']

        print(f'{nome} - {golos} golos marcados')
        os.system('Pause')



