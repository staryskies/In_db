import sqlite3




class userDb():

    def __init__(self):
        self.connection  = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (user TEXT, passcode TEXT)")
        self.connection.commit()

    def insert(self, user, password):
        connection  = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?)", (user, passcode))
        connection.commit()

    def returnByFilter(self, filters):
        connection  = sqlite3.connect("users.db")
        cursor = connection.cursor()

        conditions = []
        values = []
        for column, value in filters.items():
            conditions.append(f"{column} = ?")
            values.append(value)
        
        where_clause = " AND ".join(conditions)
        query = f"SELECT name, passcode FROM users WHERE {where_clause}"
        
        returnItems = cursor.execute(query, tuple(values))
        return returnItems.fetchall()
    
    def returnAll(self):
        connection  = sqlite3.connect("users.db")
        cursor = connection.cursor()
        tempList = []
        for item in cursor.execute("SELECT user, passcode FROM users").fetchall():
            tempList.append(item)
        return tempList



