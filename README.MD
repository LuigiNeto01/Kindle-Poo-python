# Projeto POO de um Kindle

Este projeto simula uma biblioteca de livros em um Kindle, onde é possível adicionar, listar, remover e ativar livros. Apenas um livro pode estar ativo (com página aberta) por vez.

## Classes e Métodos

### Classe `Livro`

A classe `Livro` representa um livro com as seguintes propriedades e métodos:

- **Propriedades:**
  - `titulo`: Título do livro.
  - `paginas`: Número de páginas do livro.
  - `id`: Identificador único do livro, gerado automaticamente.
  - `ativo`: Indica se o livro está ativo (com página aberta).

- **Métodos:**
  - `__init__(self, titulo, paginas, ativo=False)`: Inicializa um novo livro com título, páginas e status ativo.
  - `abrir(self)`: Define o livro como ativo.
  - `fechar(self)`: Define o livro como inativo.
  - `__str__(self)`: Retorna uma representação em string do livro.

### Classe `Biblioteca`

A classe `Biblioteca` gerencia a coleção de livros com as seguintes funcionalidades:

- **Propriedades:**
  - `livros`: Lista de livros na biblioteca.

- **Métodos:**
  - `__init__(self)`: Inicializa a biblioteca com uma lista vazia de livros.
  - `addLivros(self, livro)`: Adiciona um livro à biblioteca.
  - `delLivros(self, id_livro)`: Remove um livro da biblioteca pelo seu ID.
  - `listarLivros(self)`: Lista todos os livros na biblioteca.
  - `activeLivro(self, id_livro)`: Ativa um livro pelo seu ID e desativa todos os outros.

## Exemplo de Uso

Aqui está um exemplo de como usar as classes `Livro` e `Biblioteca`:

```python
# Criação da biblioteca
biblioteca = Biblioteca()

# Lista de livros a serem adicionados
ListaLivros = [['Branca de neve', 300], ['Malevola', 350], ['Gasparzinho', 895]]

# Adiciona os livros na biblioteca
for livro in ListaLivros:
    biblioteca.addLivros(Livro(livro[0], livro[1]))

# Lista todos os livros na biblioteca
biblioteca.listarLivros()

# Remove o livro com ID 2
biblioteca.delLivros(2)

# Ativa o livro com ID 1
biblioteca.activeLivro(1)

# Lista os livros restantes na biblioteca
biblioteca.listarLivros()
