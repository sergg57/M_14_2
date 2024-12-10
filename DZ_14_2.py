# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
#                    (f"User{i+1}",f"example{i+1}@gmail.com", str((i+1)*10), "1000"))
#

for i in range(5):
    #print(2*i + 1)
    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", ("500",f"User{((2*i)+1)}"))

for i in range(4):
    #print(3*i+1)
    #cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{(3*i)+1}"),)
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{((3*i)+1)}",))


# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя: {user[0]} | Почта:{user[1]} | Возраст:{user[2]} | Баланс:{user[3]}')

cursor.execute("DELETE FROM Users WHERE username = ?", ("User6",))
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(total_users)

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances)
print(all_balances/total_users)

cursor.execute("SELECT AVG(balance) FROM Users")
print(cursor.fetchone()[0])


connection.commit()
connection.close()