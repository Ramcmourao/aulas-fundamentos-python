from time import sleep
from random import randint

print(' ~*º~*º [DESENHADOR DE FORMAS] ~*º~*º ')
sleep(0.5)
print(' ~*º~*º UMA PRODUÇÃO DE ~*º~*º')
sleep(0.5)
print(' ~*º~*º FRANCISCA ~*º~*º')
print(' ~*º~*º INÊS ~*º~*º')
print(' ~*º~*º PEDRO ~*º~*º')
sleep(0.5)
opcao = 0

while True:
    c = 0
    print()
    print('[1] Escada à esquerda')
    print('[2] Escada à direita')
    print('[3] Pirâmide')
    print('[4] Cruz')
    print('[5] Sair')
    opcao = int(input('--> '))

    if opcao == 1:
        for c in range(1,6):
            print('*' * c) # print estrelas pelo valor do contador
            sleep(0.3)

    elif opcao == 2:
        n = 5 # altura da meia piramide invertida
        for i in range(1, n+1):
            print(' ' * (n - i) + '*' * i) #multiplica a quantidade de espaços pela altura - 1 e a quantidade de estrelas pelo contador do for
            sleep(0.3)

    elif opcao == 3:
        altura = 5 # altura da piramide
        for c in range(0, altura + 1):
            for blank in range(0, altura - c): # espaços para centrar conforme o numero de estrelas (altura - contador)
                print(' ', end='')
            for estrela in range(1, 2 * c): # estrelas (o dobro do contador)
                print('*', end='')
            sleep(0.3)
            print() # nova linha, print vazio

    elif opcao == 4:
        altura = 5  # limite da altura da figura
        for c in range(altura): # contador altura
            for z in range(altura): # contador largura
                if z == c or z == altura - c - 1: # se altura = largura ou limite da altura - altura - 1 = largura
                    print('*', end='')
                else:
                    print(' ', end='')
            sleep(0.3)
            print() # nova linha, print vazio
            '''
            outra alternativa:
            for c in range(1,6):
                Espaco = ' '*(5-c)
                Estrela = '*'*(c*2-1)
            print(f'{espaco}{estrela}')
            '''
    elif opcao == 5:
        lol = randint(1, 5) #desculpa
        print('A sair.', end='')
        sleep(lol)
        print('.', end='')
        sleep(lol)
        print('.')
        sleep(lol)
        print('Está quase')
        sleep(lol*2)
        print('Obrigado por esperar')
        break

    else: #verificação de input
        print('Opção inválida tente novamente')

