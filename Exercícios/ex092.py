class Produto:
    def __init__(self, nome, qtd):
        self.nome = nome
        self.quantidade = qtd

    def mostra_stock(self):
        print(f'O produto {self.nome} tem {self.quantidade} unidades em stock.')


    def aumentar_stock(self, valor):
        self.quantidade += valor


tomates = Produto('Tomates', 10)

tomates.mostra_stock()
tomates.aumentar_stock(20)
tomates.mostra_stock()