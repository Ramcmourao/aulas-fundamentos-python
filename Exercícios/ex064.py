aluno = {'Nome': input('Digite o seu nome: '),
         'Média': float(input('Digite a sua média: '))
         }

if aluno['Média'] >= 9.5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

# aluno['Situação'] = 'Aprovado' if if aluno['Média'] >= 9.5 else 'Reprovado'

for chave, valor in aluno.items():
    print(f'{chave} -> {valor}')
