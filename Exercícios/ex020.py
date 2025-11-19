'''

Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas as letras minúsculas;
Quantidade de letras sem espaços;
Quantas letras tem o primeiro nome.

'''

nome = input('Digite o seu nome: ').strip()

print(nome.upper()) # nome com todas as letras maiúsculas
print(nome.lower()) # O nome com todas as letras minúsculas;
qtd_espacos = nome.count(' ') # conta quantos espaços existe
print(len(nome) - qtd_espacos) # mostra qtd caracteres - qtd espaços
print(len(nome.replace(' ', ''))) # mostra qtd caracteres sem espaços

pEspaco = nome.find(' ') # encontro o indice do primeiro espaço
print(nome[:pEspaco]) # imprimo a string do inicio até ao indice do primeiro espaço