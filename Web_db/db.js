const sqlite3 = require('sqlite3')
const md5 = require('md5');

function encodeToMD5(string) {
    return md5(string);
}

class In_db {
    constructor(databasePath) {
        this.databasePath = databasePath;
        this.db = new sqlite3.Database(databasePath);
        this.db.run('CREATE TABLE IF NOT EXISTS users (name TEXT, hash TEXT, pay INTEGER)');
    }

    insertUser(name, pay) {
        const hash = md5(name);
        const stmt = this.db.prepare('INSERT INTO users (name, hash, pay) VALUES (?, ?, ?)');
        stmt.run(name, hash, pay);
        stmt.finalize();
    }

    getUsers() {
        return new Promise((resolve, reject) => {
            this.db.all('SELECT * FROM users', (err, rows) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(rows);
                }
            });
        });
    }
}

module.exports = In_db;
