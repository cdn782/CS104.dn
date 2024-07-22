import sqlite3
from users import users

conn = sqlite3.connect('people.db')
cursor = conn.cursor()

for users in users:
    cursor.execute("INSERT INTO users (username, password, auth_level) VALUES (?, ?, ?)", (users['username'], users['password'], users['auth_level']))

conn.commit()
conn.close()

print("Data inserted successfully.")