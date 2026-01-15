class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

livro1 = Livro('A História do Purfazz', 'Purfazz')
livro2 = Livro('A Criada', 'Freida')
livro3 = Livro('O Hobit', 'Tolkien')


print(livro1.titulo)
print(livro1.autor)
print(livro2.titulo)
print(livro2.autor)
print(livro3.titulo)
print(livro3.autor)