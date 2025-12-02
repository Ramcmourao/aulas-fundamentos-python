from pathlib import Path

input_data = Path(r'ficheiros/teste.txt')
saida = Path(r'ficheiros/teste_copy.txt')

with input_data.open('r', encoding='utf-8', errors='ignore') as file:
    dados = file.readlines()

with saida.open('w', encoding='utf-8', errors='ignore') as out:
    for linha in dados:
        if 'amor' in linha.lower():
            out.write(linha)
