from tabulate import tabulate
from database import cursor, conexao


def emprestar_livro():
    id_usuario = input("Digite o ID do usuário: ")
    id_livro = input("Digite o ID do livro: ")
    data_emprestimo = input("Digite a data do empréstimo: ")

    if None in (id_usuario, id_livro, data_emprestimo) or "" in (id_usuario, id_livro, data_emprestimo):
        print("Todos os campos são obrigatórios. Por favor, preencha todos os campos.")
        return

    cursor.execute("SELECT disponibilidade FROM livros WHERE id = ?", (id_livro,))
    livro = cursor.fetchone()
    if livro is None:
        print("Livro não encontrado.")
        return

    if livro[0] == "indisponível":
        print("O livro não está disponível para empréstimo.")
        return

    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
    usuario = cursor.fetchone()
    if usuario is None:
        print("Usuário não encontrado.")
        return

    cursor.execute(
        "INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo) VALUES (?, ?, ?)",
        (id_livro, id_usuario, data_emprestimo),
    )

    cursor.execute(
        "UPDATE livros SET disponibilidade = ? WHERE id = ?",
        ("indisponível", id_livro),
    )

    conexao.commit()
    print("Empréstimo registrado com sucesso!")


def devolver_livro():
    id_emprestimo = input("Digite o ID do empréstimo: ")

    cursor.execute(
        "SELECT id_livro FROM emprestimos WHERE id = ?", (id_emprestimo,)
    )
    emprestimo = cursor.fetchone()
    if emprestimo is None:
        print("Empréstimo não encontrado.")
        return

    id_livro = emprestimo[0]

    cursor.execute(
        "UPDATE livros SET disponibilidade = ? WHERE id = ?", ("disponível", id_livro)
    )
    cursor.execute("DELETE FROM emprestimos WHERE id = ?", (id_emprestimo,))
    conexao.commit()
    print("Livro devolvido com sucesso!")


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