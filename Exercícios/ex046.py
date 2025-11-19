'''

Crie um programa que leia vários números inteiros
e que termine apenas quando o utilizador digitar a
opção para parar. No final mostre quantos números
o utilizador inseriu e qual a soma entre eles.

'''

soma = 0
contador = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break

    soma += numero
    contador += 1

print(f'A soma entre os valores digitados é: {soma}.')
print(f'Digitou {contador} números.')