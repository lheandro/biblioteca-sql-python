from tabulate import tabulate
from database import cursor, conexao

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    genero = input("Digite o gênero do livro: ")

    cursor.execute(
        """
        INSERT INTO livros (titulo, autor, ano_publicacao, genero, disponibilidade) 
        VALUES (?, ?, ?, ?, ?)
        """, (titulo, autor, ano_publicacao, genero, "disponível"))

    conexao.commit()


def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")

    cursor.execute(
        """
        INSERT INTO usuarios (nome) 
        VALUES (?)
        """, (nome,))

    conexao.commit()


def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    print(tabulate(livros, headers=["ID", "Título", "Autor", "Ano de Publicação", "Gênero", "Disponibilidade"], tablefmt="grid"))

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print(tabulate(usuarios, headers=["ID", "Nome"], tablefmt="grid"))

def emprestar_livro():
    id_usuario = input("Digite o ID do usuário: ")
    id_livro = input("Digite o ID do livro: ")
    data_emprestimo = input("Digite a data do empréstimo: ")

    cursor.execute(
        "INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo) VALUES (?, ?, ?)",
        (id_livro, id_usuario, data_emprestimo),
    )
    cursor.execute(
        "UPDATE livros SET disponibilidade = ? WHERE id = ?",
        ("indisponível", id_livro),
    )
    conexao.commit()


def devolver_livro():
    id_emprestimo = input("Digite o ID do empréstimo: ")

    cursor.execute(
        "SELECT id_livro FROM emprestimos WHERE id = ?", (id_emprestimo,)
    )
    id_livro = cursor.fetchone()[0]

    cursor.execute(
        "UPDATE livros SET disponibilidade = ? WHERE id = ?", ("disponível", id_livro)
    )
    cursor.execute("DELETE FROM emprestimos WHERE id = ?", (id_emprestimo,))
    conexao.commit()


def listar_emprestimos():
    cursor.execute(
        """
        SELECT emprestimos.id, usuarios.nome, livros.titulo, emprestimos.data_emprestimo
        FROM emprestimos
        JOIN usuarios ON emprestimos.id_usuario = usuarios.id
        JOIN livros ON emprestimos.id_livro = livros.id
        """
    )
    emprestimos = cursor.fetchall()
    print(tabulate(emprestimos, headers=["ID", "Nome do Usuário", "Título do Livro", "Data do Empréstimo"], tablefmt="grid"))

def menu():

    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Listar livros")
    print("4. Listar usuários")
    print("5. Emprestar livro")
    print("6. Devolver livro")
    print("7. Listar empréstimos")
    print("8. Sair")    

    while True:
        opcao = input("Escolha uma opção: ")   
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            listar_livros()
        elif opcao == "4":
            listar_usuarios()
        elif opcao == "5":
            emprestar_livro()
        elif opcao == "6":
            devolver_livro()
        elif opcao == "7":
            listar_emprestimos()
        elif opcao == "8":
            break
    