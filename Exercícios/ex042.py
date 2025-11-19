'''
Crie o jogo da adivinha v2.0. O computador deve “pensar”
num número de 0 a 10 e o utilizador deve adivinhar o número
escolhido. Só que agora o jogador vai tentar adivinhar até
acertar. No final mostre quantas tentativas foram necessárias.
'''
# Computador pensar num numero de 0 a 10
from random import randint
from time import sleep

CPU = randint(0, 10)
tentativas = 0

jogada = ''

print('--- JOGO DA ADIVINHA V. 2.0 ---')
sleep(1)
print('Pensei num número entre 0 e 10')
sleep(1)
print('--> Achas que consegues acertar??????\n')
sleep(1)

while jogada != CPU:
    tentativas += 1
    jogada = int(input('---> '))
    if jogada > CPU:
        print('Mais abaixo...')
    elif jogada < CPU:
        print('Mais acima...')

print(f'Acertas-te! Eu pensei no {CPU}.')
print(f'Total de tentativas: {tentativas}.')