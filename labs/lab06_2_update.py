import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="wsaa"
)

cursor = db.cursor()

sql = "UPDATE student SET name=%s, age=%s WHERE id=%s"
values = ("Joe", 33, 1)

cursor.execute(sql, values)
db.commit()

print("update done")

cursor.close()
db.close()