import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = connection.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS wsaa")

print("Database wsaa created or already exists")

mycursor.close()
connection.close()