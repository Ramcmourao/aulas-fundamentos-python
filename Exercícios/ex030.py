from random import randint

print('--- Pedra, Papel, Tesoura ---')

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogador = int(input('---> '))
cpu = randint(1, 3)

if jogador == 1:
    if cpu == 1:
        print('Empate')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')
    elif cpu == 2:
        print('CPU ganha')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')
    elif cpu == 3:
        print('Jogador ganha')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')

elif jogador == 2:
    if cpu == 1:
        print('Jogador ganha')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')
    elif cpu == 2:
        print('Empate')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')
    elif cpu == 3:
        print('CPU ganha')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')

elif jogador == 3:
    if cpu == 1:
        print('CPU ganha')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')
    elif cpu == 2:
        print('Jogador ganha')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')
    elif cpu == 3:
        print('Empate')
        print(f'CPU: {cpu}')
        print(f'Jogador: {jogador}')

else:
    print('Jogada invalida.')
