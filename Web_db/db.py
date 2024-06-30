import sqlite3




class workerDb():

    def __init__(self):
        self.connection  = sqlite3.connect("msgs.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS msgs (name TEXT, msg TEXT)")
        self.connection.commit()

    def insert(self, name, msg):
        connection  = sqlite3.connect("msgs.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO msgs VALUES (?, ?)", (name, msg))
        connection.commit()

    def returnByFilter(self, column, value):
        query = f"SELECT name, msg FROM msgs WHERE {column} = ?"
        returnItems = self.cursor.execute(query, (value,))
        return returnItems.fetchall()
    
    def returnAll(self):
        connection  = sqlite3.connect("msgs.db")
        cursor = connection.cursor()
        tempList = []
        for item in cursor.execute("SELECT name, msg FROM msgs").fetchall():
            tempList.append(item)
        return tempList



