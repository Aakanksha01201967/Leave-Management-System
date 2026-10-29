import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS leave_ledger
(
    ledger_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    leave_type TEXT,
    days INTEGER,
    transaction_type TEXT
)
""")

conn.commit()
conn.close()

print("Leave Ledger Created")