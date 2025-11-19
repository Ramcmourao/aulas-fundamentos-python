'''
Crie um programa que leia um número de 0 a 20
introduzido pelo utilizador. Depois deverá
mostrar por extenso o número introduzido.
'''

numeros = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
    'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Catorze', 'Quinze', 'Dezasseis', 'Dezassete', 'Dezoito',
    'Dezanove', 'Vinte'
)

numero = int(input('Digite um número entre 0 - 20: '))

print(numeros[numero])