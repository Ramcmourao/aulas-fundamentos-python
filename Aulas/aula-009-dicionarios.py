turma = []
qtd_alunos = 5
aluno = dict() # ou {}

for c in range(qtd_alunos):
    aluno['Nome'] = input(f'Digite o nome do {c+1}º aluno: ')
    aluno['Média'] = float(input(f'Digite a média do {aluno["Nome"]}: '))

    # Situação com OPERADOR TERNÁRIO
    aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 9.5 else 'Reprovado'

    # Situação com IF normal
    '''if aluno['Média'] > 9.5:
        aluno['Situação'] = 'Aprovado'
    else:
        aluno['Situação'] = 'Reprovado' '''

    turma.append(aluno.copy())

print(turma)
