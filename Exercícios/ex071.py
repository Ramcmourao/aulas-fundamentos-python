'''
-=-=-=-=-=-=-=-=
   Olá mundo.
-=-=-=-=-=-=-=-=
'''

def cabecalho(txt: str):
    tamanho = len(txt) + 8

    print('-=' * int(tamanho / 2))
    print(f'{txt:^{tamanho}}')
    print('-=' * int(tamanho / 2))


cabecalho(input('Digite uma mensagem: '))