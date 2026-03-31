import sqlite3

conn = sqlite3.connect(r"C:\Users\mjaga\PycharmProjects\FabricProject_pipeline\Scripts\data\warehouse.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM titanic_clean LIMIT 5;")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()