from random import randint
from time import sleep

qtdJogadores = int(input('Digite quandos jogadores vão jogar: '))
jogadores = {}

for c in range(qtdJogadores):
    nome = f'JOGADOR{c+1}' #input(f'Digite o nome do {c+1}º jogador: ')
    jogada = randint(1, 6)
    jogadores[nome] = jogada

    #jogadores[input(f'Digite o nome do {c+1}º jogador: ')] = randint(1,6)

auxiliar = jogadores.copy()
ranking = list()

while auxiliar:
    maior_jogador = ''
    maior_valor = 0

    for jogador, jogada in auxiliar.items():
        if jogada > maior_valor:
            maior_jogador = jogador
            maior_valor = jogada
    ranking.append((maior_jogador, maior_valor))
    del auxiliar[maior_jogador]

for tupla in ranking:
    for elemento in tupla:
        print(f'{elemento}', end=' - ')
    sleep(1)
    print()