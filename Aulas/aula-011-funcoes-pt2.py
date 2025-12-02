def soma_numeros(lista: list) -> int:
    soma = 0

    for numero in lista:
        soma += numero

    return soma

notas = [20, 20, 20, 20, 20]

media = soma_numeros(notas) / len(notas)

print(media)