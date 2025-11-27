'''
Crie um programa que tenha uma função que receba vários parâmetros como valores inteiros. O programa deve analisar todos os valores e dizer qual deles é o maior.
'''


def maior(*valor: int):
    maior_valor = max(valor)
    print(f'O maior valor encontrado é {maior_valor}')


maior(1, 2, 3,4 ,5 ,65 ,84,9684, 6, 846874 ,68 ,746 ,74 ,68 ,4)
maior(1, 2, 3, 4)
maior(6, 4, 5, 8)