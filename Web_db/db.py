import sqlite3




class msgDb():

    def __init__(self):
        self.connection  = sqlite3.connect("msgs.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS msgs (name TEXT, recipient TEXT, msg TEXT)")
        self.connection.commit()

    def insert(self, name, recipient, msg):
        connection  = sqlite3.connect("msgs.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO msgs VALUES (?, ?, ?)", (name, recipient, msg))
        connection.commit()

    def returnByFilter(self, user, recipient):
        connection = sqlite3.connect("msgs.db")
        cursor = connection.cursor()
        user = str(user)
        recipient = str(recipient)

        query = f"SELECT name, recipient, msg FROM msgs WHERE (name = '{user}' and recipient = '{recipient}' or name = '{recipient}' and recipient = '{user}')"


        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()

        return result

    def returnByGlobal(self):
        connection = sqlite3.connect("msgs.db")
        cursor = connection.cursor()

        query = "SELECT name, recipient, msg FROM msgs WHERE recipient = 'global'"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()

        return result

        
    def returnAll(self):
        connection  = sqlite3.connect("msgs.db")
        cursor = connection.cursor()
        tempList = []
        for item in cursor.execute("SELECT name, recipient, msg FROM msgs").fetchall():
            tempList.append(item)
        return tempList



