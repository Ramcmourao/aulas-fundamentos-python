'''
Crie um programa que tenha uma função que receba um número inteiro e mostre a tabuada desse número.
'''
import random
def tabuada(num: int):
    """
    -> Apresenta a tabuada de um valor.
    :param num: o valor sobre o qual será apresentada a tabuada
    :return: sem retorno
    Desenvolvido por: Ricardo Mourão
    """
    for c in range(1, 11):
        print(f'{num} x {c} = {c * num}')


help(random)