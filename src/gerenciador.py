import bcrypt
import mysql.connector

class GerenciadorBD:
    def __init__(self, host="localhost", user="root", password=""):
        self.host = host
        self.user = user
        self.password = password
        self.conn = None
        self.conectar_bd()


    def conectar_bd(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            if self.conn.is_connected():
                print("Conectado ao servidor MySQL")

                self.criar_banco_de_dados()
                self.usar_banco_de_dados()
                self.criar_tabela_users()

                return True

        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao conectar: {e}")
            return False

    def criar_banco_de_dados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS usuarios_bd")
            print("Banco de dados criado com sucesso")
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao criar o banco de dados: {e}")


    def usar_banco_de_dados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("USE usuarios_bd")
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao usar o banco de dados: {e}")


    def criar_tabela_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                username VARCHAR(255) NOT NULL,
                                password VARCHAR(255) NOT NULL
                            )""")
            print("Tabela Users criada com sucesso")
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao criar a tabela Users: {e}")
    
    def cadastrar(self, nomeUsuario, usuarioSenha):
        senha = self.criptografar_senha(usuarioSenha)

        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO Users VALUES (NULL, %s, %s)"
            cursor.execute(query, (nomeUsuario, senha,))
            self.conn.commit()
            print("Usuário cadastrado")
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
            return False
        
    def login(self, nomeUsuário, usuárioSenha):
        if self.verifica_login(nomeUsuário, usuárioSenha):
            pass
        

    def verifica_login(self, nome, senha):
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM Users WHERE username = %s"
            cursor.execute(query, (nome, senha,))
            resultado = cursor.fetchone()[0]

            if resultado == 1:
                print("Usuário aceito!")
                return True
            else:
                print("Usuário não cadastrado!")
                return False
            
        except Exception as e:
            print(f"Erro ao verificar login: {e}")


    def criptografar_senha(self, senha):
        try:
            complemento = bcrypt.gensalt()
            senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), complemento)
            return senha_criptografada
        except Exception as e:
            print(f"Aconteceu algo de errado ao criptografar senha: {e}")
            return None
        

    def verificar_nome_usuário(self, nomeUsuário):
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM Users WHERE username = %s"
            cursor.execute(query, (nomeUsuário,))
            resultado = cursor.fetchone()[0]

            if resultado != 0:
                print("Nome de usuário já está sendo utilizado")
                return False
            else:
                print("Nome de usuário aceito!")
                self.conn.commit()
                return True

        except mysql.connector.Error as e:
            print(f"Aconteceu um erro: {e}")