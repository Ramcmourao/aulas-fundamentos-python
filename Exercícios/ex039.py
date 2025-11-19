from datetime import datetime

qtd_maiores = 0
qtd_menores = 0

ano_atual = datetime.now().year

for c in range(0, 7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))

    idade = ano_atual - ano_nascimento

    if idade >= 18:
        qtd_maiores += 1
    else:
        qtd_menores += 1

print(f'Há {qtd_maiores} pessoas maior de idade.')
print(f'Há {qtd_menores} pessoas menor de idade.')
