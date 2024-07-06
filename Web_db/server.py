# app.py
from  db import workerDb
from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

db = workerDb()

class Chat(Resource):
    def get(self):
        return db.returnAll()

    def post(self):
        new_message = request.json.get('message')
        user = request.json.get('user')
        db.insert(user, new_message)
        return {'user': user, 'message': new_message}, 201
    
    def is_login(self):
        return db.is_login()

api.add_resource(Chat, '/chat')

@app.route('/')
def index():
    print("index")
    return app.send_static_file('index.html')

@app.route('/login.html')
def login():
    print("login")
    return app.send_static_file('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
