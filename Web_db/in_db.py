import sqlite3
import hashlib

def hashMD5(value):
    encoded_value = value.encode()
    result = hashlib.md5(encoded_value)
    return result.hexdigest()


class workerDb():
    
    def __init__(self):
        self.connection  = sqlite3.connect("worker.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS worker (name TEXT, hash TEXT, pay INTEGER)")
        self.connection.commit()
    
    def insert(self, name, pay):
        hash = hashMD5(name)
        self.cursor.execute("INSERT INTO worker VALUES (?, ?, ?)", (name, hash, pay))
        self.connection.commit()
    def returnByFilter(self, column, value):
        query = f"SELECT name, hash, pay FROM worker WHERE {column} = ?"
        returnItems = self.cursor.execute(query, (value,))
        return returnItems.fetchall()





