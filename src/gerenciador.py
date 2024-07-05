import bcrypt
import mysql.connector

class GerenciadorBD:
    def __init__(self, host="localhost", user="root", password=""):
        self.host = host
        self.user = user
        self.password = password
        self.conn = None  # Conexão será estabelecida quando necessário

    def conectar_bd(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            if self.conn.is_connected():
                print("Conectado ao servidor MySQL")
                self.criar_tabelas()
                return True
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao conectar: {e}")
            return False

    def criar_tabelas(self):
        try:
            cursor = self.conn.cursor()

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
            
            cursor.close()
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao criar tabelas: {e}")

    def criptografar_senha(self, senha):
        try:
            complemento = bcrypt.gensalt()
            senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), complemento)
            return senha_criptografada
        except Exception as e:
            print(f"Aconteceu algo de errado ao criptografar senha: {e}")
            return None


    def verificar_senha(self, senha, confirmacaoSenha):
        if senha == confirmacaoSenha:
            if len(senha) < 8:
                print("Sua senha deve ter pelo menos 8 caracteres.")
            else:
                print("Tudo certo.")
                return True
        else:
            print("Senhas diferentes.")
        return False


    def verificar_username(self, username):
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM Users WHERE username = %s"
            cursor.execute(query, (username,))
            resultado = cursor.fetchone()[0]

            if resultado != 0:
                print("Nome de usuário já está sendo utilizado")
                return False
            else:
                print("Nome de usuário aceito!")
                return True
            
            cursor.close()

        except mysql.connector.Error as e:
            print(f"Aconteceu um erro: {e}")

        finally:
            self.conn.close()
        

