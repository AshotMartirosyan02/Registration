import sqlite3
def create_database():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            image TEXT
        )
    ''')
    conn.commit()
    conn.close()


def view_all_users():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, password, image FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def add_new_user(username, password, image_address):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, password, image)
        VALUES (?, ?, ?)
    ''', (username, password, image_address))
    conn.commit()
    conn.close()

# clear Data-base

# def clear_database():
#     conn = sqlite3.connect('user_data.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM users")  # This deletes all data in the 'users' table
#     conn.commit()
#     conn.close()
#
# clear_database()
#
#
#
# #View data_base
#
# for i in view_all_users():
#     print(i)
