"""
Projeto feito por:
-Julia
-Nadia
-Telmo
"""





while True:
    print("--- Desenhador de Formas ---")
    print("[1] - Escada a esquerda")
    print("[2] - Escada a direita")
    print("[3] - Pirâmide centrada")
    print("[4] - Cruzado")
    print("[5] - Sair")
    opcao=int(input("Escolha uma opção: "))

    if opcao == 1:
        for c in range(0,5):
            print("*" * (c+1))
    elif opcao == 2:
        for c in range(0,5):
            escada= "*" * (c+1)
            print(f"{escada :>10}")
    elif opcao == 3:
        for c in range(0,9):
            if (c+1)  % 2 != 0:
                piramide = ("*" * (c + 1))
                print(f"{piramide :^10}")
    elif opcao == 4:
        tamanho=5
        for linha in range (tamanho):
            for coluna in range(tamanho):
                if linha == coluna or linha + coluna == tamanho-1:
                    print("*",end="")
                else:
                    print(" ", end="")
            print()
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida")













