'''

Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “A”;
Em que posição aparece a primeira vez;
Em que posição aparece a última vez.

'''

frase = 'A minha prima falou com o António'

qtd_a = frase.count('A')
print(f'O A aparece {qtd_a} vezes.')

p_posicao = frase.find('A')
print(f'Aparece pela primeira vez na posição {p_posicao + 1}.')

u_posicao = frase.rfind('A')
print(f'Aparece pela última vez na posição {u_posicao + 1}.')