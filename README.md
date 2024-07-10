# Sistema de Login e Cadastro
Este é um sistema de gerenciamento de despesas pessoais com interface gráfica, desenvolvido em Python usando Tkinter e integrado a um banco de dados MySQL para armazenamento seguro de informações de usuário.

##Funcionalidades

###Cadastro de Usuário
- Permite que novos usuários se cadastrem fornecendo um nome de usuário e senha.
- Verifica a validade dos dados inseridos (mínimo de caracteres para usuário e senha, correspondência de senha e confirmação).
- Criptografa a senha usando bcrypt antes de armazenar no banco de dados.
  
### Login de Usuário
- Usuários cadastrados podem fazer login usando seu nome de usuário e senha.
- Utiliza bcrypt para verificar a correspondência da senha criptografada armazenada no banco de dados.
