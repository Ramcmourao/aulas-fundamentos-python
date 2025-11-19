# estante = input('Digite uma consola: '), input('Digite outra consola')

nomes = ('Nádia', 'Julia', 'Alexandra', 'Telmo',
         'Victor', 'Rafael', 'Daniel', 'Leticia',
         'Roman', 'Pedro', 'Francisca', 'Inês', 32, True, 3.14)

for c in range(0, len(nomes)):
    print(f'{c} -> {nomes[c]}')

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes):
    print(f'No índice {indice} o valor é {nome}')

print(type(nomes))