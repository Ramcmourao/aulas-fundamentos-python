# range(inicio, fim, passo)
from time import sleep

numero = 7

for c in range(0, 10):
    print(f'{numero} x {c + 1} = {numero * (c + 1)}')
    input()