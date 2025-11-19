'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa registada o programa deverá perguntar se o
utilizador quer continuar ou não. No final mostre:

Quantas pessoas têm mais de 25 anos.
Quantos homens com menos 17 anos foram registados.
Quantas mulheres foram registadas.
Quantos menores de idade foram registados.
'''

pessoas_mais25 = 0
homens_menos17 = 0
mulheres = 0
menores = 0

resposta = ''
while resposta != 'nao':
    idade = int(input('Digite a idade: '))
    if idade < 0:
        print('Por favor insira uma idade válida...')
        continue

    while True:
        sexo = input('Digite o sexo [M/F]: ').strip().lower()
        if sexo != 'm' and sexo != 'f':
            print('Por favor digite F ou M...')
        else:
            break

    if idade > 25:
        pessoas_mais25 += 1

    if sexo == 'm' and idade < 17:
        homens_menos17 += 1

    if sexo == 'f':
        mulheres += 1

    if idade < 18:
        menores += 1

    resposta = input('Deseja continuar? [ SIM / NÃO ]: ').strip().lower()

    if 'ã' in resposta:
        resposta = resposta.replace('ã', 'a')

print(f'{pessoas_mais25} pessoas com menos de 25 anos registadas.')
print(f'{homens_menos17} homens com menos de 17 anos registados.')
print(f'{mulheres} mulheres registadas.')
print(f'{menores} menores registados.')