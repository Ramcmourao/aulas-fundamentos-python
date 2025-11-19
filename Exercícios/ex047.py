'''

Crie um programa que leia várias notas introduzidas pelo utilizador.
No final mostre quantas notas o utilizador inseriu, qual a média entre
elas e qual a maior e a menor nota.

'''

contagem = soma = maior = menor = 0

while True:
    nota = float(input(f'Digite a {contagem + 1}ª nota [0 para parar]: '))

    if nota == 0:
        break

    if contagem == 0:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    contagem += 1
    soma += nota

media = soma / contagem

print(f'Inseriu {contagem} notas.')
print(f'Média: {media:.2f} valores')
print(f'A maior nota inserida é: {maior}')
print(f'A menor nota inserida é: {menor}')