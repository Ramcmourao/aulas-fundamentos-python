'''
Crie um programa que leia 4 valores e guarde-os num tuple. No final exiba:

Quantas vezes aparece o número 7.
Em que posição foi digitado o número 5.
Quais são os números pares.

O programa deve informar quando não encontrar resposta.
'''
from setuptools.build_meta import prepare_metadata_for_build_wheel

valores = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
    )

qtd_setes = 0
indice_cinco = ''
existe_cinco = False
TAM = len(valores)

for c in range(0, TAM):
    if valores[c] == 7:
        qtd_setes += 1

    if valores[c] == 5:
        if not existe_cinco:
            indice_cinco = c
            existe_cinco = True

if qtd_setes > 0:
    print(f'Foram digitados {qtd_setes} setes.')
else:
    print('Não foram digitados setes.')

if existe_cinco:
    print(f'O cinco foi digitado na {indice_cinco + 1} posição.')
else:
    print('Não foi encontrado nenhum cinco.')