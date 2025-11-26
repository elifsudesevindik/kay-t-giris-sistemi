import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('user.db')
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT NOT NULL,
                              password TEXT NOT NULL''')
        self.connection.commit()

    def kayit(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.connection.commit()

    def ekleme(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if self.cursor.fetchone():
            return False
        self.kayit(username, password)
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return self.cursor.fetchone() is not None
        
    def arama(self):      
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
    def giris(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return self.cursor.fetchone() is not None  
    
    def guncelle_sifre(self, username, new_password):
        self.cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        self.connection.commit()
    
    def guncelle_kullanici_adi(self, user_id, new_username):
        self.cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user_id))
        self.connection.commit()
    
    def silme(self, username, password):
        self.cursor.execute("DELETE FROM users WHERE username = ? AND password = ?", (username, password))
        self.connection.commit()
       
        