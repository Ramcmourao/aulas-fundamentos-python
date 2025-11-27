'''
Crie um programa que tenha uma função que receba um número inteiro e mostre a tabuada desse número.
'''

def tabuada(num: int):
    for c in range(1, 11):
        print(f'{num} x {c} = {c * num}')


tabuada(7)