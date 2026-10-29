import sqlite3

conn = sqlite3.connect("leave.db")

cursor = conn.cursor()

print("USERS:")
cursor.execute("SELECT * FROM User")
for row in cursor.fetchall():
    print(row)

print("\nLEAVES:")
cursor.execute("SELECT * FROM Leave")
for row in cursor.fetchall():
    print(row)

conn.close()