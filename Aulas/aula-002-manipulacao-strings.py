from queue import PriorityQueue

string = 'Python é Poderoso'

# Fatiamento de String / String Slicer
print(string[7]) # é
print(string[-1]) # último caracter
print(string[:6]) # Python
print(string[9:]) # Poderoso
print((string[::3])) # do inicio ao fim de 2 em 2
print(string[::-1]) # mostra a string ao contrário

# Análise de String / String Analisys
print(len(string)) # tamanho da String
print(string.count('o')) # quantas vezes aparece o 'o'
print('Python' in string) # Devolve true ou false
print(string.find('é')) # devolve a posição do solicitado
print(string.find('Olé')) # não encontra e devolve -1
print(string.startswith('Python')) # devolve true ou false
print(string.endswith('Fraquinho'))

# Transformação de String / String Transfiguration
string = input('Digite uma frase:')
print(len(string))
print(len(string.strip()))
print(len(string.rstrip()))
print(string.lower())
print(string.upper())
print(len(string.replace(' ', '')))