'''

Crie o jogo da adivinha v1.0.
O computador deve “pensar” num número de 0 a 7
e o utilizador deve adivinhar o número escolhido.
O programa deve apresentar se o utilizador venceu ou perdeu.

'''

from time import sleep
from random import randint

aleatorio = randint(0, 7)

print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('-', end=' ')
sleep(0.5)
print('JOGO DA ADIVINHA', end=' ')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('-', end='')
sleep(0.5)
print('-')
sleep(1)

print('Escolhi um número entre 0 e 7.\nÉs capaz de o adivinhar?')
jogada = int(input('---> '))

print('A verificar...')
sleep(1)

if jogada == aleatorio:
    print('VENCEU!!!')
    print(f'Eu pensei em {aleatorio} e tu jogaste {jogada}.')
else:
    print('PERDESTE AHAHAHAHAHAH')
    print(f'Eu pensei em {aleatorio} e tu jogaste {jogada}.')