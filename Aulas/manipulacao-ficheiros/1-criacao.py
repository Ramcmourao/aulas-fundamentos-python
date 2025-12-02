from pathlib import Path # classe Path que dá métodos/funções típicas de ficheiro

# Informar qual é o caminho do ficheiro
# Criar a variável que representa o caminho do ficheiro
caminho = Path(r'ficheiros\teste.txt')
print('Caminho criado com sucesso.')

# O Python cria o ficheiro se ele não existir
# Podemos abrir o ficheiro em modo:
# Write - 'w' escrever
# Read - 'r' ler
# Append - 'a' acrescentar

with caminho.open('w', encoding='utf-8', errors='ignore') as file:
    print('Ficheiro aberto em modo escrita com sucesso')
    file.write('Olá turma!!!\n')
    file.write('Olá novamente!!!!\n')
    print('Mensagens escritas com sucesso.')