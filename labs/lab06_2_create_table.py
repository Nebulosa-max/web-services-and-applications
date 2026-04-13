import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="wsaa"
)

mycursor = mydb.cursor()

sql = """
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
"""
mycursor.execute(sql)

print("Table student created or already exists")

mycursor.close()
mydb.close()