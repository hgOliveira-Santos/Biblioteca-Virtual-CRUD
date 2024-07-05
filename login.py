import bcrypt
import mysql.connector

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="despesas_pessoais_db"
        )
        if conn.is_connected():
            print("conectado ao servidor mysql")
            return conn
    except Exception as e:
        print(f"Aconteceu algo de errado: {e}")

def criptografar_senha(senha):
    
    complemento = bcrypt.gensalt()

    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), complemento)

    return senha_criptografada

def cadastro(usuário):
    servidor_bd = conectar_bd()


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