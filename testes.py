import mysql.connector

def conexao():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        if conn.is_connected():
            print("CONECTADO AO MYSQL")
            return conn
    except Exception as e:
        print(e)

servidor = conexao()
cursor = servidor.cursor()

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













"""# Commitar as alterações
servidor.commit()

# Fechar o cursor e a conexão
cursor.close()
servidor.close()"""