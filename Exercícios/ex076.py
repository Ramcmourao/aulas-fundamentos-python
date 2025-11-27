'''
Crie um programa que tenha uma função que converta a temperatura de Celsius para Fahrenheit.
'''

def conversor(temp: float):
    fahrenheit = temp * 1.8 + 32

    print(f'{temp:.2f}ºC')
    print(f'{fahrenheit:.2f}ºF')

conversor(-2)