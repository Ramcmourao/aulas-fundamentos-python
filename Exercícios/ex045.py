'''
Escreva um programa que leia um número N inteiro qualquer
e mostre os N primeiros elementos de uma sequência de Fibonacci.
'''

from time import sleep

# 0 1 1 2 3 5 8 13 21

antecessor = 0 # atribuo o primeiro valor da sequencia
atual = 1 # atribuo o segundo valor da sequencia
sequencia = int(input('Digite um valor: ')) # peço ao utilizador quantos valores quer ver sa sequencia

if sequencia < 1: # se a sequencia a ser mostrada é inferior a 1, ele não mostra e diz invalido.
    print('Inválido.')
elif sequencia == 1: # se a sequencia for 1, ele mostra o primeiro valor da sequencia de fibo
    print(antecessor)
elif sequencia == 2: # se a sequencia for 2, ele mostra os 2 primeiros valores da sequencia de fibo
    print(f'{antecessor} -> {atual}')
else:
    print(f'{antecessor} -> {atual}', end=' ')
    sequencia = sequencia - 2 # libertamos 2 valores da sequencia porque na linha anterior 2 já foram exibidos

    while sequencia >= 1: # enquanto a sequencia for superior ou igual a 1, ele repete o abaixo
        sucessor = antecessor + atual # calcula o valor seguinte aos dois primeiros
        print(f'-> {sucessor}', end=' ') # mostra esse valor calculado
        antecessor = atual # transfere os valores
        atual = sucessor # transfere os valores
        sleep(0.5)
        sequencia -= 1 # retira 1 à sequencia pois foi exibido mais um valor