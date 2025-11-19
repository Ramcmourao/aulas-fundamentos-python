'''
Crie um programa que tenha um tuple com nomes
de jogos e os seus respetivos preços em sequência.

No final, mostre uma listagem de preços
organizados como tabela.
'''

jogos = (
'Assassins Creed: Shadows - Standard Edition PS5', '69.99 €',
'Metal Gear Solid Delta Snake Eater - Day One Edition PS5', '69.99 €',
'Elden Ring: Nightreign - Standard Edition PS5', '35.99 €',
'Digimon Story: Time Stranger PS5', '64.99 €',
'Final Fantasy Tactics: The Ivalice Chronicles PS5', '54.99 €',
'Five Nights at Freddys: Help Wanted 2 PS5', '29.99 €',
'Dragon Ball Xenoverse 2 PS5', '19.99 €',
'Dragon Ball: Sparking! Zero PS5 - Oferta DLC', '59.99 €'
)

print(f'{"LISTA DE JOGOS FANS FANS":-^70}')
print('_' * 70)
print(f'  {"JOGO": <62} PREÇO')
print('-' * 70)

for c in range(0, len(jogos)):
    if c % 2 == 0:
        print(f'{jogos[c]:.<62}', end='')
    else:
        print(f' {jogos[c]}')

print('-' * 70)
