from tabulate import tabulate
from database import cursor, conexao


def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    genero = input("Digite o gênero do livro: ")

    if None in (titulo, autor, ano_publicacao, genero) or "" in (titulo, autor, ano_publicacao, genero):
        print("Todos os campos são obrigatórios. Por favor, preencha todos os campos.")
        return

    cursor.execute(
        """
        INSERT INTO livros (titulo, autor, ano_publicacao, genero, disponibilidade) 
        VALUES (?, ?, ?, ?, ?)
        """, (titulo, autor, ano_publicacao, genero, "disponível"))

    conexao.commit()
    print("Livro cadastrado com sucesso!")


def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    print(tabulate(livros, headers=["ID", "Título", "Autor", "Ano de Publicação", "Gênero", "Disponibilidade"], tablefmt="grid"))