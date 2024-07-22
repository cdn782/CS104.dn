import sqlite3
conn = sqlite3.connect('people.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY autoincrement,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    auth_level INTEGER NOT NULL
                )''')
conn.commit()
conn.close()
print("Database 'people.db' created successfully.")
