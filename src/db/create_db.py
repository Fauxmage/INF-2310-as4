import sqlite3 as db

conn = db.connect('test.db')
print("Test table opened!")

conn.execute('''CREATE TABLE IF NOT EXISTS USERS
            (ID         INTEGER         PRIMARY KEY,
             USERNAME   TEXT            NOT NULL,
             PASSWORD   TEXT            NOT NULL
             );''')

print("Test table created!")
conn.close()