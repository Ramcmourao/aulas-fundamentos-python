'''

Faça um programa que leia 10 números e conte quantos deles são pares.

'''

qtd_pares = 0

for c in range(0, 10):
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        qtd_pares += 1
        #qtd_pares = qtd_pares + 1

print(qtd_pares)