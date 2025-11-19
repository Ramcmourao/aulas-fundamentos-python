'''
Tabuada V2.0 – Faça um programa que mostre a tabuada de vários
números inseridos pelo utilizador. O programa deverá ser
interrompido quando o número inserido for negativo ou 0.
'''

print('--- TABUADA 2.0 ---')

while True:

    numero = int(input('Digite um número: '))

    if numero <= 0:
        break

    for c in range(0, 10):
        print(f'{numero} x {c + 1} = {numero * (c + 1)}')