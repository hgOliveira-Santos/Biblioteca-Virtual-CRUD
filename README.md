# Despesas Pessoais

Este repositório contém um aplicativo para controle de despesas pessoais desenvolvido em Python usando Tkinter e MySQL.

## Estrutura do Projeto

Funcionalidades
1. Conectar e Configurar Banco de Dados
A classe GerenciadorBD se conecta ao MySQL, cria um banco de dados usuarios_bd se não existir, e cria a tabela users para armazenar usuários com campos id, username, e password.

2. Cadastro de Usuários
cadastrar(nomeUsuario, usuarioSenha): Criptografa a senha usando bcrypt e armazena o nome de usuário e senha criptografada na tabela users.
3. Login de Usuários
login(nomeUsuario, usuarioSenha): Verifica se o usuário existe no banco de dados e se a senha fornecida corresponde à senha armazenada usando bcrypt.
4. Interface Gráfica
A classe InterfaceInicial utiliza customtkinter para criar uma interface gráfica com duas telas: cadastro e login.

Funcionalidades da Interface:
Cadastro: Validações de campos (nome de usuário e senha), verificações de existência de usuário, e inserção segura no banco de dados.

Login: Verificações de usuário e senha, usando o banco de dados para autenticação.
