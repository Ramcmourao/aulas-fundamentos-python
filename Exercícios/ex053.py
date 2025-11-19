'''
Crie um programa que gere 5 números aleatórios dentro de um tuple.
Depois mostra a listagem de números gerados, o menor e o maior.
'''

from random import randint

minha_tuple = (randint(0, 20),
               randint(0, 20),
               randint(0, 20),
               randint(0, 20),
               randint(0, 20))

print('Números gerados:')
menor = maior = 0

for numero in minha_tuple:
    print(f'\t{numero}', end='')

    if numero == minha_tuple[0]:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero
print()
print(f'O maior valor encontrado é {maior}')
print(f'O menor valor encontrado é {menor}')
