# Projeto POO de um kindle

'''
biblioteca que tenha varios livros, o livro terá titulo, paginas, id, ativo;
somente 1 livro podera estar ativo; (ativo = pagina aberta)
'''

class Livro: #classe de livro para sua criação
    proximo_id = 1

    def __init__(self, titulo, paginas, ativo = False): #recebe as variaveis para a criação do livro
        self.titulo = titulo
        self.paginas = paginas
        self.id = Livro.proximo_id
        Livro.proximo_id += 1 
        self.ativo = ativo

    def abrir(self): #abre o livro e deixa ele ativo
        self.ativo = True

    def fechar(self): #fecha o livro e deixa ele inativo
        self.ativo = False

    def __str__(self): #log mostrando os livros
        return f"{self.titulo} - Páginas: {self.paginas} - Id: {self.id} - Ativo: {self.ativo}"

class Biblioteca: #classe biblioteca para armazenar os livros

    def __init__(self): #cria lista de livros
        self.livros = []

    def addLivros(self, livro): #adiciona o livro chamando a classe
        self.livros.append(livro)

    def delLivros(self, id_livro):
        for livro in self.livros: #apaga o livro de acordo com o id
            if livro.id == id_livro:
                self.livros.remove(livro)

    def listarLivros(self): #lista todos os itens da lista
        print('\n')
        for livro in self.livros:
            print(livro)
    
    def activeLivro(self, id_livro): #ativa o livro para poder ler, boolean
        for livro in self.livros:
            if livro.id == id_livro:
                livro.abrir()
            else:
                livro.fechar()

biblioteca = Biblioteca() #chama a classe livro

ListaLivros = [['Branca de neve', 300],['Malevola', 350],['Gasparzinho', 895]] #adiciona livro na lista

for livro in ListaLivros:
    biblioteca.addLivros(Livro(livro[0],livro[1])) #coloca os livros na biblioteca

biblioteca.listarLivros() #lista todos os livros

biblioteca.delLivros(2) #apaga o livro de acordo com seu id

biblioteca.activeLivro(1) #ativa o livro de id 1

biblioteca.listarLivros() #lista os livros restantes
