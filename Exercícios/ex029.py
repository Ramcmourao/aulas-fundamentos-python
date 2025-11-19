print('--- Calculadora ---')                     # Escreve o título do programa no ecrã
print('[ 1 ] – Tabuada')                        # Opção 1: mostrar a tabuada de um número
print('[ 2 ] – Calculadora')                    # Opção 2: mini-calculadora de duas parcelas (ex: 12+5, 7x3, 10/2)
print('[ 3 ] – Números Pares')                  # Opção 3: verificar se um número é par ou ímpar
print('[ 4 ] – Sair')                           # Opção 4: terminar o programa
opcao = int(input('---> '))                     # Lê a opção escolhida pelo utilizador e converte para inteiro

if opcao == 1:                                  # Se a opção for 1, entra no modo "Tabuada"
    print('--- Tabuada ---')
    numero = int(input('Digite um número: '))   # Pede um número inteiro para calcular a tabuada

    # Imprime a tabuada do 1 ao 10 usando f-strings
    print(f'{numero} x 1 = {numero * 1}')
    print(f'{numero} x 2 = {numero * 2}')
    print(f'{numero} x 3 = {numero * 3}')
    print(f'{numero} x 4 = {numero * 4}')
    print(f'{numero} x 5 = {numero * 5}')
    print(f'{numero} x 6 = {numero * 6}')
    print(f'{numero} x 7 = {numero * 7}')
    print(f'{numero} x 8 = {numero * 8}')
    print(f'{numero} x 9 = {numero * 9}')
    print(f'{numero} x 10 = {numero * 10}')

elif opcao == 2:                                # Se a opção for 2, entra no modo "Calculadora"
    print('--- Calculadora ---')

    calculo = input('Digite o cálculo: ')       # Lê uma expressão simples (ex.: "12 + 5", "7x3", "10/2")
    calculo = calculo.strip().replace(' ', '')  # Remove espaços para simplificar o parsing (ex.: "12+5")

    if '+' in calculo:                          # Se houver um '+' na expressão, trata como soma
        pos = calculo.find('+')                 # Índice (posição) do sinal '+'
        num1 = int(calculo[:pos])               # Parte à esquerda do '+', convertida para inteiro
        num2 = int(calculo[pos+1:])             # Parte à direita do '+', convertida para inteiro
        print(f'{num1} + {num2} = {num1 + num2}')  # Mostra o resultado da soma

    elif '-' in calculo:                        # Se houver um '-' na expressão, trata como subtração
        pos = calculo.find('-')                 # Índice do '-'
        num1 = int(calculo[:pos])               # Parte à esquerda do '-'
        num2 = int(calculo[pos + 1:])           # Parte à direita do '-'
        print(f'{num1} - {num2} = {num1 - num2}')  # Mostra o resultado da subtração

    elif '*' in calculo or 'x' in calculo:      # Se houver '*' ou 'x', trata como multiplicação (ambos aceites)
        if 'x' in calculo:
            pos = calculo.find('x')             # Índice do 'x' quando o utilizador escreve "3x4"
        else:
            pos = calculo.find('*')             # Índice do '*' quando o utilizador escreve "3*4"

        num1 = int(calculo[:pos])               # Parte à esquerda do operador de multiplicação
        num2 = int(calculo[pos + 1:])           # Parte à direita do operador de multiplicação
        print(f'{num1} x {num2} = {num1 * num2}')  # Mostra o resultado da multiplicação (usa 'x' na apresentação)

    elif '/' in calculo:                        # Se houver '/', trata como divisão
        pos = calculo.find('/')                 # Índice do '/'
        num1 = int(calculo[:pos])               # Parte à esquerda do '/'
        num2 = int(calculo[pos + 1:])           # Parte à direita do '/'
        if num2 == 0:                           # Verifica divisão por zero (não permitido)
            print('Não é possível dividir por ZERO')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')  # Mostra o resultado da divisão (float)

elif opcao == 3:                                # Se a opção for 3, verifica paridade de um número
    print('--- Números pares--- ')
    numero = int(input('Digite um número: '))   # Lê um número inteiro

    if numero % 2 == 0:                         # Usa o operador módulo (%) para testar o resto da divisão por 2
        print(f'{numero} é PAR')                # Se resto for 0, é par
    else:
        print(f'{numero} é IMPAR')              # Caso contrário, é ímpar

elif opcao == 4:                                # Se a opção for 4, finaliza
    print('A sair...')
else:                                           # Qualquer outro valor é inválido
    print('Opção inválida...')
