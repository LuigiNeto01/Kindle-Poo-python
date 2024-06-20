# Projeto POO de um kindle

'''
biblioteca que tenha varios livros, o livro terá titulo, paginas, id, ativo;
somente 1 livro podera estar ativo; (ativo = pagina aberta)
'''

class Livro:
    proximo_id = 1

    def __init__(self, titulo, paginas, id, ativo = False):
        self.titulo = titulo
        self.paginas = paginas
        self.id = Livro.proximo_id
        Livro.proximo_id += 1 
        self.ativo = ativo

    def abrir(self, livro):
        self.ativo = True

    def fechar(self, livro):
        self.ativo = False

    def __str__(self):
        return f"{self.titulo} - Páginas: {self.paginas} - Id: {self.id}"


class Biblioteca: