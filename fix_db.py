import sqlite3

# Hubungkan ke database SQLite Anda
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Buat tabel untuk Experience starred_by
cursor.execute('''
CREATE TABLE IF NOT EXISTS main_experience_starred_by (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    experience_id CHAR(32) NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user (id)
)
''')

# Buat tabel untuk Project starred_by 
cursor.execute('''
CREATE TABLE IF NOT EXISTS main_project_starred_by (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id CHAR(32) NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user (id)
)
''')

conn.commit()
conn.close()