resposta = ''
print('O céu é azul?')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Acertou! Vamos à próxima.')
    elif resposta == 'F':
        print('Erroooooou!')
    else:
        print('Resposta inválida.')

resposta = ''
print('O Palmeiras tem mundial?')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Erroooooou!')
    elif resposta == 'F':
        print('Acertou! Vamos à próxima.')
    else:
        print('Resposta inválida.')

print('O formador é o Ricardo?')
while True:
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Acertou! Fim!')
        break
    elif resposta == 'F':
        print('Erroooooou!')
        break
    else:
        print('Resposta inválida.')