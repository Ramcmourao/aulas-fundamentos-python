import os

nome_pasta = 'ficheiros'
os.mkdir(nome_pasta)


caminho = 'fans/ficheiros'
os.makedirs(caminho, exist_ok=True)