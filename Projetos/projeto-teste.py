# Desenhador de Formas ASCII (altura fixa = 5)

N = 5  # altura fixa (não alterar durante o programa)

while True:
    print("\n--- DESENHADOR DE FORMAS ---")
    print("1 - Escada Direita")
    print("2 - Escada Esquerda")
    print("3 - Pirâmide Centrada")
    print("4 - X (Cruzado)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("A sair... Até logo.")

        break

    elif opcao == "1":
        # Escada Direita
        for i in range(1, N + 1):
            print("*" * i)
        input()

    elif opcao == "2":
        # Escada Esquerda
        for i in range(1, N + 1):
            print(" " * (N - i) + "*" * i)
        input()

    elif opcao == "3":
        # Pirâmide Centrada
        for i in range(1, N + 1):
            print(" " * (N - i) + "*" * (2 * i - 1))
        input()

    elif opcao == "4":
        # X (Cruzado) em área NxN
        for i in range(N):
            linha = ""
            for j in range(N):
                if j == i or j == N - 1 - i:
                    linha += "*"
                else:
                    linha += " "
            print(linha)
        input()

    else:
        print("Opção inválida.")
    input()
