import mysql.connector

def conectar_bd():
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
        print


myDatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = myDatabase.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Biblioteca")
print("Database 'Biblioteca' criado com sucesso!")

cursor.execute("USE Biblioteca")

myDatabase = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="",
    database = "Biblioteca"
)

cursor = myDatabase.cursor()
cursor.execute()

