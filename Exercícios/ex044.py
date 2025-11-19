'''

Desenvolva um programa que leia um número qualquer e que mostre o seu fatorial.

'''

numero = int(input('Digite um número: '))

if numero == 0 or numero == 1:
    print(f'O fatorial de {numero} é 1.')
else:
    fatorial = 1

    while numero >= 1:
        if numero == 1:
            print(numero, end=' = ')
        else:
            print(numero, end=' x ')
        fatorial *= numero
        numero -= 1

    print(fatorial)