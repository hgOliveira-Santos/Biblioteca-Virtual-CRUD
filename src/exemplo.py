import mysql.connector

# Conectando ao servidor MySQL (localhost no caso do XAMPP)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",   # Substitua com seu usuário do MySQL
    password=""  # Substitua com sua senha do MySQL
)

# Criando o banco de dados 'escola' se não existir
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS escola")
print("Banco de dados 'escola' criado com sucesso.")

# Conectando ao banco de dados 'escola'
mydb = mysql.connector.connect(
    host="localhost",
    user="root",   # Substitua com seu usuário do MySQL
    password="", # Substitua com sua senha do MySQL
    database="escola"
)

# Criando a tabela 'alunos' se não existir
cursor = mydb.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  nome VARCHAR(255) NOT NULL,
                  idade INT,
                  cidade VARCHAR(255)
                  )""")
print("Tabela 'alunos' criada com sucesso.")

# Inserindo alguns registros na tabela 'alunos'
sql = "INSERT INTO alunos (nome, idade, cidade) VALUES (%s, %s, %s)"
val = [
    ('João', 15, 'São Paulo'),
    ('Maria', 16, 'Rio de Janeiro'),
    ('José', 14, 'Belo Horizonte'),
    ('Ana', 15, 'Porto Alegre')
]

cursor.executemany(sql, val)
mydb.commit()
print(cursor.rowcount, "registro(s) inserido(s) na tabela 'alunos'.")

# Exibindo os registros da tabela 'alunos'
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()

print("\nLista de Alunos:")
for aluno in alunos:
    print(aluno)

# Fechando a conexão com o banco de dados
mydb.close()




import bcrypt
import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados
def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host='seu_host',
            database='seu_banco_de_dados',
            user='seu_usuario',
            password='sua_senha'
        )
        if conn.is_connected():
            print('Conectado ao MySQL!')
            return conn
    except Error as e:
        print(e)

# Função para verificar o login
def verificar_login(username, senha):
    try:
        conn = conectar_bd()
        if conn:
            cursor = conn.cursor(dictionary=True)
            
            # Consulta para obter o hash da senha do usuário
            query = "SELECT password_hash FROM usuarios WHERE username = %s"
            cursor.execute(query, (username,))
            
            usuario = cursor.fetchone()
            if usuario:
                # Obtemos o hash da senha armazenada no banco de dados
                stored_hash = usuario['password_hash'].encode('utf-8')
                
                # Verificamos se a senha fornecida corresponde ao hash armazenado
                if bcrypt.checkpw(senha.encode('utf-8'), stored_hash):
                    print("Login bem-sucedido!")
                else:
                    print("Usuário ou senha incorretos.")
            else:
                print("Usuário não encontrado.")
            
            cursor.close()
            conn.close()
    
    except Error as e:
        print(e)

# Exemplo de uso da função verificar_login
if __name__ == "__main__":
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    verificar_login(username, senha)
