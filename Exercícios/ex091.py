class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostra(self):
        return f'O livro "{self.titulo}" foi escrito pelo autor {self.autor}'

livro1 = Livro('A História do Purfazz', 'Purfazz')
livro2 = Livro('A Criada', 'Freida')
livro3 = Livro('O Hobit', 'Tolkien')

print(livro1.mostra())
print(livro2.mostra())
print(livro3.mostra())