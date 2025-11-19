'''
Desenvolva um programa que leia 3 valores e mostre o menu:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
O programa deve realizar a operação solicitada em cada caso.
'''

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite mais um valor: '))

while True:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    opcao = int(input('---> '))

    if opcao == 1:
        print(f'{num1} + {num2} + {num3} = {num1 + num2 + num3}')

    elif opcao == 2:
        print(f'{num1} x {num2} x {num3} = {num1 * num2 * num3}')

    elif opcao == 3:
        if num1 > num2 and num1 > num3:
            print(f'{num1} é o maior valor.')
        elif num2 > num1 and num2 > num3:
            print(f'{num2} é o maior valor.')
        elif num3 > num1 and num3 > num2:
            print(f'{num3} é o maior valor.')

    elif opcao == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
        num3 = int(input('Digite mais um valor: '))

    elif opcao == 5:
        print('Bye bye bye')
        break
