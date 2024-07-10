# Sistema de Login e Cadastro
Este é um sistema de gerenciamento de despesas pessoais com interface gráfica, desenvolvido em Python usando Tkinter e integrado a um banco de dados MySQL para armazenamento seguro de informações de usuário.

Funcionalidades
Cadastro de Usuário

Permite que novos usuários se cadastrem fornecendo um nome de usuário e senha.
Verifica a validade dos dados inseridos (mínimo de caracteres para usuário e senha, correspondência de senha e confirmação).
Criptografa a senha usando bcrypt antes de armazenar no banco de dados.
Login de Usuário

Usuários cadastrados podem fazer login usando seu nome de usuário e senha.
Utiliza bcrypt para verificar a correspondência da senha criptografada armazenada no banco de dados.
Componentes Utilizados
Tkinter Personalizado (customtkinter):
Oferece uma interface gráfica mais estilizada e responsiva, com personalização de cores, fontes e botões.
Banco de Dados MySQL:
Armazena informações de usuário de forma segura.
Utiliza uma tabela users para armazenar nomes de usuário e senhas criptografadas.
Estrutura do Código
InterfaceInicial Class:

Gerencia a interface gráfica do programa.
Implementa métodos para cadastro de usuários, validação de dados e gerenciamento de login.
GerenciadorBD Class:

Gerencia a conexão com o banco de dados MySQL.
Inclui métodos para criar banco de dados, tabela de usuários, cadastro de novos usuários, login e verificação de nome de usuário.
