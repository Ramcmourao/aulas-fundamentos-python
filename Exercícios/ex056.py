'''
Crie um programa que leia 5 números e guarde-os numa lista.
No final mostre o maior e o menor valor e a respetiva posição na lista.
'''

numeros = []

for c in range(0, 5):
    numero = int(input(f'Digite o {c + 1}º valor: '))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

pos_maior = numeros.index(maior)
pos_menor = numeros.index(menor)

print(f'O maior valor encontrado foi o {maior} na posição {pos_maior + 1}.')
print(f'O menor valor encontrado foi o {menor} na posição {pos_menor + 1}.')