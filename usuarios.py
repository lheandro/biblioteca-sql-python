from tabulate import tabulate
from database import cursor, conexao


def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    if nome is None or nome.strip() == "":
        print("O campo nome é obrigatório. Por favor, preencha o campo.")
        return
    cursor.execute(
        """
        INSERT INTO usuarios (nome) 
        VALUES (?)
        """, (nome,))

    conexao.commit()
    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print(tabulate(usuarios, headers=["ID", "Nome"], tablefmt="grid"))