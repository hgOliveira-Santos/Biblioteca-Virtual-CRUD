import bcrypt
import mysql.connector

bd = mysql.connector.connect(
    host="localhost", 
    user="root",
    password=""
)

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        if conn.is_connected():
            print("Conectado ao servidor MySQL")
            return conn
    except mysql.connector.Error as e:
        print(f"Aconteceu algo de errado ao conectar: {e}")

def cadastro(usuário):
    servidor_bd = conectar_bd()
    if not servidor_bd:
        return

    cursor = servidor_bd.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS despesas_pessoais_bd")
    print("Banco de dados criado com sucesso")

    cursor.execute("USE despesas_pessoais_bd")
    cursor.execute("SHOW TABLES")
    # Aqui você pode adicionar a criação de tabelas ou outras operações no banco de dados


def criptografar_senha(senha):
    
    complemento = bcrypt.gensalt()

    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), complemento)

    return senha_criptografada



def verifica_nome_usuário(nomeUsuário):
    pass


def verificar_senha(self):
    if self.senha_value.get() == self.confirmar_senha_value.get():
        if len(self.senha_value.get()) < 8:
            print("Sua senha deve ter 8 caracteres")
        else:
            print("tudo certo")
            criptografar_senha(self.senha_value.get())
    else:
        print("Senhas diferentes")

cadastro("hg")