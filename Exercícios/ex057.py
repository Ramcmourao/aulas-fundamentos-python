'''
Crie um programa onde o utilizador possa digitar vários
números e guardá-los numa lista. Caso o número inserido
esteja na lista ele não deve ser adicionado.
No final mostre todos os valores por ordem DECRESCENTE.
'''

numeros = []

contador = 0

while contador < 10:
    numero = int(input(f'Digite o {contador + 1}º valor: '))
    if numero not in numeros:
        numeros.append(numero)
        contador += 1
    else:
        print(f'O valor {numero} já se encontra na lista.')

numeros.sort(reverse=True)

for numero in numeros:
    print(f'{numero} -> ', end='')