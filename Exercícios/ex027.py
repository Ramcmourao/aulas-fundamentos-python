'''

Crie um programa que leia dois números inteiros e compare-os da seguinte forma:

- O primeiro número é maior;
- O segundo número é maior;
- Os números são iguais.

'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num1} é menor que {num2}')
else:
    print(f'{num1} é igual ao {num2}')
