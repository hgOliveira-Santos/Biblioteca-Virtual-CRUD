import bcrypt
import mysql.connector

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        if conn.is_connected():
            print("Conectado ao servidor MySQL")

            criar_tabelas()

            return conn
    except mysql.connector.Error as e:
        print(f"Aconteceu algo de errado ao conectar: {e}")

def criar_tabelas():
    servidor_bd = conectar_bd()
    cursor = servidor_bd.cursor()

    # Criar o banco de dados se não existir
    cursor.execute("CREATE DATABASE IF NOT EXISTS despesas_pessoais_bd")
    print("Banco de dados criado com sucesso")

    # Usar o banco de dados criado
    cursor.execute("USE despesas_pessoais_bd")

    # Criar tabela Users
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                    )""")

    # Criar tabela Categorias_Despesas
    cursor.execute("""CREATE TABLE IF NOT EXISTS Categorias_Despesas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                                nome_categoria VARCHAR(255) NOT NULL
                        )""")

        # Criar tabela Despesas
    cursor.execute("""CREATE TABLE IF NOT EXISTS Despesas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    categoria_id INT NOT NULL,
                    data DATE,
                    info VARCHAR(255),
                    valor DECIMAL(10, 2),
                    FOREIGN KEY (user_id) REFERENCES Users(id),
                    FOREIGN KEY (categoria_id) REFERENCES Categorias_Despesas(id)
                    )""")   

def cadastro(usuário, senha, confirmaçãoSenha):
    servidor_bd = conectar_bd()
    if not servidor_bd:
        return
    


def criptografar_senha(senha):
    complemento = bcrypt.gensalt()
    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), complemento)
    return senha_criptografada


def verifica_nome_usuário(nomeUsuário):
    servidor_bd = conectar_bd()



def verificar_senha(senha, confirmaçãoSenha):
    if senha == confirmaçãoSenha:
        if len(senha) < 8:
            print("Sua senha deve ter 9 caracteres")
        else:
            print("Tudo certo")
            criptografar_senha(senha)
    else:
        print("Senhas diferentes")
