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
            cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                username VARCHAR(255) NOT NULL,
                                password VARCHAR(255) NOT NULL
                            )""")
            print("Tabela Users criada com sucesso")
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Aconteceu algo de errado ao criar a tabela users: {e}")
    
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

    def login(self, nomeUsuario, usuarioSenha):
        try:
            cursor = self.conn.cursor()

            # Verificar se o usuário existe
            queryUsuario = "SELECT COUNT(*) FROM users WHERE username = %s"
            cursor.execute(queryUsuario, (nomeUsuario,))
            usuarioExiste = cursor.fetchone()[0]

            if usuarioExiste == 1:
                # Recuperar o hash da senha do banco de dados
                querySenha = "SELECT password FROM users WHERE username = %s"
                cursor.execute(querySenha, (nomeUsuario,))
                hashed_password = cursor.fetchone()[0]

                # Verificar a senha usando bcrypt
                if bcrypt.checkpw(usuarioSenha.encode('utf-8'), hashed_password.encode('utf-8')):
                    print("Usuário está no sistema!")
                    return True
                else:
                    print("Você digitou a senha errada!")
                    return False
            else:
                print("Usuário não cadastrado!")
                return False
            
        except Exception as e:
            print(f"Erro ao verificar login: {e}")
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