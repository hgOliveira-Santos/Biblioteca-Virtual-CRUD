import bcrypt
import mysql.connector

class GerenciadorBD:
    def __init__(self, host="localhost", user="root", password="", database="despesas_pessoais_bd"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
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
                self.criar_tabela_categorias_despesas()
                self.criar_tabela_despesas()

                return True

        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao conectar: {e}")
            return False


    def criar_banco_de_dados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS despesas_pessoais_bd")
            print("Banco de dados criado com sucesso")
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao criar o banco de dados: {e}")


    def usar_banco_de_dados(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("USE despesas_pessoais_bd")
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


    def criar_tabela_categorias_despesas(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS Categorias_Despesas (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                nome_categoria VARCHAR(255) NOT NULL
                            )""")
            print("Tabela Categorias_Despesas criada com sucesso")
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao criar a tabela Categorias_Despesas: {e}")


    def criar_tabela_despesas(self):
        try:
            cursor = self.conn.cursor()
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
            print("Tabela Despesas criada com sucesso")
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao criar a tabela Despesas: {e}")

    
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


"""
app = GerenciadorBD()
app.cadastrar("hugo", "hg123456")"""