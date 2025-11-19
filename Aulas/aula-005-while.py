'''# Contador que vai de 1 até 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Contador que vai de 10 até 0
contador = 10
while contador >= 0:
    print(contador)
    contador -= 1

# Criar um programa que some todos os números digitados pelo utilizador.
# Quantos? Não sei. Só sei que se o utilizador digirar 0, é para parar.
soma = 0
numero = ''
while numero != 0:
    numero = int(input('Digite um número: '))
    soma += numero
print(soma)

# Eu quero criar um programa que peça o género de uma pessoa
# Apenas aceita como resposta "M" ou "F"
# Se o utilizador digitar outra resposta ele vai ter de pedir novamente
genero = ' '
while genero != 'M' and genero != 'F':
    genero = input('Digite o seu género: ').strip().upper()

'''

'''# Quero criar um menu onde o utilizador pode escolher 3 opções
# Escrever "olá", "tudo bem?", sair do programa.
opcao = ''
while opcao != 3:
    print('--- MENU --- ')
    print('[ 1 ] - Olá')
    print('[ 2 ] - Tudo bem?')
    print('[ 3 ] - Sair')
    opcao = int(input('---> '))

    if opcao == 1:
        print('Olá')
    elif opcao == 2:
        print('Tudo bem?')
    elif opcao == 3:
        print('A sair...')
    else:
        print('Opção inválida')'''

'''while True:
    print('--- MENU --- ')
    print('[ 1 ] - Olá')
    print('[ 2 ] - Tudo bem?')
    print('[ 3 ] - Sair')
    opcao = int(input('---> '))

    if opcao == 1:
        print('Olá')
    elif opcao == 2:
        print('Tudo bem?')
    elif opcao == 3:
        print('A sair...')
        break
    else:
        print('Opção inválida')'''

# contagem de 0 até 1000
contador = 0
print(contador)
while True:
    contador += 1
    print(contador)

    if contador == 1000:
        break
