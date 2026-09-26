from livros import cadastrar_livro, listar_livros
from usuarios import cadastrar_usuario, listar_usuarios
from emprestimos import emprestar_livro, devolver_livro, listar_emprestimos


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
        else:
            print("Opção inválida. Tente novamente.")