import sqlite3

conn = sqlite3.connect("leave.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS User(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Leave(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    from_date TEXT,
    to_date TEXT,
    days INTEGER,
    reason TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

cursor.execute("""
INSERT OR IGNORE INTO User
(username,password,role)
VALUES
('admin','admin123','admin')
""")

conn.commit()
conn.close()

print("Database Created Successfully")