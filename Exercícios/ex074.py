'''
Crie um programa que tenha uma função que receba o nome de um aluno e uma lista das suas notas. Ele deve calcular a média do aluno e mostrar no ecrã o nome do aluno, a sua média e se ele ficou aprovado ou não.
'''
from statistics import mean

def analisa_notas(nome: str, notas: list):
    media = mean(notas)
    situacao = 'Aprovado' if media >= 9.5 else 'Reprovado'

    print(f'Nome: {nome}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')


name = 'Elionai'
lst_notas = [9, 9, 9, 9, 9, 9]

analisa_notas(name, lst_notas)

