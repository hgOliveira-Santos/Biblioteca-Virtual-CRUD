# Sistema de Login e Cadastro

Este é um sistema de gerenciamento de usuários com interface gráfica, desenvolvido em Python e integrado a um banco de dados MySQL para armazenamento seguro de informações.

## Funcionalidades

### Cadastro de Usuário

- Permite que novos usuários se cadastrem fornecendo um nome de usuário e senha.
- Verifica a validade dos dados inseridos (mínimo de caracteres para usuário e senha, correspondência de senha e confirmação).
- Criptografa a senha usando bcrypt antes de armazenar no banco de dados.

### Login de Usuário

- Usuários cadastrados podem fazer login usando seu nome de usuário e senha.
- Utiliza bcrypt para verificar a correspondência da senha criptografada armazenada no banco de dados.

## Estrutura do Código

- **`InterfaceInicial` Class:**
  - Gerencia a interface gráfica do programa.
  - Implementa métodos para cadastro de usuários, validação de dados e gerenciamento de login.

- **`GerenciadorBD` Class:**
  - Gerencia a conexão com o banco de dados MySQL.
  - Inclui métodos para criar banco de dados, tabela de usuários, cadastro de novos usuários, login e verificação de nome de usuário.

## Requisitos e Instalação

Para executar o sistema localmente, siga estas etapas:

1. **Python e Bibliotecas Necessárias:**
   - Python 3.x
   - `bcrypt` (para criptografia de senha)
   - `mysql-connector-python` (para conexão com MySQL)
   - `customtkinter` (Tkinter personalizado)

2. **Configuração do Banco de Dados:**
   - Configure um servidor MySQL local com as credenciais apropriadas.

3. **Execução do Programa:**
   - Execute o arquivo principal `interface.py` para iniciar a interface gráfica.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para melhorar este sistema, adicionar novas funcionalidades, otimizar o código ou corrigir problemas existentes.
