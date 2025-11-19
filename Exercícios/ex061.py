'''
Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz com a formatação adequada.
'''
from random import randint

numeros = list()

for linha in range(0, 3):
    temp = list()
    for coluna in range(0, 3):
        num = randint(0, 9)
        temp.append(num)

    numeros.append(temp[:])

for lista in numeros:
    for valor in lista:
        print(valor, end=' ')
    print()

