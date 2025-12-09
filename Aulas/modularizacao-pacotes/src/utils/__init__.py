from time import sleep

def delay(time: int) -> None:
    sleep(time)


def pausa(txt: str) -> None:
    input(txt)


def cabecalho(txt: str) -> None:
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


def menu() -> None:
    from src.handlers import pesquisar_notas, mostrar_notas, adicionar_notas, apagar_notas

    while True:
        cabecalho('MENU')
        print('[ 1 ] Adicionar notas')
        print('[ 2 ] Mostrar notas')
        print('[ 3 ] Apagar notas')
        print('[ 4 ] Pesquisar notas')
        print('[ 5 ] Sair')
        opcao = int(input('---> '))

        match opcao:
            case 1:
                adicionar_notas()
            case 2:
                mostrar_notas()
            case 3:
                apagar_notas()
            case 4:
                pesquisar_notas()
            case 5:
                break

        pausa('---ENTER para continuar---')