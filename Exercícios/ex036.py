'''

Faça um programa que mostre a tabuada de um número introduzido pelo utilizador.

'''

numero = int(input('Digite um número: '))

for c in range(0, 10):
    print(f'{numero} x {c + 1} = {numero * (c + 1)}')