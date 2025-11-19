from random import randint

print('--- Pedra, Papel, Tesoura ---')

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogador = int(input('---> '))
cpu = randint(1, 3)

calculo = jogador - cpu

if jogador == cpu:
    print('Empate')
    print(f'CPU: {cpu}')
    print(f'Jogador: {jogador}')
elif calculo == -1 or calculo == 2:
    print('CPU ganha')
    print(f'CPU: {cpu}')
    print(f'Jogador: {jogador}')
elif calculo == 1 or calculo == -2:
    print('Jogador ganha')
    print(f'CPU: {cpu}')
    print(f'Jogador: {jogador}')
else:
    print('Jogada inválida')
