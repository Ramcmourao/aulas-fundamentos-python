print('Trabalho realizado por Leticia, Elionai, Rafael e Roman')

while True:

    print("\n----------------------------------")
    print("--- MENU ---")
    print("[1] Escada à Esquerda")
    print("[2] Escada à Direita")
    print("[3] Árvore de Natal")
    print("[4] Forma de X")
    print("[5] Sair")

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        print("\n--- Escada à Esquerda ---")
        tamanho = 5

        for c in range(1, tamanho + 1):
            print('*' * c)

    elif opcao == 2:
        print("\n--- Escada à Direita ---")
        tamanho = 5
        for c in range(0, tamanho):
            espacos = ' ' * (tamanho -(c + 1))
            asteriscos = '*' * (c + 1)
            print(espacos + asteriscos) # espaços, não identado



    elif opcao == 3:
        print("\n--- Árvore de Natal ---")
        altura = 5
        largura_maxima = altura * 2 - 1

        for c in range(1, altura + 1):
            folhas = '*' * (2 * c - 1)
            print(folhas.center(largura_maxima))

        for _ in range(1):
            print("*".center(largura_maxima))

    elif opcao == 4:
        print("\n--- Forma de X ---")
        tamanho = 5
        for linha in range(tamanho):
            for coluna in range(tamanho):
                if linha == coluna or linha + coluna == tamanho - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()

    elif opcao == 5:
        print("A sair...")
        break
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 5.")








