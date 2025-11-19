'''
Desenvolva o jogo par ou ímpar.
O jogo só será interrompido quando
o jogador perder e deverá exibir o
total de vitórias consecutivas.
'''
import random

vitorias = 0

print('--- PAR OU ÍMPAR ---')

while True:
    jogada = int(input('Digite um valor entre 0 e 5: '))
    if jogada > 5 or jogada < 0:
        print('Por favor escolha um valor entre 0 e 5')
        continue

    while True:
        jogada_pi = input('[ PAR OU ÍMPAR ]: ').strip().lower()
        if jogada_pi == 'par' or jogada_pi == 'impar':
            break
        else:
            print('Por favor, digite [ PAR OU ÍMPAR ]...')

    CPU = random.randint(0, 5)

    res = CPU + jogada

    if res % 2 == 0 and jogada_pi == 'par':
        print(f'Jogador: {jogada} e PAR')
        print(f'CPU: {CPU}')
        print(f'{jogada} + {CPU} = {res}')
        print('JOGADOR GANHA')

        vitorias += 1

    elif res % 2 != 0 and jogada_pi == 'impar':
        print(f'Jogador: {jogada} e ÍMPAR')
        print(f'CPU: {CPU}')
        print(f'{jogada} + {CPU} = {res}')
        print('JOGADOR GANHA')

        vitorias += 1

    else:
        print(f'Jogador: {jogada} e {jogada_pi.upper()}')
        print(f'CPU: {CPU}')
        print(f'{jogada} + {CPU} = {res}')
        print('JOGADOR PERDE')
        break

print(f'\nVITÓRIAS CONSECUTIVAS: {vitorias}')