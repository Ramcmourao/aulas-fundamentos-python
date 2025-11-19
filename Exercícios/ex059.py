'''
Crie um programa que leia vários números e coloca-os numa lista.
Crie duas listas adicionais que vão conter os números pares e
impares da lista principal. No final mostre todas as listas.
'''

numeros = []

for c in range(0, 10):
    numero = int(input(f'Digite o {c + 1} número: '))
    numeros.append(numero)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(numeros)
print(pares)
print(impares)