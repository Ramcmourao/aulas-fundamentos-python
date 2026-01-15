import utils.cabecalhos
from utils.cabecalhos import cabecalho


def menu():
    while True:
        utils.cabecalhos.cabecalho('GESTÃO DE PRODUTOS')

        print('[ 1 ] - Adicionar novo produto')
        print('[ 2 ] - Mostrar todos produtos')
        print('[ 3 ] - Alterar um produto')
        print('[ 4 ] - Bye bye bye')
        opcao = input('---> ')

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            mostrar_produtos()
        elif opcao == '3':
            alterar_produtos()
        elif opcao == '4':
            print('A sair...')
            break
        else:
            print('Opção inválida...')


def adicionar_produto():
    from data import adicionar_produto_db
    utils.cabecalhos.cabecalho('ADICIONAR PRODUTO')
    nome = input('Nome: ')
    preco = float(input('Preço: €'))
    stock = int(input('Stock [unid.]: '))

    adicionar_produto_db(nome, preco, stock)

    print('Produto adicionado com sucesso!')


def mostrar_produtos():
    from data import mostrar_produtos_db
    produtos = mostrar_produtos_db()

    for produto in produtos:
        print(f'ID: {produto[0]}')
        print(f'--- {produto[1]}')
        print(f'--- {produto[2]:.2f}€')
        print(f'--- {produto[3]}')

    input()


def alterar_produtos():
    from data import alterar_poduto_db
    cabecalho('ALTERAR PRODUTO')
    id = int(input('Digite o ID: '))
    nome = input('Digite o novo nome [ENTER para manter]: ')
    preco = input('Digite o novo nome [ENTER para manter]: ')
    stock = input('Digite o novo nome [ENTER para manter]: ')

    alterar_poduto_db(id, nome, preco, stock)

