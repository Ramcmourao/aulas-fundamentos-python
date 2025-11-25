"""Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando cada dado num dicionário e todos os dicionários numa lista. No final mostre:

Quantas pessoas foram registadas;
Qual a média de idades do grupo;
Quantas mulheres foram registadas;
Quantos homens com idade acima da média foram registados.
"""
from fpdf.php import print_r

pessoas = []
dados = dict()
qtd_pessoas = 0
soma_idades = 0
qtd_mulheres = 0


while True:
    dados['nome'] = input('Digite um nome:').strip()
    while True:
        dados['sexo'] = input('Digite o sexo [m/f]:').strip().lower()
        if dados['sexo'] != 'm' and dados['sexo'] != 'f':
            print('Por favor introduza um sexo válido.')
        else:
            break

    if dados['sexo'] == 'f':
        qtd_mulheres += 1

    dados['idade'] = int(input('Digite a idade:'))
    soma_idades += dados['idade']

    pessoas.append(dados.copy())
    qtd_pessoas += 1

    dados.clear()

    opcao = input('--- digite sim para terminar ---').strip().lower()
    if opcao == 'sim':
        break

media_idades = round(soma_idades / qtd_pessoas, 2)
qtd_homens_acima_media = 0

for pessoa in pessoas:
    if pessoa['sexo'] == 'm':
        if pessoa['idade'] > media_idades:
            qtd_homens_acima_media += 1

print('##################################')
print('Informações:')
print(f'-- Foram registadas {qtd_pessoas} pessoas.')
print(f'-- A média de idade é {media_idades} anos.')
print(f'-- Foram registadas {qtd_mulheres} mulheres.')
print(f'-- Foram registados {qtd_homens_acima_media} homens com idade acima da média.')