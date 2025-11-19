'''

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

'''

numero = int(input('Digite um número: '))

contador = 0

for c in range(0, numero):
    if numero % (c+1) == 0:
        contador = contador + 1


if contador == 2:
    print(f'O número {numero} É PRIMO.')
else:
    print(f'O número {numero} NÃO É PRIMO.')