import sqlite3


def conectar_db():
    return sqlite3.connect('loja.db')


def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL,
        stock INTEGER
    )
    '''

    cursor.execute(query)
    conn.commit()
    conn.close()


def adicionar_produto_db(nome: str, preco: float, stock: int) -> None:
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)', (nome, preco, stock))

    conn.commit()
    conn.close()


def mostrar_produtos_db() -> list:
    conn = conectar_db()
    cursor = conn.cursor()

    query = 'SELECT * FROM produtos'

    cursor.execute(query)
    produtos = cursor.fetchall()

    conn.close()

    return produtos


def alterar_poduto_db(identificador: int, nome='', preco='', stock=''):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM produtos WHERE id = ?', (identificador,))

    produto = cursor.fetchone()

    if produto:

        if len(nome) > 0:
            novo_nome = nome
        else:
            novo_nome = produto[1]

        if len(preco) > 0:
            novo_preco = preco
        else:
            novo_preco = produto[2]

        if len(stock) > 0:
            novo_stock = stock
        else:
            novo_stock = produto[3]

        cursor.execute('UPDATE produtos SET nome = ?, preco = ?, stock = ? WHERE id = ?', (novo_nome, float(novo_preco), int(novo_stock), identificador))

    else:
        print('ERRO, não existe produto com esse ID.')
    conn.commit()
    conn.close()