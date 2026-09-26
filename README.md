# Sistema de Biblioteca - Python + SQL

Projeto que fiz pra praticar SQL na prática, indo além de exercício solto: um sistema de controle de empréstimos de biblioteca, rodando no terminal.

## O que ele faz

- Cadastra livros e usuários
- Lista tudo formatado em tabela
- Registra empréstimo (e marca o livro como indisponível)
- Registra devolução (volta a ficar disponível)
- Lista os empréstimos já cruzando as informações das 3 tabelas

## Stack

Python 3, SQLite e a biblioteca `tabulate` pra formatar a saída no terminal.

## Estrutura

Separei o projeto em arquivos, cada um com uma responsabilidade:

- `database.py` - conexão com o banco e criação das tabelas
- `livros.py` - cadastro e listagem de livros
- `usuarios.py` - cadastro e listagem de usuários
- `emprestimos.py` - registro, devolução e listagem de empréstimos
- `menu.py` - menu do sistema e chamada das funções
- `main.py` - chama o menu e inicia o programa

## Banco de dados

3 tabelas: `livros`, `usuarios` e `emprestimos`. A tabela de empréstimos se conecta com as outras duas, guardando qual usuário pegou qual livro e quando.

## Rodando o projeto

```bash
git clone https://github.com/lheandro/biblioteca-sql-python.git
cd biblioteca-sql-python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Menu

```
1. Cadastrar livro
2. Cadastrar usuário
3. Listar livros
4. Listar usuários
5. Emprestar livro
6. Devolver livro
7. Listar empréstimos
8. Sair
```

---
Lheandro Junior