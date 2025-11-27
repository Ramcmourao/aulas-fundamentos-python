'''
Crie um programa que tenha uma função que receba 3 parâmetros: inicio, fim e passo. O programa deve realizar 3 contagens através da função.

De 1 até 20, de 2 em 2
De 10 até 0, de 1 em 1
Contagem personalizada
'''

def contagem(i: int, f: int, p: int):

    if p < 1:
        p = 1
        print('Passo vai iniciar com o valor padrão')

    if i > f:
        p = -p
        f = f - 1

    for c in range(i, f, p):
        print(c)


contagem(1, 20, 2)
contagem(10, 0, 1)

print('Contagem personalizada')
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

contagem(inicio, fim, passo)