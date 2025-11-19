'''

Crie um programa que leia um número inteiro introduzido
pelo utilizador e que simule um radar de velocidade.

>80km/h multado
<=80km/h não multado

A multa são 100€ + 7€ por cada km/h acima

'''

print('--- RADAR DE VELOCIDADE ---')

limite = 80
velocidade = int(input('---> '))

multa = 100 + 7 * (velocidade - limite)

if velocidade > limite:
    print('-> MULTADO <-')
    print(f'-- MULTA: {multa:.2f}€ --')
else:
    print('Não multado! Boa Viagem!')