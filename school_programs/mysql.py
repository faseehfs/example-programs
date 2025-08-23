import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="faseeh",
    password="password",
    database="example_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM your_table")

results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
conn.close()
