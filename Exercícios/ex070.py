'''
Crie um programa que tenha uma função chamada area() que receba as dimensões de um terreno e mostre a área do terreno.
'''

# parametro: typo de dado
def area(l: float, c:float):
    area_calculada = l * c
    print(f'Área do terreno: {area_calculada:.2f}m²')

#################################################################

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area(largura, comprimento)