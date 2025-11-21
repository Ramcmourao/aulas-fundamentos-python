jogador = dict()

jogador['Nome'] = input('Digite o nome do Jogador: ')
jogador['Quantidade de jogos'] = int(input('Digite quantos jogos jogou: '))
jogador['Quantidade de golos'] = int(input('Digite quantos golos marcou: '))
jogador['Média de golos'] = jogador['Quantidade de golos'] / jogador['Quantidade de jogos']

for chave, valor in jogador.items():
    print(f'{chave} -> {valor}')