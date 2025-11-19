from time import sleep

print('--- REGISTO DE UTILIZADOR ---')

nome = input('Nome: ').strip().lower()
sleep(1)
print(f'Olá {nome.title()}, o seu registo está completo.')

sleep(0.5)
print('A gerar o seu email...')
sleep(1)

p_nome = nome[0] # recebe a primeira letra inserida na string
indice_espaco = nome.find(' ') + 1 # procura o índice do espaço e adiciona 1
u_nome = nome[indice_espaco:] # devole a string do indice do espaço +1 até ao final

email = f'{p_nome}.{u_nome}@empresa.pt'
print(f'O seu email é {email}')

# [R][i][c][a][r][d][o][ ][M][o][u ][r ][ã ][o ]
# [0][1][2][3][4][5][6][7][8][9][10][11][12][13]